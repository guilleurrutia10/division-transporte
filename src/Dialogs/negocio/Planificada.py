# -*- coding: utf-8 -*-
'''
Created on 07/11/2012

@author: urrutia
'''
from EstadoOrdenReparacion import EstadoOrdenReparacion
from Finalizada import Finalizada

class Planificada(EstadoOrdenReparacion):
    '''
    classdocs
    @version: 
    @author:
    
    atributes 
                plan.
    '''


    def __init__(self, orden_de_reparacion):
        '''
        Constructor
        @return: 
        @author: 
        '''
        super(Planificada, self).__init__(orden_de_reparacion)
        
    def __str__(self):
        return 'Planificada'
    
    def turnosSinAtender(self):
        #return self._plan.getTurnos()
        return self._orden_de_reparacion.getPlan().getTurnos()
    
    def tieneTodosLosTurnosFinalizados(self):
        return filter(lambda t: not t.estaFinalizado(), self._orden_de_reparacion.getPlan().getTurnos()) == []
    
    def finalizarVerificacionReparacion(self):
        self._orden_de_reparacion.setEstado(Finalizada(self._orden_de_reparacion))

    def getTurnosOrdenados(self):
        turnos_ordenados = sorted(self._orden_de_reparacion.getPlan().getTurnos(), key= lambda turno: turno.getFecha())
        return dict(zip(range(50),turnos_ordenados))
