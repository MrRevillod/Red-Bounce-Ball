import pygame,world,botones,bots
from pygame.locals import *
from world import *
from botones import *
from bots import *

#====================================================================================================#
#                                    Funciones Blits de pantalla                                     #
#        Funciones blit():     Entradas: self, Screen, sprt  ; Salidas:  Screen.blit(sprt)           #
#====================================================================================================#     

def cupblit(Screen,sprt):
    Screen.blit((sprt[5]),(380,200))
    Screen.blit((sprt[5]),(380,680))
    return

def vidasblit(self,Screen,sprt):
    if self.vida == 3:
        Screen.blit((sprt[16]),(380,300))
    if self.vida == 2:
        Screen.blit((sprt[17]),(380,300))
    if self.vida == 1:
        Screen.blit((sprt[18]),(380,300))


#====================================================================================================#
#                              Clase Redball e Iniciacion de parametros                              #
# Funcion __init__():  Entradas: self, x, y  ;  Salidas: update visual (blits en pantalla)           #                              
#====================================================================================================#

class Redball():
    def __init__(self, x, y): #............................ Se inicializan los parametros de la pelota.
        img = pygame.image.load("./sprt/S07.png") #........ Carga de imagen asignada a la pelota.
        self.rescale = pygame.transform.scale(img, (20, 20)) #... Rescala la imagen cargada.
        self.rect = self.rescale.get_rect() #.............. Se obtiene el "rect" de la img reescalada
        self.ancho = self.rescale.get_width() #............ Se obtiene el ANCHO del "rect".
        self.alto = self.rescale.get_height() #............ Se obtiene el ALTO del "rect".
        self.rect.x = x #.................................. Posicion de la pelota en eje X.
        self.rect.y = y #.................................. Posicion de la pelota en eje Y.
        self.gravity = 0 #................................. Gravedad Inicial de la pelota.
        self.salto = False #............................... Valor False, se usa para checkar si se salto.
        self.vida = 3  #................................... Vida inicial del jugador.

#====================================================================================================#
#                                       Funcion update                                               #
#                Actualiza los parametros de la pelota (posicion, colision, etc)                     #
#     Ademas se encarga de identificar las distintas situaciones durante la ejecucion del juego      #
#====================================================================================================#

    def update(self,Screen,mundo,sprt): 
        dirX = 0 #..............(movimiento)............... Direccion en X inicial.
        dirY = 0 #..............(movimiento)............... Direccion en Y inicial.

#====================================================================================================#
#                              Se verifica la pulsacion de teclas.                                   #
#====================================================================================================#

        if self.vida == 3 or self.vida == 2 or self.vida == 1: #.... Check de las vidas del jugador.
            cupblit(Screen,sprt) #.................................. Blit de las copas.
            vidasblit(self,Screen,sprt)#............................ Blit de las vidas.
        
            key = pygame.key.get_pressed() #........................ Verificador de teclas presionadas.
            if key[pygame.K_UP] and self.salto == False: #.......... Tecla Arriba
                self.gravity = -13 #.....  Se resta 13 a la "gravedad", de esta forma la pelota subira
                self.salto = True #................................. Check de salto
            elif key[pygame.K_LEFT]:
                dirX -= 5 #......................................... Direccion a la izquierda
            elif key[pygame.K_RIGHT]:
                dirX += 5 #......................................... Direccion a la derecha

#====================================================================================================#
#                                   Actualizacion de "Gravedad"                                      #
#====================================================================================================#

            self.gravity += 1 #... En todo momento +1 de esta forma, aunque la pelota suba, va a bajar.
            if self.gravity > 10: #... Si la suma constante es mayor a 
                self.gravity = 10 #... Solo un limitador
            dirY += self.gravity  #... La gravedad va a ser igual a nuestra direccion en Y (Movimiento)

#====================================================================================================#
#                                           Colisiones                                               #
#                             Uso de la funcion colliderect de pygame                                #
#====================================================================================================#

            for i in mundo.listaTile: #............ Se recorren los elementos de la listaTile.
                if i[1].colliderect(self.rect.x + dirX, self.rect.y, self.ancho, self.alto):
                    dirX = 0 #..................... Si se detecta colision con el rect de la lista:
                    #.............................. DirX = 0/ no ha movimiento en eje X

                    #.........................(Gravity < 0 / saltar).........................#
                if i[1].colliderect(self.rect.x, self.rect.y + dirY, self.ancho, self.alto):
                    if self.gravity < 0: #......... Si la gravedad es negativa, osea el player sube:
                        dirY = i[1].bottom - self.rect.top #.... Cambia la Direccion en Y
                        self.gravity = 0 #.... La gravedad retorna a 0, por lo tanto el player caera.

                    #..................(Gravity >= 0 / Reposo o caida libre).................#
                    elif self.gravity >= 0: #....Si el player esta en reposo o cayendo:
                        dirY = i[1].top - self.rect.bottom #Cambia la direccion en eje Y.
                        self.gravity = 0   #.... Gravedas igual a cero, por lo tanto el player caera, 
                        # o se mantendra pegado al suelo.
                        self.salto = False #.... Check de salto

#====================================================================================================#
#                                             DEADPOINTS                                             #
#====================================================================================================#

            for i in mundo.deadpoint: #............ Se recorren los elementos de la lista deadpoint.
                if i[1].colliderect(self.rect.x + dirX, self.rect.y, self.ancho, self.alto):
                    self.vida -= 1 #............... Se resta una vida al contador.
                    dirX = 0 #..................... Frena el movimiento en eje X
                    dirY = 0 #..................... Frena el movimiento en eje Y
                    self.gravity = 0  #............ Frena la "Gravedad"
                    self.rect.x = self.rect.x #.... Retorna posicion de inicio en X
                    self.rect.y = 775 #............ Retorna posicion de inicio en Y

                if i[1].colliderect(self.rect.x, self.rect.y + dirY, self.ancho, self.alto):
                    self.vida -= 1 #............... Se resta una vida al contador.
                    dirX = 0 #..................... Frena el movimiento en eje X
                    dirY = 0 #..................... Frena el movimiento en eje Y
                    self.gravity = 0  #............ Frena la "Gravedad"
                    self.rect.x = self.rect.x #.... Retorna posicion de inicio en X
                    self.rect.y = 775 #............ Retorna posicion de inicio en Y

            #...............Actualizacion de las coordenadas de la pelota..........#

            self.rect.x += dirX 
            self.rect.y += dirY
            Screen.blit(self.rescale, self.rect) #.... Blit del sprt sobre la posicion de la pelota.

            if self.rect.y < 0 or self.rect.y > 780: #.... Condicional creado para solucionar un error.
                self.rect.y = 775
                self.rect.x = self.rect.x

#====================================================================================================#
#                                         Banderas de NEXT LEVEL                                     #
#====================================================================================================#

            for i in mundo.flag: #.......... En esta caso la lista flag tiene solo un elemento.
                if i[1].colliderect(self.rect.x + dirX, self.rect.y, self.ancho, self.alto): # Eje X
                    Screen.blit(sprt[7],(0,0)) #....... Blit "NEXT LEVEL"
                    pygame.mouse.set_visible(True) #... Mouse se vuelve visible
                    b_vamos = botones(290,650, sprt[8]) #... Se define el boton "vamos"
                    if b_vamos.draw(Screen):   #....... Si se presiona el boton:
                        pygame.mouse.set_visible(False)
                        self.rect.x = 600      #....... Cambian los parametros de la pelota,
                        self.rect.y = 760      #....... Posicion en X e Y.
                        self.gravity = 0       #....... Gravedad.
                        self.salto = False     #....... Check de salto.
                        self.vida = 3          #....... Se recargan las vidas del jugador.

                if i[1].colliderect(self.rect.x, self.rect.y + dirY, self.ancho, self.alto):# Eje Y
                    Screen.blit(sprt[7],(0,0)) #....... Blit "NEXT LEVEL"
                    pygame.mouse.set_visible(True) #... Mouse se vuelve visible
                    b_vamos = botones(290,650, sprt[8]) #... Se define el boton "vamos"
                    if b_vamos.draw(Screen):   #....... Si se presiona el boton:
                        pygame.mouse.set_visible(False)
                        self.rect.x = 600      #....... Cambian los parametros de la pelota,
                        self.rect.y = 760      #....... Posicion en X e Y.
                        self.gravity = 0       #....... Gravedad.
                        self.salto = False     #....... Check de salto.
                        self.vida = 3          #....... Se recargan las vidas del jugador.

#====================================================================================================#
#                                         Banderas de END GAME                                       #
#====================================================================================================#

            for i in mundo.final:
                #check de colision en eje X e Y
                if i[1].colliderect(self.rect.x + dirX, self.rect.y, self.ancho, self.alto): # Eje X
                    pygame.mouse.set_visible(True) #......... Mouse se vuelve visible
                    b_vamos = botones(430,650, sprt[8]) #.... Defino los botones con su respectiva posicion
                    b_salir = botones(150,650, sprt[22])#.... (Volver a jugar y salir)
                    Screen.blit(sprt[10],(0,0)) #............ Blit del background final (Ganador!)  
                    if b_vamos.draw(Screen):    #............ Si se presiona el boton:
                        pygame.mouse.set_visible(False)
                        self.rect.x = 180       
                        self.rect.y = 760       
                        self.gravity = 0        #...Se reinician los parametros de la pelota...#
                        self.salto = False
                        self.vida = 3
                    if b_salir.draw(Screen):    #............ Si se presiona el boton:
                        pygame.display.quit()   #............ Se cierra el juego.

            for i in mundo.final:
                #check de colision en eje X e Y
                if i[1].colliderect(self.rect.x, self.rect.y + dirY, self.ancho, self.alto): # Eje Y
                    pygame.mouse.set_visible(True) #......... Mouse se vuelve visible
                    b_vamos = botones(430,650, sprt[8]) #.... Defino los botones con su respectiva posicion
                    b_salir = botones(150,650, sprt[22])#.... (Volver a jugar y salir)
                    Screen.blit(sprt[10],(0,0)) #............ Blit del background final (Ganador!)  
                    if b_vamos.draw(Screen):    #............ Si se presiona el boton:
                        pygame.mouse.set_visible(False)
                        self.rect.x = 180       
                        self.rect.y = 760       
                        self.gravity = 0        #...Se reinician los parametros de la pelota...#
                        self.salto = False
                        self.vida = 3
                    if b_salir.draw(Screen):    #............ Si se presiona el boton:
                        pygame.display.quit()   #............ Se cierra el juego.
    
#====================================================================================================#
#                                           Cero vidas vidas                                         #
#====================================================================================================#                        

        elif self.vida == 0 or self.vida < 0: #.............. Si se agotan las vidas:
            pygame.mouse.set_visible(True) #................. Mouse se vuelve visible.
            b_reintentar = botones(430,650, sprt[20])#....... Defino los botones con su respectiva posicion
            b_salir = botones(150,650, sprt[22]) #........... (Volver a jugar y salir)
            Screen.blit(sprt[19],(0,0))#..................... Blit del background final (Game over!)  
            if b_reintentar.draw(Screen): #.................. Si se presiona el boton:
                pygame.mouse.set_visible(False)
                self.rect.x = 180
                self.rect.y = 760
                self.gravity = 0          #...Se reinician los parametros de la pelota...#
                self.salto = False
                self.vida = 3

            if b_salir.draw(Screen):      #............ Si se presiona el boton:
                pygame.display.quit()     #............ Se cierra el juego.
#====================================================================================================#  
#                                  Coordenadas ; Manejo de archivos                                  #
#====================================================================================================#  

