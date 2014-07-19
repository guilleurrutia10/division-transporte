# -*- coding: utf-8 -*-
'''
Created on 28/10/2012

@author: urrutia
'''

#from negocio.DetalleRepuesto import DetalleRepuesto
from DetalleRepuesto import DetalleRepuesto

class RepuestoRequeridos(DetalleRepuesto):
    '''
    classdocs
    @version: 
    @author: 
    '''

    ''' ATTRIBUTES
    
    
    
    cantidad  (private)
    
    '''

    def __init__(self, tipoDeRepuesto=None, cantidad=4):
        '''
        Constructor
        @return: 
        @author: 
        '''
        super(RepuestoRequeridos, self).__init__(tipoDeRepuesto, cantidad)
        
    def __cmp__(self, other):
        return self.getTipoDeRepuesto().__cmp__(other.getTipoDeRepuesto())