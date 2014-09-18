# -*- coding: utf-8 -*-
'''
Created on 26/09/2012

@author: Usuario
'''
from PyQt4 import QtCore, QtGui

from Dialogs.formularios.FormLogin import Ui_Dialog
from Dialogs.negocio.usuario import Usuario


class MyLogin(QtGui.QDialog, Ui_Dialog):
    '''
    :version: 
    :author: 
    '''
    def __init__(self, parent = None):
        super(MyLogin, self).__init__(parent)
        self.setupUi(self)
        self.label.setObjectName('label')
        self.label_3.setObjectName('label')
        self.puedoAbrirVentanaPrincipal = False

        self.lineEditUser.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[0-9|a-z|A-z]+'),self))
        self.linePassword.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[0-9|a-z|A-z]+'),self))
        #Mostrar asteriscos en lugar de los caracteres introducidos en realidad.
        self.linePassword.setEchoMode(2)

        #self.aplicacionPadre = aplicacionPadre

    @QtCore.pyqtSlot()    
    def on_pushButtonOk_clicked(self):
        '''
        Función que permite al usuario ingresar a la aplicación.
        :version: 
        :author:  
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
            :version: 
            :author:
        '''
        self.reject()

    def mostrarMensaje(self, mensaje, titulo):
        '''
        Función que muestra un pequeña ventana con información relevante.
        '''
        msgBox = QtGui.QMessageBox.critical(self, titulo, mensaje)

    def validarUsr(self):
        '''
            Retorna un nuevo usuario con el nombre y la contrasena ingresados al login.
            El usuario creado se valida, es decir se verifica que los datos ingresados existen (esta registrado),
            en la misma creacion del usuario.

        '''


        #tomamos el nombre ingresado por el usuario:
        username = unicode(self.lineEditUser.text())
        #tomamos el password ingresado por el usuario:
        password = unicode(self.linePassword.text())

        #creamos un usuario con el nombre que ingresó
        #usr = Usuario(username)

        #y lo validamos...
        #usr.validar(password)

        #return usr

        #import hashlib
        #hash_password = hashlib.sha1(username + password).hexdigest()
        #hash_password = password
        #creamos un usuario con el nombre que ingresó y el password.
        usr = Usuario(username, password)
        usr.validar(password)

        return usr

    def keyPressEvent(self, keyEvent):
        """
        Se sobreescribe el método para atrapar el evento de presionar
        alguna tecla.
        Según la tecla presionada se lleva a cabo la acción requerida.
        """
        # Atrapar el evento de teclear F1
        if keyEvent.key() == QtCore.Qt.Key_F1:
            print 'Se presiono la tecla F1 en Login'
            qlanguage = QtCore.QLocale().language()
            language = QtCore.QLocale.languageToString(qlanguage)
            # Para mostrar internacionalización
            print 'Mostrar ayuda para idioma: %s' % (language)
            path = QtCore.QDir.currentPath()
            # Se arma la URL para caragr en el Browser
            urlString = 'file:///%s/Help/%s/topics/Login.htm' % (path, language)
            url = QtCore.QUrl(urlString)
            print url.path()
            # Solicitamos que se abra el Browser con la url indicada
#             QtGui.QDesktopServices.openUrl(url)
        # Para agilizar la entrada del usuario
        if keyEvent.key() == QtCore.Qt.Key_Enter or keyEvent.key() == QtCore.Qt.Key_Return:
            print 'Se presiono Enter'
            self.on_pushButtonOk_clicked()
        # Para salir rápidamente
        if keyEvent.key() == QtCore.Qt.Key_Escape:
            self.on_pushButtonCancel_clicked()
