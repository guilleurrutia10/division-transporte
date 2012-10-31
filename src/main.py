# -*- coding: utf-8 -*-
import sys
sys.path.append("..")

from PyQt4 import QtGui

from mainwindow import MyMainWindow
from mainLogin import MyLogin

#constante global que referencia a la aplicación
APP = None

def main(args):
    global APP
    APP = QtGui.QApplication(sys.argv)
    #conectamos la senal que indica que se cerró la ultima ventana con la fc cerrar aplicación
    APP.lastWindowClosed.connect(cerrarAplicacion)

    #abrimos el Dialog de Login principal...
    myLogin = MyLogin()
    #si se presionó Aceptar del Login, abrimos la Ventana Principal...
    if myLogin.exec_():
        mainWindow = MyMainWindow()
        mainWindow.show()
    else:
        return
    
    return APP.exec_()    

def cerrarAplicacion():
    '''
    Cierra la Aplicación
    '''
    global APP
    APP.exit()
    
if __name__ == "__main__":
    main(sys.argv)
    
