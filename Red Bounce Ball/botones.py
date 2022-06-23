import pygame

#=========================================================================================================#
#                                        Clase Botones                                                    #
#Funcion __init__(self, x, y): Entradas: self, Screen, sprt, img  ; Salidas:  inicializacion de parametros#
#       Funcion Draw(self,Screen): Entradas: self, Screen ; Salidas: blit del boton en pantalla           #
#=========================================================================================================# 
class botones():
    def __init__(self, x, y, img): #.......... Inicializacion de parametros.
        self.img = img #...................... Imagen (la funcion la recibe como entrada)
        self.rect = self.img.get_rect() #..... Se obtiene el rect de la imagen cargada.
        self.rect.x = x #..................... Coordenada en X donde se posicionara la img.
        self.rect.y = y #..................... Coordenada en Y donde se posicionara la img.
        self.click = False #.................. Check de clickeo. (True or False)

    def draw(self,Screen): #.................. Se dibujan los botones en la pantalla (Screen).
        button = False  #..................... Representa si se realiza lo que esta indicando el boton.
        pos = pygame.mouse.get_pos() #........ Check de la posicion del mouse en la pantalla

        if self.rect.collidepoint(pos): #..... Check de colision entre el mouse y el rect del boton.
            if pygame.mouse.get_pressed()[0] == True and self.click == False: #.... [0] corresponde al click derecho
                button = True #............... Se realiza la accion.
                self.click = True #........... Clickeo del mouse = True
                
        if pygame.mouse.get_pressed()[0] == False:
            self.click = False
        Screen.blit(self.img, self.rect) #.... Se dibuja por pantalla el boton, recibe una imageny un rect.
        return button