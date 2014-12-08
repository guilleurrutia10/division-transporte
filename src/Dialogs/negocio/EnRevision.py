# -*- coding: utf-8 -*-
'''
Created on 07/11/2012

@author: urrutia
'''

from EstadoOrdenReparacion import EstadoOrdenReparacion
from excepciones.Excepcion_Orden_Posee_Reparacion import Excepcion_Orden_Posee_Reparacion
from PedidoDeActuacion import PedidoDeActuacion

class EnRevision(EstadoOrdenReparacion):
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
        super(EnRevision, self).__init__(orden_de_reparacion)
    
    def addReparacion(self,unaReparacion):
        '''
        Agrega reparaciones a la Orden de Reparación.
        @return: 
        @author: 
        '''
        #reparaciones = self.getEstadoOrden().reparaciones
        #TODO: Agregar la reparacion a la OR si no estaba en la reparacion...
        if not unaReparacion in self._orden_de_reparacion.getReparaciones():
            self._orden_de_reparacion.getReparaciones().append(unaReparacion)
            print 'Se agrego una nueva Reparación'
        else:
            raise Excepcion_Orden_Posee_Reparacion('La Reparacion ya se encuentra en la Orden de Reparacion del Vehiculo')
        #reparacion[numero] = reparacion
        
#    def cambiarProximoEstado(self):
#        '''
#        Del estado EnRevision pasamos al estado EsperandoAprobacion
#        '''
#        from negocio.EsperandoAprobacion import EsperandoAprobacion
#        
#        self.getEstadoOrden().setEstadoOrdenReparacion(EsperandoAprobacion(self.getEstadoOrden()))
        
    def generarPedidoDeActuacion_deprecated(self, unaOrdenReparacion):
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
                    repuestosSolicitados[repuestosSolicitados.index(repuesto)].incrementarCantidad(cantRepuesto)
                else:
                    #si no existia lo agregamos...
                    repuestosSolicitados.append(repuesto)
        #creamos el Pedido de Actuacion y se lo agregamos a la orden:

        self.pedidoActuacion = PedidoDeActuacion(repuestosSolicitados)
        #unaOrdenReparacion.setPedidoDeActuacion(pedidoActuacion)
#        unaOrdenReparacion.setPedidoDeActuacion(PedidoDeActuacion(repuestosSolicitados))

    def generarPedidoDeActuacion(self, pedido_de_actuation_code):
        '''
        Genera un pedido de actuacion con todos los repuestos de todas las reparaciones de la 
        orden de reparacion.
        '''
        #recolectamos todos los repuestos solicitados...
        repuestosSolicitados = []
        for reparacion in self._orden_de_reparacion.getReparaciones():
            for repuesto in reparacion.getRepuestosUtilizados():
                if repuesto in repuestosSolicitados:
                    # si ya existia:
                    # guardamos la cantidad solicitada:
                    cantRepuesto = repuesto.getCantidad()
                    # y se la agregamos al repuesto...
                    repuestosSolicitados[repuestosSolicitados.index(repuesto)].incrementarCantidad(cantRepuesto)
                else:
                    #si no existia lo agregamos...
                    repuestosSolicitados.append(repuesto)
        #creamos el Pedido de Actuacion y se lo agregamos a la orden:

        self._orden_de_reparacion.setPedidoDeActuacion(PedidoDeActuacion(pedido_de_actuation_code, repuestosSolicitados))
        print "DEBUG: PEDIDO DE ACTUACION GENERADO Y ASIGNADO A LA ORDEN"

    def __str__(self):
        return 'En Revision'
        
        