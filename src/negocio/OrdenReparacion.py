# -*- coding: utf-8 -*-
'''
Created on 28/10/2012

@author: urrutia
'''

from persistent import Persistent

from EstadoOrdenReparacion import *
#from PedidoDeActuacion import *
from Reparacion import *
from EnRevision import *
from EsperandoAprobacion import *
from Planificada import *

class OrdenReparacion(object):
    '''
    classdocs
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
        #La primera vez debe instanciarse como EnRevision()
#        self.estado = EstadoOrdenReparacion(), self.estado =  EnRevision()
        self.codigoOrdenReparacion = codigoOrdenReparacion
        self.estado = EnRevision()
        self.reparaciones = []
        self._plan = None
        
        self.kilometrajeActual = kilometrajeActual
        self.combustibleActual = combustibleActual
        self.equipamiento = equipamiento
        self.reparacion = reparacion
        self.comisaria = comisaria
        self.localidad = localidad
        self.fecha = fecha
        self.chofer = 'Jose Luis Barrionuevo'
        
        self._pedidoDeActuacion = None
            
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
        @return: 
        @author: 
        '''
        self.estado.generarPedidoDeActuacion(self)
        self.estado = EsperandoAprobacion()
    
    def registrarOrdenDeReparacionPlanificada(self):
        '''
        @return: 
        @author: 
        '''
        self.estado = Planificada()
    
    '''
    TODO: este método debería estar en el EstadoOrden-->EnRevision.
    '''
    def addReparacion(self, unaReparacion):
        '''
        @return: 
        @author: 
        '''
        try:
            self.estado.addReparacion(self, unaReparacion)
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
    
    def setPlan(self,unPlan):
        self._plan = unPlan
        
    def __str__(self):
        return 'En Revision'
    
    def setPedidoDeActuacion(self, pedidoDeActuacion):
        self._pedidoDeActuacion = pedidoDeActuacion
    
    def getPedidoDeActuacion(self):
        return self._pedidoDeActuacion