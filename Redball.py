import pygame,world
from pygame.locals import *
from world import *
#====================================================================================================#
#                                                                                                    #
#  Clase Redball:                                                                                    #
#                                                                                                    #
#  Esta clase contiene todo lo necesario para el correcto funcionamiento de nuestro "player"         #
#  La clase contiene dos funciones:                                                                  #
#                                                                                                    #
#  Funcion __init__():                                                                               #
#  Entradas: self,x,y                                                                                #
#  Salidas: self(distintos parametros correspondientes a nuestro objeto/player)                      #
#                                                                                                    #
#       Definiciones:                                                                                #
#                                                                                                    #
#       img : Carga el sprite del objeto self/ pelota                                                #
#       self.rescale: Recibe la imagen cargada (img) y la rescala mediante una funcion de pygame.    #
#                                                                                                    #
#       self.rect: Obtiene la "hitbox"/ rect que envuelve a nuestro sprt reescalado                  #
#       self.ancho: Obtiene el ancho en px de el sprt reescalado                                     #
#       self.alto: Obtiene el ancho en px de el sprt reescalado                                      #
#       self.rect.x : Coordenadas en eje X del RECT                                                  #
#       self.rect.y : Coordenadas en eje Y del RECT                                                  #
#       self.gravity: valor de gravedad, al saltar, toma valor -13, esto se le suma a la dirY        #
#                     haciendo que la pelota suba.                                                   #
#       dirX: Direccion eX de la pelota, Inicialmente se asigna a 0                                  #
#       dirY: Direccion eY de la pelota, Inicialmente se asigna a 0                                  #
#                                                                                                    #
#====================================================================================================#
#                                                                                                    #
#  Funcion update():                                                                                 #
#  Entradas: self, Screen,mundo                                                                      #
#  Salidas:  Actualizacion de posicion de nuestro objeto (Redball)                                   #
#                                                                                                    #
#                                                                                                    #
#====================================================================================================#



class Redball():

#====================================================================================================#
#                                          Funcion __init__                                          #
#====================================================================================================#

    def __init__(self, x, y):
        img = pygame.image.load("./sprt/S07.png")
        self.rescale = pygame.transform.scale(img, (20, 20))
        self.rect = self.rescale.get_rect()
        self.ancho = self.rescale.get_width()
        self.alto = self.rescale.get_height()
        self.rect.x = x
        self.rect.y = y
        self.gravity = 0
        self.salto = False

#====================================================================================================#
#                                          Funcion update                                            #
#====================================================================================================#

    def update(self,Screen,mundo):
        dirX = 0
        dirY = 0
#-----------------------------------------------------------------#
#      Se verifica la pulsacion de teclas.
#-----------------------------------------------------------------#
        key = pygame.key.get_pressed() 
        if key[pygame.K_UP] and self.salto == False: 
            self.gravity = -13
            self.salto = True
        elif key[pygame.K_LEFT]:
            dirX -= 5
        elif key[pygame.K_RIGHT]:
            dirX += 5 
#-------------------------------------------------------------------#
#                         Gravedad                                  #
#-------------------------------------------------------------------#
#Sumo 1 en todo momento a la gravedad para evitar que la pelota vuele
#
        self.gravity += 1   
        if self.gravity > 10:
            self.gravity = 10
        dirY += self.gravity 
#
#Sumo gravity a dY, si no ha saltado, entonces la pelota se mantiene en el suelo.
#Sino se le suma el valoir de gravedad por salto, osea que sube, y luego retorna.
#-------------------------------------------------------------------#

#-------------------------------------------------------------------#
#                          Colisiones                               #
#-------------------------------------------------------------------#
# Si recordamos listaTile contiene la informacion de rect de todos 
# los objetos que conforman el mapal, de esta forma, a traves del ciclo for
# recorre y verifica si alguno de todos los movimientos de la pelota la ha llevado 
# a la misma coordenada de donde se encuentra algun objeto de la lista, si ocurre 
# esto la pelota detendra su movimiento, y por la gravedad asignada bajara si la 
# colision es vertical, en cambiosi la colision es horizontal, solo se detendra.

        for i in mundo.listaTile:
            #check de colision en eje X
            if i[1].colliderect(self.rect.x + dirX, self.rect.y, self.ancho, self.alto):
                dirX = 0
            #check de colision en eje Y
            if i[1].colliderect(self.rect.x, self.rect.y + dirY, self.ancho, self.alto):
                #check de salto
                if self.gravity < 0:
                    dirY = i[1].bottom - self.rect.top
                    self.gravity = 0
                #check de caida
                elif self.gravity >= 0:
                    dirY = i[1].top - self.rect.bottom
                    self.gravity = 0
                    self.salto = False
                    

        #Actualiza las cordenadas de la pelota
        self.rect.x += dirX
        self.rect.y += dirY

        if self.rect.bottom > 800:
            self.rect.bottom = 800
            dirY = 0
#-------------------------------------------------------------------#
#                          Coordenadas                              #
#-------------------------------------------------------------------#
#Creo un archivo en modo a, en el se escribiran las cordenadas del 
# jugador a travez del mapa
        with open("Coordenadas.txt", "a") as c:
            coordenada = f"X: {self.rect.x}  ,Y: {self.rect.y}\n"
            c.write(coordenada)
        c.close()
        #Asigna el sprite a la pelota (self)
        Screen.blit(self.rescale, self.rect)
