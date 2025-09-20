import { capitalize } from "../utils/MDcapitalize.ts";

/**
 * Valida si una cadena puede convertirse al tipo especificado.
 *
 * Realiza validación básica de formato para conversión de tipos desde string.
 *
 * @param x - Cadena a validar
 * @param targetType - Tipo al que se quiere convertir (String, Boolean, Number)
 * @param isFloat - Si true, valida como número flotante en lugar de entero
 * @param strict - Si true, para float requiere punto decimal explícito
 * @returns True si la cadena puede convertirse al tipo, false en caso contrario
 *
 * @example
 * ```typescript
 * validateType("123", Number, false)  // true
 * validateType("true", Boolean)       // true
 * validateType("3.14", Number, true)  // true
 * validateType("abc", Number)         // false
 * ```
 */
export function validateType(
  x: string,
  targetType: Function,
  isFloat: boolean = false,
  strict: boolean = false
): boolean {
  if (targetType === String) return true;
  if (targetType === Boolean)
    return ["T", "True", "F", "False"].includes(capitalize(x));
  x = x.trim().replace(/^[+-]/, "");

  if (!isFloat) return x.match(/^\d+$/) !== null;
  return (x.includes(".") || !strict) && x.match(/^\d*\.?\d+$/) !== null;
}

// Entry point para pruebas cuando se ejecuta directamente
if (import.meta.main) {
  // Ejemplos de validación de tipos
  const testCases: Array<[string, Function, boolean?, boolean?]> = [
    ["123", Number],
    ["true", Boolean],
    ["3.14", Number, true],
    ["abc", Number],
    ["True", Boolean],
    ["hello", String],
  ];

  console.log("Ejemplos de validación de tipos:");
  for (const [value, expectedType, isFloat, strict] of testCases) {
    const result = validateType(value, expectedType, isFloat, strict);
    console.log(`'${value}' -> ${expectedType.name}: ${result}`);
  }
}
