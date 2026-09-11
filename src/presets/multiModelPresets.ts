import { Model, ModelOrigin } from '../utils/types';
import { chatTemplates } from '../utils/chat';
import { defaultCompletionParams } from '../utils/completionSettingsVersions';
import { ModelRuntimeType } from '../services/runtime/types';

export const MODEL_RUNTIME_MAP: Record<string, ModelRuntimeType> = {
  'functiongemma-270m-it': ModelRuntimeType.LLAMA_CPP,
  'gemma-3-270m-it': ModelRuntimeType.LLAMA_CPP,
};

export const MULTI_MODEL_PRESETS: Partial<Model>[] = [
  {
    id: 'functiongemma-270m-it',
    author: 'google',
    name: 'FunctionGemma 270M IT',
    size: 253127392,
    params: 270000000,
    isDownloaded: false,
    downloadUrl:
      'https://huggingface.co/bartowski/google_functiongemma-270m-it-GGUF/resolve/main/google_functiongemma-270m-it-Q4_K_M.gguf',
    hfUrl: 'https://huggingface.co/google/functiongemma-270m-it',
    filename: 'google_functiongemma-270m-it-Q4_K_M.gguf',
    isLocal: false,
    origin: ModelOrigin.PRESET,
    defaultChatTemplate: chatTemplates.gemmaIt,
    chatTemplate: chatTemplates.gemmaIt,
    defaultStopWords: ['<end_of_turn>', '<start_function_response>'],
    stopWords: ['<end_of_turn>', '<start_function_response>'],
    defaultCompletionSettings: defaultCompletionParams,
    completionSettings: defaultCompletionParams,
  },
  {
    id: 'gemma-3-270m-it',
    author: 'google',
    name: 'Gemma 3 270M IT',
    size: 253115168,
    params: 270000000,
    isDownloaded: false,
    downloadUrl:
      'https://huggingface.co/bartowski/google_gemma-3-270m-it-GGUF/resolve/main/google_gemma-3-270m-it-Q4_K_M.gguf',
    hfUrl: 'https://huggingface.co/google/gemma-3-270m-it',
    filename: 'google_gemma-3-270m-it-Q4_K_M.gguf',
    isLocal: false,
    origin: ModelOrigin.PRESET,
    defaultChatTemplate: chatTemplates.gemmaIt,
    chatTemplate: chatTemplates.gemmaIt,
    defaultStopWords: ['<end_of_turn>'],
    stopWords: ['<end_of_turn>'],
    defaultCompletionSettings: defaultCompletionParams,
    completionSettings: defaultCompletionParams,
  },
];
