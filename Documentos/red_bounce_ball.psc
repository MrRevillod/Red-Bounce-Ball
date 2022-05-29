Algoritmo red_bounce_ball
	ejeX <- 0
	ejeY <- 0
	vida <- 3
	Inicio <- True
	Movimiento <- False
	Repetir
		Escribir 'Se presiono alguna tecla?'
		Leer tecla
		Si tecla=='Si' Entonces
			Escribir 'Cual tecla se presiono?'
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
			Escribir ' El jugador ha colisionado con algun obstaculo?'
			Leer obstaculo
			Si obstaculo=='Si' Entonces
				Escribir 'Jugador pierde una vida'
				vida <- vida-1
				Escribir 'Ahora usted posee ',vida,' vidas'
				Escribir 'Jugador retorna al inicio'
				Inicio <- True
			SiNo
				vida <- vida
				Escribir 'Usted posee ',vida,' vidas'
				Inicio <- False
				Movimiento <- True
			FinSi
		SiNo
			Escribir 'Entonces no hay movimiento'
			Inicio <- True
		FinSi
	Hasta Que vida==0
	Si vida==0 Entonces
		Escribir 'Se han agotado las vidas del jugador'
	FinSi
FinAlgoritmo
