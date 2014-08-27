# -*- coding: utf-8 -*-
'''
Created on 28/10/2012

@author: urrutia
'''

from persistent import Persistent
import transaction


class Empleado(Persistent):
    '''
    classdocs
    :version:
    :author:
    ATTRIBUTES

        numeroDocumento  (private)

        nombre  (private)

        apellido  (private)

        fechaNacimiento  (private)

        fechaAlta  (private)

        fechaBaja  (private)

        email  (private)

        telefono_  (private)

        domicilio  (private)


    '''

    def __init__(self, nombre, apellido, documento, tipoDocumento, fechaNacimiento=None, domicilio=None, telefono=None, email=None, localidad=None):
        '''
        Constructor
        :version:
        :author:
        '''
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.tipoDocumento = tipoDocumento
        self.password = ''
        self.fechaNacimiento = fechaNacimiento
        self.domicilio = domicilio
        self.telefono = telefono
        self.email = email
        self.localidad = localidad
        # Se setea si el usuario termina siendo encargado...
        self._usuario = None

    def __eq__(self, otro):
        return self.documento == otro.documento

    def nombreCompleto(self):
        return '%s %s' % (self.nombre, self.apellido)

    def nombreCompletoUsr(self):
        return '%s%s' % (self.apellido, self.nombre)

    def setPassword(self, unaPass):
        self.password = unaPass

    def getPassword(self):
        return self.password

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getApellido(self):
        return self.apellido

    def setApellido(self, apellido):
        self.apellido = apellido

    def getDocumento(self):
        return self.documento

    def setDocumento(self, documento):
        self.documento = documento

    def getTipoDocumento(self):
        return self.tipoDocumento

    def getFechaNacimiento(self):
        return self.fechaNacimiento

    def getDomicilio(self):
        return self.domicilio

    def getTelefono(self):
        return self.telefono

    def getEmail(self):
        return self.email

    def getLocalidad(self):
        return self.localidad

    def tieneReparacionesPendientes(self):
        # TODO: Implementar!
        return False

    def quienSos(self):
        return 'Soy %s %s, %s nro: %s' % (self.getNombre(), self.getApellido(), self.getTipoDocumento(), self.getDocumento())

    def __cmp__(self, other):
        if self.documento == other.documento:
            return 0
        elif self.documento > other.documento:
            return 1
        else:
            return -1

    def setUsuario(self, usr):
        self._usuario = usr
        transaction.commit()

    def getUsuario(self):
        try:
            return self._usuario
        except AttributeError:
            return None

    def comparar(self, other):
        return self.documento == other.documento and self.tipoDocumento == other.tipoDocumento

    def imprimirFechaNacimiento(self):
        return '%s/%s/%s' % (self.getFechaNacimiento().day, self.getFechaNacimiento().month, self.getFechaNacimiento().year)
