# -*- coding: utf-8 -*-
'''
Created on 03/10/2012

@author: Usuario
'''
from PyQt4 import QtCore, QtGui
from formularios.DialogAltaPersonal import Ui_DialogAltaPersonal

import re

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
        
        self.buttonBox.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.cargarPersonal)
        self.buttonBox.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), self.cerrar)
        
        #Validación a medida que se escribe en el lineEdit
        self.lineEditNombre.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[A-Za-z]+'),self))
        self.lineEditNroDocumento.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[0-9]+'),self))
        self.lineEditEmail.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[A-Za-z][\w]+@'),self))
        
        self.buttonBox = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Cancel)
        
#    @QtCore.pyqtSignature('QString')
#    def on_lineEditNombre_textEdited(self):
#        #Valida a medida que se escribe en el lineEdit
#        self.lineEditNombre.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[A-Z][a-z]+'),self))
#        self.testearNombre()
        
#        self.lineEditNombre.connect(self.lineEditNombre, QtCore.SIGNAL("editingFinished()"),self.testearNombre)
#        self.connect(self.lineEditNombre, QtCore.SIGNAL("editingFinished()"),self.testearNombre)
#        self.connect(self.lineEditApellido, QtCore.SIGNAL("editingFinished()"),self.testearApellido)
#        self.connect(self.lineEditNroDocumento, QtCore.SIGNAL("editingFinished()"),self.testearNroDocumento)
    
#    @QtCore.pyqtSlot()
#    def on_lineEditNombre_editingFinished(self):
#        self.testearNombre()
    
    
    def cerrar(self):
        self.close()
    
    def mostrarMensaje(self, mensaje):
        msgBox = QtGui.QMessageBox(self)
        msgBox.setText(QtCore.QString.fromUtf8(mensaje))
        msgBox.show()
    
    #Sirve para Validar una vez completado el campo del Nombre
    def testearNombre(self):
        nombre = unicode(self.lineEditNombre.text())
        if re.match('[A-Z][a-z]+', str(nombre)):
            return True
        else:
            self.mostrarMensaje("El Nombre debe comenzar con mayúscula")
            self.lineEditNombre.clear()
            self.lineEditNombre.setFocus()
            return
        
    #Como los campos a llenar se validan mientras se van completando, este metodo
    #se vuelve mas legible...
    def cargarPersonal(self):
        print "Guardando personal"
        from negocio.Empleado import Empleado
        from adminBaseDatos import Local
        
        if self.testearNombre():
            nombre = unicode(self.lineEditNombre.text())
        else:
            print "Debe ingresar el Nombre"
            return
        
        apellido = unicode(self.lineEditApellido.text())
        documento = unicode(self.lineEditNroDocumento.text())
        
        personal = Empleado(nombre, apellido, documento)
        print "Persona Creada, nombre %s Apellido %s Nro Documento %s" %(nombre,apellido,documento)
        Local.cargarEmpleado(personal, documento)
        
        p = Local.mostrarEmpleado(documento)
        print 50*"-"
        print "Recuperada"
        print "Persona Creada, nombre %s Apellido %s Nro Documento %s" %(p.nombre,p.apellido,p.documento)
    
    def testearApellido(self):
        apelldio = unicode(self.lineEditApellido.text())
        if re.match('[A-Z][a-z]+', str(apelldio)):
            return apelldio
        else:
            self.mostrarMensaje("El Apelldio debe comenzar con mayúscula")
            self.lineEditApellido.clear()
            self.lineEditApellido.setFocus()
            return
        
    def testearNroDocumento(self):
        documento = unicode(self.lineEditNroDocumento.text())
        if re.match('[0-9]{8}', str(documento)):
            return documento
        else:
            self.mostrarMensaje("El Nro de Documento debe tener 8 dígitos")
            self.lineEditNroDocumento.clear()
            self.lineEditNroDocumento.setFocus()
            return