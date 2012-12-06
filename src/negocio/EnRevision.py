# -*- coding: utf-8 -*-
'''
Created on 07/11/2012

@author: urrutia
'''

from EstadoOrdenReparacion import *

class EnRevision(EstadoOrdenReparacion):
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
        super(EnRevision, self).__init__()
    
    def addReparacion(self, orden, unaReparacion):
        '''
        Agrega reparaciones a la Orden de Reparación.
        @return: 
        @author: 
        '''
        #reparaciones = self.getEstadoOrden().reparaciones
        orden.getReparaciones().append(unaReparacion)
        print 'Se agrego una nueva Reparación'
        #reparacion[numero] = reparacion
        
    def cambiarProximoEstado(self):
        '''
        Del estado EnRevision pasamos al estado EsperandoAprobacion
        '''
        from negocio.EsperandoAprobacion import EsperandoAprobacion
        
        self.getEstadoOrden().setEstadoOrdenReparacion(EsperandoAprobacion(self.getEstadoOrden()))
        
    def generarPedidoDeActuacion(self, unaOrdenReparacion):
        '''
        Genera un pedido de actuacion con todos los repuestos de todas las reparaciones de la 
        orden de reparacion recibida.
        '''
        #recolectamos todos los repuestos solicitados...
        repuestosSolicitados = []
        for reparacion in unaOrdenReparacion.getReparaciones():
            for repuesto in reparacion.getRepuestosUtilizados():
                if repuesto in repuestosSolicitados:
                    # si ya existia:
                    # guardamos la cantidad solicitada:
                    cantRepuesto = repuesto.getCantidad()
                    # y se la agregamos al repuesto...
                    repuestosSolicitados[repuestosSolicitados.index(repuesto)].agregarCantidad(cantRepuesto)
                else:
                    #si no existia lo agregamos...
                    repuestosSolicitados.append(repuesto)
        #creamos el Pedido de Actuacion y se lo agregamos a la orden:
        from negocio.PedidoDeActuacion import PedidoDeActuacion
        pedidoActuacion = PedidoDeActuacion(repuestosSolicitados)
        pedidoActuacion.setNumeroPedido(1)
        unaOrdenReparacion.setPedidoDeActuacion(pedidoActuacion)
#        unaOrdenReparacion.setPedidoDeActuacion(PedidoDeActuacion(repuestosSolicitados))
        
        print 'pedido generado'
