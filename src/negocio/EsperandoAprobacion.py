# -*- coding: utf-8 -*-
'''
Created on 07/11/2012

@author: urrutia
'''

from EstadoOrdenReparacion import *

class EsperandoAprobacion(EstadoOrdenReparacion):
    '''
    classdocs
    @version: 
    @author: 
    '''


    def __init__(self, ordenReparacion):
        '''
        Constructor
        @return: 
        @author: 
        '''
        super(EsperandoAprobacion, self).__init__(ordenReparacion)
        self.pedidoDeActuacion = None 
    
    def generarPedidoDeActuacion(self):
        '''
        @return: 
        @author: 
        '''
        if self.pedidoDeActuacion is None:
            self.pedidoDeActuacion = PedidoDeActuacion()