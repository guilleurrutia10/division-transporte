# -*- coding: utf-8 -*-
'''
Created on 28/10/2012

@author: urrutia
'''

from DetalleRepuesto import DetalleRepuesto


class RepuestoUtilizados(DetalleRepuesto):
    '''
    classdocs
    @version:
    @author:
    '''

    ''' ATTRIBUTES

    cantidad  (private) --> heredado

    '''

    def __init__(self, tipoRepuesto, cantidad):
        '''
        Constructor
        @return: 
        @author: 
        '''
        super(RepuestoUtilizados, self).__init__(tipoRepuesto, cantidad)

    def __cmp__(self, otro):
        if self._tipoDeRepuesto == otro.getTipoDeRepuesto():
            return 0
        else:
            return -1

    def incrementarCantidad(self, unaCantidad):
        #TODO: Debugear para ver si son necesarios los cast
        nuevaCantidad = int(self.getCantidad()) + int(unaCantidad)
        self.setCantidad(nuevaCantidad)

    def __str__(self):
        return self.getTipoDeRepuesto()
