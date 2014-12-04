# -*- coding: utf-8 -*-
'''
Created on 3/12/2014

@author: LeoMorales
'''

from persistent import Persistent
import transaction


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
        self._codigosTiposDeRepuestos = 80000
        self._codigosTiposDeReparaciones = 90000
        
        
        
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
