# -*- coding: utf-8 -*-
'''
Created on 28/10/2012

@author: urrutia
'''

from persistent import Persistent

from Empleado import *
from Legajo import *
from Localidad import *
#Puedo obtenerlos a través de los Legajos. (1 a 1 con la Orden de Reparación)
#from PedidoDeActuacion import *
from TipoRepuesto import *
from Seccion import *
from TipoDeReparacion import *
from TipoDocumento import *
from PyQt4 import QtCore

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
        self.instance.empleados = {}
    
    def getSecciones(self):
        '''
        @return: 
        @author: 
        '''
        from MiZODB import ZopeDB, MiZODB
        zodb = ZopeDB(MiZODB('zeo.conf'))
        return zodb.getAlls('secciones')
#        return self.secciones
    
    def agregarSecciones(self, nombreSeccion, empleados, encargado):
        '''
        @return: 
        @author: 
        '''
        seccion = Seccion(nombreSeccion, empleados, encargado)
#        seccion.setEncargado(encargado)
        # Para cada x en empleados hacer seccion.agregarEmpleado(x)
        seccion.save()
        
    def getTipoDeDocumentos(self):
        '''
        @return: 
        @author: 
        '''
        from MiZODB import ZopeDB, MiZODB
        zodb = ZopeDB(MiZODB('zeo.conf'))
        return zodb.getAlls('tiposDocumentos')
#        return self.tiposDeDocumentos
    
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
        from MiZODB import ZopeDB, MiZODB
        zodb = ZopeDB(MiZODB('zeo.conf'))
        return zodb.getAlls('empleados')
    
    def getEmpleadosSinAsignar(self):
        '''
        @return: 
        @author: 
        '''
        from MiZODB import ZopeDB, MiZODB
        zodb = ZopeDB(MiZODB('zeo.conf'))
        empleados = zodb.getAlls('empleados')
        secciones = zodb.getAlls('secciones')
        empleadosSinAsignar = {}
        esta = False
        for empleado  in empleados:
            esta = False
            for seccion in secciones:
                    if ((empleados[empleado].documento in secciones[seccion].empleados)or(empleados[empleado] == secciones[seccion].encargado)):
                        esta = True
                        break
            if not esta:
                empleadosSinAsignar[empleados[empleado].documento] = empleados[empleado]
        return empleadosSinAsignar
            
    
    def getEmpleado(self, clave):
        '''
        @return: 
        @author: 
        '''
        from MiZODB import ZopeDB, MiZODB
        zodb = ZopeDB(MiZODB('zeo.conf'))
        return zodb.get('empleados',clave)
    
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
        from MiZODB import ZopeDB, MiZODB
        zodb = ZopeDB(MiZODB('zeo.conf'))
        return zodb.getAlls('vehiculos')
#        return self.vehiculos

    def modificarVehiculo(self, dominio, marca, registroInterno, numeroChasis):
        from MiZODB import ZopeDB, MiZODB
        zodb = ZopeDB(MiZODB('zeo.conf'))
        zodb.remove('vehiculos', dominio)
        vehiculo = Legajo(dominio, marca, registroInterno, numeroChasis)
        vehiculo.save()
    
    def addVehiculo(self, dominio, marca, registroInterno, numeroChasis):
        '''
        @return: 
        @author: 
        '''
        vehiculo = Legajo(dominio, marca, registroInterno, numeroChasis)
        vehiculo.save()
#        self.vehiculos[dominio] = vehiculo 
    
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
    
    def agregarEmpleado(self, nombre, apellido, numeroDocumento):
        '''
        @return: 
        @author: 
        '''
        empleado = Empleado(nombre,apellido, numeroDocumento)
        empleado.save()
#        self.empleados[numeroDocumento] = empleado

    def __str__(self):
        '''
        Sobrecarga del método que imprime una cadena que representa a la División Transporte.
        '''
        return '%s, Id: %s'%(self.__class__, id(self))