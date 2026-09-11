import struct
import sys
import os

def read_string(f):
    length_bytes = f.read(8)
    if len(length_bytes) < 8:
        return None
    length = struct.unpack('<Q', length_bytes)[0]
    data = f.read(length)
    return data.decode('utf-8', errors='replace')

def validate_gguf(file_path):
    if not os.path.exists(file_path):
        return {"valid": False, "error": "File does not exist"}
    
    file_size = os.path.getsize(file_path)
    if file_size < 16:
        return {"valid": False, "error": "File too small (< 16 bytes)"}
    
    try:
        with open(file_path, 'rb') as f:
            magic = f.read(4)
            if magic != b'GGUF':
                return {"valid": False, "error": f"Invalid magic: {magic} (expected b'GGUF')"}
            
            version = struct.unpack('<I', f.read(4))[0]
            tensor_count = struct.unpack('<Q', f.read(8))[0]
            kv_count = struct.unpack('<Q', f.read(8))[0]
            
            metadata = {}
            for _ in range(min(kv_count, 100)):
                key = read_string(f)
                if not key:
                    break
                val_type = struct.unpack('<I', f.read(4))[0]
                
                # We extract common string/uint keys of interest
                if val_type == 8: # STRING
                    val = read_string(f)
                    metadata[key] = val
                elif val_type in (0, 1, 2, 3): # 8-bit ints
                    f.seek(1, 1)
                elif val_type in (4, 5, 6): # 16-bit / 32-bit ints/floats
                    f.seek(4, 1)
                elif val_type in (7, 10, 11): # 64-bit
                    f.seek(8, 1)
                elif val_type == 9: # ARRAY
                    arr_type = struct.unpack('<I', f.read(4))[0]
                    arr_len = struct.unpack('<Q', f.read(8))[0]
                    # Skip array content safely
                    if arr_type == 8:
                        for _ in range(arr_len):
                            s = read_string(f)
                    elif arr_type in (0, 1, 2, 3):
                        f.seek(arr_len, 1)
                    elif arr_type in (4, 5, 6):
                        f.seek(arr_len * 4, 1)
                    elif arr_type in (7, 10, 11):
                        f.seek(arr_len * 8, 1)
            
            return {
                "valid": True,
                "version": version,
                "tensor_count": tensor_count,
                "kv_count": kv_count,
                "file_size_bytes": file_size,
                "file_size_mb": round(file_size / (1024 * 1024), 2),
                "architecture": metadata.get("general.architecture", "unknown"),
                "name": metadata.get("general.name", "unknown"),
                "file_type": metadata.get("general.file_type", "unknown")
            }
    except Exception as e:
        return {"valid": False, "error": str(e)}

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python validate_gguf.py <model.gguf>")
        sys.exit(1)
    res = validate_gguf(sys.argv[1])
    print(res)
