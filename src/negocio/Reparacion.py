# -*- coding: utf-8 -*-
'''
Created on 28/10/2012

@author: urrutia
'''

from persistent import Persistent

from Empleado import *
from RepuestoUtilizados import *
from TipoDeReparacion import *

class Reparacion(Persistent):
    '''
    classdocs
    @version: 
    @author: 
    '''
    
    ''' ATTRIBUTES
    
    
    
    codigoReparacion  (private)
    
    
    tipoDeReparacion (private)
    
    
    descripcion  (private)
    
    
    
    fechaEstimadaInicio  (private)
    
    
    
    fechaInicio  (private)
    
    
    
    fechaFin  (private)
    
    
    
    nroOrden  (private)
    
    repuestosUtilizados (private)
    
    '''

    def __init__(self, tipoDeReparacion, descripcion, repuestosUtilizados):
        '''
        Constructor
        @return: 
        @author: 
        '''
        self._tipoDeReparacion = tipoDeReparacion
        self._descripcion = descripcion
        self._repuestosUtilizados = repuestosUtilizados
        
    def getDatos(self):
        '''
        @return: 
        @author: 
        '''
        pass
    
    def setFinalizacion(self):
        '''
        @return: 
        @author: 
        '''
        pass
    
    def addResponsable(self):
        '''
        @return: 
        @author: 
        '''
        pass
    
    def setFechaDeInicio(self):
        '''
        @return: 
        @author: 
        '''
        pass
    
    def planificarReparacion(self):
        '''
        @return: 
        @author: 
        '''
        pass
    
    def getTipoDeReparacion(self):
        return self._tipoDeReparacion
    
    def getDescripcion(self):
        return self._descripcion
    
    def getRepuestosUtilizados(self):
        return self._repuestosUtilizados