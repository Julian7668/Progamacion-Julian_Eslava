"use strict";

const NOMBRE_PERSONA: string = "Julian";
console.log(
  "Hola,",
  NOMBRE_PERSONA,
  "! Bienvenido a la programación en JavaScript."
);

let soyFeliz: boolean = false;
let miPapaEsFeliz: boolean = false;

if (soyFeliz) {
  console.log("Soy feliz");
} else if (miPapaEsFeliz) {
  console.log("Mi papa es feliz");
} else {
  console.log("¡Nadie es feliz!");
}
console.log();

import range from "./MDrange.ts";

for (let i of range(10)) {
  console.log(i + 1);
}
