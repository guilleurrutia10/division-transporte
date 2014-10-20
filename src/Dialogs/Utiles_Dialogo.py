# -*- coding: utf-8 -*-
'''
Created on 28/01/2014

@author: Urrutia
'''
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMessageBox
from PyQt4.QtCore import QString


def mostrarMensaje(aplicacion, mensaje, titulo):
    msgBox = QtGui.QMessageBox(aplicacion)
    msgBox.setText(mensaje)
    msgBox.setWindowTitle(titulo)
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

    if dia1 == dia2 and mes1 == mes2 and anio1 == anio2:
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
    msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
    return msgBox.exec_()


class Mensaje(object):

    def __init__(self, aplicacion, mensaje='', titulo=''):
        self.messageBox = QMessageBox(aplicacion)
        self.messageBox.setText(QString.fromUtf8(mensaje))
        self.messageBox.setWindowTitle(QString.fromUtf8(titulo))
        self.messageBox.setStandardButtons(QMessageBox.Ok)

    def setTitle(self, titulo):
        self.messageBox.setWindowTitle(QString.fromUtf8(titulo))

    def setMensaje(self, mensaje):
        self.messageBox.setText(QString.fromUtf8(mensaje))

    def setCritical(self):
        '''
        Agrega el icono de crítico.
        Agrega los siguientes botones estándar:
            - Ok
        '''
        self.messageBox.setIcon(QMessageBox.Critical)

    def setWarning(self):
        '''
        Agrega el icono de warning (precaución).
        Agrega los siguientes botones estándar:
            - Ok
        '''
        self.messageBox.setIcon(QMessageBox.Warning)

    def setInformative(self):
        '''
        Agrega el icono de información.
        Agrega los siguientes botones estándar:
            - Ok
        '''
        self.messageBox.setIcon(QMessageBox.Information)

    def setQuestion(self):
        '''
        Agrega el icono de interrogación.
        Agrega los siguientes botones estándar:
            - Ok
        '''
        self.messageBox.setIcon(QMessageBox.Question)

    def agregarBotonOk(self):
        '''
        Agrega el botón de Ok.
        '''
        self.messageBox.addButton(QMessageBox.Ok)

    def agregarBotonAbrir(self):
        '''
        Agrega el botón de Abrir.
        '''
        self.messageBox.addButton(QMessageBox.Open)

    def agregarBotonCancelar(self):
        '''
        Agrega el botón de Cancelar.
        '''
        self.messageBox.addButton(QMessageBox.Cancel)

    def agregarBotonCerrar(self):
        '''
        Agrega el botón de Cerrar.
        '''
        self.messageBox.addButton(QMessageBox.Close)

    def agregarBotonNegar(self):
        '''
        Agrega el botón de Negar.
        '''
        self.messageBox.addButton(QMessageBox.No)

    def agregarBotonAfirmar(self):
        '''
        Agrega el botón de Afirmar.
        '''
        self.messageBox.addButton(QMessageBox.Yes)

    def quitarBotones(self):
        '''
        Quita todos los botones del diálogo.
        '''
        for boton in self.messageBox.buttons():
            self.messageBox.removeButton(boton)

    def exec_(self):
        return self.messageBox.exec_()
