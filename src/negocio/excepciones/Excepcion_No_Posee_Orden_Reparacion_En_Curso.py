'''
Created on 5/12/2012

@author: LeoM
'''

class Excepcion_No_Posee_Orden_Reparacion_En_Curso(Exception):
    '''
    Excepcion que se dispara cuando un vehiculo no posee una orden de reparacion 
    sin finalizar.
    '''


    def __init__(self, mensaje=None):
        '''    
        Constructor
        '''
        self.mensaje = mensaje
        
    def __str__(self):
        return self.mensaje
    
    def getMensaje(self):
        return self.mensaje