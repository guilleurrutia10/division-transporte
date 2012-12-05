'''
Created on 5/12/2012

@author: LeoM
'''

class Excepcion_Orden_No_Esta_En_Revision(Exception):
    '''
    Excepcion que se dispara cuando la orden de reparacion posee un estado que no es instancia de EnRevision
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