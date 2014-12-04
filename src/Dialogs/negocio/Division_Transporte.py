# -*- coding: utf-8 -*-
'''
Created on 28/10/2012

@author: urrutia
'''

from persistent import Persistent
from persistent.list import PersistentList
from sys import maxint
from time import mktime
from datetime import date

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
from excepciones.ExcepcionObjetoExiste import ExcepcionObjetoExiste, ExcepcionVehiculoExiste, ExcepcionEmpleadoExiste
from excepciones.ExcepcionObjetoNoExiste import ExcepcionObjeNoExiste


class MiZODB(object):
    '''
    Clase que representa la conexión con la ZODB (Zope Object Data Base).
    @author: urrutia
    '''

#    def __init__(self, url):
    def __init__(self):
        '''
        Constructor, se conecta al Servidor de la BD a través del archivo de configuracion zeo.conf
        en donde se indica la IP:PORT.
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
        # The object has been changed.
        self.raiz._p_changed = True
        # setUser(user, path) -> "%s %s" % (path, user_name)
        transaction.get().setUser(self.getNombreUsuario(), path='')
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
            raise ExcepcionObjetoExiste(clave)
        except KeyError:
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

    def borraUsuario(self, empleado):
        '''
        Borra Usuario (tupla: nombre-pass-rol) en la lista de Usuarios
        Confirma la transaccion.
        '''
        lista_de_usrs = self.getDiccionarioElementos('USUARIOS')
        usuario_a_eliminar = filter(lambda tupla: tupla[0] == empleado.nombreCompletoUsr(), lista_de_usrs)
        usuario_a_eliminar = usuario_a_eliminar[0]
        lista_de_usrs.remove(usuario_a_eliminar)
        self.commiting()

    def remove(self, claveDiccionario, clave):
        '''
        @raise exception: ObjetoNoExiste
        '''
        try:
            diccionario = self.getDiccionarioElementos(claveDiccionario)
            del diccionario[clave]
            self.commiting()
        except KeyError:
            raise ExcepcionObjeNoExiste

    def setFechaMinimaDeshacer(self, fecha):
        '''
        Se utiliza para indicar la mínima fecha a tener en cuenta para
        deshacer los commits realizados en bd.
        Convierte la fecha de tipo time tuple en un floating point number.
        fecha: a time tuple expressing local time.
            More information see time.localtime()
        '''
        # Convert a time tuple in local time to seconds since the Epoch.
        # time.mktime(tuple) -> floating point number.
        self.fechaMinima = mktime(fecha)

    def getFechaMinimaDeshacer(self):
        '''
        Devuelve un float a partir de la fecha establecida.
        @return: floating point number.
        '''
        return self.fechaMinima

    def deshacerCommits(self):
        '''
        Elimina todos los commits realizados hasta la fecha mínima
        establecida. Se tiene en cuenta el nombre del usuario.
        '''
        lista_deshacer = []
        # maxint -> Se lo pedimos a sys
        for item in self.db.undoLog(0, maxint):
            # Formato del diccionario que representa el commit.
            # {'description': '', 'id': 'A6mkrSvMssw=', 'size': 163,
            # 'time': 1411014550.265532, 'user_name': ''}
            # Se obtiene el campo time y usuario de la transacción.
            if item['time'] >= self.fechaMinima and item['user_name'] == ' ' + self.nombreUsuario:
                lista_deshacer.append(item)
        # TODO: [ok] Usar el user_name para filtrar por aplicación. En este
        # momento se borran los commits realizados por todos clientes.
        for item in lista_deshacer:
            # Se obtiene el id de la transacción.
            tid = item['id']
            self.db.undo(tid)
            transaction.get().setUser(self.getNombreUsuario(), path='')
            transaction.commit()

    def seNombreUsuario(self, nombre):
        '''
        Se utiliza para indicar el nombre del usuario que utiliza la
        aplicación.
        Sirve para filtrar las transacciones hechas por el usuario
        establecido.
        nombre: string.
        '''
        self.nombreUsuario = nombre

    def getNombreUsuario(self):
        return self.nombreUsuario

    def getTransacciones(self):
        '''
        Devuelve el historial de transacciones realizadas por el usuario de
        la aplicación.
        @return: list. De la forma [{T1}, {T2}, ..., {Tn}]
        '''
        lista_transacciones = []
        for item in self.db.undoLog(0, maxint):
            # if item['user_name'].strip(' ') == self.nombreUsuario:
            if item['user_name'] == ' ' + self.nombreUsuario:
                lista_transacciones.append(item)
        return lista_transacciones


class Division_Transporte(Persistent):
    '''
    Clase que representa a la División de Transporte.
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
        # TODO: try: ... ClientDisconnected -> Error en BD
        self.zodb = MiZODB()
        print "La base soporta undo: %s" % self.zodb.db.supportsUndo()
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
        dialogo de creacion de la Seccion. 
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
        Devuelve los tipos de documentos.
        @return: TipoDocumento
        '''
        self.zodb.conexion.sync()
        return self.zodb.getDiccionarioElementos('tiposDocumentos')

    def getEmpleados(self):
        '''
        Devuelve todos los empleados que se encuentran en la División.
        Asignados y no asignados.
        @return: diccionario de empleados.
        '''
        self.zodb.conexion.sync()
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
            empleadosSeccion = seccion.getEmpleados()
            for empleado in empleadosSeccion:
                empleadosAsignados[empleado.getDocumento()] = empleado
            empleadosAsignados[seccion.getEncargado().getDocumento()] = seccion.getEncargado()

        for empleado in empleados:
            empleadosAsignados[empleado.getDocumento()] = empleado
        return empleadosAsignados

    def getEmpleadosSinAsignar(self):
        '''
            @return: Devuelve un diccionario con todos los empleados de la
            Division que no estan asiganados a ninguna Seccion.
        '''
        self.zodb.conexion.sync()
        try:
            return self.zodb.raiz['empleados']
        except KeyError:
            return {}

    def getEmpleado(self, clave):
        '''
        Devuelve un objeto del tipo Empleado.
        @return: empleado
        '''
        self.zodb.conexion.sync()
        try:
            return self.zodb.raiz['empleados'][clave]
        except KeyError:
            raise ExcepcionObjeNoExiste

    def agregarEmpleado(self, nombre, apellido, numeroDocumento, tipoDocumento,
                        fechaNac, domicilio, telefono, email):
        '''
            Crea un empleado nuevo con los datos recibidos y lo guarda en la BD.
            Se comprueba si el número de documento y el tipo de documento son
            iguales.
        '''
        tiposDocumentos = self.zodb.raiz['tiposDocumentos']
        tipoDocSeleccionado = tiposDocumentos[tipoDocumento]
        empleado = Empleado(nombre, apellido, numeroDocumento, tipoDocSeleccionado,
                            fechaNac, domicilio, telefono, email)
        fecha = date.today()
        empleado.setFechaAlta(fecha)
        # Se obtienen todos los empleados de la División.
        empleados = self.getEmpleados().values()
        # Se comprueba si el empleado se encuentra en la División.
        # Se verifica si el número de documento y el tipo de documento son
        # iguales.
        for e in empleados:
            if empleado.comparar(e):
                raise ExcepcionObjetoExiste
        self.zodb.save('empleados', empleado.getDocumento(), empleado)

    def agregarEmpleadoDisponible(self, empleado):
        '''
        Mejorable!
        '''
        # Se obtienen todos los empleados de la División.
        empleados = self.getEmpleados().values()
        # Se comprueba si el empleado se encuentra en la División.
        # Se verifica si el número de documento y el tipo de documento son
        # iguales.
        for e in empleados:
            if empleado.comparar(e):
                raise ExcepcionObjetoExiste
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
        repTypeCode = self.getGestorDeCodigos().nextCodigoTipoDeRepuesto()
        repuesto = TipoRepuesto(repTypeCode, nombre, descripcion)
        self.zodb.conexion.sync()
        try:
            tiposRepuestos = self.zodb.raiz['tiposRepuestos']
        except KeyError, e:
            #Si se ejecuta el script de cargado de datos, nunca se debe ingresar aca...
            if e.message == 'tiposRepuestos':
                self.zodb.raiz['tiposRepuestos'] = {}
            #tiposRepuestos[nombre] = repuesto
        finally:
            tiposRepuestos[repTypeCode] = repuesto
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
        '''
        self.zodb.conexion.sync()
        # TODO: try-except KeyError, No existe el dict de vehiculos
        vehiculos = self.zodb.raiz['vehiculos']
        try:
            return vehiculos[clave]
        except KeyError:
            raise ExcepcionObjeNoExiste(clave)

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

    def agregarVehiculo(self, dominio, marca, registroInterno, numeroChasis, modelo):
        '''
        Crea un Legajo nuevo con los datos recibidos y lo guarda en la BD.
        Se comprueba si el dominio ya se encuentra cargado.
        @return:
        @author:
        '''
        vehiculo = Legajo(dominio, marca, registroInterno, numeroChasis)
        vehiculo.setModelo(modelo)
        self.zodb.conexion.sync()
        # TODO: Se debería comprobar si el dominio y el registro interno son iguales.
        try:
            self.zodb.save('vehiculos', dominio, vehiculo)
            print self.zodb.getTransacciones()
        except ExcepcionObjetoExiste:
            raise ExcepcionVehiculoExiste(dominio)
        # TODO:
        # Falta manejar el tema del R.I, es autonumérico o
        # se debe avisar al usr que ya existe un móvil con ese R.I?

#    def registrarEgresoDeVehiculo(self, dominio, kilometrajeEgreso, CombustibleEgreso, fechaEgreso):
#        '''
#        @return: 
#        @author: 
#        '''
#        vehiculo = self.getVehiculo(dominio)
#        # Obtener orden reparacion
#        # si finalizada, Ok egreso sino pa' tras

    def registrarIngresoDeVehiculo(self, dominio, kilometrajeActual, combustibleActual, equipamiento, reparacion, comisaria, localidad, chofer):
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
        ordenReparationCode = self.getGestorDeCodigos().nextCodigoOrdenDeReparacion()
        vehiculo.crearOrdenDeReparacion(ordenReparationCode, kilometrajeActual, combustibleActual, equipamiento, reparacion, comisaria, localidad, hoy, chofer)
        transaction.commit()

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
        '''
        Una vez que las reparaciones han sido asignadas, este metodo sirve para generar el 
        pedido de actuacion al vehiculo seleccionado.
        Por <<insert_alguna_razon_aqui>> se penso que esto era responsabilidad de la DT.
        '''
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
        '''
        Retorna el vehiculo que posee el nro de pedido con el 
        numeroPedido
        '''
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
        return filter(lambda unVehiculo: unVehiculo.tieneOrdenesReparacionFinalizadas(), self.getVehiculos().values())

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
    
    def borraUsuario(self, viejoUsr):
        self.zodb.borraUsuario(viejoUsr)
    
    def eliminarEmpleadoDisponible(self, empleado):
        self.zodb.remove('empleados', empleado.getDocumento())
        
    def getGestorDeCodigos(self):
        '''
        @return: El objeto manejador de los codigos de los objetos de la DIvision
        @author:
        '''
        self.zodb.conexion.sync()
        try:
            return self.zodb.raiz['gestorDeCodigos']
        except KeyError:
            raise ExcepcionObjeNoExiste


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