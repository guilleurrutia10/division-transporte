'''
Created on 13/11/2012

@author: Usuario
'''
from persistent import Persistent
import Reparacion

class DetallePlan(Persistent):
    '''
    DetallePlan
    
    atributos 
            _reparacion
            _fechaInicio
    '''


    def __init__(self, unaReparacion, fechaInicio, fechaFin=None):
        '''
        Constructor
        '''
        self._reparacion = unaReparacion
        self._fechaInicio = fechaInicio
        self._fechaFin = fechaFin
        
    def getReparacion(self):
        return self._reparacion
    
    def setReparacion(self, reparacion):
        self._reparacion = reparacion
    
    def getFechaInicio(self):
        return self._fechaInicio
    
    def setFechaInicio(self, fechaInicio):
        self._fechaInicio = fechaInicio
        
    def getFechaFin(self):
        return self._fechaFin
    
    def setFechaFin(self, fechaInicio):
        self._fechaInicio = fechaInicio    