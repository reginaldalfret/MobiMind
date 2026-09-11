import { ToolDefinition } from '../talents/types';

export function formatToolDeclarations(tools: ToolDefinition[]): string {
  let declarations = '<start_function_declaration>\n';
  
  for (const tool of tools) {
    const fn = tool.function;
    declarations += `declaration:${fn.name}{\n`;
    declarations += `  description:<escape>${fn.description || ''}<escape>,\n`;
    
    if (fn.parameters) {
      declarations += `  parameters:{\n`;
      declarations += `    type:<escape>${(fn.parameters.type || 'OBJECT').toUpperCase()}<escape>,\n`;
      
      if (fn.parameters.properties) {
        declarations += `    properties:{\n`;
        const propKeys = Object.keys(fn.parameters.properties);
        for (let i = 0; i < propKeys.length; i++) {
          const key = propKeys[i];
          const prop = (fn.parameters.properties as Record<string, any>)[key];
          declarations += `      ${key}:{\n`;
          if (prop.description) {
            declarations += `        description:<escape>${prop.description}<escape>,\n`;
          }
          if (prop.type) {
            declarations += `        type:<escape>${String(prop.type).toUpperCase()}<escape>\n`;
          }
          declarations += `      }${i < propKeys.length - 1 ? ',' : ''}\n`;
        }
        declarations += `    }\n`;
      }
      declarations += `  }\n`;
    }
    declarations += `}\n`;
  }
  
  declarations += '<end_function_declaration>';
  return declarations;
}

export function parseFunctionCall(text: string): { name: string; arguments: Record<string, any> } | null {
  const match = text.match(/<start_function_call>call:([^{]+)\{(.*)\}<end_function_call>/s);
  if (!match) return null;

  const name = match[1].trim();
  const argsString = match[2];

  const args: Record<string, any> = {};
  
  const argRegex = /([a-zA-Z0-9_]+):<escape>(.*?)<escape>/gs;
  let argMatch;
  
  while ((argMatch = argRegex.exec(argsString)) !== null) {
    args[argMatch[1]] = argMatch[2];
  }

  return {
    name,
    arguments: args,
  };
}

export function formatFunctionResponse(name: string, result: Record<string, any>): string {
  const resultJson = JSON.stringify(result);
  return `<start_function_response>call:${name}{${resultJson}}<end_function_response>`;
}

export function buildFunctionGemmaSystemPrompt(tools: ToolDefinition[]): string {
  if (!tools || tools.length === 0) {
    return '';
  }
  return formatToolDeclarations(tools);
}
