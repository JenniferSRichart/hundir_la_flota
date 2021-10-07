
import random
import numpy as np

def print_tablero(tablero):
    for fila in tablero:
        print (" ".join(fila)) #espacios entre posiciones

def fila_aleatoria(tablero): # posicion aleatoria barco por fila
    return random.randint(0,len(tablero)-1)

def columna_aleatoria(tablero): # posicion aleatoria barco por columna
    return random.randint(0,len(tablero[0])-1)

def comprobadorEspacios(columna,fila,orientacion,tamanoEsloraBarco, tablero):
	try:
		posicionFila = 0
		posicionColumna = 0
		if orientacion == 1: #horizontal
			tablero[fila][columna+(tamanoEsloraBarco-1)] #comprobar si el barco cabe
			for x in tablero:
				if (fila == posicionFila):
					for y in x:
						if (columna==posicionColumna and tamanoEsloraBarco!=0):
							tamanoEsloraBarco-=1
							if (y!="0"):
								return False
						elif(tamanoEsloraBarco!=0):
							posicionColumna +=1
				posicionFila+=1
					
		elif orientacion == 0: #vertical
			tablero[fila+(tamanoEsloraBarco-1)][columna] #comprobar si el barco cabe
			for x in tablero:
				if posicionFila==fila and tamanoEsloraBarco!=0:
					tamanoEsloraBarco-=1
					if x[columna]=="1" or x[columna]=="2" or x[columna]=="3" or x[columna]=="4" or x[columna]=="5":
						return False
				elif tamanoEsloraBarco!=0:
					posicionFila+=1
		return True
	except IndexError:
		return False


						