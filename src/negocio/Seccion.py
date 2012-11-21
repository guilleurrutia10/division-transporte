# -*- coding: utf-8 -*-
'''
Created on 28/10/2012

@author: urrutia
'''

from persistent import Persistent

from Empleado import *
from TipoDeReparacion import *

class Seccion(Persistent):
    '''
    classdocs
    @version: 
    @author: 
    '''
    
    """ ATTRIBUTES
    
    
    
    codigoSeccion  (private)
    
    
    
    nombre  (private)
    
    """


    def __init__(self, nombre, empleados, encargado):
        '''
        Constructor
        @return: 
        @author: 
        '''
        self.nombre = nombre
        self.empleados = empleados
        self.encargado = encargado
    
    
    def setEncargado(self, encargado):
        '''
        @return: 
        @author: 
        '''
        pass
    
    def setNombre(self):
        '''
        @return: 
        @author: 
        '''
        pass
    
    def agregarEmpleado(self, empleado):
        '''
        @return: 
        @author: 
        '''
        self.empleados[empleado.documento] = empleado
    
    def quitarEmpleado(self):
        '''
        @return: 
        @author: 
        '''
        pass
    
    def save(self):
        '''
        @return: 
        @author: 
        '''
        from MiZODB import ZopeDB, MiZODB
        zodb = ZopeDB(MiZODB('zeo.conf'))
        zodb.save('secciones', self.nombre, self)
    
    def cantidadEmpleados(self):
        '''
        Devuelve la cantidad de empleados que tiene la Sección.
        '''
        return len(self.empleados) + 1