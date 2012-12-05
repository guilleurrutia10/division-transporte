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


    def __init__(self):
        '''
        Constructor
        @return: 
        @author: 
        '''
        super(EsperandoAprobacion, self).__init__()
        
    def getPedidoActuacion(self, ordenReparacion):
        return ordenReparacion.getPedidoDeActuacion()
