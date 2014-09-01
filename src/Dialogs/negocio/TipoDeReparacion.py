# -*- coding: utf-8 -*-
'''
Created on 28/10/2012

@author: urrutia
'''

from persistent import Persistent
from persistent.list import PersistentList


class TipoDeReparacion(Persistent):
    '''
    classdocs
    @version: 
    @author: 
    '''

    ''' ATTRIBUTES

    codigoTipoReparacion  (private)

    nombre  (private)

    descripcion  (private)

    tiempoEstimado  (private)

    repuestosRequeridos 

    '''

    def __init__(self, nombre, descripcion, repuestos=[]):
        '''
        Constructor
        @return: 
        @author: 
        '''
        self._nombre = nombre
        self._descripcion = descripcion
        self._repuestos = PersistentList()
        self._repuestos.extend(repuestos)

    def getRepuestos(self):
        return self._repuestos

    def getRepuesto(self, unNombreRepuesto):
        repuestos = filter(lambda n: n.getTipoDeRepuesto().getNombre() == unNombreRepuesto, self.getRepuestos())
        return repuestos[0]

    def setRepuestos(self, repuestos):
        self._repuestos = repuestos

    def addRepuesto(self, unRepuesto):
        self._repuestos.append(unRepuesto)
        self._repuestos.sort(cmp=lambda x, y: cmp(x.getNombre(), y.getNombre()))

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getDescipcion(self):
        return self._descripcion

    def setDescripcion(self, descripcion):
        self._descripcion = descripcion

    def __eq__(self, otro):
        return self.getNombre() == otro.getNombre()
