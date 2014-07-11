# -*- coding: utf-8 -*-
'''
Created on 28/10/2012

@author: urrutia
'''
import datetime
from persistent import Persistent

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
        self._nroDePedido = 1
        self._repuestosSolicitados = repuestosSolicitados

        self._fechaRealizacion = datetime.datetime.now()
        self._fechaRecepcion = None
        self._numeroPedido = None
        
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
    
    def setNumeroPedido(self, numero):
        self._numeroPedido = numero
        
    def getNumeroPedido(self):
        return self._numeroPedido
    