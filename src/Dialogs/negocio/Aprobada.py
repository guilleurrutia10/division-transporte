# -*- coding: utf-8 -*-
'''
Created on 28/11/2012

@author: alum
'''

from EstadoOrdenReparacion import EstadoOrdenReparacion
import transaction

class Aprobada(EstadoOrdenReparacion):
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
        super(Aprobada, self).__init__(orden_de_reparacion)
        
    def __str__(self):
        return 'Aprobada'
    
    def agregarTurnoAlPlan(self, turno):
        self._orden_de_reparacion.getPlan().addTurno(turno)
#        transaction.commit()