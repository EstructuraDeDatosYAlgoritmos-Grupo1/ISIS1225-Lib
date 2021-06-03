﻿"""
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
    print("5- ")
    print("6- ")
    print("7- ")
    print("0- Salir")
    print("*******************************************")



def optionTwo(analyzer):
    print("\nCargando información....")
    controller.loadCables(analyzer, LPfile, connectionsfile)
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
            print("Ingrese dos landing points para saber si están conectados....")
            lp1 = input('Ingrese el id de un landing point: ')
            lp2 = input('Ingrese el id de otro landing point: ')
            optionThree(analyzer, lp1, lp2)

        elif int(inputs[0]) == 4:
           optionFour(analyzer)
            

        elif int(inputs[0]) == 5:
            pass

        elif int(inputs[0]) == 6:
            pass

        elif int(inputs[0]) == 7:
            pass

        else:
            sys.exit(0)
    sys.exit(0)


if __name__ == "__main__":
    threading.stack_size(67108864)  # 64MB stack
    sys.setrecursionlimit(2 ** 20)
    thread = threading.Thread(target=thread_cycle)
    thread.start()
