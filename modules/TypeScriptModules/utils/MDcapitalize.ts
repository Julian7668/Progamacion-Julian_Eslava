/**
 * Capitaliza la primera letra de una cadena y convierte el resto a minúsculas.
 *
 * @param str - La cadena a capitalizar
 * @returns La cadena con la primera letra en mayúscula y el resto en minúsculas
 *
 * @example
 * ```typescript
 * capitalize("hello")     // "Hello"
 * capitalize("WORLD")     // "World"
 * capitalize("")          // ""
 * capitalize("a")         // "A"
 * ```
 */
export function capitalize(str: string): string {
  if (!str) return str;
  return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
}

// Entry point para pruebas cuando se ejecuta directamente
if (import.meta.main) {
  // Ejemplos de capitalización
  const testCases: string[] = [
    "hello",
    "WORLD",
    "tEsT",
    "",
    "a",
    "JavaScript",
  ];

  console.log("Ejemplos de capitalización:");
  for (const testCase of testCases) {
    const result = capitalize(testCase);
    console.log(`'${testCase}' -> '${result}'`);
  }
}
