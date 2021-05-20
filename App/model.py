﻿"""
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import haversine as hs
from DISClib.ADT.graph import gr
from DISClib.ADT import map as mp
from DISClib.ADT import list as lt
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.Algorithms.Sorting import mergesort as merge
from DISClib.Utils import error as error
assert cf

# -----------------------------------------------------
#                       API
# -----------------------------------------------------


# Construccion de modelos

def newAnalyzer():
    try:
        analyzer = {
                    'cables': None,
                    "landingPoints":None,
                    'connections': None,
                    'components': None,
                    'paths': None
                    }

        analyzer['cables'] = mp.newMap(numelements=14000,
                                     maptype='PROBING',
                                     comparefunction=compareLandingPointIds)
                                     
        analyzer["landingPoints"] = mp.newMap(numelements=14000,
                                     maptype='PROBING',
                                     comparefunction=compareLandingPointIds)

        analyzer['connections'] = gr.newGraph(datastructure='ADJ_LIST',
                                              directed=True,
                                              size=14000,
                                              comparefunction=compareLandingPointIds)
        return analyzer
    except Exception as exp:
        error.reraise(exp, 'model:newAnalyzer')

# Funciones para agregar informacion al grafo

def addStopConnection(analyzer, cable):
    """
    Adiciona los landing points al grafo como vertices y arcos entre los landing points adyacentes.

    Los vertices tienen por nombre el identificador del landing point
    seguido del cable que sirve.
    """
    try:
        origin = formatVertexOrigin(cable)
        destination = formatVertexDestination(cable)

        distance = formatDistance(cable)
        
        addStop(analyzer, origin)
        addStop(analyzer, destination)
        addConnection(analyzer, origin, destination, distance)
        addRouteStop(analyzer, service)
        addRouteStop(analyzer, lastservice)
        return analyzer
    except Exception as exp:
        error.reraise(exp, 'model:addStopConnection')

# ==============================
# Funciones de consulta
# ==============================

# ==============================
# Funciones Helper
# ==============================




def formatVertexOrigin(cable):
    """
    Se formatea el nombrer del vertice con el id de la estación
    seguido de la ruta.
    """
    name = cable['origin'] + '-'
    name = name + cable['cable_id']
    return name

def formatVertexDestination(cable):
    name = cable["destination"] + '-'
    name = name + cable["cable_id"]
    return name

def formatDistance(cable, analizer):
    origin = cable["origin"]
    destination = cable["destination"]
    coordinatesOrigin = getCoordinates(analizer, origin)
    coordinatesDestination = getCoordinates(analizer,destination)
    



def getCoordinates(analizer, place):
    latitudePlace = mp.get(analizer["landingPoints"], place)
    latitudePlace = me.getValue(latitudePlace)
    latitudePlace = float(latitudePlace["latitude"])

    longitudePlace = mp.get(analizer["landingPoints"], place)
    longitudePlace = me.getValue(longitudePlace)
    longitudePlace = float(longitudePlace["longitude"])
    return latitudePlace, longitudePlace


# ==============================
# Funciones de Comparacion
# ==============================

def compareLandingPointIds(stop, keyValueLP):
    """
    Compara dos estaciones
    """
    LPId = keyValueLP['key']
    if (stop == LPId):
        return 0
    elif (stop > LPId):
        return 1
    else:
        return -1