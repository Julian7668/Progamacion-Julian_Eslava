export function validateRangeNum(
  number: number,
  validationRange: [number | [number, boolean], number | [number, boolean]] = [
    Number.NEGATIVE_INFINITY,
    Number.POSITIVE_INFINITY,
  ]
): boolean {
  let minimoRango: boolean;
  if (!Array.isArray(validationRange[0])) {
    minimoRango = number >= validationRange[0];
  } else {
    minimoRango = validationRange[0][1]
      ? number >= validationRange[0][0]
      : number > validationRange[0][0];
  }
  if (!minimoRango) return minimoRango;

  let maximoRango: boolean;
  if (!Array.isArray(validationRange[1])) {
    maximoRango = number <= validationRange[1];
  } else {
    maximoRango = validationRange[1][1]
      ? number <= validationRange[1][0]
      : number < validationRange[1][0];
  }
  return minimoRango && maximoRango;
}
