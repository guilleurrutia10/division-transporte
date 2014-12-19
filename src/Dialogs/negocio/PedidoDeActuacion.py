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
    - numeroPedidoActuacion  (private)
    - fechaDeRealizacion  (private)
    - fechaDeRecepcion  (private)
    - repuestosUtilizados
    '''

    def __init__(self, codigo, repuestosSolicitados):
        '''
        Constructor
        @return:
        @author:
        '''
        self._nroDePedido = codigo
        self._repuestosSolicitados = repuestosSolicitados

        self._fechaRealizacion = datetime.date.today()
        self._fechaHoraRealizacion = datetime.datetime.today()
        self._fechaRecepcion = None
#        self._numeroPedido = None

    def setFechaRecepcion(self, fechaRecepcion):
        '''
        @return:
        @author:
        '''
        if (self.getFechaRealizacion() < fechaRecepcion):
            self._fechaRecepcion = fechaRecepcion
        # else
        # error

    def getRepuestosSolicitados(self):
        return self._repuestosSolicitados

    def getFechaRealizacion(self):
        return self._fechaRealizacion

    def setNumeroPedido(self, numero):
        self._numeroPedido = numero

    def getNumeroPedido(self):
#        return self._numeroPedido
        return self._nroDePedido

    def __str__(self):
        return 'Pedido de Actuacion | Nro: %s | Fecha: %s' %(self._nroDePedido,
                                                             self._fechaRealizacion
                                                             )

    def __cmp__(self, other):
        if self._fechaRealizacion == other._fechaRealizacion:
            return 0
        elif self._fechaRealizacion > other._fechaRealizacion:
            return 1
        else:
            return -1

    def getFechaRecepcion(self):
        return self._fechaRecepcion

    def getFechaHoraDeRealizacion(self):
        return self._fechaHoraRealizacion