# -*- coding: utf-8 -*-
'''
Created on 03/10/2012

@author: Usuario
'''
from PyQt4 import QtCore, QtGui
from formularios.DialogAltaPersonal import Ui_DialogAltaPersonal

from re import match
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
        self.pushButtonCancelar
        
        #Validación a medida que se escribe en el lineEdit
        self.lineEditNombre.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[A-Za-z]+'),self))
        self.lineEditNroDocumento.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[0-9]+'),self))
        self.lineEditEmail.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[A-Za-z][\w]+@'),self))
        
        '''
        @todo: Crear metodo llenarComBox
        '''
        from negocio import Division_Transporte
        dvTrans = Division_Transporte.Division_Transporte()
        print dvTrans

        for i in dvTrans.getTipoDeDocumentos():
            self.comboBoxTipoDocumento.addItems(QtCore.QStringList(i))
    
    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        self.close()
        
    @QtCore.pyqtSlot()
    def on_pushButtonAceptar_clicked(self):
        try:
            assert self.testearDialogo() is True
        except AssertionError:
            return
        nombre = self.lineEditNombre.text()
        apellido = self.lineEditApellido.text()
        nroDocumento = self.lineEditNroDocumento.text()
        
        division = Division_Transporte()
        division.agregarEmpleado(nombre, apellido, nroDocumento)
        msgBox = QtGui.QMessageBox(self)
        msgBox.setText(QtCore.QString.fromUtf8('El Empleado se ha cargado exitosamente!! :)'))
        if msgBox.exec_():
            self.close()
    
    def mostrarMensaje(self, mensaje):
        msgBox = QtGui.QMessageBox(self)
        msgBox.setText(QtCore.QString.fromUtf8(mensaje))
        msgBox.show()
    
    #Sirve para Validar una vez completado el campo del Nombre
    def testearNombre(self):
        nombre = unicode(self.lineEditNombre.text())
        if match('[A-Z][a-z]+', str(nombre)):
            return True
        else:
            self.mostrarMensaje("El Nombre debe comenzar con mayúscula")
            self.lineEditNombre.clear()
            self.lineEditNombre.setFocus()
            return
        
    #Como los campos a llenar se validan mientras se van completando, este metodo
    #se vuelve mas legible...
    def cargarPersonal(self):
        nombre = unicode(self.lineEditNombre.text())
        try:
            if len(nombre)==0:
                raise Exception
        except Exception,e:
            e.message
            msgBox = QtGui.QMessageBox(self)
            msgBox.setText(QtCore.QString.fromUtf8('Debe ingresar el nombre'))
            msgBox.show()
            self.lineEditNombre.clear()
            self.lineEditNombre.setFocus()
        
    
    def testearApellido(self):
        apelldio = unicode(self.lineEditApellido.text())
        if match('[A-Z][a-z]+', str(apelldio)):
            return apelldio
        else:
            self.mostrarMensaje("El Apelldio debe comenzar con mayúscula")
            self.lineEditApellido.clear()
            self.lineEditApellido.setFocus()
            return
        
    def testearNroDocumento(self):
        documento = unicode(self.lineEditNroDocumento.text())
        if match('[0-9]{8}', str(documento)):
            return documento
        else:
            self.mostrarMensaje("El Nro de Documento debe tener 8 dígitos")
            self.lineEditNroDocumento.clear()
            self.lineEditNroDocumento.setFocus()
            return
        
    def testearDialogo(self):
        '''
            @todo: Cambiar el nombre si no es significativo.
        '''
        if not match('[A-Z][a-z]+', self.lineEditNombre.text()):
            self.mostrarMensaje('Debe ingresar el nombre.')
            return
        if not match('[a-z|A-Z]+', self.lineEditApellido.text()):
            self.mostrarMensaje('Debe ingresar el apellido')
            return
        if not match('[0-9]+', self.lineEditNroDocumento.text()):
            self.mostrarMensaje('Debe ingresar el numero de Documento.')
            return
        if not match('[0-9]+', self.lineEditDomicilio.text()):
            self.mostrarMensaje('Debe ingresar el Domicilio.')
            return
        if not match('[0-9]+', self.lineEditTelefono.text()):
            self.mostrarMensaje('Debe ingresar el telefono.')
            return
#        if not match('^[\w\-][\w\-\.]+@[a-zA-Z]+', self.lineEditEmail.text()):
#            self.mostrarMensaje('Debe ingresar el e-mail.')
#            return
        return True