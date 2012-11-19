# -*- coding: utf-8 -*-
'''
Created on 26/09/2012

@author: Usuario
'''
from PyQt4 import QtCore, QtGui

from formularios.FormLogin import Ui_Dialog


class MyLogin(QtGui.QDialog, Ui_Dialog):
    '''
    @version: 
    @author: 
    '''
    def __init__(self, parent = None):
        super(MyLogin, self).__init__(parent)
        self.setupUi(self)
        self.puedoAbrirVentanaPrincipal = False
        self.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.abrirVentanaPrincipal)
        
        #Definimos los roles de los botones, Aceptar y Cancelar
        self.buttonBox = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Cancel)
        
        self.lineEditUser.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[0-9|a-z|A-z]+'),self))
        self.linePassword.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[0-9|a-z|A-z]+'),self))
        #Mostrar asteriscos en lugar de los caracteres introducidos en realidad.
        self.linePassword.setEchoMode(2)
        
    def abrirVentanaPrincipal(self):
        '''
            Función que permite al usuario ingresar a la aplicación.
            @version: 
            @author:  
        '''
        print 'Debo configurar los usuarios!!!! ;P'
        self.close()
    
    @QtCore.pyqtSlot()
    def on_buttonBox_rejected(self):
        '''
            Función que define que se hace al cerrar el login.
            @version: 
            @author:
        '''
        self.close()