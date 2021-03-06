# -*- coding: utf-8 -*-
'''
Created on 28/10/2012

@author: urrutia
'''

from persistent import Persistent
#from Localidad import Localidad
from OrdenReparacion import OrdenReparacion
from EnRevision import EnRevision
from excepciones.ExcepcionPoseeOrdenReparacionEnCurso import ExcepcionPoseeOrdenReparacionEnCurso
from excepciones.Excepcion_No_Posee_Orden_Reparacion_En_Curso import Excepcion_No_Posee_Orden_Reparacion_En_Curso
from excepciones.Excepcion_Orden_No_Esta_En_Revision import Excepcion_Orden_No_Esta_En_Revision 
from excepciones.Excepcion_No_Posee_Orden_Reparacion_En_Curso import Excepcion_No_Posee_Orden_Reparacion_En_Curso
from Aprobada import Aprobada
from Finalizada import Finalizada
from persistent.list import PersistentList

class Legajo(Persistent):
    '''
    classdocs
    @version: 
    @author: 
    '''

    ''' ATTRIBUTES

      - dominio  (private)
      - modelo  (private)
      - marca  (private)
      - registroInterno  (private)
      - numeroChasis  (private)
      - ordenesReparacion

    '''

    def __init__(self, dominio, marca, registroInterno, numeroChasis, comisaria=''):
        '''
        Constructor
        @return: 
        @author: 
        '''
        self.modelo = 'None'
        self.dominio = dominio
        self.marca = marca
        self.registroInterno = registroInterno
        self.numeroChasis = numeroChasis
        self.comisaria = comisaria
        # Tener en consideraón luego.
        self.localidad = ''
        #self.ordenesDeReparacion = []
        self.ordenesDeReparacion = PersistentList()
        self.numeroOrden = 0

    def noEstaFinalizada(self, ordenReparacion):
        return ordenReparacion.getEstadoOrdenReparacion() != 'Finalizada'

    def obtenerOrdenDeReparacionEnCurso(self):
        '''
        @return: 
        @author: 
        '''
#         ordenEnCurso = filter(lambda unaOrden: unaOrden.getEstado() != 'Finalizada', self.ordenesDeReparacion)
        ordenEnCurso = filter(lambda unaOrden: not isinstance(unaOrden.getEstado(), Finalizada), self.ordenesDeReparacion)
        try:
            return ordenEnCurso[0]
            raise ExcepcionPoseeOrdenReparacionEnCurso('El vehículo ya posee una orden de Reparación en Curso.')
        except IndexError:
            return None

    def dameOrdenDeReparacionEnCurso(self):
        '''
        @return: 
        @author: 
        '''
        ordenEnCurso = filter(lambda unaOrden: unaOrden.getEstado() != 'Finalizada', self.ordenesDeReparacion)
        try:
            return ordenEnCurso[0]
        except IndexError:

            raise Excepcion_No_Posee_Orden_Reparacion_En_Curso('El vehículo no posee una Orden de Reparación en Curso.')

    def getOrdenDeReparacionEnCurso(self):
        '''
        @return: 
        @author: 
        '''
        # ordenEnCurso = filter(lambda unaOrden: unaOrden.getEstadoOrdenReparacion() != 'Finalizada', self.ordenesDeReparacion)
        ordenEnCurso = filter(lambda unaOrden: isinstance(unaOrden.getEstado(), EnRevision), self.ordenesDeReparacion)
#        ordenEnCurso = filter(self.noEstaFinalizada, self.ordenesDeReparacion)
        try:
            return ordenEnCurso[0]
        except IndexError:
            # return None

            raise Excepcion_Orden_No_Esta_En_Revision('La Orden de Reparacion del vehiculo no se encuentra en revision')

    def crearOrdenDeReparacion(self, codigo, kilometrajeActual, combustibleActual, equipamiento, reparacion, comisaria, localidad, fecha, chofer):
        '''
        @return: 
        @author: 
        '''
        # Antes de crear la orden, obtener orden en curso, si no existe(no tiene) crearla.
        try:
            self.obtenerOrdenDeReparacionEnCurso()
            #ordenReparacion = OrdenReparacion(self.dameNumeroOrden(), kilometrajeActual, combustibleActual, equipamiento, reparacion, comisaria, localidad, fecha)
            ordenReparacion = OrdenReparacion(codigo, kilometrajeActual, combustibleActual, equipamiento, reparacion, comisaria, localidad, fecha)
            ordenReparacion.setChofer(chofer)
            self.ordenesDeReparacion.append(ordenReparacion)
        except ExcepcionPoseeOrdenReparacionEnCurso, e:
            raise ExcepcionPoseeOrdenReparacionEnCurso(e.getMensaje())

    def dameNumeroOrden(self):
        self.numeroOrden += 1
        return self.numeroOrden

    def __eq__(self, otro):
        return (self.dominio == otro.dominio)

    def __str__(self):
        return 'Dominio: %s' % self.dominio

    def getDominio(self):
        return self.dominio

    def getNumeroChasis(self):
        return self.numeroChasis

    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def getMarca(self):
        return self.marca

    def setMarca(self, marca):
        self.marca = marca

    def getRegistroInterno(self):
        return self.registroInterno

    def setRegistroInterno(self, registroInterno):
        self.registroInterno = registroInterno

    def getComisaria(self):
        return self.comisaria

    def setComisaria(self, comisaria):
        self.comisaria = comisaria

    def getPedidoActuacionSinFechaRecepcion(self):

        try:
            #ordenEnCurso = self.dameOrdenDeReparacionEnCurso()
            ordenEnCurso = self.obtenerOrdenDeReparacionEnCurso()
            return ordenEnCurso.getPedidoDeActuacionActual()
        except Excepcion_No_Posee_Orden_Reparacion_En_Curso:
            pass

    def registrarRecepcionPedidoActuacion(self, fechaRecepcion):
        recepcion_exitosa = self.obtenerOrdenDeReparacionEnCurso().registrarRecepcionPedidoActuacion(fechaRecepcion)
        return recepcion_exitosa

    def puedeRegistrarIngreso(self):
        ordenesEnCurso = filter(lambda unaOrden: unaOrden.noEstaFinalizada(), self.ordenesDeReparacion)
        # Si el vehiculo posee una orden en curso, es decir, una orden que no este finalizada, no puede registrar el ingreso.
        if ordenesEnCurso:
            return False
        return True

    def generarPedidoDeActuacion(self):
        '''
        Genera un pedido de actuacion con los repuestos que tienen las reparaciones
        de la OR.
        @return: True si la operacion fue realizada con exito. False en caso contrario
        '''
        generacion_exitosa = self.obtenerOrdenDeReparacionEnCurso().generarPedidoDeActuacion()
        return generacion_exitosa

    def registrarNuevoIngreso(self, kilometrajeActual, combustibleActual, equipamiento, reparacion, comisaria, localidad, fecha):
        if self.obtenerOrdenDeReparacionEnCurso() == None:
            ordenReparacion = OrdenReparacion(self.dameNumeroOrden(), kilometrajeActual, combustibleActual, equipamiento, reparacion, comisaria, localidad, fecha)
            self.ordenesDeReparacion.append(ordenReparacion)
            return True
        else:
#            print 'El vehiculo ya posee una OR en curso. No se registro el ingreso'
            return False

    def registrarReparaciones(self, reparaciones):
        '''
        Recibe una lista de reparaciones, las cuales agrega a la OR en curso
        '''
        # agregar las reparaciones a la OR en curso...
        for reparacion in reparaciones:
            self.obtenerOrdenDeReparacionEnCurso().addReparacion(reparacion)

    def agregarTurnoAlPlan(self, turno):
        self.obtenerOrdenDeReparacionEnCurso().agregarTurnoAlPlan(turno)

    def planificacionFinalizada(self):
        finalizacion_exitosa = self.obtenerOrdenDeReparacionEnCurso().planificacionFinalizada()
        return finalizacion_exitosa

    def getTurnosSinAtender(self):
        '''
        Esta accion solo es realizable en estado 'Planificada'
        '''
        return self.obtenerOrdenDeReparacionEnCurso().getTurnosSinAtender()

    #Los try and except de los estaEn.... se deben a que el vehiculo puede no tener
    #orden en curso.
    def estaEnRevision(self):
        try:
            return isinstance(self.obtenerOrdenDeReparacionEnCurso().getEstado(), EnRevision)
        except AttributeError:
            return False

    def estaEnAprobada(self):
        #return isinstance(self.obtenerOrdenDeReparacionEnCurso().getEstado(), Aprobada)
        try:
            return self.obtenerOrdenDeReparacionEnCurso().estaAprobada()
        except AttributeError:
            return False

    def estaEsperandoAprobacion(self):
        try:
            return self.obtenerOrdenDeReparacionEnCurso().estaEsperandoAprobacion()
        except AttributeError:
            return False

    def estaFinalizado(self):
        try:
            return self.obtenerOrdenDeReparacionEnCurso().estaFinalizada()
        except AttributeError:
            return False

    def tieneOrdenesReparacionFinalizadas(self):
        '''
        Verifica si el vehículo tiene al menos una orden de reparación
        en Finalizada.
        @return: True si tiene al menos una orden finalizada, False en
        caso contrario.
        '''
        ordenes = filter(lambda orden: orden.estaFinalizada(), self.getOrdenesDeReparacion())
        return len(ordenes) > 0

    def estaPlanificado(self):
        try:
            return self.obtenerOrdenDeReparacionEnCurso().estaPlanificada()
        except AttributeError:
            return False

    def getPedidoDeActuacion(self):
        return self.obtenerOrdenDeReparacionEnCurso().getPedidoDeActuacion()

    def pedidoDeActuacionTePertenece(self, unPedidoDeActuacion):
        #return unPedidoDeActuacion == self.getPedidoDeActuacion()
        return unPedidoDeActuacion.getNumeroPedido() == self.getPedidoDeActuacion().getNumeroPedido()

    def tieneReparacionesMecanicas(self):
        pass

    def getOrdenesDeReparacionFinalizadas(self):
        return filter(lambda ordenReparacion: ordenReparacion.estaFinalizada(), self.getOrdenesDeReparacion())

    def getReparacionesFinalizadas(self):
        '''
        Devuelve todas las reparaciones finalizadas de un vehículo. Busca
        en cada orden de reparación aquellas reparaciones se encuentren
        finalizadas.
        @return: list list Reparacion. De la forma [[Rep1, Rep2], [Rep1]]
        '''
        reparaciones = [orden.getReparaciones() for orden in self.getOrdenesDeReparacionFinalizadas()]
        return reparaciones

    def getReparacionesFinalizadasOrdenadasPorOrdenReparacion(self):
        '''
        Devuelve todas las reparaciones finalizadas de un vehículo. Busca
        en cada orden de reparación aquellas reparaciones se encuentren
        finalizadas.
        @return: diccionario de la siguiente forma:
            {'ORD0001':[Rep1, Rep2,.., RepN],
            ...
            }
        '''
        reparacionespororden = {}
        for orden in self.getOrdenesDeReparacionFinalizadas():
            reparacionespororden[orden.getCodigoOrdenReparacion()] = orden.getReparaciones()
        return reparacionespororden

    def getOrdenesDeReparacion(self):
        return self.ordenesDeReparacion

    def getReparacionesSinPlanificarDeLaSeccion(self, nombre_seccion):
        try:
            return self.obtenerOrdenDeReparacionEnCurso().getReparacionesClasificadas()[nombre_seccion]
        except KeyError:
            return []

    def tieneTodasLasReparacionesPlanificadas(self):
        return self.obtenerOrdenDeReparacionEnCurso().getReparacionesSinPlanificar() == []

    def getReparacionesSinPlanificar(self):
        return self.obtenerOrdenDeReparacionEnCurso().getReparacionesSinPlanificar()

    def getReparaciones(self):
        return self.obtenerOrdenDeReparacionEnCurso().getReparaciones()

    def getReparacionesPlanificadas(self):
        '''
        Obtiene todas las reparaciones planificadas del vehículo.
        @return: list Reparacion
        '''
        return self.obtenerOrdenDeReparacionEnCurso().getReparacionesPlanificadas()

    def getReparacionesFinalizadasActuales(self):
        '''
        Obtiene todas las reparaciones planificadas del vehículo de la OR actual.
        @return: list Reparacion
        '''
        return self.obtenerOrdenDeReparacionEnCurso().getReparacionesFinalizadas()

    def tieneTodosLosTurnosFinalizados(self):
        return self.obtenerOrdenDeReparacionEnCurso().tieneTodosLosTurnosFinalizados()

    def finalizarVerificacionReparacion(self):
        return self.obtenerOrdenDeReparacionEnCurso().finalizarVerificacionReparacion()

    def puedeEgresar(self):
        return self.getOrdenParaEgreso() != None

    def getOrdenParaEgreso(self):
        orden = filter(lambda unaOrden: unaOrden.puedeEgresar(), self.ordenesDeReparacion)
        try:
            orden = orden[0]
            return orden
        except IndexError:
            return None

    def registrarEgreso(self, kilometraje, combustible, fecha):
        self.getOrdenParaEgreso().registrarEgreso(kilometraje, combustible, fecha)

    def getTurnosOrdenados(self):
        '''
        Devuelve un diccionario con los turnos por los que debe pasar el vehiculo:
        turnos= {   1:Turno1
                    2:Turno2
                    ...
                    N:TurnoN
                }
        '''
        #Tengo una OR planificada? Si, retornar lo que pidieron. No, return None
        return self.obtenerOrdenDeReparacionEnCurso().getTurnosOrdenados()
    
    def getCodigoPlan(self):
        return self.obtenerOrdenDeReparacionEnCurso().getCodigoPlan()
    
    def horasOcupadasParaElDia(self, dia):
        '''
        @param dia: QDate
        @return: Una lista de entero que representan las horas en las que el vehiculo tiene ya asignado un turno
                 para el dia recibido
        '''
        return self.obtenerOrdenDeReparacionEnCurso().getPlan().horasOcupadasParaElDia(dia)
    
    def getFechasDeTurnos(self):
        '''
        @return: lista de unafecha de tipo str.
        
        '''
        ordenes = filter(lambda orden: orden.getFechaEgreso() == None, self.ordenesDeReparacion)
        return ordenes[0].getPlan().getFechasDeTurnos()
##############################################################################
########################## TEST LEGAJO #######################################
##############################################################################
import unittest

class TddLegajo(unittest.TestCase):
    
    def setUp(self):
        dominio, marca, registroInterno, numeroChasis, comisaria = 'ERR333', 'Ford','1111','0001','Primera'
        self.legajo  = Legajo(dominio, marca, registroInterno, numeroChasis, comisaria)

    def tearDown(self):
        pass
    
    def test_patente_correcta(self):
        patente = self.legajo.getDominio()
        self.assertEqual('ERR333', patente)
    
    def test_registrar_ingreso(self):
        sePudo = self.legajo.registrarNuevoIngreso()
        self.assertEqual(sePudo, True)
        