'''
Created on 04/10/2014

@author: LeoMorales
'''

class Except_NoHayReparacionesDisponibles(Exception):
    '''
    Excepcion que se da cuando se trata de agregar reparaciones a la DIvision, pero esta
    no tiene ninguna cargada.
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass