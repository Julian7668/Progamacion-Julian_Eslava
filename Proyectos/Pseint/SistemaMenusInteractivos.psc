Algoritmo SistemaMenusInteractivos
	Definir opcionPrincipal, opcionSecundaria Como Entero
	Definir nombreUsuario Como Caracter
	Definir continuar Como Logico
	Definir accesoWifi, accesoBluetooth, accesoLlamadas, accesoCorreo Como Logico
	
	accesoWifi <- Verdadero
	accesoBluetooth <- Verdadero
	accesoLlamadas <- Verdadero
	accesoCorreo <- Verdadero
	
	Limpiar Pantalla
	Escribir "=============================================="
	Escribir "      SISTEMA DE MENUS INTERACTIVOS"
	Escribir "        Aprendizaje Digital Facil"
	Escribir "       Para la Tercera Edad"
	Escribir "=============================================="
	Escribir ""
	Escribir "Por favor, ingrese su nombre:"
	Leer nombreUsuario
	
	continuar <- Verdadero
	
	Mientras continuar Hacer
		Limpiar Pantalla
		Escribir "=============================================="
		Escribir "  Hola ", nombreUsuario, "! Que desea aprender hoy?"
		Escribir "=============================================="
		Escribir ""
		Escribir "======== MENU PRINCIPAL ========"
		Escribir ""
		
		Escribir "1. APRENDER SOBRE WiFi"
		Si accesoWifi Entonces
			Escribir "   Disponible - Conectarse a Internet"
		SiNo
			Escribir "   Bloqueado"
		FinSi
		Escribir ""
		
		Escribir "2. APRENDER SOBRE BLUETOOTH"
		Si accesoBluetooth Entonces
			Escribir "   Disponible - Conexion sin cables"
		SiNo
			Escribir "   Bloqueado"
		FinSi
		Escribir ""
		
		Escribir "3. HACER LLAMADAS"
		Si accesoLlamadas Entonces
			Escribir "   Disponible - Comunicacion telefonica"
		SiNo
			Escribir "   Bloqueado"
		FinSi
		Escribir ""
		
		Escribir "4. ENVIAR CORREOS"
		Si accesoCorreo Entonces
			Escribir "   Disponible - Mensajeria electronica"
		SiNo
			Escribir "   Bloqueado"
		FinSi
		Escribir ""
		
		Escribir "5. CONFIGURACION"
		Escribir "6. AYUDA Y SOPORTE"
		Escribir "0. SALIR"
		Escribir ""
		Escribir "Seleccione una opcion (0-6):"
		Leer opcionPrincipal
		
		Segun opcionPrincipal Hacer
			Caso 1:
				Si accesoWifi Entonces
					Repetir
						Limpiar Pantalla
						Escribir "=============================================="
						Escribir "           LECCION: WiFi"
						Escribir "=============================================="
						Escribir ""
						Escribir "Que desea aprender sobre WiFi?"
						Escribir ""
						Escribir "1. Que es el WiFi?"
						Escribir "2. Como conectarse al WiFi"
						Escribir "3. Solucionar problemas"
						Escribir "4. Seguridad en WiFi"
						Escribir "0. Regresar al menu principal"
						Escribir ""
						Escribir "Seleccione una opcion:"
						Leer opcionSecundaria
						
						Segun opcionSecundaria Hacer
							Caso 1:
								Limpiar Pantalla
								Escribir "=============================================="
								Escribir "           QUE ES EL WiFi?"
								Escribir "=============================================="
								Escribir ""
								Escribir "DEFINICION SIMPLE:"
								Escribir "El WiFi es como una conexion invisible"
								Escribir "que permite conectar su dispositivo"
								Escribir "a Internet SIN cables."
								Escribir ""
								Escribir "COMO FUNCIONA:"
								Escribir "- Su proveedor instala un router"
								Escribir "- El router crea Internet en el aire"
								Escribir "- Su dispositivo se conecta a esa señal"
								Escribir ""
								Escribir "Presione ENTER para continuar..."
								Esperar Tecla
								
							Caso 2:
								Limpiar Pantalla
								Escribir "=============================================="
								Escribir "        COMO CONECTARSE AL WiFi"
								Escribir "=============================================="
								Escribir ""
								Escribir "PASOS SIMPLES:"
								Escribir ""
								Escribir "PASO 1: Abrir Configuracion"
								Escribir "- Busque el icono del engranaje"
								Escribir "- Toquelo para abrirlo"
								Escribir ""
								Escribir "PASO 2: Buscar WiFi"
								Escribir "- Busque WiFi o Conexiones"
								Escribir "- Toque esa opcion"
								Escribir ""
								Escribir "PASO 3: Seleccionar red"
								Escribir "- Vera lista de redes"
								Escribir "- Toque su red WiFi"
								Escribir ""
								Escribir "PASO 4: Contraseña"
								Escribir "- Escriba la contraseña"
								Escribir "- Toque Conectar"
								Escribir ""
								Escribir "Presione ENTER para continuar..."
								Esperar Tecla
								
							Caso 3:
								Limpiar Pantalla
								Escribir "=============================================="
								Escribir "      SOLUCIONAR PROBLEMAS"
								Escribir "=============================================="
								Escribir ""
								Escribir "PROBLEMAS COMUNES:"
								Escribir ""
								Escribir "No se conecta:"
								Escribir "- Verifique que WiFi este activado"
								Escribir "- Revise la contraseña"
								Escribir "- Acerquese al router"
								Escribir ""
								Escribir "Muy lento:"
								Escribir "- Cierre apps que no use"
								Escribir "- Reinicie el dispositivo"
								Escribir ""
								Escribir "Se desconecta:"
								Escribir "- Desactive ahorro de bateria"
								Escribir "- Olvide la red y reconecte"
								Escribir ""
								Escribir "Presione ENTER para continuar..."
								Esperar Tecla
								
							Caso 4:
								Limpiar Pantalla
								Escribir "=============================================="
								Escribir "         SEGURIDAD WiFi"
								Escribir "=============================================="
								Escribir ""
								Escribir "CONSEJOS DE SEGURIDAD:"
								Escribir ""
								Escribir "1. Contraseña segura"
								Escribir "   - Al menos 8 caracteres"
								Escribir "   - Letras, numeros y simbolos"
								Escribir ""
								Escribir "2. WiFi publico"
								Escribir "   - No haga compras online"
								Escribir "   - No revise el banco"
								Escribir "   - Solo para navegacion basica"
								Escribir ""
								Escribir "3. Red privada"
								Escribir "   - No comparta contraseña"
								Escribir "   - Cambie contraseña ocasionalmente"
								Escribir ""
								Escribir "Presione ENTER para continuar..."
								Esperar Tecla
						FinSegun
						
					Hasta Que opcionSecundaria = 0
				SiNo
					Escribir ""
					Escribir "Esta seccion esta bloqueada."
					Escribir "Presione ENTER para continuar..."
					Esperar Tecla
				FinSi
				
			Caso 2:
				Si accesoBluetooth Entonces
					Limpiar Pantalla
					Escribir "=============================================="
					Escribir "          LECCION: BLUETOOTH"
					Escribir "=============================================="
					Escribir ""
					Escribir "QUE ES BLUETOOTH:"
					Escribir "Conexion inalambrica de corta distancia"
					Escribir "para conectar dispositivos SIN Internet."
					Escribir ""
					Escribir "USOS COMUNES:"
					Escribir "- Conectar audifonos"
					Escribir "- Enviar fotos a otro telefono"
					Escribir "- Conectar teclados"
					Escribir "- Conectar altavoces"
					Escribir ""
					Escribir "COMO ACTIVAR:"
					Escribir "1. Ir a Configuracion"
					Escribir "2. Buscar Bluetooth"
					Escribir "3. Activar el interruptor"
					Escribir "4. Aparecera simbolo en pantalla"
					Escribir ""
					Escribir "Presione ENTER para continuar..."
					Esperar Tecla
				SiNo
					Escribir ""
					Escribir "Esta seccion esta bloqueada."
					Escribir "Presione ENTER para continuar..."
					Esperar Tecla
				FinSi
				
			Caso 3:
				Si accesoLlamadas Entonces
					Limpiar Pantalla
					Escribir "=============================================="
					Escribir "          LECCION: LLAMADAS"
					Escribir "=============================================="
					Escribir ""
					Escribir "COMO HACER LLAMADAS:"
					Escribir ""
					Escribir "1. Abrir app Telefono"
					Escribir "2. Marcar numero o elegir contacto"
					Escribir "3. Tocar boton verde (llamar)"
					Escribir "4. Para colgar, tocar boton rojo"
					Escribir ""
					Escribir "CONSEJOS:"
					Escribir "- Hable cerca del microfono"
					Escribir "- Verifique señal (barras)"
					Escribir "- Suba volumen si no escucha"
					Escribir ""
					Escribir "Presione ENTER para continuar..."
					Esperar Tecla
				SiNo
					Escribir ""
					Escribir "Esta seccion esta bloqueada."
					Escribir "Presione ENTER para continuar..."
					Esperar Tecla
				FinSi
				
			Caso 4:
				Si accesoCorreo Entonces
					Limpiar Pantalla
					Escribir "=============================================="
					Escribir "          LECCION: CORREO"
					Escribir "=============================================="
					Escribir ""
					Escribir "COMO ENVIAR CORREOS:"
					Escribir ""
					Escribir "1. Abrir app correo (Gmail, etc.)"
					Escribir "2. Tocar Redactar o +"
					Escribir "3. Escribir direccion destinatario"
					Escribir "4. Escribir asunto del mensaje"
					Escribir "5. Escribir mensaje"
					Escribir "6. Tocar Enviar"
					Escribir ""
					Escribir "CONSEJOS:"
					Escribir "- Verifique direccion antes de enviar"
					Escribir "- Use asunto claro"
					Escribir "- Sea cortes en mensajes"
					Escribir ""
					Escribir "Presione ENTER para continuar..."
					Esperar Tecla
				SiNo
					Escribir ""
					Escribir "Esta seccion esta bloqueada."
					Escribir "Presione ENTER para continuar..."
					Esperar Tecla
				FinSi
				
			Caso 5:
				Repetir
					Limpiar Pantalla
					Escribir "=============================================="
					Escribir "            CONFIGURACION"
					Escribir "=============================================="
					Escribir ""
					Escribir "1. Desbloquear todas las secciones"
					Escribir "2. Bloquear secciones"
					Escribir "3. Cambiar nombre"
					Escribir "0. Regresar"
					Escribir ""
					Escribir "Seleccione opcion:"
					Leer opcionSecundaria
					
					Segun opcionSecundaria Hacer
						Caso 1:
							accesoWifi <- Verdadero
							accesoBluetooth <- Verdadero
							accesoLlamadas <- Verdadero
							accesoCorreo <- Verdadero
							Escribir ""
							Escribir "Todas las secciones desbloqueadas"
							Escribir "Presione ENTER..."
							Esperar Tecla
							
						Caso 2:
							accesoWifi <- Verdadero
							accesoBluetooth <- Falso
							accesoLlamadas <- Falso
							accesoCorreo <- Falso
							Escribir ""
							Escribir "Solo WiFi disponible"
							Escribir "Presione ENTER..."
							Esperar Tecla
							
						Caso 3:
							Escribir ""
							Escribir "Nuevo nombre:"
							Leer nombreUsuario
							Escribir "Nombre cambiado"
							Escribir "Presione ENTER..."
							Esperar Tecla
					FinSegun
					
				Hasta Que opcionSecundaria = 0
				
			Caso 6:
				Limpiar Pantalla
				Escribir "=============================================="
				Escribir "           AYUDA Y SOPORTE"
				Escribir "=============================================="
				Escribir ""
				Escribir "CONTACTO:"
				Escribir "- Telefono: 1-800-AYUDA"
				Escribir "- Email: ayuda@app.com"
				Escribir ""
				Escribir "CONSEJOS:"
				Escribir "- Tome su tiempo"
				Escribir "- No tenga miedo de explorar"
				Escribir "- Practique regularmente"
				Escribir "- Pida ayuda cuando necesite"
				Escribir ""
				Escribir "Esta app ayuda a personas mayores"
				Escribir "a usar tecnologia de forma facil."
				Escribir ""
				Escribir "Presione ENTER para continuar..."
				Esperar Tecla
				
			Caso 0:
				Limpiar Pantalla
				Escribir "=============================================="
				Escribir "             HASTA LUEGO!"
				Escribir "=============================================="
				Escribir ""
				Escribir "Gracias por usar la app, ", nombreUsuario
				Escribir ""
				Escribir "RECUERDE:"
				Escribir "- La tecnologia esta para ayudar"
				Escribir "- Siempre se puede aprender algo nuevo"
				Escribir "- No hay preguntas tontas"
				Escribir ""
				Escribir "Siga practicando!"
				continuar <- Falso
				
			De Otro Modo:
				Escribir ""
				Escribir "Opcion invalida. Use numeros 0-6"
				Escribir "Presione ENTER..."
				Esperar Tecla
		FinSegun
		
	FinMientras
	
FinAlgoritmo