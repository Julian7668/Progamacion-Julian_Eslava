/**
 * Genera un array de números desde 0 hasta n-1.
 *
 * Equivalente a range(n) en Python, útil para crear secuencias numéricas.
 *
 * @param n - El número de elementos a generar (límite superior exclusivo)
 * @returns Array de números desde 0 hasta n-1
 *
 * @example
 * ```typescript
 * range(5)    // [0, 1, 2, 3, 4]
 * range(0)    // []
 * range(1)    // [0]
 * range(3)    // [0, 1, 2]
 * ```
 */
export function range(n: number): number[] {
  return Array.from({ length: n }, (_, i) => i);
}

// Entry point para pruebas cuando se ejecuta directamente
if (import.meta.main) {
  // Ejemplos de generación de rangos
  const testCases: number[] = [0, 1, 3, 5, 10];

  console.log("Ejemplos de generación de rangos:");
  for (const n of testCases) {
    const result = range(n);
    console.log(`range(${n}): [${result.join(", ")}]`);
  }
}
