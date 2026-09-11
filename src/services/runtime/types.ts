/**
 * Runtime abstraction layer for model support.
 */

export enum ModelRuntimeType {
  /** Standard llama.cpp via llama.rn — handles GGUF models */
  LLAMA_CPP = 'llama_cpp',
}

/**
 * Capabilities a model runtime can declare.
 */
export interface RuntimeCapabilities {
  streaming: boolean;
  toolCalling: boolean;
  multimodal: boolean;
  reasoning: boolean;
  draftDecoding: boolean;
}

export interface ModelRuntimeConfig {
  runtimeType: ModelRuntimeType;
  capabilities: RuntimeCapabilities;
  toolCallingFormat?: 'openai' | 'functiongemma';
}

/** Capabilities for FunctionGemma (llama.cpp with tool calling) */
export const FUNCTIONGEMMA_CAPABILITIES: RuntimeCapabilities = {
  streaming: true,
  toolCalling: true,
  multimodal: false,
  reasoning: false,
  draftDecoding: false,
};

/** Capabilities for Gemma 3 270M (llama.cpp general chat) */
export const GEMMA3_CAPABILITIES: RuntimeCapabilities = {
  streaming: true,
  toolCalling: false,
  multimodal: false,
  reasoning: false,
  draftDecoding: false,
};
