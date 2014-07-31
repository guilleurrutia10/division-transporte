# -*- coding: utf-8 -*-
'''
Created on 28/10/2012

@author: urrutia
'''

from persistent import Persistent
from persistent.list import PersistentList

from Empleado import Empleado
from Legajo import Legajo
#from Localidad import *
# Puedo obtenerlos a trav�s de los Legajos. (1 a 1 con la Orden de Reparaci�n)
# from PedidoDeActuacion import *
from TipoRepuesto import TipoRepuesto
from Seccion import Seccion
#from TipoDeReparacion import *
#from TipoDocumento import *

from ZODB import config
from ZEO.Exceptions import ClientDisconnected
import transaction
#from copy import deepcopy
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

    def saveUsr(self, usr):
        '''
        Agrega un nuevo Usuario (tupla: nombre-pass-rol) en la lista de Usuarios
        Confirma la transaccion.
        
        '''
        lista_de_usrs = self.getDiccionarioElementos('USUARIOS')
        lista_de_usrs.append(usr) #USUARIOS.append((self.name, hash_password, rol))
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
    
    @classmethod
    def divisionTransporte(cls):
        zodb = MiZODB()
        dbroot = zodb.raiz
        div = dbroot['DIVISION']
        return div
        
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
        #TODO: try: ... ClientDisconnected -> Error en BD
        self.zodb = MiZODB()
        self.legajos = PersistentList()
        self.localidades = PersistentList()
        self.empleados = PersistentList()
        self.tiposDeDocumentos = PersistentList()
        self.tiposDeRepuestos = PersistentList()
        self.tiposDeReparacion =PersistentList()
        self.secciones = PersistentList()
        self.NRO_PEDIDO_DE_ACTUACION = 0

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
        #Antes de guardar, creamos el Usuario del Encargado, para que pueda loguearse luego
        from usuario import Usuario
        usrNew = Usuario(unicode(encargado.nombreCompletoUsr()), unicode(encargado.getPassword()))
        usrNew.registrar('jefeSeccion')
        encargado.setUsuario(usrNew)
        self.zodb.conexion.sync()
        
        #Armar un diccionario de empleados (bien podria hacerlo la misma seccion, tmb):
#         empleadosSeccion = {}
        for empleado in empleados:
#             empleadosSeccion[empleado.getDocumento()] = empleado
            self.zodb.remove('empleados', empleado.getDocumento())
        
        self.zodb.remove('empleados', encargado.getDocumento())
        codigoDeSeccion = len(self.secciones)
        seccion = Seccion(codigoDeSeccion, nombreSeccion, empleados, encargado)
        
        #TODO: Esto respeta el modelo, seguimos de esta forma?
        self.secciones.append(seccion)
        
        self.zodb.save('secciones', seccion.getNombre(), seccion)


    def getTipoDeDocumentos(self):
        '''
        @return: 
        @author: 
        '''
        self.zodb.conexion.sync()
        return self.zodb.getDiccionarioElementos('tiposDocumentos')
    
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
#             empleadosSeccion = seccion.empleados.values()
            empleadosSeccion = seccion.getEmpleados()
            for empleado in empleadosSeccion:
                empleadosAsignados[empleado.getDocumento()] = empleado
            empleadosAsignados[seccion.getEncargado().getDocumento()] = seccion.getEncargado()
    
        for empleado in empleados:
            empleadosAsignados[empleado.getDocumento()] = empleado
        return empleadosAsignados
    
    def getEmpleadosSinAsignar(self):
        '''
            @return: Devuelve un diccionario con todos los empleados de la Division que no estan asiganados a ninguna Seccion. 
             
        '''
        self.zodb.conexion.sync()
        try:
            return self.zodb.raiz['empleados']
        except KeyError:
            return {}

    
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
        '''
            Crea un empleado nuevo con los datos recibidos y lo guarda en la BD.
        '''
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
#            vehiculo.crearDeReparacion(kilometrajeActual, combustibleActual, equipamiento, reparacion, comisaria, localidad, hoy)
#            transaction.commit()

    def getVehiculosSinOrdenEnCurso(self):
        #print '#'*20
        #print self.getVehiculos().values()
        return filter(lambda unVehiculo: unVehiculo.puedeRegistrarIngreso(), self.getVehiculos().values())
        

    def getTipoReparaciones_deprecated(self):
        self.zodb.conexion.sync()
        try:
            return self.zodb.raiz['tiposReparaciones']
        except KeyError:
            self.zodb.raiz['tiposReparaciones'] = {}
            return self.zodb.raiz['tiposReparaciones']

    def getTipoReparaciones(self):
        todas_las_reparaciones_de_la_div = []
        for seccion in self.getSecciones().values():
            todas_las_reparaciones_de_la_div.extend(seccion.getTiposDeReparaciones())
        
        return todas_las_reparaciones_de_la_div

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
    
    def registrarReparaciones(self, vehiculoSeleccionado):
        # primero cambiamos el estado de la orden
        # vehiculoSeleccionado.getOrdenDeReparacionEnCurso().getEstadoOrdenReparacion().cambiarProximoEstado()
        vehiculoSeleccionado.getOrdenDeReparacionEnCurso().generarPedidoDeActuacion()
        

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

    def getUsuarios(self):
        '''
        @return: 
        @author: 
        '''
        self.zodb.conexion.sync()
        return self.zodb.getDiccionarioElementos('USUARIOS')
    
    def registrarUsuario(self, nuevoUsr):
        self.zodb.saveUsr(nuevoUsr)
        
    def getSeccionesQuePuedenTransferir(self):
        '''
        @return: una lista con todas las Secciones que cumplen las condiciones para tranferir empleados.
        @author: 
        '''
        self.zodb.conexion.sync()
        #todasLasSecciones = self.zodb.raiz['secciones'].values() #para mejor visibilidad
        todasLasSecciones = self.getSecciones().values() #para mejor visibilidad
        return filter(lambda unaSeccion: unaSeccion.puedeTransferir(), todasLasSecciones)
    
    def getSeccionesParaCambiarEmpleado(self, unEmpleado):
        '''
            Retorna todas las secciones a las que unEmpleado puede ser transferido
        '''
        return filter(lambda unaSeccion: unaSeccion != self.getSeccionDeEmpleado(unEmpleado), self.getSecciones().values())
        
    def getSeccionDeEmpleado(self, empleado):
        '''
            Retorna la seccion en la que se encuentra el empleado.
            En caso de no encontrarse en ninguna seccion, retorna None.
        '''
        seccion_del_empleado = None
        for seccion in self.getSecciones().values():
            if seccion.poseeAEmpleado(empleado): 
                seccion_del_empleado = seccion
                break
        #print 'La seccion del empleado: %s, es: %s' %(empleado.quienSos(), seccion_del_empleado.getNombre())
        return seccion_del_empleado
    
    def cambiarDeSeccionAEmpleado(self, unEmpleado, seccionNueva):
        '''
        Remueve al empleado de su Seccion actual y lo ubica en la nueva Seccion
        @precondition: unEmpleado no se encuentra en la nuevaSeccion
        '''
        #Recuperamos la seccione del empleado:
        seccionVieja = self.getSeccionDeEmpleado(unEmpleado)
        #Removemos
        seccionVieja.removerEmpleado(unEmpleado)
        #Agregamos a la nueva:
        seccionNueva.agregarEmpleado(unEmpleado)
        #TODO: Guardamos, esto es todo?
        transaction.commit()
        self.zodb.commiting()
        
    def asignarNuevoEncargadoDeSeccion(self, seccion, nuevoEncargado):
        encargadoAnterior = seccion.asignarNuevoEncargado(nuevoEncargado)
        #TODO: Verificar!
        self.agregarEmpleadoDisponible(encargadoAnterior)
        
    def agregarEmpleadoDisponible(self, empleado):
        '''
            Asigna al empleado recibido a la 'lista' de empleados disponibles.
        '''
        self.zodb.save('empleados', empleado.getDocumento(), empleado)

    def getProximoNroPedidoActuacion(self):
        self.NRO_PEDIDO_DE_ACTUACION += 1
        return self.NRO_PEDIDO_DE_ACTUACION
    
    def getVehiculosEnRevision(self):
        return filter(lambda unVehiculo: unVehiculo.estaEnRevision(), self.getVehiculos().values())

    def getVehiculosEnAprobada(self):
        return filter(lambda unVehiculo: unVehiculo.estaEnAprobada(), self.getVehiculos().values())
    
    def getVehiculosEsperandoAprobacion(self):
        return filter(lambda unVehiculo: unVehiculo.estaEsperandoAprobacion(), self.getVehiculos().values())
    
    def getVehiculosEnFinalizada(self):
        return filter(lambda unVehiculo: unVehiculo.estaFinalizado(), self.getVehiculos().values())
    
    def getVehiculosEnPlanificacion(self):
        return filter(lambda unVehiculo: unVehiculo.estaPlanificado(), self.getVehiculos().values())
    
    def getTipoRepuestos(self):
        '''
        @return: 
        @author: 
        '''
        self.zodb.conexion.sync()
        return self.zodb.getDiccionarioElementos('tiposRepuestos')
    
    def modificarRepuesto(self, clave, nombre, descripcion):
        try:
            repuesto = self.getRepuesto(clave)
            repuesto.setNombre(nombre)
            repuesto.setDescripcion(descripcion)
            
            transaction.commit()
        except KeyError:
            pass
    
    def getVehiculosParaEgreso(self):
        return filter(lambda unVehiculo: unVehiculo.puedeEgresar(), self.getVehiculos().values())
    
##############################################################################
########################## TEST DIVISION #####################################
##############################################################################
import unittest

class TddDivision(unittest.TestCase):
    
    def setUp(self):
        #self.division  = Division_Transporte()
        pass

    def tearDown(self):
        pass
    
    def test_division_no_tiene_vehiculos_para_registrar_ingreso(self):
        #sin_orden = self.division.getVehiculosSinOrdenEnCurso()
        sin_orden = Division_Transporte().getVehiculosSinOrdenEnCurso()
        self.assertEqual(4, len(sin_orden))
        
#    def test_division_tiene_vehiculos_para_registrar_ingreso(self):
#        dominio, marca, registroInterno, numeroChasis = 'GGG555', 'Ford', '1234', '1111'
#        self.division.addVehiculo(dominio, marca, registroInterno, numeroChasis)
#        sin_orden = self.division.getVehiculosSinOrdenEnCurso()
#        self.assertEqual(1, len(sin_orden))