# -*- coding: utf-8 -*-
'''
Created on 10/11/2012

@author: urrutia
'''
from PyQt4 import QtGui, QtCore
from re import match

from formularios.DialogAltaVehiculoPrueba import Ui_DialogAltaVehiculo

from negocio.Division_Transporte import Division_Transporte
from negocio.excepciones.ExcepcionObjetoExiste import ExcepcionObjetoExiste


class DialogAltaVehiculo(QtGui.QDialog, Ui_DialogAltaVehiculo):
    '''
        Classdocs
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

    def validacionesLineEdit(self):
        '''
        '''
        self.lineEditDominio.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[A-Z|a-z]{3}[0-9]{3}'),self))
        self.lineEditMarca.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[A-Z|a-z]+'),self))
        self.lineEditRegistroInterno.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[0-9]+'),self))
        self.lineEditChasisNro.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[0-9]+'),self))

    @QtCore.pyqtSlot()
    def on_pushButton_Cancelar_pressed(self):
        '''
        '''
        self.reject()

    @QtCore.pyqtSlot()
    def on_pushButton_2Aceptar_pressed(self):
        '''
        Acciones que se deben llevar a cabo al presionar el botón aceptar.
        Validar los lineEdit, y más....
        '''
        try:
            assert self.testearDialogo() is True
        except AssertionError:
            return
        self.cargarVehiculo()
        if self.mostrarMensaje('El vehiculo se ha ingresado correctamente!!! :)', 'Ingresando Vehiculo'):
            self.accept()

    def testearDialogo(self):
        '''
        TODO: Cambiar el nombre si no es significativo.
        '''
        if not match('([A-Z|a-z]{3})([0-9]{3})', self.lineEditDominio.text()):
            self.mostrarMensaje('Debe ingresar el dominio del vehículo. Debe ser alfanumérico.', 'Ingresar Dominio')
            self.lineEditDominio.clear()
            self.lineEditDominio.setFocus()
            return
        if not match('[a-z|A-Z]+', self.lineEditMarca.text()):
            self.mostrarMensaje('Debe ingresar la Marca del vehículo.Debe ser alfabético.', 'Ingresar Marca')
            self.lineEditMarca.clear()
            self.lineEditMarca.setFocus()
            return
        if not match('[0-9]+', self.lineEditRegistroInterno.text()):
            self.mostrarMensaje('Debe ingresar el Registro Interno del vehículo.Debe ser numérico.', 'Ingresar Registro Interno')
            self.lineEditRegistroInterno.clear()
            self.lineEditRegistroInterno.setFocus()
            return
        if not match('[0-9]+', self.lineEditChasisNro.text()):
            self.mostrarMensaje('Debe ingresar el Número de Chasis del vehículo.Debe ser numérico.', 'Ingresar Número de Chasis')
            self.lineEditChasisNro.clear()
            self.lineEditChasisNro.setFocus()
            return
        return True

    '''
    TODO: Este método se repite en varios Dialogs.
    '''
    def mostrarMensaje(self, mensaje, titulo):
        msgBox = QtGui.QMessageBox(self)
        msgBox.setText(QtCore.QString.fromUtf8(mensaje))
        msgBox.setWindowTitle(QtCore.QString.fromUtf8(titulo))
        return msgBox.exec_()

    def cargarVehiculo(self):
        dominio = unicode(self.lineEditDominio.text())
        marca = unicode(self.lineEditMarca.text())
        registroInterno = unicode(self.lineEditRegistroInterno.text())
        numeroChasis = unicode(self.lineEditChasisNro.text())
        modelo = unicode(self.lineEditModelo.text())
        # Se carga el Vehículo en el sistema.
        # TODO: falta mandar el modelo del vehículo.
        # Tmb, falta atrapar si ya se encuentra cargado.
        try:
            self.DIVISION.agregarVehiculo(dominio, marca, registroInterno, numeroChasis)
        except ExcepcionObjetoExiste:
            self.mostrarMensaje(
                                 mensaje='El vehiculo con el dominio %s ya se encuentra cargado en el sitema' % (dominio),
                                 titulo='Error Alta Vehículo')
        # division.addVehiculo(dominio, marca, registroInterno, numeroChasis, modelo)