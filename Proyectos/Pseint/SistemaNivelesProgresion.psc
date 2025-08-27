Algoritmo SistemaNivelesProgresion
	Definir nivelActual, puntosTotales Como Entero
	Definir nombreUsuario Como Caracter
	Definir leccionesCompletadas Como Entero
	Definir wifiCompleto, bluetoothCompleto, llamadasCompleto, correoCompleto Como Logico
	Definir opcion Como Entero
	Definir progresoGeneral Como Real
	
	nivelActual <- 1
	puntosTotales <- 0
	leccionesCompletadas <- 0
	wifiCompleto <- Falso
	bluetoothCompleto <- Falso
	llamadasCompleto <- Falso
	correoCompleto <- Falso
	
	Escribir "=============================================="
	Escribir "    SISTEMA DE NIVELES Y PROGRESION"
	Escribir "      Aplicacion Educativa Digital"
	Escribir "=============================================="
	Escribir ""
	Escribir "Ingrese su nombre:"
	Leer nombreUsuario
	
	Repetir
		Limpiar Pantalla
		
		Escribir "=============================================="
		Escribir "Usuario: ", nombreUsuario
		Escribir "Nivel Actual: ", nivelActual, "/4"
		Escribir "Puntos Totales: ", puntosTotales
		Escribir "Lecciones Completadas: ", leccionesCompletadas, "/4"
		Escribir "=============================================="
		Escribir ""
		
		Escribir "PROGRESO POR NIVELES:"
		Escribir ""
		
		Escribir "NIVEL 1 - Fundamentos WiFi"
		Si wifiCompleto Entonces
			Escribir "   Estado: COMPLETADO"
			Escribir "   Puntos: 25/25"
		SiNo
			Si nivelActual >= 1 Entonces
				Escribir "   Estado: DISPONIBLE"
				Escribir "   Puntos: 0/25"
			SiNo
				Escribir "   Estado: BLOQUEADO"
			FinSi
		FinSi
		Escribir ""
		
		Escribir "NIVEL 2 - Conexion Bluetooth"
		Si bluetoothCompleto Entonces
			Escribir "   Estado: COMPLETADO"
			Escribir "   Puntos: 30/30"
		SiNo
			Si nivelActual >= 2 Entonces
				Escribir "   Estado: DESBLOQUEADO"
				Escribir "   Puntos: 0/30"
			SiNo
				Escribir "   Estado: BLOQUEADO"
				Escribir "   Requisito: Completar Nivel 1"
			FinSi
		FinSi
		Escribir ""
		
		Escribir "NIVEL 3 - Realizar Llamadas"
		Si llamadasCompleto Entonces
			Escribir "   Estado: COMPLETADO"
			Escribir "   Puntos: 35/35"
		SiNo
			Si nivelActual >= 3 Entonces
				Escribir "   Estado: DESBLOQUEADO"
				Escribir "   Puntos: 0/35"
			SiNo
				Escribir "   Estado: BLOQUEADO"
				Escribir "   Requisito: Completar Nivel 2"
			FinSi
		FinSi
		Escribir ""
		
		Escribir "NIVEL 4 - Enviar Correos"
		Si correoCompleto Entonces
			Escribir "   Estado: COMPLETADO"
			Escribir "   Puntos: 40/40"
		SiNo
			Si nivelActual >= 4 Entonces
				Escribir "   Estado: DESBLOQUEADO"
				Escribir "   Puntos: 0/40"
			SiNo
				Escribir "   Estado: BLOQUEADO"
				Escribir "   Requisito: Completar Nivel 3"
			FinSi
		FinSi
		Escribir ""
		
		progresoGeneral <- (leccionesCompletadas * 100) / 4
		
		Escribir "PROGRESO GENERAL: ", progresoGeneral, "%"
		Escribir "===================="
		Escribir ""
		
		Escribir "======== OPCIONES ========"
		Escribir "1. Completar leccion actual"
		Escribir "2. Ver detalles de niveles"
		Escribir "3. Simular completar leccion"
		Escribir "4. Ver logros y medallas"
		Escribir "5. Reiniciar progreso"
		Escribir "0. Salir"
		Escribir ""
		Escribir "Seleccione opcion:"
		Leer opcion
		
		Segun opcion Hacer
			Caso 1:
				Escribir ""
				Si nivelActual = 1 Y NO wifiCompleto Entonces
					Escribir "COMPLETANDO: Leccion de WiFi"
					Escribir "Simulando examen..."
					Escribir "Examen aprobado!"
					puntosTotales <- puntosTotales + 25
					wifiCompleto <- Verdadero
					leccionesCompletadas <- leccionesCompletadas + 1
					nivelActual <- 2
					Escribir "WiFi completado - +25 puntos"
					Escribir "Nivel 2 desbloqueado!"
					
				SiNo
					Si nivelActual = 2 Y NO bluetoothCompleto Entonces
						Escribir "COMPLETANDO: Leccion de Bluetooth"
						Escribir "Simulando examen..."
						Escribir "Examen aprobado!"
						puntosTotales <- puntosTotales + 30
						bluetoothCompleto <- Verdadero
						leccionesCompletadas <- leccionesCompletadas + 1
						nivelActual <- 3
						Escribir "Bluetooth completado - +30 puntos"
						Escribir "Nivel 3 desbloqueado!"
						
					SiNo
						Si nivelActual = 3 Y NO llamadasCompleto Entonces
							Escribir "COMPLETANDO: Leccion de Llamadas"
							Escribir "Simulando examen..."
							Escribir "Examen aprobado!"
							puntosTotales <- puntosTotales + 35
							llamadasCompleto <- Verdadero
							leccionesCompletadas <- leccionesCompletadas + 1
							nivelActual <- 4
							Escribir "Llamadas completado - +35 puntos"
							Escribir "Nivel 4 desbloqueado!"
							
						SiNo
							Si nivelActual = 4 Y NO correoCompleto Entonces
								Escribir "COMPLETANDO: Leccion de Correo"
								Escribir "Simulando examen..."
								Escribir "Examen aprobado!"
								puntosTotales <- puntosTotales + 40
								correoCompleto <- Verdadero
								leccionesCompletadas <- leccionesCompletadas + 1
								Escribir "Correo completado - +40 puntos"
								Escribir "FELICITACIONES! Completaste todo!"
								Escribir "Eres un EXPERTO DIGITAL!"
								
							SiNo
								Escribir "No hay lecciones disponibles"
							FinSi
						FinSi
					FinSi
				FinSi
				
				Escribir ""
				Escribir "Presione ENTER..."
				Esperar Tecla
				
			Caso 2:
				Escribir ""
				Escribir "DETALLES DE NIVELES:"
				Escribir ""
				Escribir "NIVEL 1 - WiFi (25 puntos)"
				Escribir "   - Que es el WiFi"
				Escribir "   - Como conectarse"
				Escribir "   - Solucion de problemas"
				Escribir ""
				Escribir "NIVEL 2 - Bluetooth (30 puntos)"
				Escribir "   - Activar Bluetooth"
				Escribir "   - Emparejar dispositivos"
				Escribir "   - Transferir archivos"
				Escribir ""
				Escribir "NIVEL 3 - Llamadas (35 puntos)"
				Escribir "   - Realizar llamadas"
				Escribir "   - Contestar llamadas"
				Escribir "   - Gestionar contactos"
				Escribir ""
				Escribir "NIVEL 4 - Correo (40 puntos)"
				Escribir "   - Configurar email"
				Escribir "   - Enviar mensajes"
				Escribir "   - Adjuntar archivos"
				Escribir ""
				Escribir "Presione ENTER..."
				Esperar Tecla
				
			Caso 3:
				Definir leccionSim Como Entero
				Escribir ""
				Escribir "MODO SIMULACION"
				Escribir "Que leccion marcar como completada?"
				Escribir "1. WiFi (Nivel 1)"
				Escribir "2. Bluetooth (Nivel 2)"
				Escribir "3. Llamadas (Nivel 3)"
				Escribir "4. Correo (Nivel 4)"
				Escribir "0. Cancelar"
				Leer leccionSim
				
				Segun leccionSim Hacer
					Caso 1:
						Si NO wifiCompleto Entonces
							wifiCompleto <- Verdadero
							puntosTotales <- puntosTotales + 25
							leccionesCompletadas <- leccionesCompletadas + 1
							Si nivelActual < 2 Entonces
								nivelActual <- 2
							FinSi
							Escribir "WiFi marcado como completado"
						SiNo
							Escribir "WiFi ya completado"
						FinSi
					Caso 2:
						Si NO bluetoothCompleto Entonces
							bluetoothCompleto <- Verdadero
							puntosTotales <- puntosTotales + 30
							leccionesCompletadas <- leccionesCompletadas + 1
							Si nivelActual < 3 Entonces
								nivelActual <- 3
							FinSi
							Escribir "Bluetooth marcado como completado"
						SiNo
							Escribir "Bluetooth ya completado"
						FinSi
					Caso 3:
						Si NO llamadasCompleto Entonces
							llamadasCompleto <- Verdadero
							puntosTotales <- puntosTotales + 35
							leccionesCompletadas <- leccionesCompletadas + 1
							Si nivelActual < 4 Entonces
								nivelActual <- 4
							FinSi
							Escribir "Llamadas marcado como completado"
						SiNo
							Escribir "Llamadas ya completado"
						FinSi
					Caso 4:
						Si NO correoCompleto Entonces
							correoCompleto <- Verdadero
							puntosTotales <- puntosTotales + 40
							leccionesCompletadas <- leccionesCompletadas + 1
							Escribir "Correo marcado como completado"
						SiNo
							Escribir "Correo ya completado"
						FinSi
					Caso 0:
						Escribir "Cancelado"
				FinSegun
				
				Escribir ""
				Escribir "Presione ENTER..."
				Esperar Tecla
				
			Caso 4:
				Escribir ""
				Escribir "LOGROS Y MEDALLAS:"
				Escribir ""
				
				Si puntosTotales >= 25 Entonces
					Escribir "Bronce Digital - Primeros 25 puntos"
				FinSi
				Si puntosTotales >= 50 Entonces
					Escribir "Plata Tecnologica - 50 puntos"
				FinSi
				Si puntosTotales >= 100 Entonces
					Escribir "Oro Conectado - 100 puntos"
				FinSi
				Si puntosTotales >= 130 Entonces
					Escribir "Diamante Digital - Puntaje maximo"
				FinSi
				
				Si wifiCompleto Entonces
					Escribir "Maestro WiFi - Conexion perfecta"
				FinSi
				Si bluetoothCompleto Entonces
					Escribir "Experto Bluetooth - Sin cables"
				FinSi
				Si llamadasCompleto Entonces
					Escribir "Comunicador Estrella - Conectado"
				FinSi
				Si correoCompleto Entonces
					Escribir "Cartero Digital - Sin limites"
				FinSi
				
				Si wifiCompleto Y bluetoothCompleto Y llamadasCompleto Y correoCompleto Entonces
					Escribir "GRADUADO DIGITAL SUPREMO"
					Escribir "Has dominado toda la tecnologia!"
				FinSi
				
				Escribir ""
				Escribir "Presione ENTER..."
				Esperar Tecla
				
			Caso 5:
				Definir confirmacion Como Caracter
				Escribir ""
				Escribir "Seguro que desea reiniciar TODO?"
				Escribir "Esta accion NO se puede deshacer."
				Escribir ""
				Escribir "Escriba SI para confirmar:"
				Leer confirmacion
				
				Si confirmacion = "SI" O confirmacion = "si" Entonces
					nivelActual <- 1
					puntosTotales <- 0
					leccionesCompletadas <- 0
					wifiCompleto <- Falso
					bluetoothCompleto <- Falso
					llamadasCompleto <- Falso
					correoCompleto <- Falso
					
					Escribir ""
					Escribir "Progreso reiniciado"
					Escribir "Empezamos desde el principio!"
				SiNo
					Escribir ""
					Escribir "Reinicio cancelado"
				FinSi
				
				Escribir ""
				Escribir "Presione ENTER..."
				Esperar Tecla
				
			Caso 0:
				Escribir ""
				Escribir "Hasta la vista, ", nombreUsuario, "!"
				Escribir "Tu progreso se ha guardado."
				
			De Otro Modo:
				Escribir ""
				Escribir "Opcion no valida."
				Escribir "Presione ENTER..."
				Esperar Tecla
		FinSegun
		
	Hasta Que opcion = 0
	
FinAlgoritmo