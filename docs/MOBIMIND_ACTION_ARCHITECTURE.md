# MobiMind Action Architecture: The Dual-Engine Intelligence Loop

## Concept & Motivation
On-device models face an acute trade-off: larger conversational models (1B–3B) excel at dialogue and reasoning but struggle with strict, error-free function calling without massive system prompts that exhaust local context memory. Conversely, ultra-compact models (270M) can be fine-tuned specifically for precise schema generation.

MobiMind resolves this using a **Dual-Engine Architecture**:
1. **The Brain (Selected LLM):** Handles intent comprehension, natural conversation, user interaction, and response synthesis (e.g. Gemma 3 1B, Qwen 2.5 Coder 1.5B, Llama 3.2 1B).
2. **The Muscle (FunctionGemma 270M):** Functions behind the scenes as a dedicated Action Engine that converts user goals into structured tool invocations without consuming conversational context.

---

## Action Execution Flow

`
User Input
    │
    ▼
Selected LLM / Intent Classifier
    │
    ├───────────────┬────────────────┐
    │ [Chat Query]  │                │ [Actionable Query]
    ▼               │                ▼
Selected LLM        │        FunctionGemma 270M (Action Engine)
    │               │                │ (Emits <start_function_call>)
    │               │                ▼
    │               │        Tool Dispatcher & Native Executor
    │               │                │ (App Launch / File / Device Setting)
    │               │                ▼
    │               │        Verification Engine
    │               │                │ (Inspects exit code, state change)
    │               │                ▼
    │               │        Evidence Collector
    │               │                │ (Formats execution proof)
    │               ▼                ▼
    └──────────────► Selected LLM (Synthesis)
                            │
                            ▼
                     Final User Response
`

---

## Verification & Evidence States

1. **Requested:** User issues a task (e.g. Turn on Wi-Fi and open Notes).
2. **Executing:** Tool Dispatcher triggers the native Android capability or headless script.
3. **Verifying:** System executes post-action sanity check (e.g. checking system state or return value).
4. **Verified:** Grounded evidence is formatted into the conversational context, allowing the primary LLM to present a confirmed response to the user.
