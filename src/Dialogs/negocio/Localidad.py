# -*- coding: utf-8 -*-
'''
Created on 28/10/2012

@author: urrutia
'''

from persistent import Persistent

class Localidad(Persistent):
    '''
    classdocs
    @version: 
    @author: 
    '''
    
    ''' ATTRIBUTES       
    
    codigoPostal  (private)
        
    nombre  (private)
    
    '''
    
    def __init__(self, nombre, codigoPostal):
        '''
        Constructor
        @author: 
        '''
        self._nombre = nombre
        self._codigoPostal = codigoPostal
        
    def getNombre(self):
        return self._nombre
    
    def getCodigoPostal(self):
        return self._codigoPostal
    
    def setNombre(self, nombre):
        self._nombre = nombre
        
    def setCodigoPostal(self, codigoPostal):
        self._codigoPostal = codigoPostal
        
    def setProvincia(self, provincia):
        self._provincia = provincia
        
    def getProvincia(self):
        return self._provincia
    
    #===========================================================================
    # Para ir agragando provincias en tiempo de ejecucion
    # Métodos estáticos.
    #===========================================================================
    '''
    def agregarProvincia(self, provincia):
        try:
            self._localidades[provincia]
        except KeyError:
            self._localidades[provincia] = {}
            
    def agregarLocalidad(self, provincia, localidad, codigoPostal):
        try:
            self._localidades[provincia]
        except KeyError:
            provincia = self._localidades[provincia]
            provincia[codigoPostal] = localidad
            self._localidades[provincia] = provincia'''