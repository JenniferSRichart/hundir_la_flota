import numpy as np
import random
from Tableros import tableroJugadorDisparos, tableroBarcos, tableroBarcosMaquina, tableroMaquinaDisparos
from Variables import fila_aleatoria, columna_aleatoria, comprobadorEspacios


'''
    Juego de Hundir la Flota cuenta con 10 barcos, desde una posicion de eslora hasta 4,
    en cada jugada se tendra la oportunidad de disparar a los barcos, si aciertas podras volver a jugar. 
    el juego finaliza cuando tu o la maquina acierten las 20 posiciones donde se encuentran los barcos. 
    Observacion: Su nivel de dificultad es alto, ya que no existe distancia minima entre barcos, 
    solo sabras que has hundido a un barco, mas no a cual.
'''
print("\n")
print('Bienvenido al Juego Hundir la Flota. Version 1.0 Je!')
print("\n")
print('Reglas del juego: ')
print("\n")
print('* Tu objetivo es derribar la flota de barcos del enemigo, antes de que el derribe los tuyos\ntanto tu como el tienen 10 barcos, de tamanos entre 1 a 4 esloras,')
print('* Ganaras la partida cuando logres completar los 20 aciertos, eso si la maquina no te gana primero!\nno solo es suerte sino estrategia!')
print('Recuerda los barcos no tienen espacios entre ellos (para que hacerlo facil si se puede hacer dificil!)')
print("\n")
turno = 0
aciertos1 = 0
aciertos2 = 0
contador = 1

while aciertos1 != 20 or aciertos2!= 20:
    
    if turno%2==0: # Momento de jugar
        miTablero = tableroBarcos
        suTablero = tableroBarcosMaquina
        aciertaBarco = tableroMaquinaDisparos
        listaBarcos = tableroJugadorDisparos
        aciertosJugador = aciertos1	

    else:  #ahora le toca a la maquina
        miTablero = tableroBarcosMaquina
        suTablero = tableroBarcos
        aciertaBarco = tableroJugadorDisparos
        listaBarcos = tableroMaquinaDisparos
        aciertosJugador = aciertos2
        	

    bandera = True 
    while bandera:
        try:       #error si ingresa letras o numeros mayores a 9
            valido = False
            while valido == False:
                imput_fila = int(input("Indica la fila:"))
                imput_columna = int(input("Indica la columna:"))
                if (imput_columna >= 0 and imput_columna <= 9) or (imput_fila >= 0 and imput_fila <= 9):
                    valido = True
                else:
                    print("Vuelve a interlo el tablero es del 0 al 9")
                break
        except ValueError:
            print("Oops! Esas no pueden ser las coordenadas del barco, tu puedes, venga!!!") 

        if tableroBarcos[imput_fila][imput_columna]!= "|_|":
            tableroJugadorDisparos [imput_fila][imput_columna] = ' B '
            tableroBarcos [imput_fila][imput_columna] = ' B '
            aciertosJugador += 1
            print('Tus disparos han sido:')
            print(f"X: {imput_fila}\nY: {imput_columna}")
            print("\t")
            print(tableroJugadorDisparos)
            contador +=1
            
        else:
            tableroJugadorDisparos [imput_fila][imput_columna] = ' A '
            print('Tus disparos han sido:')
            print(f"X: {imput_fila}\nY: {imput_columna}")
            print("\t")
            print(tableroJugadorDisparos)
            bandera = False

print("Game Over")


'''
    Mejoras pendientes:
    - Que la asignacion de los barcos se haga de manera aleatoria
    - Y una vez sea asi que los barcos no esten en la posicion donde hay uno
    - Que puedas ver a cual barco le has dado, no solo si es barco
    - Que se guarde el Id del Jugador, con las puntuaciones, para luego sacar el ranking
    - Mejorar el codigo con Clases
'''