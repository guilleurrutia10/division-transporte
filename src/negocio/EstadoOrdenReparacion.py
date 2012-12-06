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

    # def __init__(self, estado)
    def __init__(self):
        '''
        Constructor
        @return: 
        @author:
        '''
        
    
    '''
    TODO: implementado sólo estado EnRevision()
    '''    
    def addReparacion(self):
        NotImplemented
        
    def cambiarProximoEstado(self):
        NotImplemented
    
    def getPedidoActuacion(self):
        NotImplemented
