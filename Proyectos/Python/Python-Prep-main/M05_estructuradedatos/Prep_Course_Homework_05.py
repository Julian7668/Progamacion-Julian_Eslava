#!/usr/bin/env python
# coding: utf-8

# ## Estructuras de Datos

# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla
from typing import Union


print(lista := ["Tokio", "Nueva York", "París", "Bogotá", "Sídney"])

# 2) Imprimir por pantalla el segundo elemento de la lista
print(lista[1])

# 3) Imprimir por pantalla del segundo al cuarto elemento
print(lista[1:4])

# 4) Visualizar el tipo de dato de la lista
print(type(lista))

# 5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento
print(lista[2:])

# 6) Visualizar los primeros 4 elementos de la lista
print(lista[:4])

# 7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?
lista.append("Medellin")
# * Da error porque ´lista_chancha´ no esta definida
# lista_chancha.append("Cali")

# 8) Agregar otra ciudad, pero en la cuarta posición
lista.insert(3, "Dakota del norte")

# 9) Concatenar otra lista a la ya creada
# * El type hints me regaña
lista.extend(["4", "56", "61", "54", "34"])

# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?
print(lista.index("Medellin"))
# * Parece que insert no reemplaza solo añade hay el valor y el resto lo pasa para adelante

# 11) ¿Qué pasa si se busca un elemento que no existe?
# * Error
# print(lista[42])

# 12) Eliminar un elemento de la lista
lista.remove("Sídney")

# 13) ¿Qué pasa si el elemento a eliminar no existe?
# * Error
# lista.remove("Chanchito Feliz")

# 14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo
print(ultimo_elemento := lista[-1])

# 15) Mostrar la lista multiplicada por 4
print(lista * 4)

# 16) Crear una tupla que contenga los números enteros del 1 al 20
tupla = tuple(range(1, 21))

# 17) Imprimir desde el índice 10 al 15 de la tupla
print(tupla[10:16])
print()

# 18) Evaluar si los números 20 y 30 están dentro de la tupla
print(
    *(
        f"{'20' if j == 0 else '30'} {'Si esta en la tupla'if (20 in tupla if j == 0 else 30 in tupla) else 'No esta en la tupla'}"
        for j in range(2)
    ),
    sep="\n",
)


# 19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.
print(
    "'París' existe en la lista"
    if (resultado := lista.count("París") >= 1)
    else "Ahora, 'París' existe en la lista"
)
if resultado:
    lista.append("París")

# 20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista
print(
    *(
        f"""
'Nueva York' se encuentra en la {'tupla' if j == 0 else 'lista'} un total de {(resultado := (tupla if j == 0 else lista).count('Nueva York'))} {'veces' if resultado != 1 else 'vez'}"""
        for j in range(2)
    )
)

# 21) Convertir la tupla en una lista
ex_tupla = list(tupla)

# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables
var1, var2, var3 = tupla[:3]
print(var1, var2, var3)

# 23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".
diccionario = {
    "ciudad": lista,
    "pais": ["Japón", "Estados Unidos", "Francia", "Colombia", "Australia"],
    "continente": ["Asia", "América", "Europa"],
}

# 24) Imprimir las claves del diccionario
print(diccionario.keys())

# 25) Imprimir las ciudades a través de su clave
print(diccionario["ciudad"])


lis: list[Union[int, str, tuple]] = [1, 2, 3, 4, 5, 6, "Chancho", (4.2, 14.2)]
tupla = ("Paises:", "Colombia", "Argentina", "Brasil", "Chile", "Perú")
lis.append(tupla)
print(lis)
