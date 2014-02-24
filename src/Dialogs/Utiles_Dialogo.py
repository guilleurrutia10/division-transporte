'''
Created on 28/01/2014

@author: Usuario
'''
from PyQt4 import QtCore, QtGui

def mostrarMensaje(aplicacion, mensaje, titulo):
    msgBox = QtGui.QMessageBox(aplicacion)
    msgBox.setText(QtCore.QString.fromUtf8(mensaje))
    msgBox.setWindowTitle(QtCore.QString.fromUtf8(titulo))
    return msgBox.exec_()

def mostrarMensajeParaConfirmarTwo(aplicacion, mensaje, titulo):
    msgBox = QtGui.QMessageBox(parent=aplicacion)
    msgBox.setText(QtCore.QString.fromUtf8(mensaje))
    msgBox.setWindowTitle(QtCore.QString.fromUtf8(titulo))
    return msgBox.exec_()

def mostrarMensajeParaConfirmar(aplicacion, mensaje, titulo):
    print 'Aca va un dialogo!' + mensaje
    return 'Ok'