
import pygame,world,Redball,bots,botones,time as t
from world import *
from pygame.locals import *
from Redball import *
from bots import *
from botones import *

#====================================================================================================#
#                                    Variables y constantes                                          #
#====================================================================================================#

minX = 0      ; maxX = 800                    ;         xd = 0             ;           yd = 0                          
#Valor minimo y maximo del eje X en el mapa.    #Valor asignado a 0 en x       #Valor asignado a 0 en Y          
minY = 0      ; maxY = 800                      #se puede usar para sumar      #se puede usar para sumar         
#Valor minimo y maximo del eje Y en el mapa.    #un numero y asi cambiar       #un numero y asi cambiar          
#                                               #el valor del eje x.           #el valor del eje y.
menu = True   ; ToF = True
#Valores True or False

res = (maxX,maxY)                 
#Resolucion de la ventana.

tileX = 128            ;              tileY = 128
#Valores en X e Y del tile principal, a futuro se reescalara.

tileSize = 20
#valor rescalado de algunos sprt.

mouX = 0                       ; mouY = 0                       
#Valor asignado a 0 en x       #Valor asignado a 0 en Y          
#se puede usar para sumar      #se puede usar para sumar         
#un numero y asi cambiar       #un numero y asi cambiar          
#el valor del eje x(MOUSE).    #el valor del eje y(MOUSE).       

#====================================================================================================#
#                                        Funcion "Load_Image'                                        #
#                            Carga imagenes y convierte formato PyGame.                              #
#====================================================================================================#

def Load_Image(sFile,transp = False):
    try: image = pygame.image.load(sFile)
    except pygame.error.message:
        raise SystemExit.message
    image = image.convert()  
    if transp:
        color = image.get_at((0,0))
        image.set_colorkey(color)
    return image

#====================================================================================================#
#                                            Fig Init                                                #
#                         Arreglo con los sprites que se usaran en el juego                          #
#====================================================================================================#

def arraySprt():
    aSprt = []
    aSprt.append(Load_Image('./sprt/S01.png',False )) # Background               [0]
    aSprt.append(Load_Image('./sprt/S02.png',False )) # Red tile                 [1]
    aSprt.append(Load_Image('./sprt/S12.png',False )) # InitFlag                 [2]
    aSprt.append(Load_Image('./sprt/S06.png',False )) # Obstaculo                [3]
    aSprt.append(Load_Image('./sprt/enemie.png',True )) # enemie                 [4]
    aSprt.append(Load_Image('./sprt/coup.png',False )) # Coup                    [5]
    aSprt.append(Load_Image('./sprt/S07.png',True ))  # Red Ball                 [6]
    aSprt.append(Load_Image('./sprt/nextlevel.png',False )) # next level         [7]
    aSprt.append(Load_Image('./sprt/gobutton.png',False )) # GO Button           [8]
    aSprt.append(Load_Image('./sprt/S11.png',True)) # green flag                 [9]
    aSprt.append(Load_Image('./sprt/winner.png',False )) # winner                [10]
    aSprt.append(Load_Image('./sprt/Inicio.png',False ))# Inicio                 [11]
    aSprt.append(Load_Image('./sprt/Opciones.png',False ))# MenuManual           [12]
    aSprt.append(Load_Image('./sprt/start.png',False ))# start button            [13]
    aSprt.append(Load_Image('./sprt/Manual.png',False ))# Manual button          [14]
    aSprt.append(Load_Image('./sprt/Menuball.png',True ))# Ball Inicio           [15]
    aSprt.append(Load_Image('./sprt/fullv.png',False ))# Vidas = 3               [16]
    aSprt.append(Load_Image('./sprt/midv.png',False ))#  Vidas = 2               [17]
    aSprt.append(Load_Image('./sprt/minv.png',False ))#  Vidas = 1               [18]
    aSprt.append(Load_Image('./sprt/over.png',False ))#  gameover                [19]
    aSprt.append(Load_Image('./sprt/restartbutton.png',True ))#  restart button  [20]
    aSprt.append(Load_Image('./sprt/seeu.png',False ))#  seeu                    [21]
    aSprt.append(Load_Image('./sprt/exitbutton.png',False ))#  exit button       [22]
    return aSprt
    
#====================================================================================================#
#                                        Inicializa PyGames.-                                        #
#                                  Inicializa el Engine de PyGame.                                   #
#====================================================================================================#

def pygame_init():
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption('Red Bounce Ball - Luciano Revillod Jerez')
    pygame.mouse.set_visible(False)
    return pygame.display.set_mode(res)

#====================================================================================================#
#                                         Funcion MapInit                                            #
#                       Crea y retorna una surface donde se imprimira el mapa                        #
#         Entradas: (AnchoX,AnchoY en Pixeles)   Salidas: Surface de las medidas indicadas           #   
#====================================================================================================#

def MapInit(AnchoX,AnchoY):
    return pygame.Surface((AnchoX,AnchoY))

#====================================================================================================#
#                                  Funcion Background y manual                                       #
#                   Imprime el fondo del juego sobre la surface creada anteriormente                 #
#                    Salidas: Muestra una imagenindicada sprt[x] por pantalla                        #
#====================================================================================================#

def Background():
    return Screen.blit(sprt[0],(xd,yd))

def Menu():
    return Screen.blit(sprt[11],(xd,yd))

def Manual():
    return Screen.blit(sprt[12],(xd,yd))

#====================================================================================================#
#                                    La mitica funcion pausa.                                        #
#                                      La de toda la vida.                                           #
#====================================================================================================#

def Pausa():
    while 1:
        e = pygame.event.wait()
        if e.type in (pygame.QUIT, pygame.KEYDOWN):
            return

#====================================================================================================#
#                                         While principal                                            #
#                    Ciclo principal del codigo, en el se registran algunos eventos                  #
#                                      Ejecucion de funciones                                        #
#====================================================================================================#

Screen = pygame_init() #.......................... Pantalla
sprt = arraySprt()     #.......................... Imagenes Cargadas
Map = MapInit(maxX,maxY) #........................ Mapa
pelota = Redball(180,760) #....................... Jugador
mundo = world(matriz,sprt) #...................... Matriz
initball = ball() #............................... BotInicio
ckey = pygame.key.get_pressed()#.................. Verificador de pulsaciones

boton_iniciar = botones(150,650, sprt[13]) #...... Boton Iniciar
boton_manual = botones(430,650, sprt[14])  #...... Boton Manual

ball.ballInit(initball) #......................... Inicializo la pelota del inicio (bot)

while ToF:

    if ckey[pygame.K_q]: #........................ Atajo para cerrar el programa
        ToF = False

    ev = pygame.event.get() #..................... Capturador de eventos
    for e in ev:
        if e.type == pygame.QUIT:
            ToF = False
        if e.type == pygame.MOUSEMOTION : mouX,mouY = e.pos #Event Mouse.

    if menu == True: #............................ Si la variable menu es True:
        pygame.mouse.set_visible(True)#........... Mouse Visible.
        ball.Updateball(initball) #............... Comienza el update del bot de inicio.
        Menu() #.................................. Blit de background del menu.
        ball.Pintaball(initball,Screen,sprt) #.... Se pinta el sprt sobre la posicion del bot (Update).

        if boton_manual.draw(Screen): #........... Si se presiona el boton manual:
            Manual()#............................. Blit de background del manual.
            pygame.display.flip()
            Pausa()#.............................. Pausa la img por tiempo indefinido.

        if boton_iniciar.draw(Screen):#........... Si se presiona el boton manual:
            pygame.mouse.set_visible(False)#...... Mouse se vuelve invisible
            menu = False #........................ Variable menu toma valor False.

    else:    #.................................... Por lo tanto, si menu es falto se ejecutan
        #......................................... el resto de las acciones update y da inicio al level01.
        Background() #............................ Blit de background del mapa.
        mundo.draw(Screen) #...................... mundo corresponde a la clase mundo, por lo tanto
        mundo.deadpointdraw(Screen) #............. las 4 funciones rellenan/dibujan el mapa con los 
        mundo.flagdraw(Screen) #.................. distintos sprites/rect correspondiente.
        mundo.finaldraw(Screen) #.................
        pelota.update(Screen,mundo,sprt) #........ Update de la posicion e imagen de la pelota (player)

    pygame.time.delay(22)
    pygame.display.flip()
pygame.quit
