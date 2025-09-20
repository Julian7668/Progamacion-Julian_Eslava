Algoritmo OperacionesConjuntos
    // ============================================================================
    // Descripci�n: Programa para realizar operaciones entre dos conjuntos num�ricos
    // Operaciones disponibles: Uni�n (A [UNION] B), Intersecci�n (A [INTERSECCION] B), Diferencia (A - B)
    // 
    // Autor: Julian Eslava
    // Fecha: 24/07/25
    // ============================================================================
    
    // Declaraci�n de variables y arreglos
    Definir conjuntoA, conjuntoB, resultado Como Entero
    Definir tamA, tamB, tamResultado, opcion, i Como Entero
    Dimension conjuntoA[20]   // Arreglo para almacenar el conjunto A (m�x 20 elementos)
    Dimension conjuntoB[20]   // Arreglo para almacenar el conjunto B (m�x 20 elementos)
    Dimension resultado[40]   // Arreglo para almacenar el resultado de la operaci�n
    
    // ----------------------------------------------------------------------------
    // Entrada del conjunto A
    // ----------------------------------------------------------------------------
    Escribir "=== ENTRADA DEL CONJUNTO A ==="
    Escribir "Ingrese el tama�o del conjunto A (max 20): "
    Leer tamA
    
    // Validaci�n de tama�o
    Mientras tamA < 1 O tamA > 20 Hacer
        Escribir "Tama�o inv�lido! Debe ser entre 1 y 20"
        Leer tamA
    FinMientras
    
    Escribir "Ingrese los elementos num�ricos del conjunto A:"
    Para i <- 1 Hasta tamA Hacer
        Escribir "Elemento ", i, ": "
        Leer conjuntoA[i]
    FinPara
    
    // ----------------------------------------------------------------------------
    // Entrada del conjunto B
    // ----------------------------------------------------------------------------
    Escribir "=== ENTRADA DEL CONJUNTO B ==="
    Escribir "Ingrese el tama�o del conjunto B (max 20): "
    Leer tamB
    
    // Validaci�n de tama�o
    Mientras tamB < 1 O tamB > 20 Hacer
        Escribir "Tama�o inv�lido! Debe ser entre 1 y 20"
        Leer tamB
    FinMientras
    
    Escribir "Ingrese los elementos num�ricos del conjunto B:"
    Para i <- 1 Hasta tamB Hacer
        Escribir "Elemento ", i, ": "
        Leer conjuntoB[i]
    FinPara
    
    // ----------------------------------------------------------------------------
    // Men� de operaciones
    // ----------------------------------------------------------------------------
    Repetir
        Escribir ""
        Escribir "=== MEN� DE OPERACIONES ==="
        Escribir "1. Uni�n (A [UNION] B)"
        Escribir "2. Intersecci�n (A [INTERSECCION] B)"
        Escribir "3. Diferencia (A - B)"
        Escribir "4. Salir"
        Escribir "Seleccione una operaci�n (1-4): "
        Leer opcion
        
        Segun opcion Hacer
            1: // Uni�n
                tamResultado <- UnionNumerica(conjuntoA, tamA, conjuntoB, tamB, resultado)
                Escribir "Uni�n (A [UNION] B): "
                MostrarConjunto(resultado, tamResultado)
                
            2: // Intersecci�n
                tamResultado <- InterseccionNumerica(conjuntoA, tamA, conjuntoB, tamB, resultado)
                Escribir "Intersecci�n (A [INTERSECCION] B): "
                Si tamResultado = 0 Entonces
                    Escribir "Conjunto vac�o"
                Sino
                    MostrarConjunto(resultado, tamResultado)
                FinSi
                
            3: // Diferencia
                tamResultado <- DiferenciaNumerica(conjuntoA, tamA, conjuntoB, tamB, resultado)
                Escribir "Diferencia (A - B): "
                Si tamResultado = 0 Entonces
                    Escribir "Conjunto vac�o"
                Sino
                    MostrarConjunto(resultado, tamResultado)
                FinSi
                
            4: // Salir
                Escribir "Saliendo del programa..."
                
            De Otro Modo:
                Escribir "Opci�n inv�lida! Intente nuevamente."
        FinSegun
    Hasta Que opcion = 4
FinAlgoritmo

// ================================================================================
// SUBPROGRAMAS
// ================================================================================

// Funci�n para mostrar un conjunto
Funcion MostrarConjunto(conjunto Por Referencia, tam)
    Definir i Como Entero
    Para i <- 1 Hasta tam Hacer
        Escribir conjunto[i], " " Sin Bajar
    FinPara
    Escribir "" // Salto de l�nea
FinFuncion

// Funci�n para calcular la uni�n
Funcion tamUnion <- UnionNumerica(conjuntoA Por Referencia, tamA, conjuntoB Por Referencia, tamB, resultado Por Referencia)
    Definir i, j Como Entero
    Definir existe Como Logico
    
    tamUnion <- 0
    
    // Procesar conjunto A (elementos �nicos)
    Para i <- 1 Hasta tamA Hacer
        existe <- Falso
        Si tamUnion > 0 Entonces
            Para j <- 1 Hasta tamUnion Hacer
                Si conjuntoA[i] = resultado[j] Entonces
                    existe <- Verdadero
                FinSi
            FinPara
        FinSi
        Si existe = Falso Entonces
            tamUnion <- tamUnion + 1
            resultado[tamUnion] <- conjuntoA[i]
        FinSi
    FinPara
    
    // Procesar conjunto B (elementos �nicos)
    Para i <- 1 Hasta tamB Hacer
        existe <- Falso
        Si tamUnion > 0 Entonces
            Para j <- 1 Hasta tamUnion Hacer
                Si conjuntoB[i] = resultado[j] Entonces
                    existe <- Verdadero
                FinSi
            FinPara
        FinSi
        Si existe = Falso Entonces
            tamUnion <- tamUnion + 1
            resultado[tamUnion] <- conjuntoB[i]
        FinSi
    FinPara
FinFuncion

// Funci�n para calcular la intersecci�n (corregida)
Funcion tamInterseccion <- InterseccionNumerica(conjuntoA Por Referencia, tamA, conjuntoB Por Referencia, tamB, resultado Por Referencia)
    Definir i, j, k Como Entero
    Definir encontrado, duplicado Como Logico
    
    tamInterseccion <- 0
    
    // Recorrer elementos de A
    Para i <- 1 Hasta tamA Hacer
        encontrado <- Falso
        
        // Verificar si elemento de A est� en B (sin modificar j)
        j <- 1
        Mientras j <= tamB Y encontrado = Falso Hacer
            Si conjuntoA[i] = conjuntoB[j] Entonces
                encontrado <- Verdadero
            FinSi
            j <- j + 1
        FinMientras
        
        // Si est� en ambos conjuntos, verificar duplicados
        Si encontrado Entonces
            duplicado <- Falso
            Si tamInterseccion > 0 Entonces
                k <- 1
                Mientras k <= tamInterseccion Y duplicado = Falso Hacer
                    Si conjuntoA[i] = resultado[k] Entonces
                        duplicado <- Verdadero
                    FinSi
                    k <- k + 1
                FinMientras
            FinSi
            
            // Agregar si no es duplicado
            Si duplicado = Falso Entonces
                tamInterseccion <- tamInterseccion + 1
                resultado[tamInterseccion] <- conjuntoA[i]
            FinSi
        FinSi
    FinPara
FinFuncion

// Funci�n para calcular la diferencia (A - B)
Funcion tamDiferencia <- DiferenciaNumerica(conjuntoA Por Referencia, tamA, conjuntoB Por Referencia, tamB, resultado Por Referencia)
    Definir i, j, k Como Entero
    Definir encontrado, duplicado Como Logico
    
    tamDiferencia <- 0
    
    // Recorrer elementos de A
    Para i <- 1 Hasta tamA Hacer
        encontrado <- Falso
        
        // Verificar si elemento de A est� en B (sin modificar j)
        j <- 1
        Mientras j <= tamB Y encontrado = Falso Hacer
            Si conjuntoA[i] = conjuntoB[j] Entonces
                encontrado <- Verdadero
            FinSi
            j <- j + 1
        FinMientras
		
        // Si no est� en B, verificar duplicados
        Si encontrado = Falso Entonces
            duplicado <- Falso
            Si tamDiferencia > 0 Entonces
                k <- 1
                Mientras k <= tamDiferencia Y duplicado = Falso Hacer
                    Si conjuntoA[i] = resultado[k] Entonces
                        duplicado <- Verdadero
                    FinSi
                    k <- k + 1
                FinMientras
            FinSi
            
            // Agregar si no es duplicado
            Si duplicado = Falso Entonces
                tamDiferencia <- tamDiferencia + 1
                resultado[tamDiferencia] <- conjuntoA[i]
            FinSi
        FinSi
    FinPara
FinFuncion