'''
Created on 06/12/2012

@author: Usuario
'''

class Excepcion_Orden_Posee_Reparacion(Exception):
    '''
    Excepcion que se dispara cuando se desea agregar una reparacion a 
    la orden de reparacion y esta ya existia.
    '''


    def __init__(self, mensaje='Error: OR posee Reparacion'):
        '''    
        Constructor
        '''
        self.mensaje = mensaje
        
    def __str__(self):
        return self.mensaje
    
    def getMensaje(self):
        return self.mensaje
