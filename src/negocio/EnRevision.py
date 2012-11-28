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


    def __init__(self, ordenReparacion):
        '''
        Constructor
        @return: 
        @author: 
        '''
        super(EnRevision, self).__init__(ordenReparacion)
    
    def addReparacion(self):
        '''
        Agrega reparaciones a la Orden de Reparación.
        @return: 
        @author: 
        '''
        reparaciones = self.getEstadoOrden().reparaciones
        print 'Se agrego una nueva Reparación'
        print reparaciones
        #reparacion[numero] = reparacion