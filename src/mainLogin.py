# -*- coding: utf-8 -*-
'''
Created on 26/09/2012

@author: Usuario
'''
from PyQt4 import QtCore, QtGui

from formularios.FormLogin import Ui_Dialog


class MyLogin(QtGui.QDialog, Ui_Dialog):
    def __init__(self, parent = None):
        super(MyLogin, self).__init__(parent)
        self.setupUi(self)
        self.puedoAbrirVentanaPrincipal = False
        self.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.abrirVentanaPrincipal)
        
        #Definimos los roles de los botones, Aceptar y Cancelar
        self.buttonBox = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Cancel)
        
        self.lineEditNumeroDocumento.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[0-9]+'),self))
        #Mostrar asteriscos en lugar de los caracteres introducidos en realidad.
        self.lineEditNumeroDocumento.setEchoMode(2)
        
#        import adminBaseDatos
#        adminBaseDatos.Local.cargarUsuarios()
#        
#        lista = []
#        lista = adminBaseDatos.Local.obtenerUsuarios()
#        if len(lista)>0:
#            for i in lista:
#                #Sirve para agragar informacion a los comboBox
#                self.comboBoxUsuario.addItems(QtCore.QStringList(i))
        
    def abrirVentanaPrincipal(self):
        '''
            Función que permite al usuario ingresar a la aplicación. 
        '''
        self.close()
    
    @QtCore.pyqtSlot()
    def on_buttonBox_rejected(self):
        '''
            Función que define que se hace al cerrar el login.
        '''
        self.close()