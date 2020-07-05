#!/usr/bin/env python3

import math, os, random, sys

import pygame
from pygame.locals import *

from configuracion import *
from funcionesVACIAS import *
from extras import *


def main():
    # centrar la ventana y despues inicializar pygame
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    # pygame.mixer.init()

    # preparar la ventana
    pygame.display.set_caption("TutiFrutiUNGS")
    screen = pygame.display.set_mode((ANCHO, ALTO))

    # Tiempo total del juego
    gameClock = pygame.time.Clock()
    totaltime = 0
    fps = FPS_INICIAL

    puntos = 0
    candidata = ""



    #musica de fondo
    pygame.mixer.music.load("Test_Card.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(99)

    #sonidos
    sonidoGana=pygame.mixer.Sound("correct-ding.wav")
    sonidoPierde=pygame.mixer.Sound("wrong-sound.wav")



    abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    items=["colores","paises","animales","nombres","frutas","instrumentos"]
    # lectura de los archivos .txt de cada item
    colores=LeoLista('colores.txt')
    paises=LeoLista('paises.txt')
    animales=LeoLista('animales.txt')
    nombres=LeoLista('nombres.txt')
    frutas=LeoLista('frutas.txt')
    instrumentos=LeoLista('instrumentos.txt')

    # listado completo
    listaDeTodo=[colores,paises,animales,nombres,frutas,instrumentos]
    letraAzar = unaAlAzar(abc)
    palabraUsuario=""
    eleccionUsuario=[]
    eleccionCompu=[]
    i=0

    
    while i < len(items):
        # 1 frame cada 1/fps segundos
        gameClock.tick(fps)
        totaltime += gameClock.get_time()

        fps = 3


        # buscar la tecla presionada del modulo de eventos de pygame
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                return
            if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    palabraUsuario += letra
                    if e.key == K_BACKSPACE:
                        palabraUsuario = palabraUsuario[0:len(palabraUsuario)-1]
                    if e.key == K_RETURN:
                        eleccionUsuario.append(palabraUsuario)
                        #chequea si es correcta y suma o resta puntos
                        sumar=esCorrecta(palabraUsuario, letraAzar, items[i], items, listaDeTodo)
                        if sumar==10:
                             #Sonido correcto
                            sonidoGana.play()
                            puntos=puntos+sumar
                            palabraUsuario=""
                        else:
                              #Sonido incorrecto
                            sonidoPierde.play()
                            puntos=puntos+sumar
                            palabraUsuario=""
                        i=i+1

        segundos = pygame.time.get_ticks() / 1000



        # limpiar pantalla anterior
        screen.fill(COLOR_FONDO)
        if i<len(items):
            dibujar(screen, letraAzar, items[i], palabraUsuario, puntos, segundos)
        else:
            eleccionCompu=juegaCompu(letraAzar, listaDeTodo)
            # puntuacion especial
            cont=0
            while cont<len(items):
                if eleccionUsuario[cont] == eleccionCompu[cont]:
                    puntos=puntos-5
                cont=cont+1
            dibujarSalida(screen, letraAzar, items, eleccionUsuario, eleccionCompu, puntos, segundos)
        pygame.display.flip()


    # quitar programa
    while True:
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                return
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return


if __name__ == "__main__":
    main()
