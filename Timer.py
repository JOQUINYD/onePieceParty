import pygame
import random
from pygame.locals import *
import sys 
import math
import numpy as np
import time

def juego():
    iniTime = time.time()
    timer = 0
    maxTime = 60            #Tiempo maximo para el juego en segundos
    while timer<maxTime:
        endTime = time.time()
        timer = endTime - iniTime
        #Ejemplo cuenta regresiva
        print(int(maxTime-timer))
        #Aquí van todos los eventos del juego


#Para imprimir el cronometro solo necesitan imprimir int(maxTime-timer)

juego()
