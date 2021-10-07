import numpy as np
import random 


#Tableros en el juego 

tableroBarcos = np.full(fill_value = "|_|", shape = (10,10)) #dimensiones del tablero

tableroBarcos[6,7] = " 1 "
tableroBarcos[1,3] = " 2 "
tableroBarcos[1,4] = " 2 "
tableroBarcos[6,4] = " 3 "
tableroBarcos[6,2] = " 3 "   
tableroBarcos[6,3] = " 3 "
tableroBarcos[5,7] = " 4 "
tableroBarcos[5,8] = " 4 "
tableroBarcos[5,9] = " 4 "
tableroBarcos[5,6] = " 4 "
tableroBarcos[7,1] = " 5 "
tableroBarcos[8,1] = " 5 "
tableroBarcos[9,1] = " 5 "
tableroBarcos[3,6] = " 6 "
tableroBarcos[4,6] = " 6 "
tableroBarcos[0,0] = " 7 "
tableroBarcos[1,0] = " 7 "
tableroBarcos[0,5] = " 8 "
tableroBarcos[0,9] = " 9 "
tableroBarcos[3,5] = " 0 "
print(tableroBarcos)

tableroJugadorDisparos = np.full(fill_value = "|_|", shape = (10,10)) 
print(tableroJugadorDisparos)

tableroBarcosMaquina = np.full(fill_value = "|_|", shape = (10,10))
print(tableroBarcosMaquina)

tableroMaquinaDisparos = np.full(fill_value = "|_|", shape = (10,10))
print(tableroMaquinaDisparos)