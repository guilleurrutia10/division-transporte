'''
Created on 13/11/2012

@author: Usuario
'''
from persistent import Persistent
import DetallePlan

class Plan(Persistent):
    '''
    Plan:
    
        atributes 
                _detalles
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self._detalles = []

    def getDetalles(self):
        return self._detalles
            
    def addDetalle(self,unNuevoDetalle):
        self.getDetalles().append(unNuevoDetalle)
        