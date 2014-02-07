'''
Created on 20/11/2012

@author: Usuario
'''

class Excepcion_usrInvalido(Exception):
    '''
    Excepcion que le eleva al queres validar un usuario invalido.
    '''

    def __init__(self, usrInvalido):
        '''
        Constructor
        '''
        self.usrInvalido = usrInvalido
    
    def __str__(self, *args, **kwargs):
        return '%s nombre o clave incorrecta' % self.usrInvalido