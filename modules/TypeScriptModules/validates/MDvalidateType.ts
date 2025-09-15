import { capitalize } from "@/utils";

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
