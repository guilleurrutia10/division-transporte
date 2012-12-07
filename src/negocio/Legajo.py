# -*- coding: utf-8 -*-
'''
Created on 28/10/2012

@author: urrutia
'''

from persistent import Persistent

from Localidad import *
from OrdenReparacion import *

from excepciones.ExcepcionPoseeOrdenReparacionEnCurso import ExcepcionPoseeOrdenReparacionEnCurso 

class Legajo(Persistent):
    '''
    classdocs
    @version: 
    @author: 
    '''
    
    ''' ATTRIBUTES

   

      dominio  (private)
    
       
    
      modelo  (private)
    
       
    
      marca  (private)
    
       
    
      registroInterno  (private)
    
       
    
      numeroChasis  (private)
      
      ordenesReparacion

    '''
    
    def __init__(self, dominio, marca, registroInterno, numeroChasis, comisaria=''):
        '''
        Constructor
        @return: 
        @author: 
        '''
        #def __init__(self, dominio, marca, registroInterno, numeroChasis, modelo = 'Corsa'):
        #self.modelo = modelo
        self.dominio = dominio
        self.marca = marca
        self.registroInterno = registroInterno
        self.numeroChasis = numeroChasis
        self.comisaria = comisaria
        # Tener en consideraón luego.
        self.localidad = ''
        self.ordenesDeReparacion = []
        self.numeroOrden = 0
    
    def datosLegajo(self):
        '''
        @return: 
        @author: 
        '''
        # Probar devolviendo vars(Legajo)
        return [self.dominio, self.marca, self.registroInterno, self.numeroChasis, self.comisaria, self.localidad, self.ordenesDeReparacion]
    
    def noEstaFinalizada(self, ordenReparacion):
        return ordenReparacion.getEstadoOrdenReparacion() != 'Finalizada'
    
    def obtenerOrdenDeReparacionEnCurso(self):
        '''
        @return: 
        @author: 
        '''
        ordenEnCurso = filter(lambda unaOrden: unaOrden.getEstado() != 'Finalizada', self.ordenesDeReparacion)
#        ordenEnCurso = filter(self.noEstaFinalizada, self.ordenesDeReparacion)
        try:
            ordenEnCurso[0]
            raise ExcepcionPoseeOrdenReparacionEnCurso('El vehículo ya posee una orden de Reparación en Curso.')
        except IndexError:
            return None
    
    def dameOrdenDeReparacionEnCurso(self):
        '''
        @return: 
        @author: 
        '''
        ordenEnCurso = filter(lambda unaOrden: unaOrden.getEstado() != 'Finalizada', self.ordenesDeReparacion)
#        ordenEnCurso = filter(self.noEstaFinalizada, self.ordenesDeReparacion)
        try:
            return ordenEnCurso[0]
        except IndexError:
            from excepciones.Excepcion_No_Posee_Orden_Reparacion_En_Curso import Excepcion_No_Posee_Orden_Reparacion_En_Curso
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
            from excepciones.Excepcion_Orden_No_Esta_En_Revision import Excepcion_Orden_No_Esta_En_Revision
            raise Excepcion_Orden_No_Esta_En_Revision('La Orden de Reparacion del vehiculo no se encuentra en revision')
        
    def crearOrdenDeReparacion(self, kilometrajeActual, combustibleActual, equipamiento, reparacion, comisaria, localidad, fecha):
        '''
        @return: 
        @author: 
        '''
        # Antes de crear la orden, obtener orden en curso, si no existe(no tiene) crearla.
        try:
            self.obtenerOrdenDeReparacionEnCurso()
            ordenReparacion = OrdenReparacion(self.dameNumeroOrden(), kilometrajeActual, combustibleActual, equipamiento, reparacion, comisaria, localidad, fecha)
            self.ordenesDeReparacion.append(ordenReparacion)
        except ExcepcionPoseeOrdenReparacionEnCurso, e:
            raise ExcepcionPoseeOrdenReparacionEnCurso(e.getMensaje())
#        ordenReparacion.addReparacion()
#        self.ordenesDeReparacion[1] = ordenReparacion
#        self.ordenesDeReparacion.append(ordenReparacion)
#        print ordenReparacion.codigoOrdenReparacion
    
    def save(self):
        from MiZODB import ZopeDB, MiZODB
        zodb = ZopeDB(MiZODB())
#        zodb = ZopeDB(MiZODB('zeo.conf'))
        zodb.save('vehiculos', self.dominio, self)
    
    def dameNumeroOrden(self):
        self.numeroOrden += 1
        return self.numeroOrden
    
    def __eq__(self, otro):
        return (self.dominio == otro.dominio)
    
    def __str__(self):
        return 'Dominio: %s' % self.dominio
        return 'Dominio: %s' % self.dominio
    
    def getDominio(self):
        return self.dominio
    
    def getPedidoActuacionSinFechaRecepcion(self):
        ordenEnCurso = self.dameOrdenDeReparacionEnCurso()
        return ordenEnCurso.getPedidoDeActuacionActual()
