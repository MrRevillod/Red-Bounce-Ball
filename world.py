import pygame
from pygame import *

#===========================================================================================================#
#                                                                                                           #
#  Clase world:                                                                                             #
#                                                                                                           # 
#  Esta clase contiene todo lo necesario para la creacion del mapa, ademas le añade colision a los          #
#  objetos que son parte del mapa esto mediante el arreglo self.listaTile                                   #
#                                                                                                           #
#  La clase contiene dos funciones:                                                                         #
#                                                                                                           #
#  Funcion __init__():                                                                                      #
#  Entradas: self,mapa,sprt                                                                                 #
#  Salidas:  self.listaTile = []                                                                            #  
#                                                                                                           #
#       Esta funcion cumple la tarea de analizar cada subindice de la matriz e identificar su valor,        #
#       dependiendo del mismo, se le asignara un sprite a esa posicion dentro de la matriz, mediante la     #
#       funcion get_rect() se encontrara su hitbox, ambos parametros se almacenaran en una tupla ("tile")   #
#       a su vez esta tupla se ingresara a self.listaTile, esta lista servira para guardar los sprt como    #
#       objetos que poseen colision                                                                         #
#                                                                                                           #
#       Ademas mediante una multiplicacion se obtendran las coordenadas de x e y de los sprites a           #
#       imprimir esto multiplicando el numero de fila/columna donde se encuentre por el tamaño del tile(20) #
#       (el numero de fila y columna aumenta atravez de los ciclos for, estos actuan como un contador)      #
#                                                                                                           #
#       Definiciones:                                                                                       #
#                                                                                                           #
#   1 - self.listaTile: lista, servira para almacenar nuestros tiles/objetos dibujados en la pantalla.      #
#   2 - filas: actua como contador de la cant, de filas de nuestra matriz.                                  # 
#   3 - columnas: actua como contador de la cant, de columnas de nuestra matriz.                            #
#   4 - i : subindices de la matriz, dependiendo del numero le asigna un sprt.                              #
#   5 - img: imagen a reescalar, contiene el sprt y su tamaño px en formato tupla.                          #
#   6 - img_rect: identifica la hitbox (rect) de nuestra imagen.                                            #
#   7 - img_rect.x: columnas x 20 = actua como un identificador de posicion en pantalla.                    #
#   8 - img_rect.y: filas x 20 = actua como un identificador de posicion en pantalla.                       #
#   9 - tile: tupla, contiene el sprt reescalado y la informacion de rect.                                  #
#                                                                                                           #
#                                                                                                           #
#  Funcion draw():                                                                                          #
#  Entradas: self, Screen                                                                                   #
#  Salidas:  Screen.blit(sprt)                                                                              #
#                                                                                                           #
#       Esta funcion se encarga de mostrar por pantalla los sprt guardados en la lista self                 #
#       en su respectiva posicion en el mapa (img_rect.x/y)                                                 #
#       Ejemplo:                                                                                            #
#       Teniendo en cuenta que el tile mide 20 px                                                           #
#       Existe un numero 1 en la columna 1 fila 3                                                           #
#       Su posicion de x sera: columna * 20 = 20 px en X                                                    #
#       Su posicion de y sera: fila * 20 = 60 px en Y                                                       #
#       En conclusion la ubicacion donde se debe dibujar el sprt es en la coordenada (20,60)                #
#                                                                                                           #
#                                                                                                           #
#===========================================================================================================#



class world():
    def __init__(self,mapa,sprt):
        self.listaTile = [] # (1)
        filas = 0           # (2)    
        for fila in mapa:
            columnas = 0    # (3)
            for i in fila:
                if i == 1:  # (4)
                    img = pygame.transform.scale(sprt[1], (20, 20)) # (5)
                    img_rect = img.get_rect()                       # (6)
                    img_rect.x = columnas * 20                      # (7)
                    img_rect.y = filas * 20                         # (8)
                    tile = (img, img_rect)                          # (9)
                    self.listaTile.append(tile) 
#
                if i == 3:                                          # (4)
                    img = pygame.transform.scale(sprt[3], (10,20))  # (5)
                    img_rect = img.get_rect()                       # (6)
                    img_rect.x = columnas * 20                      # (7)
                    img_rect.y = filas * 20                         # (8)
                    tile = (img, img_rect)                          # (9)
                    self.listaTile.append(tile)
#
                if i == 4:                                          # (4)
                    img = pygame.transform.scale(sprt[4], (20, 20)) # (5)
                    img_rect = img.get_rect()                       # (6)
                    img_rect.x = columnas * 20                      # (7)
                    img_rect.y = filas * 20                         # (8)
                    tile = (img, img_rect)                          # (9)
                    self.listaTile.append(tile)
#
                if i == 5:                                          # (4)
                    img = pygame.transform.scale(sprt[5], (20, 20)) # (5)
                    img_rect = img.get_rect()                       # (6)
                    img_rect.x = columnas * 20                      # (7)
                    img_rect.y = filas * 20                         # (8)
                    tile = (img, img_rect)                          # (9)
                    self.listaTile.append(tile)
                columnas += 1
            filas += 1
        return

    def draw(self,Screen):
        for i in self.listaTile:
            Screen.blit(i[0], i[1])
        return

#====================================================================================================#
#                                         Matriz principal                                           #
#                    Forma de interpretar las divisiones creadas anteriormente                       #
#                     Los valores 0 indican que no hay nada en ese espacio                           #
#                              la matriz tiene un tamaño de 40x40                                    #
#   para que todo funcione correctamente de deben reescalar los tiles que se mostraran por pantalla. #
#====================================================================================================#

matriz = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
    [1,1,1,0,0,0,0,1,1,0,0,0,0,1,1,1,0,0,0,1,1,0,0,0,0,0,3,1,3,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,0,0,1,1,1,0,0,0,0,1,1,0,0,0,0,1],
    [1,0,0,0,0,3,0,0,0,3,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
    [1,0,0,0,1,1,0,0,0,1,1,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,1,1,1,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,1],
    [1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,3,0,0,1],
    [1,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,1,1,1,0,1],
    [1,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
    [1,0,0,0,0,0,3,0,0,0,0,0,0,0,3,0,0,0,0,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,3,0,0,0,1],
    [1,1,0,0,0,1,1,1,1,0,0,0,1,1,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1],
    [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,1,1,0,0,3,0,0,0,0,0,0,0,0,0,0,3,0,0,1,1,1],
    [1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,1,1,1,0,0,0,0,0,0,0,0,1,1,1,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1,1,1],
    [1,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,1,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1],
    [1,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,3,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,1,1,1,1,0,0,0,0,0,0,0,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]

