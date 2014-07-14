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

    def __init__(self, orden_de_reparacion):
        '''
        Constructor
        @return: 
        @author:
        
        El estado ahora recibe la referencia a la OR para poder realizar modificaciones sobre ella
        '''
        #self.pedidoDeActuacion = None
        
        #Referencia a la orden duena de este estado
        self._orden_de_reparacion = orden_de_reparacion
    
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