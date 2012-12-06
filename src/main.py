# -*- coding: utf-8 -*-
'''
Created on 26/09/2012

@author: Usuario
'''
import sys
sys.path.append("..")

from PyQt4 import QtGui

from mainwindow import MyMainWindow
from mainLogin import MyLogin

class Aplicacion(QtGui.QApplication):
    
    def __init__(self):
        super(Aplicacion, self).__init__(sys.argv)
        self.valueDialog = True
        self.usuarioActual = None
        self.lastWindowClosed.connect(self.exit)
    
    def setUsuarioActual(self, usrActual):
        self.usuarioActual = usrActual
    
    
    def exec_(self):
        '''
        @version: 
        @author: 
        '''
        #abrimos el Dialog de Login principal...
        myLogin = MyLogin()
        #si se presionó Aceptar del Login, abrimos la Ventana Principal...
        if myLogin.exec_() == QtGui.QDialog.Accepted:
            mainWindow = MyMainWindow()
            listaPermisos = self.usuarioActual.getPermisos()
            mainWindow.habilitarMenues(listaPermisos)
            mainWindow.show()
            super(Aplicacion, self).exec_()
            

if __name__ == "__main__":
    miAplicacion = Aplicacion()
    sys.exit(miAplicacion.exec_())
