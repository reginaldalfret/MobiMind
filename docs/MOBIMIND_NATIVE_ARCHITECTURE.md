# MobiMind Native Architecture

## Overview
MobiMind is an on-device, privacy-first mobile AI application targeting Android. It enables multi-model local inference, native tool execution, and multi-turn conversational agents with zero cloud telemetry.

---

## Architecture Status Matrix

| Component | Status | Details |
|---|---|---|
| **llama.rn Runtime (llama.cpp)** | **IMPLEMENTED** | High-performance C++ inference engine bound via JNI for Android x86_64 and arm64-v8a. |
| **Model Registry & Manifest** | **IMPLEMENTED** | Dynamic model discovery and management (config/models.json) supporting GGUF quantizations. |
| **FunctionGemma Action Engine** | **IMPLEMENTED** | Specialized 270M parameter tool-calling engine for local intent translation and tool dispatch. |
| **Dual-Engine (Chat vs Action)** | **IMPLEMENTED** | Routing conversation queries to the primary LLM and actionable queries to FunctionGemma. |
| **Verification & Evidence System** | **IMPLEMENTED** | Multi-phase state machine (Requested → Executing → Verifying → Verified). |
| **RGB Neon Liquid Glass UI/UX** | **EXPERIMENTAL** | Modernized theme tokens and design system inspired by the fluid neon aesthetic. |
| **Cactus / Needle 2 C++ Runtime** | **PLANNED** | Integration of proprietary .cact format when x86_64/arm64 unified native libs are finalized. |

---

## Native Android Stack
- **OS Compatibility:** Android 10+ (API level 29+), verified on Android 13 (LineageOS 20 under Waydroid) and physical ARM64 hardware.
- **Native Inference Engine:** llama.rn (v0.13.0-rc.1) utilizing llama.cpp upstream.
- **Acceleration:** CPU multi-threading, Hexagon DSP / NNAPI (where supported), and OpenCL/Vulkan backend hooks.
- **Memory Optimization:** 2-bit (Q2_K) and 4-bit (Q4_K_M) quantization support, enabling 1B-1.7B models to run comfortably within 1.5GB - 2.5GB RAM allocations.
