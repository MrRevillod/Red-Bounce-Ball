import pygame
from pygame import *

#===========================================================================================================#
#                                  Clase world e Iniciacion de parametros                                   #
#               Funcion __init__():  Entradas: self,mapa,sprt  ;  Salidas:  self.listaTile = []             #
#               Funciones draw():     Entradas: self, Screen    ;  Salidas:  Screen.blit(sprt)              #               
#===========================================================================================================#
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
#===========================================================================================================#

class world():
    def __init__(self,matriz,sprt):
        self.listaTile = [] #................... Lista que contiene las plataformas/bordes del mapa. 
        self.deadpoint = [] #................... Lista que contiene los objetos "deadpoint".
        self.flag = []      #................... Lista que contiene la bandera roja.
        self.final = []     #................... Lista que contiene la bandera verde.
        filas = 0           #................... Contador de la cantidad de filas de la matriz.
        for fila in matriz:
            columnas = 0    #................... Contador de la cantidad de columnas de la matriz
            for i in fila:  #................... Se recorre uno a uno los subindices de la matriz
                if i == 1:  # (4)
                    img = pygame.transform.scale(sprt[1], (20, 20)) # (5)
                    img_rect = img.get_rect()                       # (6)
                    img_rect.x = columnas * 20                      # (7)
                    img_rect.y = filas * 20                         # (8)
                    tile = (img, img_rect)                          # (9)
                    self.listaTile.append(tile)
                if i == 2:                                          # (4)
                    img = pygame.transform.scale(sprt[2], (20,20))  # (5)
                    img_rect = img.get_rect()                       # (6)
                    img_rect.x = columnas * 20                      # (7)
                    img_rect.y = filas * 20                         # (8)
                    tile = (img, img_rect)                          # (9)
                    self.flag.append(tile)
                if i == 3:                                          # (4)
                    img = pygame.transform.scale(sprt[3], (10,20))  # (5)
                    img_rect = img.get_rect()                       # (6)
                    img_rect.x = columnas * 20                      # (7)
                    img_rect.y = filas * 20                         # (8)
                    tile = (img, img_rect)                          # (9)
                    self.deadpoint.append(tile)
                if i == 4:                                          # (4)
                    img = pygame.transform.scale(sprt[9], (20,20))  # (5)
                    img_rect = img.get_rect()                       # (6)
                    img_rect.x = columnas * 20                      # (7)
                    img_rect.y = filas * 20                         # (8)
                    tile = (img, img_rect)                          # (9)
                    self.final.append(tile)
                columnas += 1
            filas += 1
        return

    def draw(self,Screen): #.............. (Funcion draw)
        for i in self.listaTile:
            Screen.blit(i[0], i[1]) #..... blit de img y rect en el mapa
        return
    def deadpointdraw(self,Screen): #..... (Funcion draw)
        for i in self.deadpoint:
            Screen.blit(i[0], i[1]) #..... blit de img y rect en el mapa
        return
    def flagdraw(self,Screen): #.......... (Funcion draw)
        for i in self.flag:
            Screen.blit(i[0], i[1]) #..... blit de img y rect en el mapa 
        return
    def finaldraw(self,Screen): #......... (Funcion draw)
        for i in self.final:
            Screen.blit(i[0], i[1]) #..... blit de img y rect en el mapa
        return

#====================================================================================================#
#                                         Matriz principal                                           #
#                     Los valores 0 indican que no hay nada en ese espacio                           #
#                              la matriz tiene un tamaño de 40x40                                    #
#   para que todo funcione correctamente de deben reescalar los tiles que se mostraran por pantalla. #
#====================================================================================================#

matriz = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,1,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,3,0,0,0,0,0,0,0,3,0,0,0,0,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
    [1,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,1],
    [1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,1],
    [1,0,0,0,0,0,3,0,0,0,0,0,3,0,0,0,0,0,1,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
    [1,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
    [1,0,0,0,0,0,3,0,0,0,0,0,3,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,3,0,0,0,3,0,0,0,0,0,0,1],
    [1,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,1],
    [1,0,0,0,3,0,0,0,0,3,0,0,0,0,3,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
    [1,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,1,0,0,1,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,1],
    [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
    [1,0,0,0,0,0,3,0,0,0,0,0,3,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,1,0,0,1,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,1,0,0,0,3,0,0,0,3,0,0,0,1,0,0,1],
    [1,0,0,0,3,0,0,0,0,3,0,0,0,0,3,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,1],
    [1,0,0,1,1,1,0,0,1,1,1,0,0,1,1,1,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,1],
    [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
    [1,0,0,0,0,0,3,0,0,0,0,0,3,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,1],
    [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
    [1,0,0,3,0,0,0,0,0,3,0,0,0,0,0,3,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,1,0,0,1,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]