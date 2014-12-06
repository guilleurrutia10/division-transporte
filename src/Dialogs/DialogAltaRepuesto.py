# -*- coding: utf-8 -*-
'''
Created on 03/10/2012

@author: Usuario
'''
from PyQt4 import QtCore, QtGui

from formularios.DialogAltaRepuesto import Ui_DialogAltaRepuesto
from AyudaManejador import AyudaManejador
from negocio.Division_Transporte import Division_Transporte


class DialogAltaRepuesto(QtGui.QDialog, Ui_DialogAltaRepuesto, AyudaManejador):
    '''
    classdocs
    '''
    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super(DialogAltaRepuesto, self).__init__(parent)
        self.setupUi(self)
        self.validacionesLineEdit()
#         labels = self.findChildren(QtGui.QLabel)
        for label in self.findChildren(QtGui.QLabel):
            label.setObjectName('label')

    def validacionesLineEdit(self):
        #Validación a medida que se escribe en el lineEdit        
        self.lineEditDescRepuesto.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[A-Za-z\s]+'),self))
        self.lineEditNombreRepuesto.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[A-Za-z\s]+'),self))

    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        self.reject()

    '''
    TODO: Se ha repetido este mismo método en varias de las clsase Dialogos.
    '''
    def mostrarMensaje(self, mensaje, titulo):
        '''
        Función que muestra un pequeña ventana con información relevante.
        '''
        msgBox = QtGui.QMessageBox(self)
        msgBox.setText(QtCore.QString.fromUtf8(mensaje))
        msgBox.setWindowTitle(QtCore.QString.fromUtf8(titulo))
        return msgBox.exec_()

    @QtCore.pyqtSlot()
    def on_pushButtonAceptar_clicked(self):
        try:
            assert self.testearDialogo() is True
        except AssertionError:
            return
        self.cargarRepuesto()
        if self.mostrarMensaje('El repuesto se ha ingresado correctamente!!! :)', 'Ingresando Vehiculo'):
            self.accept()

    def testearDialogo(self):
        '''
        TODO: Cambiar el nombre si no es significativo.
        '''
        if len(self.lineEditNombreRepuesto.text()) is 0:
            self.mostrarMensaje('Debe ingresar el nombre del repuesto.', 'Ingresar Nombre')
            self.lineEditNombreRepuesto.clear()
            self.lineEditNombreRepuesto.setFocus()
            return
        if len(self.lineEditDescRepuesto.text()) is 0:
            self.mostrarMensaje('Debe ingresar la descripcion del repuesto.', 'Ingresar Descripción')
            self.lineEditDescRepuesto.clear()
            self.lineEditDescRepuesto.setFocus()
            return
        return True

    def cargarRepuesto(self):
        '''
        TODO: Deberíamos atrapar una Excepción que nos lance la División_Transporte.
        '''
        nombre = unicode(self.lineEditNombreRepuesto.text())
        descripcion = unicode(self.lineEditDescRepuesto.text())
        division = Division_Transporte()
        division.agregarRepuestos(nombre, descripcion)
