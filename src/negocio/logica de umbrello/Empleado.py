'''
Created on 27/10/2012

@author: urrutia
'''
import persistent

from Seccion import *
from TipoDocumento import *
from Localidad import *

class Empleado(object):

    """
       
    
    :version:
    :author:
    """

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

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido