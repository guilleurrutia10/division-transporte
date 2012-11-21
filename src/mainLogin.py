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
        #self.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.abrirVentanaPrincipal)
        
        #Definimos los roles de los botones, Aceptar y Cancelar
        
        
        self.lineEditUser.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[0-9|a-z|A-z]+'),self))
        self.linePassword.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[0-9|a-z|A-z]+'),self))
        #Mostrar asteriscos en lugar de los caracteres introducidos en realidad.
        self.linePassword.setEchoMode(2)
        
        #self.aplicacionPadre = aplicacionPadre
    
    @QtCore.pyqtSlot()    
    def on_pushButtonOk_clicked(self):
        '''
            Función que permite al usuario ingresar a la aplicación.
            @version: 
            @author:  
        '''
        try:
            usr = self.validarUsr()
            #self.aplicacionPadre.setUsuarioActual(usr)
            QtGui.QApplication.instance().setUsuarioActual(usr)
            self.accept()
        except:
            self.mostrarMensaje('Usuario o contrasena invalido', 'Error usuario')
        #self.close()
    
    @QtCore.pyqtSlot()
    def on_pushButtonCancel_clicked(self):
        '''
            Función que define que se hace al cerrar el login.
            @version: 
            @author:
        '''
        self.reject()
    
    def mostrarMensaje(self, mensaje, titulo):
        '''
        Función que muestra un pequeña ventana con información relevante.
        '''
        msgBox = QtGui.QMessageBox.critical(self, titulo, mensaje)
        
        
    def validarUsr(self):
        
        from usuarios import Usuario
        
        username = str(self.lineEditUser.text())
        password = str(self.linePassword.text())
        
        usr = Usuario(username)
        
        usr.validar(password)
        
        return usr