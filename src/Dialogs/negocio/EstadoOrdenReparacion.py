# -*- coding: utf-8 -*-
'''
Created on 07/11/2012

@author: urrutia
'''

from persistent import Persistent

class EstadoOrdenReparacion(Persistent):
    '''
    classdocs
    @version: 
    @author: 
    '''

    def __init__(self):
        '''
        Constructor
        @return: 
        @author:
        '''
        self.pedidoDeActuacion = None
    
    '''
    TODO: implementado sólo estado EnRevision()
    '''    
    def addReparacion(self):
        NotImplemented
        
    def cambiarProximoEstado(self):
        NotImplemented
        
    def getPedidoDeActuacionActual(self):
        NotImplemented
        
    def noEstoyFinalizada(self):
        return True