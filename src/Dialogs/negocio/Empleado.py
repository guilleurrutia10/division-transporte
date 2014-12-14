# -*- coding: utf-8 -*-
'''
Created on 28/10/2012

@author: urrutia
'''

from persistent import Persistent
import transaction
from datetime import date

class Empleado(Persistent):
    '''
    classdocs
    :version:
    :author:
    ATTRIBUTES

        numeroDocumento  (private)
        Documento  (private) -- documento del empleado. Tipo TipoDocumento.

        nombre  (private) -- nombre del empleado. Tipo string unicode

        apellido  (private) -- apellido del empleado. Tipo string unicode

        fechaNacimiento  (private) -- . Tipo datetime.date

        fechaAlta  (private) -- . Tipo datetime.date

        fechaBaja  (private) -- . Tipo datetime.date

        email  (private) -- dirección de correo eléctrónico del empleado.
                            Tipo string unicode

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
        #Para saber si pueden se transferidos/borrados, el siguiente atributo:
        self._reparaciones_asignadas = 0
        self._reparaciones_pendientes = 0
        self._fechaAlta = date.today()
        print "DEBUG: Nuevo empleado: %s | %s: %s"%(self.nombreCompleto(),
                                                    self.tipoDocumento,
                                                    self.documento
                                                    ) 
        self._fechaBaja = '-'
        
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
        # TODO: Implementar! [OK]
        return self._reparaciones_pendientes > 0

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
        '''
        Setea un usr al empleado. Sirve para transformar al empleado en un encargado
        @postcondition: Esta accion hace un commit en la base de datos.
        '''
        #Division_Transporte().borraUsuario(self)
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

    def desregistrarUsuario(self):
        '''
        Borra el usuario del empleado. 
        @postcondition: Esta accion hace un commit en la base de datos.
        '''
        #Division_Transporte.Division_Transporte().borraUsuario(self)
        self._usuario = None
        transaction.commit()

    def getFechaAlta(self):
        '''
        Devuelve la fecha de alta en la División del empleado.
        @return: Tipo datetime.date
        '''
        return self.fechaAlta

    def setFechaAlta(self, fecha):
        '''
        Establece la fecha de alta del empleado en la División.
        fecha: Tipo datetime.date
        '''
        self.fechaAlta = fecha

    def imprimirFechaAlta(self):
        '''
        Devuelve un string de la fecha de alta del empleado.
        @return: string
        '''
        return self.fechaAlta.ctime()

    def getFechaBaja(self):
        '''
        Devuelve la fecha de baja en la División del empleado.
        @return: Tipo datetime.date
        '''
        return self._fechaBaja

    def setFechaBaja(self, fecha):
        '''
        Establece la fecha de baja del empleado en la División.
        fecha: Tipo datetime.date
        '''
        self._fechaBaja = fecha

    
    def imprimirFechaBaja(self):
        '''
        Devuelve un string de la fecha de baja del empleado.
        @return: string
        '''
        return self.fechaBaja.ctime()

    def incrementarReparacionesAsignadas(self, cantidadDeReparaciones):
        self._reparaciones_pendientes += cantidadDeReparaciones
        self._reparaciones_asignadas += cantidadDeReparaciones
        
    def reparaciones_asignadas(self):
        return self._reparaciones_asignadas
    
    def reparaciones_pendientes(self):
        return self._reparaciones_pendientes
    
    def decrementarReparacionesPendientes(self):
        self._reparaciones_pendientes -= 1
   
    def set_tipo_documento(self, value):
        self.tipoDocumento = value

    def set_fecha_nacimiento(self, value):
        self.fechaNacimiento = value

    def set_domicilio(self, value):
        self.domicilio = value

    def set_telefono(self, value):
        self.telefono = value

    def set_email(self, value):
        self.email = value

