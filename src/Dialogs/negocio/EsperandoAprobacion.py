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


    def __init__(self, pedidoDeActuacion):
        '''
        Constructor
        @return: 
        @author: 
        '''
        super(EsperandoAprobacion, self).__init__()
        self.pedidoDeActuacion = pedidoDeActuacion
        
    def getPedidoDeActuacion(self, ordenReparacion):
        #return ordenReparacion.getPedidoDeActuacion()
        return self.pedidoDeActuacion
        
    def registrarRecepcionPedidoActuacion(self, ordenReparacion, fechaRecepcion):
        pedidoActuacion = ordenReparacion.getPedidoDeActuacion()
        pedidoActuacion.setFechaRecepcion(fechaRecepcion)
