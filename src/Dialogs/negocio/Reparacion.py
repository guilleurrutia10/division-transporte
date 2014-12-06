# -*- coding: utf-8 -*-
'''
Created on 28/10/2012

@author: urrutia
'''

from persistent import Persistent
from persistent.list import PersistentList

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

    def __init__(self, tipoDeReparacion, descripcion, repuestosUtilizados, codigo = None):
        '''
        Constructor
        @return: 
        @author: 
        '''
        self._codigo = codigo
        self._tipoDeReparacion = tipoDeReparacion
        self._descripcion = descripcion
        self._repuestosUtilizados = PersistentList()
        self._repuestosUtilizados.extend(repuestosUtilizados)
        self.fechaInicio = None
        self.fechaFin = None
        
        self._finalizada = False
        self._planificada = False
        
    def getCodigo(self):
        return self._codigo
    
    def getNombre(self):
        return self._tipoDeReparacion.getNombre()
        
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
    
    def __cmp__(self, otro):
        if self.getTipoDeReparacion().getNombre() == otro.getTipoDeReparacion().getNombre():
            return 0
        else:
            return -1
    
    def finalizar(self):    
        self._finalizada = True
        
    def estaFinalizada(self):
        return self._finalizada
    
    def estado(self):
        if self.estaFinalizada():
            return 'Finalizada'
        return 'Sin finalizar'
    
    def getFechaInicio(self):
        return self.fechaInicio
    
    def getFechaFin(self):
        return self.fechaFin

    def planificada(self):
        self._planificada = True
        
    def estaPlanificada(self):
        return self._planificada
    
    def __str__(self):
        return '%s | %s | %s' %(self._codigo, self._tipoDeReparacion, self._descripcion)