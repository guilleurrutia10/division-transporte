'''
Created on 13/11/2012

@author: Usuario
'''
from persistent import Persistent
from persistent.list import PersistentList
import DetallePlan

class Plan(Persistent):
    '''
    Plan:
    
        atributes 
                _detalles: Lista de Turnos
    El plan tiene una lista de Turnos.
    En cada turno se llevan a cabo cierto tipo de reparaciones
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self._detalles = PersistentList()
        self._turnos = PersistentList()

    def getDetalles(self):
        return self._detalles
            
    def addDetalle(self,unNuevoDetalle):
        self.getDetalles().append(unNuevoDetalle)
    
    def addTurno(self, nuevoTurno):    
        self._turnos.append(nuevoTurno)
    
    def getTurnos(self):
        return self._turnos
    
    def __str__(self):
        return 'Plan: \n%s' %''.join('%s\n' %str(turno) for turno in self._turnos)