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
#        self.estadoOrden = EstadoOrdenReparacion(), self.estadoOrden =  EnRevision()
        self.codigoOrdenReparacion = codigoOrdenReparacion
        self.estadoOrden = EnRevision(self)
        self.reparaciones = {}
        self._plan = None
        
        self.kilometrajeActual = kilometrajeActual
        self.combustibleActual = combustibleActual
        self.equipamiento = equipamiento
        self.reparacion = reparacion
        self.comisaria = comisaria
        self.localidad = localidad
        self.fecha = fecha
    
    def getEstadoOrdenReparacion(self):
        return self.estadoOrden
    
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
    
    def getPedidoDeActuacion(self):
        '''
        @return: 
        @author: 
        '''
        self.estadoOrden.getPedidoActuacion()
    
    def generarPedidoDeActuacion(self):
        '''
        @return: 
        @author: 
        '''
        self.estadoOrden = EsperandoAprobacion()
        self.estadoOrdengenerarPedidoDeActuacion()
    
    def registrarOrdenDeReparacionPlanificada(self):
        '''
        @return: 
        @author: 
        '''
        self.estadoOrden = Planificada()
    
    '''
    TODO: este método debería estar en el EstadoOrden-->EnRevision.
    '''
    def addReparacion(self):
        '''
        @return: 
        @author: 
        '''
        self.estadoOrden.addReparacion()
    
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