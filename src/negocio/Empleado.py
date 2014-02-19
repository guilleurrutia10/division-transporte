# -*- coding: utf-8 -*-
'''
Created on 28/10/2012

@author: urrutia
'''

from persistent import Persistent

from Localidad import *
from Reparacion import *
from TipoDocumento import *

class Empleado(Persistent):
    '''
    classdocs
    :version:
    :author:
    ATTRIBUTES

        numeroDocumento  (private)

        nombre  (private)

        apellido  (private)

        fechaNacimiento  (private)

        fechaAlta  (private)

        fechaBaja  (private)

        email  (private)

        telefono_  (private)

        domicilio  (private)

    
    '''
    
    def __init__(self, nombre, apellido, documento, tipoDocumento):
        '''
        Constructor
        :version:
        :author:
        '''
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.tipoDocumento = tipoDocumento
        self.password = ''
        
    def save(self):
        from MiZODB import ZopeDB, MiZODB
        zodb = ZopeDB(MiZODB())
#        zodb = ZopeDB(MiZODB('zeo.conf'))
        zodb.save('empleados', self.documento, self)
        
    def __eq__(self, otro):
        return self.documento == otro.documento
    
    def nombreCompleto(self):
        return '%s %s' %(self.nombre, self.apellido)
    
    def nombreCompletoUsr(self):
        return '%s%s' %(self.apellido, self.nombre)
    
    def setPassword(self, unaPass):
        self.password = unaPass
    
    def getPassword(self):
        return self.password
    
    def getDocumento(self):
        return self.documento
    
    