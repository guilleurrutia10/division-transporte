# -*- coding: utf-8 -*-
'''
Created on 28/11/2012

@author: alum
'''
from EstadoOrdenReparacion import EstadoOrdenReparacion

class Finalizada(EstadoOrdenReparacion):
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
        super(Finalizada, self).__init__(ordenReparacion)
        
    def __str__(self):
        return 'Finalizada'
    
    def noEstoyFinalizada(self):
        return False
    
    def puedeEgresar(self):
        return self._orden_de_reparacion.getFechaEgreso() == None
    
    def registrarEgreso(self, kilometraje, combustible, fecha):
        self._orden_de_reparacion.setKilometrajeEgreso(kilometraje)
        self._orden_de_reparacion.setCombustibleEgreso(combustible)
        self._orden_de_reparacion.setFechaEgreso(fecha)