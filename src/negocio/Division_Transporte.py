# -*- coding: utf-8 -*-
'''
Created on 28/10/2012

@author: urrutia
'''

from persistent import Persistent

from Empleado import *
from Legajo import *
from Localidad import *
# Puedo obtenerlos a trav�s de los Legajos. (1 a 1 con la Orden de Reparaci�n)
# from PedidoDeActuacion import *
from TipoRepuesto import *
from Seccion import *
from TipoDeReparacion import *
from TipoDocumento import *

from ZODB import config
from ZEO.Exceptions import ClientDisconnected
import transaction
from copy import deepcopy
from excepciones.ExcepcionObjetoExiste import ExcepcionObjetoExiste
from excepciones.ExcepcionObjetoNoExiste import ExcepcionObjeNoExiste

class MiZODB(object):
    '''
    Clase que representa la ZODB.
    classdocs
    @version: 
    @author: 
    '''

#    def __init__(self, url):
    def __init__(self):
        '''
        Constructor, se conecta al Servidor de la BD a través del archivo de configuracion zeo.conf
        en donde se indica la IP:PORT.
        @return: 
        @author: 
        '''
#        self.url = url
        self.url = 'zeo.conf'
        try:
            self.db = config.databaseFromURL(self.url)
            self.conexion = self.db.open()
            self.raiz = self.conexion.root()
        except ClientDisconnected:
            print 'El cliente se ha desconectado debido a que el Servidor no corre...'
        
    def open(self):
        '''
        Abre la conexion con la base de datos.
        @return: 
        @author: 
        '''
        self.db = config.databaseFromURL(self.url)
        self.conexion = self.db.open()
        self.raiz = self.conexion.root()
        
    def close(self):
        '''
        Cierra la conexion con la base de datos.
        @return: 
        @author: 
        '''
        self.conexion.close()
        self.db.close()
        self.raiz = None 
        
    def commiting(self):
        '''
        Realiza una confirmación en la base de datos.
        @return: 
        @author: 
        '''
        self.raiz._p_changed = True # The object has been changed.
        transaction.commit()
    
    def getDiccionarioElementos(self, clave):
        '''
            Retorna el valor del diccionario de elementos en la clave, 
            si el diccionario no tiene elemento, crea y devuelve un diccionario vacio (con la clave 'clave').
        '''
        try:
            return self.raiz[clave]
        except KeyError:
            self.raiz[clave] = {}
            return self.raiz[clave]
        
    def save(self, claveElementos, clave, objeto):
        '''
        Agrega un nuevo objeto en la del claveDiccionario.
        El objeto no debe existir en el diccionario.
        Confirma la transaccion.
        @raise exception: ObjetoExiste
        '''
        try:
            diccionario = self.getDiccionarioElementos(claveElementos)
            unObjeto = diccionario[clave]
            raise ExcepcionObjetoExiste
        except KeyError, e:
            diccionario[clave] = objeto
            self.commiting()
        
    def remove(self, claveDiccionario, clave):
        '''
        @raise exception: ObjetoNoExiste
        '''
        try:
            diccionario = self.getDiccionarioElementos(claveDiccionario)
            del diccionario[clave]
            self.commiting()
        except KeyError, e:
            raise ExcepcionObjeNoExiste
                
        
class Division_Transporte(Persistent):
    '''
    Clase que representa a la Divisi�n de Transporte.
    :version:
    :author:
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
        Atributos: 
            legajos
            localidades
            empleados
            tiposDeDocumentos
            tiposDeRepuestos
            tiposDeReparacion
            secciones
        '''
        self.instance.id = 1
#        self.instance.secciones = {}
#        self.instance.ordenesDeReparacion = {}
#        self.instance.tiposDeDocumentos = {}
#        self.instance.pedidosDeActuacion = {}
#        self.instance.tiposDeDocumentos = {}
#        self.instance.empleados = {}
        #TODO: try: ... ClientDisconnected -> Error en BD
        self.zodb = MiZODB()
        from pprint import pprint
        pprint(self.zodb.raiz)
        for d,s in self.zodb.raiz.items():
            pprint(d)
            pprint(s)
        print self.zodb.raiz
        self.legajos = []
        self.localidades = []
        self.empleados = []
        self.tiposDeDocumentos = []
        self.tiposDeRepuestos = []
        self.tiposDeReparacion =[]
        self.secciones = []

#    def verificar_bd(self):

    def __init__(self):
        '''
        ATTRIBUTES
        '''
        pass
        
    def getSecciones(self):
        '''
        @return: 
        @author: 
        '''
        self.zodb.conexion.sync()
        return self.zodb.getDiccionarioElementos('secciones')
    
    def agregarSeccion(self, nombreSeccion, empleados, encargado):
        '''
        @return: 
        @author:
        Recibe el nombre de la nueva Seccion y los objetos empleados y encargados que ya fueron recuperados en el
        dialogo de cracion de la Seccion. 
        '''
        self.zodb.conexion.sync()
        empleadosSeccion = {}
        for empleado in empleados:
            empleadosSeccion[empleado.getDocumento()] = empleado
            self.zodb.remove('empleados', empleado.getDocumento())
        
        self.zodb.remove('empleados', encargado.getDocumento())
        codigoDeSeccion = len(self.secciones)
        seccion = Seccion(codigoDeSeccion, nombreSeccion, empleadosSeccion, encargado)
        
        #TODO: Esto respeta el modelo, seguimos de esta forma?
        self.secciones.append(seccion)
        
        self.zodb.save('secciones', seccion.getNombre(), seccion)


    def agregarSeccionesTwo(self, nombreSeccion, empleados, encargado):
        '''
        @return: 
        @author:
        Recibe el nombre de la nueva Seccion. 
        '''
#        pass
#        # Acordarse de de que vienen los documentos del empleados y el documento del encargado
#        # y s�lo el nombre de la Secci�n.
        self.zodb.conexion.sync()
        empleadosSeccion = {}
        for empleado in empleados:
#            empleadosSeccion[empleado] = deepcopy(zodb.get('empleados', empleado))
            empleadosSeccion[empleado] = self.zodb.raiz['empleados'][empleado]
#            del self.zodb.raiz['empleados'][empleado]
#        encargadoSeccion = deepcopy(zodb.get('empleados', encargado))
        encargadoSeccion = self.zodb.raiz['empleados'][encargado]
#        del self.zodb.raiz['empleados'][encargado]
        seccion = Seccion(nombreSeccion, empleadosSeccion, encargadoSeccion)
        # TODO: Tener en cuenta de q la seccion puede existir....
        try:
            self.zodb.raiz['secciones'][nombreSeccion] = seccion
        except KeyError:
            self.zodb.raiz['secciones'] = {}
            self.zodb.raiz['secciones'][nombreSeccion] = seccion
        #Problem solve...
        self.zodb.raiz._p_changed = True
        transaction.commit()
#        seccion.save()
#        zodb.remove('empleados', empleado)
#        zodb.remove('empleados', encargado)
        
    def getTipoDeDocumentos(self):
        '''
        @return: 
        @author: 
        '''
        self.zodb.conexion.sync()
        return self.zodb.getDiccionarioElementos('tiposDocumentos')
    
#    def getOrdenesDeReparacion(self):
#        '''
#        @return: 
#        @author: 
#        '''
#        pass
#    
#    def getOrdenDeReparacionDeVehiculo(self, dominio):
#        '''
#        @return: 
#        @author: 
#        '''
#        pass
    
    def getEmpleados(self):
        '''
        @return: 
        @author: 
        '''
        self.zodb.conexion.sync()
        #TODO: debemos comprobar en c/u de los metodos que precisen trabajar con la
        #zodb si existe el dict solicitado o comprobarlos una sola vez al abrir la bd???
        try:
            empleados = self.zodb.raiz['empleados'].values()
        except KeyError:
            self.zodb.raiz['empleados'] = {}
            empleados = self.zodb.raiz['empleados'].values()
        try:
            secciones = self.zodb.raiz['secciones'].values()
        except KeyError:
            self.zodb.raiz['secciones'] = {}
            secciones = self.zodb.raiz['secciones'].values()
            
        empleadosAsignados = {}
        for seccion in secciones:
            empleadosSeccion = seccion.empleados.values()
            for empleado in empleadosSeccion:
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
        self.zodb.conexion.sync()
        return self.zodb.raiz['empleados']
    
    def getEmpleado(self, clave):
        '''
        @return: 
        @author: 
        '''
        self.zodb.conexion.sync()
        try:
            return self.zodb.raiz['empleados'][clave]
        except KeyError:
            raise ExcepcionObjeNoExiste
    
    '''
    @TODO: Tener en cuenta q la el m�dulo q manipula la BD lanzar� una Excepci�n
    si el repuesto con las caracter�stcas q se intentan ingresar y existe.
    '''
    def agregarEmpleadoTwo(self, nombre, apellido, numeroDocumento, tipoDocumento):
        '''
        @return: 
        @author: 
        '''
        tiposDocumentos = self.zodb.raiz['tiposDocumentos']
        empleado = Empleado(nombre, apellido, numeroDocumento, tiposDocumentos[tipoDocumento])
        try:
            self.zodb.raiz['empleados'][numeroDocumento]
            raise ExcepcionObjetoExiste
        except KeyError, e:
            if e.message == 'empleados':
                self.zodb.raiz['empleados'] = {}
            # El objeto no existe en la bd
            self.zodb.raiz['empleados'][numeroDocumento] = empleado
            #Problem solve...
            self.zodb.raiz._p_changed = True
            transaction.commit()
    
    def agregarEmpleado(self, nombre, apellido, numeroDocumento, tipoDocumento):
        tiposDocumentos = self.zodb.raiz['tiposDocumentos']
        empleado = Empleado(nombre, apellido, numeroDocumento, tiposDocumentos[tipoDocumento])
        self.zodb.save('empleados', empleado.getDocumento(), empleado)
        
#    def darDeBajaEmpleado(self):
#        '''
#        @return: 
#        @author: 
#        '''
#        pass
    
    '''
    TODO: Tener en cuenta q la el m�dulo q manipula la BD lanzar� una Excepci�n
    si el repuesto con las caracter�stcas q se intentan ingresar y existe.
    '''
    def agregarRepuestos(self, nombre, descripcion):
        '''
        @return: 
        @author: 
        '''
        repuesto = TipoRepuesto(nombre, descripcion)
        self.zodb.conexion.sync()
        try:
            tiposRepuestos = self.zodb.raiz['tiposRepuestos']
        except KeyError, e:
            if e.message == 'tiposRepuestos':
                self.zodb.raiz['tiposRepuestos'] = {}
            tiposRepuestos[nombre] = repuesto
            transaction.commit()
                
    
    def getRepuestos(self):
        '''
        @return: 
        @author: 
        '''
        self.zodb.conexion.sync()
        return self.zodb.raiz['tiposRepuestos']

    def getRepuesto(self, clave):
        '''
        @return: 
        @author: 
        '''
        self.zodb.conexion.sync()
        try:
            return self.zodb.raiz['tiposRepuestos'][clave]
        except KeyError:
            raise ExcepcionObjeNoExiste
    
    def getVehiculos(self):
        '''
        @return: 
        @author: 
        '''
        self.zodb.conexion.sync()
        return self.zodb.getDiccionarioElementos('vehiculos')

    def getVehiculo(self, clave):
        '''
        @return: 
        @author: 
        '''
        self.zodb.conexion.sync()
        # TODO: try-except KeyError, No existe el dict de vehiculos
        vehiculos = self.zodb.raiz['vehiculos']
        try:
            return vehiculos[clave]
        except KeyError:
            raise ExcepcionObjeNoExiste
    
    def modificarVehiculo(self, dominio, marca, registroInterno, numeroChasis):
        '''
        @raise exception: ExcepcionObjeNoExiste (el vehiculo con el dominio....)
        TODO: está mal la lógica
        '''
        self.zodb.conexion.sync()
        try:
            vehiculos = self.zodb.getDiccionarioElementos('vehiculos')
            vehiculo = vehiculos[dominio]
#            vehiculo = self.zodb.raiz['vehiculos'][dominio]
            vehiculo.dominio = dominio
            vehiculo.marca = marca
            vehiculo.registroInterno = registroInterno
            vehiculo.numeroChasis = numeroChasis
            transaction.commit()
        except KeyError:
            raise ExcepcionObjeNoExiste
    
    '''
    @TODO: Tener en cuenta q la el m�dulo q manipula la BD lanzar� una Excepci�n
    si el repuesto con las caracter�stcas q se intentan ingresar y existe.
    '''
    def addVehiculo(self, dominio, marca, registroInterno, numeroChasis):
        '''
        @return: 
        @author: 
        '''
        vehiculo = Legajo(dominio, marca, registroInterno, numeroChasis)
        self.zodb.conexion.sync()
        self.zodb.save('vehiculos', dominio, vehiculo)
        #TODO: Atrapar la excepcion y avisar al usuario...
    
#    def registrarEgresoDeVehiculo(self, dominio, kilometrajeEgreso, CombustibleEgreso, fechaEgreso):
#        '''
#        @return: 
#        @author: 
#        '''
#        vehiculo = self.getVehiculo(dominio)
#        # Obtener orden reparacion
#        # si finalizada, Ok egreso sino pa' tras

    def registrarIngresoDeVehiculo(self, dominio, kilometrajeActual, combustibleActual, equipamiento, reparacion, comisaria, localidad):
        '''
        @return: 
        @author: 
        '''
        #TODO: el vehiculo puede no existir
        vehiculo = self.getVehiculo(dominio)
        '''
        TODO: tener en cuenta el m�todo obtenerOrdenDeReparacionEnCurso de Legajo que nos indica
        si ese veh�culo tiene o no orden Reparaci�n, por lo tanto no debemos crearle otra hasta
        que esa haya sido finalizada.
        '''
        import datetime
        hoy = datetime.datetime.now()
        vehiculo.crearOrdenDeReparacion(kilometrajeActual, combustibleActual, equipamiento, reparacion, comisaria, localidad, hoy)
        transaction.commit()
#        try:
#            vehiculo.dameOrdenDeReparacionEnCurso()
#        except excepciones.Excepcion_No_Posee_Orden_Reparacion_En_Curso.Excepcion_No_Posee_Orden_Reparacion_En_Curso:
#            import datetime
#            hoy = datetime.datetime.now()
#            vehiculo.crearOrdenDeReparacion(kilometrajeActual, combustibleActual, equipamiento, reparacion, comisaria, localidad, hoy)
#            transaction.commit()

    def getVehiculosSinOrdenEnCurso(self):
        return filter(lambda unVehiculo: unVehiculo.puedeRegistrarIngreso(), self.getVehiculos().values())
        

    def getTipoReparaciones(self):
        self.zodb.conexion.sync()
        try:
            return self.zodb.raiz['tiposReparaciones']
        except KeyError:
            self.zodb.raiz['tiposReparaciones'] = {}
            return self.zodb.raiz['tiposReparaciones']

    def getTipoReparacion(self, claveTipoReparacion):
        '''
        @return: 
        @author: 
        '''
        self.zodb.conexion.sync()
        tiposReparaciones = self.zodb.raiz['tiposReparaciones']
        try:
            return tiposReparaciones[claveTipoReparacion]
        except KeyError:
            raise ExcepcionObjeNoExiste
    
#    def registrarReparaciones(self, vehiculoSeleccionado):
#        # primero cambiamos el estado de la orden
#        # vehiculoSeleccionado.getOrdenDeReparacionEnCurso().getEstadoOrdenReparacion().cambiarProximoEstado()
#        vehiculoSeleccionado.getOrdenDeReparacionEnCurso().generarPedidoDeActuacion()
#        from copy import deepcopy
#        unVehiculo = deepcopy(vehiculoSeleccionado)
#        
#        zodb = ZopeDB(MiZODB())
#        zodb.remove('vehiculos', vehiculoSeleccionado.getDominio())
#        unVehiculo.save()

#    def getPedidoActuacionSinFechaRecepcion(self):
#        vehiculos = self.getVehiculos().values()
#        pedidosDeActuacion = []
#        for vehiculo in vehiculos:
#            pedido = vehiculo.getPedidoActuacionSinFechaRecepcion()
#            if pedido:
#                pedidosDeActuacion.append(pedido)
#        return pedidosDeActuacion
    
#    def registrarRecepcionPedidoDeActuacion(self, numeroPedido, fechaRecepcion):
#        print 'Registrando Recepcion Pedido de Actuacion'
#        vehiculo = self.obtenerVehiculo(numeroPedido)
#        try:
#            vehiculo.registrarRecepcionPedidoActuacion(fechaRecepcion)
#        except AttributeError, e:
#            raise Exception
#        
#        from MiZODB import MiZODB, ZopeDB
#        zodb = ZopeDB(MiZODB())
#        zodb.remove('vehiculos', vehiculo.dominio)
#        vehiculo.save()
            
    def obtenerVehiculo(self, numeroPedido):
        self.zodb.conexion.sync()
        vehiculos =  self.zodb.raiz['vehiculos'].values()
#        vehiculo = filter(lambda vehiculo: numeroPedido == vehiculo.dameOrdenDeReparacionEnCurso().getPedidoDeActuacionActual().getNumeroPedido(), vehiculos)
        for i in vehiculos:
            try:
                if i.dameOrdenDeReparacionEnCurso().getPedidoDeActuacionActual().getNumeroPedido() == numeroPedido:
                    vehiculo = i
            except AttributeError:
                #TODO: EL vehículo no posee pedido de Actuación con el num proporcionado
                pass
        return vehiculo

    def __str__(self):
        '''
        Sobrecarga del m�todo que imprime una cadena que representa a la Divisi�n Transporte.
        '''
        return '%s, Id: %s' % (self.__class__, id(self))
