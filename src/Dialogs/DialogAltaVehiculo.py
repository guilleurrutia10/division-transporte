# -*- coding: utf-8 -*-
'''
Created on 10/11/2012

@author: urrutia, morales
'''
from PyQt4 import QtGui, QtCore
from re import match

from formularios.DialogAltaVehiculoPrueba import Ui_DialogAltaVehiculo

from negocio.Division_Transporte import Division_Transporte
from negocio.excepciones.ExcepcionObjetoExiste import ExcepcionVehiculoExiste
from Utiles_Dialogo import Mensaje


class DialogAltaVehiculo(QtGui.QDialog, Ui_DialogAltaVehiculo):
    '''
        Elementos:
            lineEditDominio
            lineEditMarca
            lineEditModelo
            lineEditRegistroInterno
            lineEditChasisNro
            pushButtonAceptar
            pushButtonCancelar
    '''

    def __init__(self, parent=None):
        '''
        '''
        super(DialogAltaVehiculo, self).__init__(parent)
        self.setupUi(self)
        self.validacionesLineEdit()
        self.DIVISION = Division_Transporte()
        # seteo de nombres de los Labels para el estilo
        self.label.setObjectName("label")
        self.label_2.setObjectName("label")
        self.label_3.setObjectName("label")
        self.label_4.setObjectName("label")
        self.label_5.setObjectName("label")
        # El único diálogo para mostrar alertas
        self._mensaje = Mensaje(self)
        self._mensaje.setTitle('Alta Vehículo')

    def validacionesLineEdit(self):
        '''
        Se cargan las expresiones regulares para validar
        la entrada de los diferentes lineEdits del diálogo.
        '''
        dominioRegExp = QtCore.QRegExp('[A-Z|a-z]{3}[0-9]{3}')
        validadorRegExp = QtGui.QRegExpValidator(dominioRegExp, self)
        self.lineEditDominio.setValidator(validadorRegExp)
        marcaRegExp = QtCore.QRegExp('[A-Z|a-z]+')
        validadorRegExp = QtGui.QRegExpValidator(marcaRegExp, self)
        self.lineEditMarca.setValidator(validadorRegExp)
        registroInternoRegExp = QtCore.QRegExp('[0-9]+')
        validadorRegExp = QtGui.QRegExpValidator(registroInternoRegExp, self)
        self.lineEditRegistroInterno.setValidator(validadorRegExp)
        numChasisRegExp = QtCore.QRegExp('[0-9]+')
        validadorRegExp = QtGui.QRegExpValidator(numChasisRegExp, self)
        self.lineEditChasisNro.setValidator(validadorRegExp)

    @QtCore.pyqtSlot()
    def on_pushButton_Cancelar_pressed(self):
        '''
        '''
        self.reject()

    @QtCore.pyqtSlot('QString')
    def on_lineEditDominio_textChanged(self, cadena):
        '''
        Al ingresar algún caracter en el lineEditDominio se lo
        convierte a mayúscula.
        '''
        mayusculas = cadena.toUpper()
        self.lineEditDominio.setText(mayusculas)

    @QtCore.pyqtSlot()
    def on_pushButton_2Aceptar_pressed(self):
        '''
        Acciones que se deben llevar a cabo al presionar el botón aceptar.
        Validar los lineEdit, y más....
        '''
#         try:
#             assert self.testearDialogo() is True
#         except AssertionError:
#             return
#         self.cargarVehiculo()
#         if self.mostrarMensaje('El vehiculo se ha ingresado correctamente!!! :)', 'Ingresando Vehiculo'):
#             self.accept()
        if not self.testearDialogo():
            self._mensaje.exec_()
            return
        else:
            if self.cargarVehiculo():
                self._mensaje.setMensaje('El vehiculo se ha cargado correctamente')
                self._mensaje.setInformative()
                self.accept()
                # Si se presionó Ok...
#                 if self._mensaje.exec_() == self._mensaje.messageBox.Ok:
#                     self.accept()
            else:
#                 self._mensaje.exec_()
                print 'No se pudo cargar......'
        self._mensaje.exec_()

    def testearDialogo(self):
        '''
        TODO: Cambiar el nombre si no es significativo.
        '''
        self._mensaje.setWarning()
        if not match('([A-Z|a-z]{3})([0-9]{3})', self.lineEditDominio.text()):
            self._mensaje.setMensaje('Debe ingresar el dominio del vehículo. Debe ser alfanumérico.')
#             self.mostrarMensaje('Debe ingresar el dominio del vehículo. Debe ser alfanumérico.', 'Ingresar Dominio')
            self.lineEditDominio.clear()
            self.lineEditDominio.setFocus()
            return
        if not match('[a-z|A-Z]+', self.lineEditMarca.text()):
            self._mensaje.setMensaje('Debe ingresar la Marca del vehículo.Debe ser alfabético.')
#             self.mostrarMensaje('Debe ingresar la Marca del vehículo.Debe ser alfabético.', 'Ingresar Marca')
            self.lineEditMarca.clear()
            self.lineEditMarca.setFocus()
            return
        if not match('[0-9]+', self.lineEditRegistroInterno.text()):
            self._mensaje.setMensaje('Debe ingresar el Registro Interno del vehículo.Debe ser numérico.')
#             self.mostrarMensaje('Debe ingresar el Registro Interno del vehículo.Debe ser numérico.', 'Ingresar Registro Interno')
            self.lineEditRegistroInterno.clear()
            self.lineEditRegistroInterno.setFocus()
            return
        if not match('[0-9]+', self.lineEditChasisNro.text()):
            self._mensaje.setMensaje('Debe ingresar el Número de Chasis del vehículo.Debe ser numérico.')
#             self.mostrarMensaje('Debe ingresar el Número de Chasis del vehículo.Debe ser numérico.', 'Ingresar Número de Chasis')
            self.lineEditChasisNro.clear()
            self.lineEditChasisNro.setFocus()
            return
        return True

    def cargarVehiculo(self):
        dominio = unicode(self.lineEditDominio.text())
        marca = unicode(self.lineEditMarca.text())
        registroInterno = unicode(self.lineEditRegistroInterno.text())
        numeroChasis = unicode(self.lineEditChasisNro.text())
        modelo = unicode(self.lineEditModelo.text())
        # Se carga el Vehículo en el sistema.
        # TODO: [ok] falta mandar el modelo del vehículo.
        try:
            self.DIVISION.agregarVehiculo(dominio, marca, registroInterno, numeroChasis, modelo)
        except ExcepcionVehiculoExiste, e:
            self._mensaje.setCritical()
            mensaje = e.__str__()
#             mensaje = 'El vehiculo con el dominio %s ya se encuentra cargado en el sistema' % (dominio)
            self._mensaje.setMensaje(mensaje)
            self.lineEditDominio.setFocus()
            return False
        return True
#             self.mostrarMensaje(
#                                  mensaje='El vehiculo con el dominio %s ya se encuentra cargado en el sitema' % (dominio),
#                                  titulo='Error Alta Vehículo')
