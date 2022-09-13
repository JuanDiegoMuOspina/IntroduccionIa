import random
from copy import deepcopy
from colorama import init, Fore, Style

#Jugando un triquit con 4 fichas
#Definiendo Letras para el juego X AZUL Y O ROJO
jugador1="X"
jugadorCPU="O"
#MINIMO DE LA MATRIZ
MINIMO_FILAS = 5
MAXIMO_FILAS = 101
MINIMO_COLUMNAS = 6
MAXIMO_COLUMNAS = 10
ESPACIO_VACIO = " "
CONECTA=4
JUGADOR_1=1
JUGADOR_2=2
#Primer paso es generar el ambiente para contruir la matriz del juego

def iniciarJuego():
   while True:
        eleccion = input("1- iniciar Juego:"
                         "\n"

                         "2- Salir"
                         "\n"
                         "Elige: ")
        if eleccion == "2":
            break
        
        if eleccion == "1":
            filas, columnas = solicitar_filas(), solicitar_columnas()
            
            while True:
                tablero = crear_tablero(filas, columnas)
                jugador_vs_computadora(tablero)
                if not volver_a_jugar():
                    break
               
                    

    #Contruir Metodo para solicitar filas, columnas
def solicitar_filas():
    while True:
        filas = solicitar_entero_valido("Ingresa el número de filas:")
        if filas < MINIMO_FILAS or filas > MAXIMO_FILAS:
            print(f"El mínimo de filas es {MINIMO_FILAS} y el máximo {MAXIMO_FILAS}")
        else:
            return filas
def solicitar_columnas():
    while True:
        columnas = solicitar_entero_valido("Ingresa el número de columnas:")
        if columnas < MINIMO_COLUMNAS or columnas > MAXIMO_COLUMNAS:
            print(f"El mínimo de columnas es {MINIMO_COLUMNAS} y el máximo {MAXIMO_COLUMNAS}")
        else:
            return columnas
        #Metodo que confirma si un carácter es valido
def solicitar_entero_valido(mensaje):
    """
    Solicita un número entero y lo sigue solicitando
    mientras no sea un entero válido
    """
    while True:
        try:
            posible_entero = int(input(mensaje))
            return posible_entero
        except ValueError:
            continue
    #Contruir Metodo para solicitar filas, columnas
    #
    #Contruir tablero
def crear_tablero(filas, columnas):
    tablero = []
    for fila in range(filas):
        tablero.append([])
        for columna in range(columnas):
            tablero[fila].append(ESPACIO_VACIO)
    return tablero
    #Contruir tablero
#Primer paso es generar el ambiente para contruir la matriz del juego





####Ejecutamos el tablero para iniciarJuego
def jugador_vs_computadora(tablero):
    global ESTA_JUGANDO_CPU
    ESTA_JUGANDO_CPU = True
    jugador_actual = elegir_jugador_al_azar()
    while True:
        imprimir_tablero(tablero)
        #imprimir_tiradas_faltantes(tablero)
        if jugador_actual == JUGADOR_1:
            
            print("turno del jugador 1")
        else:
            print("CPU pensando...")
            
        
#### Metodos de tablero #################################
#####Metodo para generar numero aleatrio
def elegir_jugador_al_azar():
    return random.choice([JUGADOR_1, JUGADOR_2])

#### Metodo para generar String en consola de tablero
def imprimir_tablero(tablero):
    # Imprime números de columnas
    print("|", end="")
    for f in range(1, len(tablero[0]) + 1):
        print(f, end="|")
    print("")
    # Datos
    for fila in tablero:
        print("|", end="")
        for valor in fila:
            color_terminal = Fore.GREEN
            if valor == jugadorCPU:
                color_terminal = Fore.RED
            print(color_terminal + valor, end="")
            print(Style.RESET_ALL, end="")
            print("|", end="")
        print("")
    

####Ejecutamos el tablero para iniciarJuego

iniciarJuego()