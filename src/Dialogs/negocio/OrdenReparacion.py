# -*- coding: utf-8 -*-
'''
Created on 28/10/2012

@author: urrutia
'''

from persistent import Persistent
from persistent.list import PersistentList

#from EstadoOrdenReparacion import *
# from PedidoDeActuacion import *
#from Reparacion import *
from EnRevision import EnRevision
from EsperandoAprobacion import EsperandoAprobacion
from Planificada import Planificada
from Aprobada import Aprobada
from Finalizada import Finalizada
from Plan import Plan
import transaction

class OrdenReparacion(Persistent):
    '''
    La Orden de Reparacion se crea cuando se registra un ingreso de un vehiculo.

    @version: 
    @author: 
    '''

    ''' ATTRIBUTES

    Fecha_de_Ingreso  (private)

    FechaDe_Ingreso  (private)

    choferAsignado  (private)

    kilometrajeIngresado  (private)

    kilometrajeEgreso  (private)

    equipamiento  (private)

    reparacionSolicitada  (private)

    combustibleIngreso  (private)

    combustibleEgreso  (private)

    comisaria  (private)

    revisada  (private)

    aprobada  (private)

    '''

    '''
    TODO: falta migrar comportamiento a las clases EstadoOrden y según dicho estado se 
    podrán realizar algunas operaciones y otras no.
    '''
    def __init__(self, codigoOrdenReparacion, kilometrajeActual, combustibleActual, equipamiento, reparacion, comisaria, localidad, fecha):
        '''
        Constructor
        @return: 
        @author: 
        '''

        '''
        TODO: tener en cuenta los comentarios siguientes.
        '''
#        self.codigoOrdenReparacion = incremental
        # La primera vez debe instanciarse como EnRevision()
#        self.estado = EstadoOrdenReparacion(), self.estado =  EnRevision()
        self.codigoOrdenReparacion = codigoOrdenReparacion

        self.estado = EnRevision(self)#para que el estado pueda realizarlemodificaciones
        self.reparaciones = PersistentList()

        self.kilometrajeActual = kilometrajeActual
        self.combustibleActual = combustibleActual
        self.equipamiento = equipamiento
        self.reparacion = reparacion
        self.comisaria = comisaria
        self.localidad = localidad
        self.fecha = fecha
        self.chofer = 'Jose Luis Barrionuevo'

        self._pedidoDeActuacion = None
        self._plan = Plan() #Sera utilizado a partir de Aprobada
        self._fechaEgreso = None
        self._kilometrajeEgreso = None
        self._combustibleEgreso = None
        
        print "DEBUG: Nueva orden de reparacion creada: %s"%self

    def getCodigoOrdenReparacion(self):
        return self.codigoOrdenReparacion

    def getFecha(self):
        return self.fecha

    def getChofer(self):
        return self.chofer

    def setChofer(self, chofer):
        self.chofer = chofer

    def getKilometrajeActual(self):
        return self.kilometrajeActual

    def getEquipamiento(self):
        return self.equipamiento

    def getCombustibleActual(self):
        return self.combustibleActual

    def getComisaria(self):
        return self.comisaria

    def getEstado(self):
        return self.estado

    def setEstado(self, estadoOrden):
        self.estado = estadoOrden

    def getReparaciones(self):
        '''
        @return: 
        @author: 
        '''
        return self.reparaciones

    def getReparacionesDeSeccion(self):
        '''
        @return: 
        @author: 
        '''
        pass

    def siguienteSeccion(self):
        '''
        @return: 
        @author: 
        '''
        pass

    def generarPedidoDeActuacion(self):
        '''
        Generar el pedido de actuacion para las reparaciones que la OR tiene cargadas
        es realizable si esta OR se encuentra el el estado 'En Revision', por lo cual 
        le delegamos al estado actual la realizacion de esta accion de ser posible.
        @return: True si la operacion salio exitosa. False en caso contrario 
        @author: 
        '''
        try:
            self.estado.generarPedidoDeActuacion()
            #cambiando a proximo estado:
            self.estado = EsperandoAprobacion(self)
            return True
        except AttributeError:
            print 'No se pueden generar el pedido de actuacion'
            return False

    def registrarOrdenDeReparacionPlanificada(self):
        '''
        @return: 
        @author: 
        '''
        self.estado = Planificada(self)

    '''
    TODO: este método debería estar en el EstadoOrden-->EnRevision.
    '''
    def addReparacion(self, unaReparacion):
        '''
        Para agregar una reparacion a la lista de reparaciones,
        la OR debe estar en estado 'En Revision', por lo cual le encomendamos
        al estado de la OR realizar esta tarea, si pudiese. 
        '''
        try:
            self.estado.addReparacion(unaReparacion)
        except AttributeError:
            print 'No se pueden agregar reparaciones'

    def getreparacionesPendientes(self):
        '''
        @return: 
        @author: 
        '''
        pass

    def getPlan(self):
        return self._plan

    def setPlan(self, unPlan):
        self._plan = unPlan

    def __str__(self):
        return 'Orden de Reparacion %s| Estado: %s' %(self.codigoOrdenReparacion, self.getEstado())

    def setPedidoDeActuacion(self, pedidoDeActuacion):
        self._pedidoDeActuacion = pedidoDeActuacion

    def getPedidoDeActuacionActual(self):
        try:
            return self.estado.getPedidoDeActuacion(self)
        except AttributeError:
            pass

    def getPedidoDeActuacion(self):
        return self._pedidoDeActuacion

    def registrarRecepcionPedidoActuacion(self, fechaRecepcion):
        '''
        Para registrar la recepcion de un pedido de actuacion referido a una OR,
        la OR debe estar en estado 'EsperandoAprobacion', por lo cual le encomendamos
        al estado de la OR realizar esta tarea, si pudiese.
        @return: True si la operacion fue exitosa. False en caso contrario.

        Es una operacion que hace cambiar el estado de la OR!
        '''
        try:
            self.estado.registrarRecepcionPedidoActuacion(fechaRecepcion)
            self.estado = Aprobada(self)
            return True
        except AttributeError:
            return False
 
    def noEstaFinalizada(self):
        return self.getEstado().noEstoyFinalizada()

    def agregarTurnoAlPlan(self, turno):
        '''
        Para agregar un turno al plan de una OR,
        la OR debe estar en estado 'Aprobada', por lo cual le encomendamos
        al estado de la OR realizar esta tarea, si pudiese.
        @return: True si la operacion fue exitosa. False en caso contrario. 
        '''
        try: 
            self.estado.agregarTurnoAlPlan(turno)
            return True
        except AttributeError:
            return False

    def planificacionFinalizada(self):
        '''
        Para finalizar la planificacion de las reparaciones de una OR,
        la OR debe estar en estado 'Aprobada'.
        @return: True si la operacion fue exitosa. False en caso contrario. 
        '''       
        if isinstance(self.estado, Aprobada):
            #self.estado = Planificada(self, self.estado.plan)
            self.estado = Planificada(self)
            transaction.commit()
            from Division_Transporte import Division_Transporte
            self.getPlan().setCodigo(Division_Transporte().getGestorDeCodigos().nextCodigoPlan())
            return True
        else:
            return False

    def getTurnosSinAtender(self):
        '''
        Para devolver los turnos que todavia no han sido atendidos de una OR,
        la OR debe estar en estado 'Planificada', por lo cual le encomendamos
        al estado de la OR realizar esta tarea, si pudiese.
        @return: None en caso fallido. 
        '''
        try: 
            return self.estado.turnosSinAtender()
        except AttributeError:
            return None

    def estaAprobada(self):
        return isinstance(self.estado, Aprobada)

    def estaEsperandoAprobacion(self):
        return isinstance(self.estado, EsperandoAprobacion)

    def getReparacionesClasificadas(self):
        '''
        Retorna un diccionario del siguiente tipo:
        return {'Seccion1': [Reparacion1_S1,Reparacion2_S1,...,ReparacionN_S1],
                ...,
                'SeccionN': [Reparacion1_SN,Reparacion2_SN,...,ReparacionN_SN]
                }
        '''
        from Division_Transporte import Division_Transporte
        reparaciones_por_seccion = {}
#        for reparacion in self.reparaciones:
        for reparacion in self.getReparacionesSinPlanificar():
            for seccion in Division_Transporte().getSecciones().values():
                if seccion.realiza(reparacion):
                    if not reparaciones_por_seccion.has_key(seccion.getNombre()):
                        reparaciones_por_seccion.update({seccion.getNombre():[]})
                    reparaciones_por_seccion[seccion.getNombre()].append(reparacion)
                    break#Analizar la siguiente reparacion

        return reparaciones_por_seccion

    def estaFinalizada(self):
        return isinstance(self.estado, Finalizada)

    def estaPlanificada(self):
        return isinstance(self.estado, Planificada)

    def getReparacionesSinPlanificar(self):
        return filter(lambda rep: not rep.estaPlanificada(), self.reparaciones)

    def getReparacionesPlanificadas(self):
        return filter(lambda rep: rep.estaPlanificada(), self.reparaciones)

    def getSeccionesDeLasReparaciones(self):
        ''''
        Retorna las secciones por las que debe pasar el vehiculo para 
        realizar sus reparaciones
        '''
        from Division_Transporte import Division_Transporte
        secciones = []
#        for reparacion in self.reparaciones:
        for reparacion in self.getReparacionesSinPlanificar():
            for seccion in Division_Transporte().getSecciones().values():
                if seccion.realiza(reparacion):
                    if not seccion in secciones:
                        secciones.append(seccion)

        return secciones

    def tieneTodosLosTurnosFinalizados(self):
        '''
        Lo sabe el estado Planificada
        '''
        try:
            return self.estado.tieneTodosLosTurnosFinalizados()
        except AttributeError:
            return False

    def finalizarVerificacionReparacion(self):
        '''
        Lo sabe el estado Planificada
        '''
        try:
            self.estado.finalizarVerificacionReparacion()
        except AttributeError:
            return False

    def puedeEgresar(self):
        '''
        Lo sabe el estado Finalizada
        '''
        try:
            #si la orden de reparacion esta finalizada pero en curso, retornara True
            #si la orden de reparacion es una del historial de ordenes, retornara False
            return self.estado.puedeEgresar()
        except AttributeError:
            #si no estoy en el estado, false
            return False

    def getFechaEgreso(self):
        return self._fechaEgreso

    def registrarEgreso(self, kilometraje, combustible, fecha):
        '''
        Lo sabe el estado Finalizada
        '''
        try:
            return self.estado.registrarEgreso(kilometraje, combustible, fecha)
        except AttributeError:
            #si no estoy en el estado, false
            return False

    def setFechaEgreso(self, value):
        self._fechaEgreso = value

    def setKilometrajeEgreso(self, value):
        self._kilometrajeEgreso = value

    def setCombustibleEgreso(self, value):
        self._combustibleEgreso = value

    def getTurnosOrdenados(self):
        '''
        Si la OR esta planificada, retorna lo que pidieron
        '''
        if self.estaPlanificada():
            return self.getEstado().getTurnosOrdenados()
        return None
    
    def getCodigoPlan(self):
        self.getPlan().getCodigo()