'''
Created on 28/11/2012

@author: alum
'''

class ExcepcionPoseeOrdenReparacionEnCurso(Exception):
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