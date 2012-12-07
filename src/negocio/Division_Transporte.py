# -*- coding: utf-8 -*-
'''
Created on 28/10/2012

@author: urrutia
'''

from persistent import Persistent

from Empleado import *
from Legajo import *
from Localidad import *
# Puedo obtenerlos a través de los Legajos. (1 a 1 con la Orden de Reparación)
# from PedidoDeActuacion import *
from TipoRepuesto import *
from Seccion import *
from TipoDeReparacion import *
from TipoDocumento import *

from MiZODB import ZopeDB, MiZODB
from copy import deepcopy
import excepciones

class Division_Transporte(Persistent):
    '''
    Clase que representa a la División de Transporte.
    :version:
    :author:
    '''
    
    ''' 
    ATTRIBUTES
        
    legajos
    
    localidades
    
    empleados
    
    tiposDocumentos
    
    repuestos
    
    tiposDeReparacion
    
    secciones
        
    '''
    
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
        self.instance.pedidosDeActuacion = {}
        self.instance.tiposDeDocumentos = {}
        self.instance.empleados = {}
    
    def getSecciones(self):
        '''
        @return: 
        @author: 
        '''
        zodb = ZopeDB(MiZODB())
        return zodb.getAlls('secciones')
    
    def agregarSecciones(self, nombreSeccion, empleados, encargado):
        '''
        @return: 
        @author: 
        '''
        pass
        # Acordarse de de que vienen los documentos del empleados y el documento del encargado
        # y sólo el nombre de la Sección.
        zodb = ZopeDB(MiZODB())
        empleadosSeccion = {}
        for empleado in empleados:
            empleadosSeccion[empleado] = deepcopy(zodb.get('empleados', empleado))
        encargadoSeccion = deepcopy(zodb.get('empleados', encargado))
        seccion = Seccion(nombreSeccion, empleadosSeccion, encargadoSeccion)
        seccion.save()
        zodb.remove('empleados', empleado)
        zodb.remove('empleados', encargado)
#        
    def getTipoDeDocumentos(self):
        '''
        @return: 
        @author: 
        '''
        zodb = ZopeDB(MiZODB())
        return zodb.getAlls('tiposDocumentos')
    
    def getOrdenesDeReparacion(self):
        '''
        @return: 
        @author: 
        '''
        pass
    
    def getOrdenDeReparacionDeVehiculo(self, dominio):
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
        zodb = ZopeDB(MiZODB())
        empleados = zodb.getAlls('empleados').values()
        secciones = zodb.getAlls('secciones').values()
        empleadosAsignados = {}
        for seccion in secciones:
            p = seccion.empleados.values()
            for empleado in p:
                empleadosAsignados[empleado.documento] = empleado
            empleadosAsignados[seccion.encargado.documento] = seccion.encargado
    
        for empleado in empleados:
            empleadosAsignados[empleado.documento] = empleado
        return empleadosAsignados
    
    def getEmpleadosSinAsignar(self):
        '''
        @return: 
        @author: 
        '''
        zodb = ZopeDB(MiZODB())
        empleados = zodb.getAlls('empleados')
        return empleados            
    
    def getEmpleado(self, clave):
        '''
        @return: 
        @author: 
        '''
        zodb = ZopeDB(MiZODB())
        return zodb.get('empleados', clave)
    
    '''
    @TODO: Tener en cuenta q la el módulo q manipula la BD lanzará una Excepción
    si el repuesto con las característcas q se intentan ingresar y existe.
    '''
    def agregarEmpleado(self, nombre, apellido, numeroDocumento, tipoDocumento):
        '''
        @return: 
        @author: 
        '''
        zodb = ZopeDB(MiZODB())
        empleado = Empleado(nombre, apellido, numeroDocumento, zodb.get('tiposDocumentos', tipoDocumento))
        zodb.save('empleados', empleado.documento, empleado)
    
    def darDeBajaEmpleado(self):
        '''
        @return: 
        @author: 
        '''
        pass
    
    '''
    TODO: Tener en cuenta q la el módulo q manipula la BD lanzará una Excepción
    si el repuesto con las característcas q se intentan ingresar y existe.
    '''
    def agregarRepuestos(self, nombre, descripcion):
        '''
        @return: 
        @author: 
        '''
        repuesto = TipoRepuesto(nombre, descripcion)
        repuesto.save()
    
    def getRepuestos(self):
        '''
        @return: 
        @author: 
        '''
        zodb = ZopeDB(MiZODB())
        return zodb.getAlls('tiposRepuestos')
        
    def getRepuesto(self, clave):
        '''
        @return: 
        @author: 
        '''
        zodb = ZopeDB(MiZODB())
        return zodb.get('tiposRepuestos', clave)
    
    def getVehiculos(self):
        '''
        @return: 
        @author: 
        '''
        zodb = ZopeDB(MiZODB())
        return zodb.getAlls('vehiculos')

    def getVehiculo(self, clave):
        '''
        @return: 
        @author: 
        '''
        zodb = ZopeDB(MiZODB())
        return zodb.get('vehiculos', clave)
    
    def modificarVehiculo(self, dominio, marca, registroInterno, numeroChasis):
        zodb = ZopeDB(MiZODB())
        vehiculo = deepcopy(zodb.get('vehiculos', dominio))
        zodb.remove('vehiculos', dominio)
        vehiculo.dominio = dominio
        vehiculo.marca = marca
        vehiculo.registroInterno = registroInterno
        vehiculo.numeroChasis = numeroChasis
        vehiculo.save()
    
    '''
    @TODO: Tener en cuenta q la el módulo q manipula la BD lanzará una Excepción
    si el repuesto con las característcas q se intentan ingresar y existe.
    '''
    def addVehiculo(self, dominio, marca, registroInterno, numeroChasis):
        '''
        @return: 
        @author: 
        '''
        vehiculo = Legajo(dominio, marca, registroInterno, numeroChasis)
        vehiculo.save() 
    
    def registrarEgresoDeVehiculo(self, dominio, kilometrajeEgreso, CombustibleEgreso, fechaEgreso):
        '''
        @return: 
        @author: 
        '''
        vehiculo = self.getVehiculo(dominio)
        # Obtener orden reparacion
        # si finalizada, Ok egreso sino pa' tras
    
    def registrarIngresoDeVehiculo(self, dominio, kilometrajeActual, combustibleActual, equipamiento, reparacion, comisaria, localidad):
        '''
        @return: 
        @author: 
        '''
        vehiculo = self.getVehiculo(dominio)
        '''
        TODO: tener en cuenta el método obtenerOrdenDeReparacionEnCurso de Legajo que nos indica
        si ese vehículo tiene o no orden Reparación, por lo tanto no debemos crearle otra hasta
        que esa haya sido finalizada.
        '''
        try:
            vehiculo.dameOrdenDeReparacionEnCurso()
#            import datetime
#            hoy = datetime.datetime.now()
#            from MiZODB import MiZODB, ZopeDB
#            zodb = ZopeDB(MiZODB())
#            zodb.remove('vehiculos', vehiculo.dominio)
#            vehiculo.crearOrdenDeReparacion(kilometrajeActual, combustibleActual, equipamiento, reparacion, comisaria, localidad, hoy)
#            vehiculo.save()
        except excepciones.Excepcion_No_Posee_Orden_Reparacion_En_Curso.Excepcion_No_Posee_Orden_Reparacion_En_Curso:
            import datetime
            hoy = datetime.datetime.now()
            from MiZODB import MiZODB, ZopeDB
            zodb = ZopeDB(MiZODB())
            zodb.remove('vehiculos', vehiculo.dominio)
            vehiculo.crearOrdenDeReparacion(kilometrajeActual, combustibleActual, equipamiento, reparacion, comisaria, localidad, hoy)
            vehiculo.save()

    def __str__(self):
        '''
        Sobrecarga del método que imprime una cadena que representa a la División Transporte.
        '''
        return '%s, Id: %s' % (self.__class__, id(self))
    
    def getTipoReparaciones(self):
        zodb = ZopeDB(MiZODB())
        return zodb.getAlls('tiposReparaciones')

    def getTipoReparacion(self, claveTipoReparacion):
        '''
        @return: 
        @author: 
        '''
        zodb = ZopeDB(MiZODB())
        return zodb.get('tiposReparaciones', claveTipoReparacion)
    
    def registrarReparaciones(self, vehiculoSeleccionado):
        # primero cambiamos el estado de la orden
        # vehiculoSeleccionado.getOrdenDeReparacionEnCurso().getEstadoOrdenReparacion().cambiarProximoEstado()
        vehiculoSeleccionado.getOrdenDeReparacionEnCurso().generarPedidoDeActuacion()
        from copy import deepcopy
        unVehiculo = deepcopy(vehiculoSeleccionado)
        
        zodb = ZopeDB(MiZODB())
        zodb.remove('vehiculos', vehiculoSeleccionado.getDominio())
        unVehiculo.save()

    def getPedidoActuacionSinFechaRecepcion(self):
        vehiculos = self.getVehiculos().values()
        pedidosDeActuacion = []
        for vehiculo in vehiculos:
            pedido = vehiculo.getPedidoActuacionSinFechaRecepcion()
            if pedido:
                pedidosDeActuacion.append(pedido)
        return pedidosDeActuacion
    
    def registrarRecepcionPedidoDeActuacion(self, numeroPedido, fechaRecepcion):
        print 'Registrando Recepcion Pedido de Actuacion'
        vehiculo = self.obtenerVehiculo(numeroPedido)
        try:
            vehiculo.registrarRecepcionPedidoActuacion(fechaRecepcion)
        except AttributeError, e:
            raise Exception
        
        from MiZODB import MiZODB, ZopeDB
        zodb = ZopeDB(MiZODB())
        zodb.remove('vehiculos', vehiculo.dominio)
        vehiculo.save()
            
    def obtenerVehiculo(self, numeroPedido):
        vehiculos = self.getVehiculos().values()
#        vehiculo = filter(lambda vehiculo: numeroPedido == vehiculo.dameOrdenDeReparacionEnCurso().getPedidoDeActuacionActual().getNumeroPedido(), vehiculos)
        for i in vehiculos:
            try:
                if i.dameOrdenDeReparacionEnCurso().getPedidoDeActuacionActual().getNumeroPedido() == numeroPedido:
                    vehiculo = i
            except AttributeError:
                pass
        return vehiculo
