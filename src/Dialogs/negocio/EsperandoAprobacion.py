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


    def __init__(self, orden_de_reparacion):
        '''
        Constructor
        @return: 
        @author: 
        '''
        super(EsperandoAprobacion, self).__init__(orden_de_reparacion)
        self.pedidoDeActuacion = orden_de_reparacion.getPedidoDeActuacion()
        
    def getPedidoDeActuacion(self, ordenReparacion):
        #return ordenReparacion.getPedidoDeActuacion()
        return self.pedidoDeActuacion
        
    def registrarRecepcionPedidoActuacion(self, fechaRecepcion):
        #pedidoActuacion = ordenReparacion.getPedidoDeActuacion()
        self.pedidoDeActuacion.setFechaRecepcion(fechaRecepcion)

    def __str__(self):
        return 'Esperando Aprobacion del Pedido de Actuacion'