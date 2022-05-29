
import pygame,world,Redball
from world import *
from pygame.locals import *
from Redball import Redball
from time import *

#====================================================================================================#
#                                     Definiciones Globales                                          #
#====================================================================================================#
#Para ver las intrucciones/mapeo de teclas para movimiento debe presionar la tecla i, 
# en la version final se encontrara dentro de un menu de inicio. 

minX = 0      ; maxX = 800                     ;         xd = 0            ;           yd = 0                          
#Valor minimo y maximo del eje X en el mapa.    #Valor asignado a 0 en x       #Valor asignado a 0 en Y          
minY = 0      ; maxY = 800                      #se puede usar para sumar      #se puede usar para sumar         
#Valor minimo y maximo del eje Y en el mapa.    #un numero y asi cambiar       #un numero y asi cambiar          
#                                               #el valor del eje x.           #el valor del eje y.

ToF = True
#Valor True, usado principalmente para crear un ciclo while infinito.

res = (maxX,maxY)                 
#Resolucion de la ventana.

tileX = 128            ;              tileY = 128
#Valores en X e Y del tile principal, a futuro se reescalara.

tileSize = 20
#valor rescalado de todos los sprt.

mouX = 0                       ; mouY = 0                       ; ToFM = True 
#Valor asignado a 0 en x       #Valor asignado a 0 en Y          
#se puede usar para sumar      #se puede usar para sumar         
#un numero y asi cambiar       #un numero y asi cambiar          
#el valor del eje x(MOUSE).    #el valor del eje y(MOUSE).       

Timer1 = 10       

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
    aSprt.append(Load_Image('./sprt/S03.png',False )) # Grey tile                [4]
    aSprt.append(Load_Image('./sprt/S04.png',False )) # Grey tile                [5]
    aSprt.append(Load_Image('./sprt/S07.png',True ))  # Red Ball                 [6]
    aSprt.append(Load_Image('./sprt/S08.png',False )) # Blue Ball                [7]
    aSprt.append(Load_Image('./sprt/S09.png',False )) # Plop Ball                [8]
    aSprt.append(Load_Image('./sprt/S10.png',False )) # Change Ring              [9]
    aSprt.append(Load_Image('./sprt/S11.png',False )) # Pinchos                  [10]
    aSprt.append(Load_Image('./sprt/Manual.png',False ))# Titulo                 [11]

    return aSprt

#====================================================================================================#
#                                        Inicializa PyGames.-                                        #
#                                  Inicializa el Engine de PyGame.                                   #
#====================================================================================================#

def pygame_init():
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption('Red Bounce Ball - Luciano Revillod')
    pygame.mouse.set_visible(False)
    return pygame.display.set_mode(res)

#====================================================================================================#
#                                         Funcion MapInit                                            #
#                       Crea y retorna una surface donde se imprimira el mapa                        #
#====================================================================================================#

def MapInit(AnchoX,AnchoY):
    return pygame.Surface((AnchoX,AnchoY))

#====================================================================================================#
#                                 Funcion Background y manual                                        #
#                   Imprime el fondo del juego sobre la surface creada anteriormente                 #
#====================================================================================================#

def Background():
    return Screen.blit(sprt[0],(xd,yd))

def Manual():
    return Screen.blit(sprt[11],(200,180))


#====================================================================================================#
#                                         While principal                                            #
#                    Ciclo principal del codigo, en el se registran algunos eventos                  #
#                                      Ejecucion de funciones                                        #
#====================================================================================================#

Screen = pygame_init()
sprt = arraySprt()
Map = MapInit(maxX,maxY)
pelota = Redball(20,760)
mundo = world(matriz,sprt)

while ToF:
    ev = pygame.event.get()
    for e in ev:
        if e.type == pygame.QUIT:
            ToF = False
        if e.type == pygame.MOUSEMOTION : mouX,mouY = e.pos #Event Mouse.
    
    Background()
    mundo.draw(Screen)
    #Se muestran por pantalla todos los sprites almacenados en la matriz y clase world.
    pelota.update(Screen,mundo)
    #update de la clase Player, recolecta las teclas presionadas y actualiza la posicion de la pelota.
    ckey = pygame.key.get_pressed() 
    if ckey[pygame.K_i]:
            Manual()
    pygame.time.delay(22)
    pygame.display.flip()
pygame.quit
