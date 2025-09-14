function validateType(
  x: string,
  typeObjective: Function = String,
  isFloat: boolean,
  strict: boolean
): boolean {
  return (
    typeObjective === String ||
    (typeObjective === Boolean
      ? ["T", "True", "F", "False"].includes(capitalize(x))
      : !isFloat
      ? x.trim().replace(/^[+-]/, "").match(/^\d+$/) !== null
      : x.includes(".") || !strict
      ? x
          .trim()
          .replace(/^[+-]/, "")
          .match(/^\d*\.?\d+$/) !== null
      : false)
  );
}
