# MobiMind Model Runtime Specification

## Supported Model Formats
MobiMind natively supports **GGUF v3** format powered by llama.cpp through the llama.rn React Native bridge.

### Model Catalog (Metadata Registered in config/models.json)

| Model | Publisher | Parameters | Quantization | Size (MB) | Primary Role |
|---|---|---|---|---|---|
| **FunctionGemma 270M** | Google | 270M | Q4_K_M | ~241 MB | Action Engine / Tool Calling |
| **Gemma 3 270M** | Google | 270M | Q4_K_M | ~241 MB | Compact On-Device Chat |
| **Gemma 3 1B** | Google | 1B | Q2_K | ~658 MB | Edge NLP / General Reasoning |
| **Qwen 2.5 Coder 1.5B** | Qwen | 1.5B | Q2_K | ~645 MB | Code Synthesis & Scripting |
| **Llama 3.2 1B** | Meta | 1B | Q2_K | ~554 MB | Fast Text & Conversational Chat |
| **IBM Granite 4.0 1B** | IBM | 1B | Q2_K | ~562 MB | Enterprise RAG & Tool Context |
| **SmolLM2 1.7B** | HuggingFaceTB | 1.7B | Q2_K | ~643 MB | Compact Reasoning & Synthesis |
| **Falcon3 1B** | TII | 1B | Q2_K | ~693 MB | Science & Math Assistant |

---

## Runtime Benchmarking
On modern x86_64 and ARM64 mobile hardware:
- **Time-to-First-Token (TTFT):** 400ms – 900ms across 1B models.
- **Generation Throughput:** 18 – 32 tokens/second on 4-8 thread CPU configurations.
- **Memory Footprint:** 1.2GB – 2.2GB total Resident Set Size (RSS) during active inference.
