"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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

from App import config as cf
from App import model
import csv



# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________


def initAnalyzer():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # analyzer es utilizado para interactuar con el modelo
    analyzer = model.newAnalyzer()
    return analyzer


# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________

def loadCables(analyzer, LPfile, connectionsfile):
    LPfile = cf.data_dir + LPfile
    LPDict = csv.DictReader(open(LPfile, encoding= "utf-8"), delimiter=",")
    connectionsfile = cf.data_dir + connectionsfile
    connectionsDict = csv.DictReader(open(connectionsfile, encoding="utf-8"), delimiter=",")

    for point in LPDict:
        model.addLP(analyzer, point)
    for cable in connectionsDict:
        model.addConnections(analyzer, cable)
    return analyzer

def totalVertices(analyzer):
    return model.totalStops(analyzer)

def totalConnections(analyzer):
    return model.totalConnections(analyzer)

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
