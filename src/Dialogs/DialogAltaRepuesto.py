# -*- coding: utf-8 -*-
'''
Created on 03/10/2012

@author: Usuario
'''
from PyQt4 import QtCore, QtGui

from re import match

from formularios.DialogAltaRepuesto import Ui_DialogAltaRepuesto


class DialogAltaRepuesto(QtGui.QDialog, Ui_DialogAltaRepuesto):
    '''
    classdocs
    '''
    def __init__(self, parent = None):
        '''
        Constructor
        '''
        super(DialogAltaRepuesto, self).__init__(parent)
        self.setupUi(self)
        self.validacionesLineEdit()        
    
    def validacionesLineEdit(self):
        #Validación a medida que se escribe en el lineEdit        
        self.lineEditDescRepuesto.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[A-Za-z]+'),self))
        self.lineEditNombreRepuesto.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[A-Za-z]+'),self))
        
    @QtCore.pyqtSlot('QString')
    def on_lineEditNombreRepuesto_textEdited(self, cadena):
        print 'El texto cambio................... %s' %cadena
    
    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        self.close()
        
    def mostrarMensaje(self, mensaje):
        '''
        '''
        msgBox = QtGui.QMessageBox(self)
        msgBox.setText(QtCore.QString.fromUtf8(mensaje))
        msgBox.show()
    
    @QtCore.pyqtSlot()
    def on_pushButtonAceptar_clicked(self):
        print 'Click sobre Aceptar'
        try:
            assert self.testearDialogo() is True
        except AssertionError:
            return
        msgBox = QtGui.QMessageBox(self)
        msgBox.setWindowTitle(QtCore.QString.fromUtf8('Ingresando Vehiculo'))
        msgBox.setText(QtCore.QString.fromUtf8('El repuesto se ha ingresado correctamente!!! :)'))
        if msgBox.exec_():
            self.accept()
            
    def testearDialogo(self):
        '''
            @todo: Cambiar el nombre si no es significativo.
        '''
        if not match('[A-Za-z]+', self.lineEditNombreRepuesto.text()):
            self.mostrarMensaje('Debe ingresar el nombre del repuesto.')
            self.lineEditNombreRepuesto.clear()
            self.lineEditNombreRepuesto.setFocus()
            return
        if not match('[A-Za-z]+', self.lineEditDescRepuesto.text()):
            self.mostrarMensaje('Debe ingresar la descripcion del repuesto.')
            self.lineEditDescRepuesto.clear()
            self.lineEditDescRepuesto.setFocus()
            return
        return True