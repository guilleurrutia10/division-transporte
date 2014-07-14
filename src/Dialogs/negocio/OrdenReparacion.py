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
#from negocio.Aproba import Aprobada
from Aprobada import Aprobada
from Plan import Plan

class OrdenReparacion(Persistent):
#class OrdenReparacion(object):
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
            
    def getCodigoOrdenReparacion(self):
        return self.codigoOrdenReparacion
    
    def getFecha(self):
        return self.fecha
    
    def getChofer(self):
        return self.chofer
    
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
        return 'Orden de Reparacion | Estado: %s' %self.getEstado()
    
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
        
    