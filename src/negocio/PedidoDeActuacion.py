# -*- coding: utf-8 -*-
'''
Created on 28/10/2012

@author: urrutia
'''

from persistent import Persistent

from RepuestoUtilizados import *

class PedidoDeActuacion(Persistent):
    '''
    classdocs
    @version: 
    @author: 
    '''
    
    ''' ATTRIBUTES
    
    
    
    numeroPedidoActuacion  (private)
    
    
    
    fechaDeRealizacion  (private)
    
    
    
    fechaDeRecepcion  (private)
    
    repuestosUtilizados
    
    '''


    def __init__(self, repuestosSolicitados):
        '''
        Constructor
        @return: 
        @author: 
        '''
        self._repuestosSolicitados = repuestosSolicitados
        import datetime
        self._fechaRealizacion = datetime.datetime.now()
        self._fechaRecepcion = None 
        
    def setFechaRecepcion(self, fechaRecepcion):
        '''
        @return: 
        @author: 
        '''
        self._fechaRecepcion = fechaRecepcion
    
    def getRepuestosSolicitados(self):
        return self._repuestosSolicitados
    
    def getFechaRealizacion(self):
        return self._fechaRealizacion
    