'''
Created on 28/10/2012

@author: urrutia
'''

from Reparacion import *
from TipoDocumento import *

class Empleado(object):
    '''
    classdocs
    '''

    """ ATTRIBUTES

   

        numeroDocumento  (private)

   

        nombre  (private)

   

        apellido  (private)

   

        fechaNacimiento  (private)

   

        fechaAlta  (private)

   

        fechaBaja  (private)

   

        email  (private)

   

        telefono_  (private)

   

        domicilio  (private)

    """
    
    def __init__(self, nombre, apellido, documento):
        '''
        Constructor
        '''
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento