# MobiMind

> **Your AI. Your Device.**

MobiMind is a privacy-focused, multi-model mobile AI platform designed for completely local LLM inference, native tool execution, and verifiable automated task completion on Android.

---

## Architecture Overview

MobiMind separates natural human dialogue from tool calling using a high-efficiency **Dual-Engine Architecture**:
- **Conversational Brain:** The user's chosen LLM (Gemma 3 1B, Qwen 2.5 Coder 1.5B, Llama 3.2 1B, etc.) generates creative and conversational answers.
- **Action Engine:** Google FunctionGemma 270M runs locally to translate actionable intents into structured tool execution declarations.
- **Verification Loop:** Verifies tool outputs, gathers evidence, and presents confirmed results back to the user.

`
                      User Input
                          │
                          ▼
                     Selected LLM
                          │
                          ▼
                   Task Classifier
                   ├── CHAT
                   │    │
                   │    ▼
                   │  Selected LLM (Direct Response)
                   │
                   └── ACTION
                        │
                        ▼
                   FunctionGemma 270M (Action Engine)
                        │
                        ▼
                   Tool Executor (Native Android APIs)
                        │
                        ▼
                   Verification Engine
                        │
                        ▼
                   Evidence Collector
                        │
                        ▼
                   Selected LLM (Synthesis)
                        │
                        ▼
                   Final Response
`

---

## Key Features

- 🔒 **100% Private & Offline:** Zero telemetry. All inference, memory storage, and tool calls execute entirely on-device.
- ⚡ **Multi-Model Support:** Native support for cutting-edge GGUF v3 models optimized with 2-bit (Q2_K) and 4-bit (Q4_K_M) quantization.
- 🛠️ **Function Calling on Edge:** Dedicated action engine powered by FunctionGemma 270M.
- 📱 **RGB Neon Liquid Glass UI/UX:** Translucent glass cards, glowing gradient borders, fluid animations, and a modern 5-tab navigation.

---

## Supported Models Catalog

Model metadata and download specifications are maintained in config/models.json:

| Model | Size | Quant | Format | Best For |
|---|---|---|---|---|
| **Google FunctionGemma 270M** | ~241 MB | Q4_K_M | GGUF | Tool calling & Action Engine |
| **Google Gemma 3 270M** | ~241 MB | Q4_K_M | GGUF | Ultra-compact general dialogue |
| **Google Gemma 3 1B** | ~658 MB | Q2_K | GGUF | Edge NLP & Reasoning |
| **Qwen 2.5 Coder 1.5B** | ~645 MB | Q2_K | GGUF | Code synthesis & Troubleshooting |
| **Meta Llama 3.2 1B** | ~554 MB | Q2_K | GGUF | Fast conversational text |
| **IBM Granite 4.0 1B** | ~562 MB | Q2_K | GGUF | Enterprise RAG & Context |
| **SmolLM2 1.7B** | ~643 MB | Q2_K | GGUF | Reasoning & general chat |
| **Falcon3 1B** | ~693 MB | Q2_K | GGUF | Scientific & analytical QA |

---

## Build & Installation

### Prerequisites
- Node.js v20+ / v22 LTS & Yarn
- JDK 21 (JAVA_HOME pointing to OpenJDK 21)
- Android SDK (API 29+) & NDK 27+

### Compile Debug APK
`ash
yarn install
cd android
./gradlew assembleProdDebug
`

The resulting APK will be located at:
`	ext
android/app/build/outputs/apk/prod/debug/app-prod-debug.apk
`

### Install onto Device / Waydroid
`ash
adb install -r android/app/build/outputs/apk/prod/debug/app-prod-debug.apk
`

---

## Testing & Benchmarking on Waydroid / WSL2
MobiMind is continuously tested in Waydroid (Android 13 x86_64) under WSL2:
`ash
# Push model to local storage
adb push ./models/q2-test/google_gemma-3-1b-it-Q2_K.gguf /data/user/0/com.pocketpalai/files/models/local/

# Start Waydroid session & launch
waydroid session start
waydroid app launch com.pocketpalai
`

---

## Roadmap

- [x] llama.rn / llama.cpp local inference integration
- [x] 6-model 2-bit GGUF evaluation and benchmark suite
- [x] FunctionGemma 270M tool calling engine
- [x] Centralized model catalog (config/models.json)
- [x] RGB Neon Liquid Glass design system & UI components
- [ ] Cactus / Needle 2 C++ engine support for .cact models
- [ ] Hardware-accelerated NPU/DSP delegates (QNN / MediaTek NeuroPilot)

---

## Attribution & License

This project originated from and builds upon the open-source [PocketPal AI](https://github.com/a-ghorbani/pocketpal-ai) project by Asghar Ghorbani and contributors, licensed under the MIT License.

MobiMind introduces the Dual-Engine Action/Chat architecture, FunctionGemma agent verification pipelines, multi-model Q2_K catalog, and RGB Neon Liquid Glass design system.

See the [LICENSE](LICENSE) file for complete license terms.
