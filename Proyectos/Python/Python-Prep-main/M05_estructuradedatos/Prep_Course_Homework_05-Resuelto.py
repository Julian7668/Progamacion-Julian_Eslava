#!/usr/bin/env python
# coding: utf-8

# ## Estructuras de Datos

# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla


lista = [
    "Buenos Aires",
    "Brasilia",
    "Asunción",
    "Montevideo",
    "Santiago",
    "Lima",
    "Caracas",
    "Bogotá",
]
print(lista)


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


lista.append("Ciudad de Méjico")


lista.append("Montevideo")


print(lista)


# 8) Agregar otra ciudad, pero en la cuarta posición


lista.insert(3, "Quito")


print(lista)


# 9) Concatenar otra lista a la ya creada


lista.extend(["Madrid", "Roma", "Bruselas"])
print(lista)


# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?


print(lista.index("Montevideo"))


# 11) ¿Qué pasa si se busca un elemento que no existe?


print(lista.index("París"))


# 12) Eliminar un elemento de la lista


lista.remove("Buenos Aires")


print(lista)


# 13) ¿Qué pasa si el elemento a eliminar no existe?


lista.remove("Buenos Aires")


# 14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo


ultimo = lista.pop()
print(ultimo)


# 15) Mostrar la lista multiplicada por 4


print(lista * 4)


# 16) Crear una tupla que contenga los números enteros del 1 al 20


tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
print(type(tupla))
print(tupla)


# 17) Imprimir desde el índice 10 al 15 de la tupla


print(tupla[10:16])


# 18) Evaluar si los números 20 y 30 están dentro de la tupla


print(20 in tupla)
print(30 in tupla)


# 19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.


elemento = "París"
if elemento not in lista:
    lista.append(elemento)
    print("Se insertó el elemento", elemento)
else:
    print("El elemento", elemento, "ya existía")


# 20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista


print(tupla.count(10))
print(lista.count("Montevideo"))


# 21) Convertir la tupla en una lista


lis2 = list(tupla)
print(lis2)


# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables


v1, v2, v3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _ = tupla
print(v1)
print(v2)
print(v3)


# 23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".


dicc = {
    "Ciudad": lista,
    "País": [
        "Brasil",
        "Paraguay",
        "Ecuador",
        "Uruguay",
        "Chile",
        "Perú",
        "Venezuela",
        "Colombia",
        "Méjico",
        "Uruguay",
        "España",
        "Italia",
        "Francia",
    ],
    "Continente": [
        "América",
        "América",
        "Europa",
        "Europa",
    ],
}


print(dicc)


# 24) Imprimir las claves del diccionario


print(dicc.keys())


# 25) Imprimir las ciudades a través de su clave


print(dicc["Ciudad"])
