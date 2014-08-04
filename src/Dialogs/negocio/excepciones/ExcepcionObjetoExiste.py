# -*- coding: utf-8 -*-
'''
Created on 12/11/2012

@author: urrutia
'''


class ExcepcionObjetoExiste(Exception):

    def __init__(self, key):
        self.key = key

    def __str__(self):
        return 'El objeto con la clave %s se encuentra cargado en la base.' % self.key


class ExcepcionObjeNoExiste(Exception):

    def __init__(self, key):
        self.key = key

    def __str__(self):
        return 'El objeto con la clave %s no se encuentra cargado en la base.' % self.key


class ExcepcionVehiculoExiste(Exception):
    """Classdocs.
    """
    def __init__(self, dominio):
        self.dominio = dominio

    def __str__(self):
        return u'El Vehículo con el dominio %s se encuentra cargado.' % self.dominio


class ExcepcionEmpleadoExiste(Exception):
    """Classdocs.
    """
    def __init__(self, dominio):
        self.dominio = dominio

    def __str__(self):
        return u'El Empleado con Tipo de Documento %s y número %s ya se encuentra cargado.' % (self.tipoDocumento, self.dominio)

    def setTipoDocumento(self, tipoDocumento):
        self.tipoDocumento = tipoDocumento
