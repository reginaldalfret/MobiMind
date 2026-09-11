import sqlite3
import json
import uuid
import os

# Configurable paths via environment variables with standard defaults
script_dir = os.path.dirname(os.path.abspath(__file__))
manifest_path = os.environ.get('BENCHMARK_MANIFEST', os.path.join(script_dir, '..', 'config', 'q2-model-benchmark.json'))

default_db = os.path.expanduser('~/.local/share/waydroid/data/data/com.pocketpalai/databases/RKStorage')
db_path = os.environ.get('WAYDROID_DB_PATH', default_db)
if not os.path.exists(db_path):
    print(f"Error: Database {db_path} does not exist")
    exit(1)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()
r = cursor.execute("SELECT value FROM catalystLocalStorage WHERE key='ModelStore'").fetchone()
if not r:
    print("Error: ModelStore key not found")
    exit(1)

data = json.loads(r[0])
existing_models = {m.get('filename', ''): m for m in data.get('models', [])}

# Load benchmark manifest
with open(manifest_path, 'r') as f:
    manifest = json.load(f)

# Baseline model
baseline_cfg = manifest['baseline']
baseline_fname = baseline_cfg['filename']
if baseline_fname not in existing_models:
    existing_models[baseline_fname] = {
        "id": "baseline-smollm2-135m",
        "author": baseline_cfg["publisher"],
        "name": baseline_cfg["display_name"],
        "size": 105454432,
        "params": baseline_cfg["parameter_count"],
        "isDownloaded": True,
        "downloadUrl": "",
        "hfUrl": "https://huggingface.co/HuggingFaceTB/SmolLM2-135M-Instruct-GGUF",
        "progress": 100,
        "filename": baseline_fname,
        "fullPath": f"/data/user/0/com.pocketpalai/files/models/local/{baseline_fname}",
        "isLocal": True,
        "origin": "local",
        "defaultChatTemplate": {
            "addBosToken": False, "addEosToken": False, "bosToken": "", "eosToken": "",
            "chatTemplate": "", "addGenerationPrompt": True, "systemPrompt": "", "name": "custom"
        },
        "chatTemplate": {
            "addBosToken": False, "addEosToken": False, "bosToken": "", "eosToken": "",
            "chatTemplate": "", "addGenerationPrompt": True, "systemPrompt": "", "name": "custom"
        },
        "defaultCompletionSettings": {
            "version": 4, "include_thinking_in_context": True, "prompt": "", "n_predict": -1,
            "temperature": 0.7, "top_k": 40, "top_p": 0.95, "min_p": 0.05, "xtc_threshold": 0.1,
            "xtc_probability": 0, "typical_p": 1, "penalty_last_n": 64, "penalty_repeat": 1,
            "penalty_freq": 0, "penalty_present": 0, "mirostat": 0, "mirostat_tau": 5,
            "mirostat_eta": 0.1, "seed": -1, "n_probs": 0, "stop": [], "jinja": True, "enable_thinking": True
        },
        "completionSettings": {
            "version": 4, "include_thinking_in_context": True, "prompt": "", "n_predict": -1,
            "temperature": 0.7, "top_k": 40, "top_p": 0.95, "min_p": 0.05, "xtc_threshold": 0.1,
            "xtc_probability": 0, "typical_p": 1, "penalty_last_n": 64, "penalty_repeat": 1,
            "penalty_freq": 0, "penalty_present": 0, "mirostat": 0, "mirostat_tau": 5,
            "mirostat_eta": 0.1, "seed": -1, "n_probs": 0, "stop": [], "jinja": True, "enable_thinking": True
        },
        "defaultStopWords": [],
        "stopWords": [],
        "supportsMultimodal": False,
        "isRulePreset": False
    }

# Six Q2 models
registered_list = [existing_models[baseline_fname]]
for m_spec in manifest['models']:
    fname = m_spec['filename']
    models_dir = os.environ.get('WAYDROID_MODELS_PATH', os.path.expanduser('~/.local/share/waydroid/data/data/com.pocketpalai/files/models/local'))
    host_path = os.path.join(models_dir, fname)
    file_size = os.path.getsize(host_path) if os.path.exists(host_path) else m_spec.get('expected_size_mb', 500) * 1024 * 1024
    
    entry = {
        "id": m_spec["model_id"],
        "author": m_spec["publisher"],
        "name": f"{m_spec['display_name']} [Q2_TEST]",
        "size": file_size,
        "params": m_spec["parameter_count"],
        "isDownloaded": True,
        "downloadUrl": "",
        "hfUrl": m_spec["source_url"],
        "progress": 100,
        "filename": fname,
        "fullPath": local_path,
        "isLocal": True,
        "origin": "local",
        "defaultChatTemplate": {
            "addBosToken": False, "addEosToken": False, "bosToken": "", "eosToken": "",
            "chatTemplate": "", "addGenerationPrompt": True, "systemPrompt": "", "name": m_spec.get("chat_template", "custom")
        },
        "chatTemplate": {
            "addBosToken": False, "addEosToken": False, "bosToken": "", "eosToken": "",
            "chatTemplate": "", "addGenerationPrompt": True, "systemPrompt": "", "name": m_spec.get("chat_template", "custom")
        },
        "defaultCompletionSettings": {
            "version": 4, "include_thinking_in_context": True, "prompt": "", "n_predict": -1,
            "temperature": 0.7, "top_k": 40, "top_p": 0.95, "min_p": 0.05, "xtc_threshold": 0.1,
            "xtc_probability": 0, "typical_p": 1, "penalty_last_n": 64, "penalty_repeat": 1,
            "penalty_freq": 0, "penalty_present": 0, "mirostat": 0, "mirostat_tau": 5,
            "mirostat_eta": 0.1, "seed": -1, "n_probs": 0, "stop": m_spec.get("stop_words", []),
            "jinja": True, "enable_thinking": True
        },
        "completionSettings": {
            "version": 4, "include_thinking_in_context": True, "prompt": "", "n_predict": -1,
            "temperature": 0.7, "top_k": 40, "top_p": 0.95, "min_p": 0.05, "xtc_threshold": 0.1,
            "xtc_probability": 0, "typical_p": 1, "penalty_last_n": 64, "penalty_repeat": 1,
            "penalty_freq": 0, "penalty_present": 0, "mirostat": 0, "mirostat_tau": 5,
            "mirostat_eta": 0.1, "seed": -1, "n_probs": 0, "stop": m_spec.get("stop_words", []),
            "jinja": True, "enable_thinking": True
        },
        "defaultStopWords": m_spec.get("stop_words", []),
        "stopWords": m_spec.get("stop_words", []),
        "supportsMultimodal": False,
        "isRulePreset": False
    }
    registered_list.append(entry)
    print(f"Registered: {entry['name']} -> {fname}")

data['models'] = registered_list
cursor.execute("UPDATE catalystLocalStorage SET value=? WHERE key='ModelStore'", (json.dumps(data),))
conn.commit()
print(f"Successfully registered {len(registered_list)} models in ModelStore database.")
conn.close()
