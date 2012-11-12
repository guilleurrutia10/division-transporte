# -*- coding: utf-8 -*-
'''
Created on 28/10/2012

@author: urrutia
'''
from persistent import Persistent

from Empleado import *
from Legajo import *
from Localidad import *
from PedidoDeActuacion import *
from Repuesto import *
from Seccion import *
from TipoDeReparacion import *
from TipoDocumento import *

class Division_Transporte(Persistent):
    """
    Clase que representa a la División de Transporte.
    :version:
    :author:
    """
    
    """ ATTRIBUTES
        
        legajos
        
        localidades
        
        empleados
        
        tiposDocumentos
        
        repuestos
        
        tiposDeReparacion
        
        secciones
        
    """
    
    instance = None
    
    def __new__(cls, *args, **kargs):
        '''
        @return: Division_Transporte
        @author: 
        '''
        if cls.instance is None:
            cls.instance = Persistent.__new__(cls, *args, **kargs)
            cls.instance.inicialize()
        return cls.instance
    
    def inicialize(self):
        '''
        @return: 
        @author: 
        '''
        self.instance.id = 1
        self.instance.secciones = {}
        self.instance.ordenesDeReparacion = {}
        self.instance.tiposDeDocumentos = {}
        self.instance.vehiculos = {}
        self.instance.tiposDeDocumentos = {}
    
    @classmethod
    def getInstancia(cls, *args, **kargs):
        '''
        @return: 
        @author: 
        '''
        if cls.instance is None:
            cls.instance = Persistent.__new__(cls, *args, **kargs)
            cls.instance.inicialize()
        return cls.instance
    
    def getSecciones(self):
        '''
        @return: 
        @author: 
        '''
        return self.secciones
        
    def getTipoDeDocumentos(self):
        '''
        @return: 
        @author: 
        '''
        return self.tiposDeDocumentos
    
    def getOrdenesDeReparacion(self):
        '''
        @return: 
        @author: 
        '''
        pass
    
    def getOrdenDeReparacionDeVehiculo(self):
        '''
        @return: 
        @author: 
        '''
        pass
    
    def getEmpleados(self):
        '''
        @return: 
        @author: 
        '''
        pass
    
    def getEmpleadosSinAsignar(self):
        '''
        @return: 
        @author: 
        '''
        pass
    
    def registrarEmpleado(self):
        '''
        @return: 
        @author: 
        '''
        pass
    
    def darDeBajaEmpleado(self):
        '''
        @return: 
        @author: 
        '''
        pass
    
    def addRepuestos(self):
        '''
        @return: 
        @author: 
        '''
        pass
    
    def getRepuestos(self):
        '''
        @return: 
        @author: 
        '''
        pass
    
    def getVehiculos(self):
        '''
        @return: 
        @author: 
        '''
        return self.vehiculos
    
    def addVehiculo(self, dominio, marca, registroInterno, numeroChasis):
        '''
        @return: 
        @author: 
        '''
        self.vehiculos[dominio] = Legajo(dominio, marca, registroInterno, numeroChasis)
    
    def registrarEgresoDeVehiculo(self):
        '''
        @return: 
        @author: 
        '''
        pass
    
    def registrarIngresoDeVehiculo(self):
        '''
        @return: 
        @author: 
        '''
        pass