import pygame
import ctypes

class ball(ctypes.Structure):
    _fields_ = [('SdX',ctypes.c_short),('SdY',ctypes.c_short),
    ('DirX',ctypes.c_short),('SdVel',ctypes.c_short)]

#====================================================================================================#
#                                       Funcion "ballInit"                                           #
#                          Asignamos valores a la estructura de la initball.                         #
#                  Entrada: ball() (_fields_) ; Salidas: Inicializacion de parametros
#====================================================================================================#

    def ballInit(initball): 
        initball.SdX = 150  # Posicion (px) inicial de la initball en eje X.
        initball.SdY = 510  # Posicion (px) inicial de la initball en eje y.
        initball.DirX = 1   # Direccion inicial/predeterminada en el eje X.(1 o -1)
        initball.SdVel = 3  # Velocidad Constante de la initball.
        return

#====================================================================================================#
#                                      Funcion "Updateball"                                          #
#                 Usamos condicionales para asignar los limites en el eje X de la initball.          #
#          Elegimos valores X312, X465 para que la onda no choque con los bordes de la barra.        #
#          Funcion Update: Entrada: ball() (_fields_) ; Salidas: Actualizacion de parametros         #
#      Funcion Pintaball: Entrada: ball(), Screen, sprt ; Salidas: Inicializacion de parametros      #
#====================================================================================================#

    def Updateball(initball):
        if initball.SdX >= 605: 
        #Basicamente, si la initball llega a la posicion 605 del eje X
            initball.DirX =- 1 #la direccion cambia hacia la izquierda(-1).

        if initball.SdX <= 160: 
        #Por otro lado, si la initball llega a la posicion 160 del eje X
            initball.DirX = 1  #la direccion retomara su sentido inicial (1).

        initball.SdX += initball.SdVel  * initball.DirX
        #Posicion de initball en X = initball.SdX+initball.SdVel*initball.DirX.
        return

    def Pintaball(initball,Screen,sprt):
        if initball.DirX == -1:
            Screen.blit(sprt[15],(initball.SdX,initball.SdY))
        elif initball.DirX == 1:
            Screen.blit(sprt[15],(initball.SdX,initball.SdY))
        return
