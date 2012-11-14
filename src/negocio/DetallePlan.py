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
            _fecha
    '''


    def __init__(self,unaReparacion,unaFecha):
        '''
        Constructor
        '''
        self._reparacion = unaReparacion
        self._fecha = unaFecha
        