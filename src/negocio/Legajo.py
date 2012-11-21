# -*- coding: utf-8 -*-
'''
Created on 28/10/2012

@author: urrutia
'''

from persistent import Persistent

from Localidad import *
from OrdenReparacion import *

class Legajo(Persistent):
    '''
    classdocs
    @version: 
    @author: 
    '''


    def __init__(self, dominio, marca, registroInterno, numeroChasis, comisaria=''):
        '''
        Constructor
        @return: 
        @author: 
        '''
        self.dominio = dominio
        self.marca = marca
        self.registroInterno = registroInterno
        self.numeroChasis = numeroChasis
        self.comisaria = comisaria
        # Tener en consideraón luego.
        self.localidad = ''
        self.ordenesDeReparacion = {}
    
    """ ATTRIBUTES

   

      dominio  (private)
    
       
    
      modelo  (private)
    
       
    
      marca  (private)
    
       
    
      registroInterno  (private)
    
       
    
      numeroChasis  (private)

    """
    
    def datosLegajo(self):
        '''
        @return: 
        @author: 
        '''
        # Probar devolviendo vars(Legajo)
        return [self.dominio, self.marca, self.registroInterno, self.numeroChasis, self.comisaria, self.localidad, self.ordenesDeReparacion]
    
    def obtenerOrdenDeReparacionEnCurso(self):
        '''
        @return: 
        @author: 
        '''
        pass
    
    def crearOrdenDeReparacion(self):
        '''
        @return: 
        @author: 
        '''
        pass
    
    def save(self):
        from MiZODB import ZopeDB, MiZODB
        zodb = ZopeDB(MiZODB('zeo.conf'))
        zodb.save('vehiculos',self.dominio,self)
        
    def __eq__(self, otro):
        return (self.dominio == otro.dominio)