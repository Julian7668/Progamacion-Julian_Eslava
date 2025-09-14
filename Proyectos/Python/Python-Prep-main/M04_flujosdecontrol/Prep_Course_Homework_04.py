import math
import questi
from utils import is_number_prime
import validates as V

# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla: si es mayor o menor a cero
numero: int = 5
print(
    numero,
    f"Es {'mayor' if numero > 0 else ('menor' if numero < 0 else 'igual')} a cero",
)

# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato
numero: int = 2
nombre: str = "Julian"
print(
    "Son del mismo tipo de dato"
    if isinstance(numero, type(nombre))
    else "No son del mismo tipo de dato"
)

# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar
print(
    *(
        f"{'Pares' if j == 0 else 'Impares'} serian los numeros: "
        + " ".join(str(i) for i in range(1, 21) if i % 2 == (0 if j == 0 else 1))
        for j in range(2)
    ),
    sep="\n",
)


# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3
# * correcto -> print(*(i**3 for i in range(6)))
for i in range(6):
    print(i**3, end=" ")
print()

# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos
ciclos: int = 5
# * correcto -> print("Chancho " * ciclos)
for _ in range(5):
    print("Chancho", end=" ")
print()

# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0
numero: int = 5
if not (
    isinstance(numero, int) and V.validate_range_num(numero, ((0, False), float("inf")))
):
    raise ValueError("El numero debe ser un entero mayor a 0")
lista: list[int] = []
i: int = 0
while numero - i != 1:
    lista.append(numero - i)
    i += 1
print(math.prod(lista))

# 7) Crear un ciclo for dentro de un ciclo while
i: int = 0
while i != 5:
    for _ in range(2):
        print("Chancho", end=" ")
    print()
    i += 1
print("FIN")

# 8) Crear un ciclo while dentro de un ciclo for
for _ in range(5):
    i: int = 0
    while i != 2:
        print("Chancho", end=" ")
        i += 1
    print()

# 9) Imprimir los números primos existentes entre 0 y 30
print(*(i for i in range(31) if is_number_prime(i)))

# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin
# ! No

# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?
# * Una linea todo lindo. Ubicada en utils

# 12) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300
# * correcta -> print(*(i for i in range(100, 301) if i % 12 == 0))
i: int = 99
while i <= 300:
    i += 1
    if i % 12 != 0:
        continue
    print(i, end=" ")
print()

# 13) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente
num: int = int(
    questi.text(
        "Ingrese el numero entero que quiera comprobar si es primo",
        validate=lambda x: V.validate_type(x, int),
    )
)
while True:
    print(
        num, "es primo!" if (resultado_bool := is_number_prime(num)) else "no es primo!"
    )
    if questi.confirm(
        "¿Le gustaria saber si el numero entero siguiente tambien es un numero primo?"
        if resultado_bool
        else "¿Le gustaria saber si el numero entero siguiente fuera un numero primo a diferencia de este?"
    ):
        num += 1
    else:
        break

# 14) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6
# * correcto -> print(next(i for i in range(100, 301) if i % 6 == 0))
i: int = 100
while i <= 300:
    if i % 6 == 0:
        print(i)
        break
    i += 1
