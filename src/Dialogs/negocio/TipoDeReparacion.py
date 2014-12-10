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

    def __init__(self, nombre, descripcion, repuestos=[], tiempo_estimado = 30, codigo= 'ERROR'):
        '''
        Constructor
        @return: 
        @author: 
        '''
        self._nombre = nombre
        self._descripcion = descripcion
        self._repuestos = PersistentList()
        self._repuestos.extend(repuestos)
        self._tiempo_estimado = tiempo_estimado
        self._codigo = codigo
        print "DEBUG: Tipo de Reparacion: %s | %s | %s | %d"%(codigo, nombre, descripcion, tiempo_estimado)

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
    
    def __str__(self):
        return "%s: %s" %(self._nombre, self._descripcion)

    def getTiempoEstimado(self):
        return self._tiempo_estimado


    def getCodigo(self):
        return self._codigo


    def setTiempoEstimado(self, value):
        self._tiempo_estimado = value


    def setCodigo(self, value):
        self._codigo = value

