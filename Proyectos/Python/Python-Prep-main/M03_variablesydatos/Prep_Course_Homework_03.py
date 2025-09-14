#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
print(numero := 5)

# 2) Imprimir el tipo de dato de la constante 8.5
print(type(8.5))

# 3) Imprimir el tipo de dato de la variable creada en el punto 1
print(type(numero))

# 4) Crear una variable que contenga tu nombre
nombre = "Julian"

# 5) Crear una variable que contenga un número complejo
numero_complejo = 1j

# 6) Mostrar el tipo de dato de la variable creada en el punto 5
print(type(numero_complejo))

# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
pi = 3.1416

# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
string_booleano = "True"
dato_booleano = True

# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8
print(type(string_booleano), type(dato_booleano))

# 10) Asignar a una variable, la suma de un número entero y otro decimal
variable_decimal = 10 + 15.4

# 11) Realizar una operación de suma de números complejos
suma_nums_complejos = 10j + 15j

# 12) Realizar una operación de suma de un número real y otro complejo
suma_num_real_and_complejo = 10 + 5j

# 13) Realizar una operación de multiplicación
print(15 * 4)

# 14) Mostrar el resultado de elevar 2 a la octava potencia
print(2 ^ 8)

# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
print(cociente := 27 / 4)

# 16) De la división anterior solamente mostrar la parte entera
print(int(cociente))

# 17) De la división de 27 entre 4 mostrar solamente el resto
print(27 % 4)

# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
print(6 * 4 + 3)

# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
print("chancho " + "Feliz!")

# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
print("2" == 2)

# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
print(int("2") == 2)

# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
# * Porque la parte entera de la decimal en un numero flotante se divide con un punto no con una coma

# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.
numero = 3
numero -= 1

print(numero)

# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
print(1 << 2)
# * Porque el numero binario del 1 es 0001. Realizada la operacion resulta en 0100; 2*2=4

# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
# * Porque no se pueden realizar sumas entre strings y numeros (enteros o flotantes)

# 26) Realizar una operación válida entre valores de tipo entero y string
print("Chanchito " * 5)
