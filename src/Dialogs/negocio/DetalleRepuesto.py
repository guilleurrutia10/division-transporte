# -*- coding: utf-8 -*-
'''
Created on 07/11/2012

@author: urrutia
'''

from persistent import Persistent

class DetalleRepuesto(Persistent):
    '''
    classdocs
    @version: 
    @author: 
    
    Atributos:
    
    tipoDeRepuesto
    cantidad
    '''


    def __init__(self, tipoDeRepuesto=None, cantidad=None):
        ''''
        Constructor
        @return: 
        @author: 
        '''
        self._tipoDeRepuesto = tipoDeRepuesto
        self._cantidad = cantidad
        
    def getTipoDeRepuesto(self):
        return self._tipoDeRepuesto
    
    def setTipoDeRepuesto(self, tipoDeRepuesto):
        self._tipoDeRepuesto = tipoDeRepuesto        
        
    def setCantidad(self, cantidad):
        self._cantidad = cantidad
        
    def getCantidad(self):
        return self._cantidad