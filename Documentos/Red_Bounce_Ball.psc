Proceso Red_Bounce_Ball
	Inicio <- Falso
	Repetir
		Escribir 'Desea Iniciar el Juego?'
		Leer menu
		Si menu=='Si' Y Inicio==Falso Entonces
			Inicio <- Verdadero
			Repetir
				Escribir '¿Se presiono alguna tecla?'
				Leer tecla
				Si tecla=='No' Entonces
					Escribir 'Entonces no hay Movimiento'
				FinSi
				Si tecla=='Si' Entonces
					Escribir'La tecla presionada corresponde a Izq/Der/arriba?'
					Leer opciones
					Si opciones == 'Si' Entonces
						Escribir '¿Cual tecla se presiono?'
						Leer presiono
						Si presiono=='arriba' Entonces
							Escribir 'Player salta'
							ejeY <- ejeY+1
							Movimiento <- True
							Inicio <- False
							Escribir 'Eje Y: ',ejeY
						SiNo
							ejeY <- ejeY
						FinSi
						Si presiono=='derecha' Entonces
							Escribir 'Player se mueve a la Derecha'
							ejeX <- ejeX+1
							Movimiento <- True
							Inicio <- False
							Escribir 'Eje X: ',ejeX
						SiNo
							ejeX <- ejeX
						FinSi
						Si presiono=='izquierda' Entonces
							Escribir 'Player se mueve a la Izquierda'
							ejeX <- ejeX-1
							Movimiento <- True
							Inicio <- False
							Escribir 'Eje X: ',ejeX
						SiNo
							ejeX <- ejeX
						FinSi
						Si presiono=='arriba y derecha' Entonces
							Escribir 'Player salta'
							ejeY <- ejeY+1
							ejeX <- ejeX+1
							Movimiento <- True
							Inicio <- False
							Escribir 'Eje Y: ',ejeY
							Escribir 'Eje X: ',ejeX
						SiNo
							ejeY <- ejeY
							ejeX <- ejeX
						FinSi
						Si presiono=='arriba e izquierda' Entonces
							Escribir 'Player salta'
							ejeY <- ejeY+1
							ejeX <- ejeX-1
							Movimiento <- True
							Inicio <- False
							Escribir 'Eje Y: ',ejeY
							Escribir 'Eje X: ',ejeX
						SiNo
							ejeY <- ejeY
							ejeX <- ejeX
						FinSi
						Escribir ' ¿El jugador ha colisionado con algun obstaculo?'
						Leer obstaculo
						Si obstaculo=='Si' Entonces
							Escribir 'Jugador pierde una vida'
							vida <- vida-1
							Escribir 'Ahora usted posee ',vida,' vidas'
							Escribir 'Jugador retorna al inicio'
							Inicio <- True
						SiNo
							vida <- vida
							Escribir 'El jugador ha llegado a la meta?'
							Leer meta
							Si meta == 'Si' Entonces
								Escribir 'Felicidades'
								Escribir  'Menu opciones volver a jugar o salir.'
							FinSi
						FinSi
					FinSi
					Si opciones == 'No' Entonces
						Escribir 'la tecla presionada no correponde a un movimiento'
					FinSi
				FinSi
			Hasta Que presiono == 'Si'
		FinSi
	Hasta Que menu == 'Si' 
FinProceso
