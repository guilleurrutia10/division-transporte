# -*- coding: utf-8 -*-
'''
Created on 3/12/2014

@author: LeoMorales
'''

from persistent import Persistent

class GestorDeCodigos(Persistent):
    '''
    Clase que se encarga de gestionar la numeracion de los codigos de los objetos de la Division
    '''

    def __init__(self):
        '''
        Constructor
        :version:
        :author:
        '''
        self._codigosSecciones = 10000
        self._codigosOrdenesDeReparacion = 20000
        self._codigosPlanes = 30000
        self._codigosEmpleados = 40000
        self._codigosVehiculos = 50000
        self._codigosTiposDeReparaciones = 60000
        self._codigosReparaciones = 70000
        self._codigosTiposDeRepuestos = 80000
        self._codigosTurnos = 90000
        self._codigosPedidosDeActuacion = 10000
        
        
        
    def nextCodigoSeccion(self):
        '''
        Retorna un string con el prox codigo de seccion disponible
        '''
        self._codigosSecciones +=1
        return 'SEC-%d'%self._codigosSecciones

    def nextCodigoOrdenDeReparacion(self):
        '''
        Retorna un string con el prox codigo de OR disponible
        '''
        self._codigosOrdenesDeReparacion +=1
        return 'ORDREP-%d'%self._codigosOrdenesDeReparacion

    def nextCodigoTipoDeReparacion(self):
        '''
        Retorna un string con el prox codigo de tipo de reparacion disponible
        '''
        self._codigosTiposDeReparaciones +=1
        return 'TIPOREPARACION-%d'%self._codigosTiposDeReparaciones

    def nextCodigoTipoDeRepuesto(self):
        '''
        Retorna un string con el prox codigo de tipo de repuesto disponible
        '''
        self._codigosTiposDeRepuestos +=1
        return 'TIPOREPUESTO-%d'%self._codigosTiposDeRepuestos

    def nextCodigoTurno(self):
        '''
        Retorna un string con el prox codigo de turno disponible
        '''
        self._codigosTurnos +=1
        return 'TURNO-%d'%self._codigosTurnos

    def nextCodigoPlan(self):
        '''
        Retorna un string con el prox codigo de plan disponible
        '''
        self._codigosPlanes +=1
        return 'PLAN-%d'%self._codigosPlanes

    def nextCodigoReparacion(self):
        '''
        Retorna un string con el prox codigo de reparacion disponible
        La repracion posee como atributo un Tipo de Reparacion
        '''
        self._codigosReparaciones +=1
        return 'REP-%d'%self._codigosReparaciones

    def nextCodigoPedidoDeActuacion(self):
        '''
        Retorna un string con el prox codigo de pedido de actuacion disponible
        '''
        self._codigosPedidosDeActuacion +=1
        return 'PEDIDO-%d'%self._codigosPedidosDeActuacion
