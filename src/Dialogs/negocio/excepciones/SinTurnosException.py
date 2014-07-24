'''
Created on 24/07/2014

@author: LeoM
'''
class SinTurnosException(Exception):
    '''
    classdocs
    '''


    def __init__(self, mensaje):
        '''    
        Constructor
        '''
        self.mensaje = mensaje
        
    def __str__(self):
        return self.mensaje
    
    def getMensaje(self):
        return self.mensaje