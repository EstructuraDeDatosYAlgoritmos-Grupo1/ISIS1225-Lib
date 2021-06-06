"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """
import time
import tracemalloc
import sys
import config
import threading
from App import controller
from DISClib.ADT import stack
assert config

# ___________________________________________________
#  Variables
# ___________________________________________________


connectionsfile = 'connections.csv'
countriesfile = 'countries.csv'
LPfile = 'landing_points.csv'
initialLP = None

# ___________________________________________________
#  Menu principal
# ___________________________________________________


def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información al analizador")
    print("3- Identificar clusteres de comunicacion")
    print("4- Encontrar los landing points que sirven como punto de interconexión")
    print("5- Encontrar ruta mínima entre países")
    print("6- Identificar red de expansión mínima")
    print("7- Impacto de falla de un landing point ")
    print("0- Salir")
    print("*******************************************")



def optionTwo(analyzer):
    print("\nCargando información....")
    controller.loadCables(analyzer, LPfile, connectionsfile, countriesfile)
    numedges = controller.totalConnections(analyzer)
    numvertex = controller.totalVertices(analyzer)
    print('Numero de vertices: ' + str(numvertex))
    print('Numero de arcos: ' + str(numedges))
    print('El limite de recursion actual: ' + str(sys.getrecursionlimit()))

def optionThree(analyzer, lp1, lp2):
    print("\nEl número de componentes conectados es: " + str(controller.connectedComponents(analyzer)))
    if controller.areConnectedLP(analyzer, lp1, lp2) == 1:  
       print("\nLos landing points "+ str(lp1) + " y " + str(lp2) + " están conectados ")
    else:
       print("\nLos landing points "+ str(lp1) + " y " + str(lp2) + " no están conectados ")

def optionFour(analyzer):
    return controller.criticalPoints(analyzer)

def optionFive(analyzer, p1,p2):
    return controller.getMinimumDistance(analyzer, p1,p2)

def optionSix(analyzer):
    return controller.getMinimumSpaningTree(analyzer)

def optionSeven(analyzer, lp):
    return controller.failureEffect(analyzer, lp)

   
#Funciones para la toma del tiempo y memoria

def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def deltaMemory(start_memory, stop_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory



"""
Menu principal
"""

def thread_cycle():
    while True:
        printMenu()
        inputs = input('Seleccione una opción para continuar\n>')

        if int(inputs[0]) == 1:
            print("\nInicializando....")
            analyzer = controller.initAnalyzer()

        elif int(inputs[0]) == 2:
            optionTwo(analyzer)

        elif int(inputs[0]) == 3:
            print("Ingrese los landing points que desea evaluar: ")
            lp1 = input('Ingrese el nombre de un landing point: ')
            lp2 = input('Ingrese el nombre de otro landing point: ')

            delta_time = -1.0
            delta_memory = -1.0
            tracemalloc.start()
            start_time = getTime()
            start_memory = getMemory()

            optionThree(analyzer, lp1, lp2)

            stop_memory = getMemory()
            stop_time = getTime()
            tracemalloc.stop()
            delta_time = stop_time - start_time
            delta_memory = deltaMemory(start_memory, stop_memory)
            print(delta_time,delta_memory)

        elif int(inputs[0]) == 4:
            
            delta_time = -1.0
            delta_memory = -1.0
            tracemalloc.start()
            start_time = getTime()
            start_memory = getMemory()

            optionFour(analyzer)

            stop_memory = getMemory()
            stop_time = getTime()
            tracemalloc.stop()
            delta_time = stop_time - start_time
            delta_memory = deltaMemory(start_memory, stop_memory)
            print(delta_time,delta_memory)
            
        elif int(inputs[0]) == 5:
            print("Ingrese los países que desea evaluar ")
            p1 = input('Ingrese el nombre del primer país: ')
            p2 = input('Ingrese el nombre del segundo país: ')

            delta_time = -1.0
            delta_memory = -1.0
            tracemalloc.start()
            start_time = getTime()
            start_memory = getMemory()

            optionFive(analyzer, p1,p2)

            stop_memory = getMemory()
            stop_time = getTime()
            tracemalloc.stop()
            delta_time = stop_time - start_time
            delta_memory = deltaMemory(start_memory, stop_memory)
            print(delta_time,delta_memory)

        elif int(inputs[0]) == 6:

            delta_time = -1.0
            delta_memory = -1.0
            tracemalloc.start()
            start_time = getTime()
            start_memory = getMemory()

            optionSix(analyzer)

            stop_memory = getMemory()
            stop_time = getTime()
            tracemalloc.stop()
            delta_time = stop_time - start_time
            delta_memory = deltaMemory(start_memory, stop_memory)
            print(delta_time,delta_memory)
            
        elif int(inputs[0]) == 7:
            lp = input('Ingrese el nombre del landing point que desea evaluar: ')

            delta_time = -1.0
            delta_memory = -1.0
            tracemalloc.start()
            start_time = getTime()
            start_memory = getMemory()

            optionSeven(analyzer, lp)

            stop_memory = getMemory()
            stop_time = getTime()
            tracemalloc.stop()
            delta_time = stop_time - start_time
            delta_memory = deltaMemory(start_memory, stop_memory)
            print(delta_time,delta_memory)

        else:
            sys.exit(0)
    sys.exit(0)

    


if __name__ == "__main__":
    threading.stack_size(67108864)  # 64MB stack
    sys.setrecursionlimit(2 ** 20)
    thread = threading.Thread(target=thread_cycle)
    thread.start()
