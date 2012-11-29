# -*- coding: utf-8 -*-
'''
Created on 28/10/2012

@author: urrutia
'''

from persistent import Persistent

from RepuestoRequeridos import *

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

    def __init__(self, nombre, descripcion):
        '''
        Constructor
        @return: 
        @author: 
        '''
        self._nombre = nombre
        self._descripcion = descripcion
    
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