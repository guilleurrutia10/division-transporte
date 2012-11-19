# -*- coding: utf-8 -*-
'''
Created on 10/11/2012

@author: urrutia
'''
from PyQt4 import QtGui, QtCore
from re import match

from formularios.DialogAltaVehiculoPrueba import Ui_DialogAltaVehiculo

class DialogAltaVehiculo(QtGui.QDialog, Ui_DialogAltaVehiculo):
    '''
        Classdocs
    '''

    def __init__(self, parent = None):
        '''
        '''
        super(DialogAltaVehiculo, self).__init__(parent)
        self.setupUi(self)
        self.validacionesLineEdit()

    def validacionesLineEdit(self):
        '''
        '''
        self.lineEditDominio.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[A-Z|a-z]{3}[0-9]{3}'),self))
        self.lineEditMarca.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[A-Z|a-z]+'),self))
        self.lineEditRegistroInterno.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[0-9]+'),self))
        self.lineEditChasisNro.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[0-9]+'),self))
        
    def mostrarMensaje(self, mensaje):
        '''
        '''
        msgBox = QtGui.QMessageBox(self)
        msgBox.setText(QtCore.QString.fromUtf8(mensaje))
        msgBox.show()
        
    @QtCore.pyqtSlot()
    def on_pushButton_Cancelar_pressed(self):
        '''
        '''
        self.close()
        
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
        dominio = unicode(self.lineEditDominio.text())
        marca = unicode(self.lineEditMarca.text())
        registroInterno = unicode(self.lineEditRegistroInterno.text())
        numeroChasis = unicode(self.lineEditChasisNro.text())
        from negocio import Division_Transporte
        division = Division_Transporte.Division_Transporte()
        division.addVehiculo(dominio, marca, registroInterno, numeroChasis)
        msgBox = QtGui.QMessageBox(self)
        msgBox.setWindowTitle(QtCore.QString.fromUtf8('Ingresando Vehiculo'))
        msgBox.setText(QtCore.QString.fromUtf8('El vehiculo se ha ingresado correctamente!!! :)'))
        if msgBox.exec_():
            self.accept()
    
    def testearDialogo(self):
        '''
            @todo: Cambiar el nombre si no es significativo.
        '''
        if not match('([A-Z|a-z]{3})([0-9]{3})', self.lineEditDominio.text()):
            self.mostrarMensaje('Debe ingresar el dominio del vehículo. Debe ser alfanumérico.')
            return
        if not match('[a-z|A-Z]+', self.lineEditMarca.text()):
            self.mostrarMensaje('Debe ingresar la Marca del vehículo.Debe ser alfabético.')
            return
        if not match('[0-9]+', self.lineEditRegistroInterno.text()):
            self.mostrarMensaje('Debe ingresar el Registro Interno del vehículo.Debe ser numérico.')
            return
        if not match('[0-9]+', self.lineEditChasisNro.text()):
            self.mostrarMensaje('Debe ingresar el Número de Chasis del vehículo.Debe ser numérico.')
            return
        return True