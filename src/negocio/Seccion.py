# -*- coding: utf-8 -*-
'''
Created on 28/10/2012

@author: urrutia
'''

from persistent import Persistent

CANTIDAD_MIN_PARA_TRANFERIR = 3

class Seccion(Persistent):
    '''
    classdocs
    @version: 
    @author:
        
        ATTRIBUTES:
        
        - codigoSeccion  (private)
        - nombre  (private)
        - empleados
        - encargado        
 
    '''
    def __init__(self, codigoSeccion, nombre, empleados, encargado):
        '''
        Constructor
        @return: 
        @author: 
        '''
        self.codigoSeccion = codigoSeccion
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
    
    def getNombre(self):
        return self.nombre
    
    def cantidadEmpleados(self):
        '''
        Devuelve la cantidad de empleados que tiene la Sección.
        (Cantidad de empleados sin contar el encargado)
        '''
        return len(self.empleados)
    
    def cantidadEmpleadosTotales(self):
        '''
        Devuelve la cantidad de empleados que tiene la Sección.
        (Cantidad de empleados mas el encargado)
        '''
        return len(self.empleados) + 1
    
    def puedeTransferir(self):
        '''
        Una Seccion puede tranferir a un empleado si:
            - Ninguno de sus empleados tiene reparaciones pendientes.
            - Posee mas de dos empleados (un empleado y el encargado).
        Util para un listado de solo Secciones que pueden transferir empleados.
        '''
        empleadosConReparacionesPendientes = filter(lambda unEmpleado: unEmpleado.tieneReparacionesPendientes() , self.getEmpleados().values())
        return len(empleadosConReparacionesPendientes) == 0 and self.cantidadEmpleadosTotales() >= CANTIDAD_MIN_PARA_TRANFERIR 
    
    def getEmpleados(self):
        '''
            Retorna un diccionario con:
                - k = dni del empleado 
                - v = Objeto Empleado.
        '''
        return self.empleados
    
    def poseeAEmpleado(self, unEmpleado):
        return unEmpleado in self.getEmpleados().values()
        
    def getEncargado(self):
        return self.encargado
    
    def getCodigo(self):
        return 'codigo'
    
    def removerEmpleado(self, empleadoARemover):
        del self.getEmpleados()[empleadoARemover.getDocumento()]
        
    def asignarNuevoEncargado(self, nuevoEncargado):
        '''
            Asigna un nuevo encargado a la Seccion.
            @return: El encargado anterior.
        '''
        encargadoAnterior = self.getEncargado()
        self.setEncargado(nuevoEncargado)
        return encargadoAnterior