# -*- coding: utf-8 -*-
'''
Created on 03/10/2012

@author: Usuario
'''
from PyQt4 import QtCore, QtGui
from re import match

from formularios.DialogAltaPersonal import Ui_DialogAltaPersonal
from negocio.Division_Transporte import Division_Transporte

class DialogAltaPersonal(QtGui.QDialog, Ui_DialogAltaPersonal):
    '''
    classdocs
    '''
    def __init__(self, parent = None):
        '''
        Constructor
        '''
        super(DialogAltaPersonal, self).__init__(parent)
        self.setupUi(self)
        self.validacionesLineEdit()
        self.llenarComboBoxTipoDocumentos()
        
            
    def validacionesLineEdit(self):
        '''
        '''
        #Validación a medida que se escribe en el lineEdit
        self.lineEditNombre.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[A-Za-z|\s]+'),self))
        self.lineEditNroDocumento.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[0-9]+'),self))
        self.lineEditDomicilio.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[A-Za-z\s]+[0-9]+'),self))
        self.lineEditTelefono.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[0-9]+'),self))
        self.lineEditEmail.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('^[_a-z0-9-]+(.[_a-z0-9-]+)*@[a-z0-9-]+(.[a-z0-9-]+)*(.[a-z]{2,3})$'),self))
    
    def llenarComboBoxTipoDocumentos(self):
        '''
        '''
        dvTrans = Division_Transporte()
        for i in dvTrans.getTipoDeDocumentos():
            self.comboBoxTipoDocumento.addItems(QtCore.QStringList(i))
            
    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        '''
        '''
        self.close()
        
    @QtCore.pyqtSlot()
    def on_pushButtonAceptar_clicked(self):
        '''
        '''
        try:
            assert self.testearDialogo() is True
        except AssertionError:
            return
        '''
        TODO: Armar métod cargarEmpleado.....
        '''
        nombre = unicode(self.lineEditNombre.text())
        apellido = unicode(self.lineEditApellido.text())
        nroDocumento = unicode(self.lineEditNroDocumento.text())
        tipoDocumento = unicode(self.comboBoxTipoDocumento.currentText())
        division = Division_Transporte()
        division.agregarEmpleado(nombre, apellido, nroDocumento)
        
        if self.mostrarMensaje('El Empleado se ha cargado exitosamente!! :)', 'Cargando Empleado'):
            self.accept()
    
    '''
    TODO: Se ha repetido este mismo método en varias de las clsase Dialogos.
    '''
    def mostrarMensaje(self, mensaje, titulo):
        '''
        Función que muestra un pequeña ventana con información relevante.
        '''
        msgBox = QtGui.QMessageBox(self)
        msgBox.setText(QtCore.QString.fromUtf8(mensaje))
        msgBox.setWindowTitle(titulo)
        return msgBox.exec_()
        
    def testearDialogo(self):
        '''
        Función que se encarga de comprobar que los campos obligatorios se completaron y correctamente.
        '''
        if not match('[A-Za-z|\s]', self.lineEditNombre.text()):
            self.mostrarMensaje('Debe ingresar el nombre.', 'Ingreso')
            self.lineEditNombre.clear()
            self.lineEditNombre.setFocus()
            return
        if not match('[a-z|A-Z]+', self.lineEditApellido.text()):
            self.mostrarMensaje('Debe ingresar el apellido', 'Ingreso')
            self.lineEditApellido.clear()
            self.lineEditApellido.setFocus()
            return
        if not match('[0-9]+', self.lineEditNroDocumento.text()):
            self.mostrarMensaje('Debe ingresar el numero de Documento.', 'Ingreso')
            self.lineEditNroDocumento.clear()
            self.lineEditNroDocumento.setFocus()
            return
        return True