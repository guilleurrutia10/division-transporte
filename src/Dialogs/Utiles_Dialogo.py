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

def compara_fechas_en_cadenas(fecha1, fecha2):
    dia1, mes1, anio1 = [int(n) for n in fecha1.split('/')]
    dia2, mes2, anio2 = [int(n) for n in fecha2.split('/')]
    
    if dia1 == dia2 and mes1 == mes2 and anio1 ==anio2:
        return 0
    if anio1 == anio2:
        if mes1 == mes2:
            if dia1 == dia2:
                return 0
            elif dia1 > dia2:
                return 1
            else:
                return -1
        if mes1 > mes2:
            return 1
        else:
            return -1
    elif anio1 > anio2:
        return 1
    else:
        return -1


def mostrarMensajeOk(aplicacion, mensaje, titulo):
    msgBox = QtGui.QMessageBox(aplicacion)
    msgBox.setText(QtCore.QString.fromUtf8(mensaje))
    msgBox.setWindowTitle(QtCore.QString.fromUtf8(titulo))
    msgBox.setStandardButtons(QtGui.QMessageBox.Ok);
    return msgBox.exec_()    