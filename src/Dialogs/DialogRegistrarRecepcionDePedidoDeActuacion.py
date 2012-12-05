# -*- coding: utf-8 -*-
'''
Created on 10/10/2012

@author: urrutia
'''

from PyQt4 import QtGui, QtCore

from formularios.DialogRegistrarRecepcionDePedidoDeActuacion import Ui_DialogRegistrarRecepcionDePedidoDeActuacion 
from formularios.DialogAsignarFechaRecepcionPedidoActuacion import Ui_DialogAsignarFechaRecepcionPedidoActuacion

class DialogRegistrarRecepcionDePedidoDeActuacion(QtGui.QDialog, Ui_DialogRegistrarRecepcionDePedidoDeActuacion):
    def __init__(self, parent = None):
        super(DialogRegistrarRecepcionDePedidoDeActuacion, self).__init__(parent)
        self.setupUi(self)
        self.pushButtonCancelar

    @QtCore.pyqtSlot()
    def on_pushButton_Registrar_clicked(self):
        dlgAsignarFecha = DialogAsignarFechaRecepcionPedidoActuacion()
        dlgAsignarFecha.exec_()
        
    @QtCore.pyqtSlot()
    def on_pushButtonAceptar_clicked(self):
        print 'Click sobre aceptar'
        
    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        self.reject()

class DialogAsignarFechaRecepcionPedidoActuacion(QtGui.QDialog, Ui_DialogAsignarFechaRecepcionPedidoActuacion):
    
    def __init__(self, parent = None):
        super(DialogAsignarFechaRecepcionPedidoActuacion, self).__init__(parent)
        self.setupUi(self)
    
    @QtCore.pyqtSlot()
    def on_pushButtonAceptar_clicked(self):
        print 'Click sobre aceptar'
        
    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        self.reject()