# -*- coding: utf-8 -*-
'''
Created on 28/10/2012

@author: urrutia
'''

from persistent import Persistent

from EstadoOrdenReparacion import *
#from PedidoDeActuacion import *
from Reparacion import *

class OrdenReparacion(object):
    '''
    classdocs
    @version: 
    @author: 
    '''
    
    """ ATTRIBUTES
    
    
    
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
    
    """
  

    def __init__(self):
        '''
        Constructor
        @return: 
        @author: 
        '''
        pass
    
    def getReparaciones(self):
        '''
        @return: 
        @author: 
        '''
        pass
    
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
        pass
    
    def generarPedidoDeActuacion(self):
        '''
        @return: 
        @author: 
        '''
        pass
    
    def registrarOrdenDeReparacionPlanificada(self):
        '''
        @return: 
        @author: 
        '''
        pass
    
    def addReparacion(self):
        '''
        @return: 
        @author: 
        '''
        pass
    
    def getreparacionesPendientes(self):
        '''
        @return: 
        @author: 
        '''
        pass