# -*- coding: utf-8 -*-
'''
Created on 07/11/2012

@author: urrutia
'''

from persistent import Persistent

from OrdenReparacion import *
from PedidoDeActuacion import *

class EstadoOrdenReparacion(Persistent):
    '''
    classdocs
    @version: 
    @author: 
    '''

    #def __init__(self, ordenReparacion)
    def __init__(self, ordenReparacion):
        '''
        Constructor
        @return: 
        @author:
        '''
        self.estadoOrden = ordenReparacion
        self.pedidoDeActuacion = None
    
    def getPedidoActuacion(self):
        '''
        Devuelve el pedido de Actuación correspondiente a la Orden de Reparación.
        @return: PedidoDeActuacion
        @author:
        ''' 
        return self.pedidoDeActuacion
    
    '''
    TODO: implementado sólo estado EnRevision()
    '''    
    def addReparacion(self):
        NotImplemented
        
    def getEstadoOrden(self):
        '''
        @return:  
        @author:
        ''' 
        return self.estadoOrden