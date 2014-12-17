# -*- coding: utf-8 -*-
'''
Created on 03/10/2012

@author: Usuario
'''
from PyQt4 import QtCore, QtGui

from formularios.DialogMostrarPedidoDeActuacion import Ui_DialogMostrarPedidoDeActuacion
from AyudaManejador import AyudaManejador


class DialogMostrarPedidoDeActuacion(QtGui.QDialog, Ui_DialogMostrarPedidoDeActuacion, AyudaManejador):
    '''
    Atributos:

    - pedidoDeActuacion

    '''
    def __init__(self, parent=None, pedidoDeActuacion=None):
        '''
        Constructor
        '''
        super(DialogMostrarPedidoDeActuacion, self).__init__()
        self.setupUi(self)
        self._pedidoDeActuacion = pedidoDeActuacion
        self.label.setObjectName("label")
        self.label_2.setObjectName("label")

    def setPedidoDeActuacion(self, pedidoDeActuacion):
        self._pedidoDeActuacion = pedidoDeActuacion

    def exec_(self, *args, **kwargs):
        self.cargarDatos()
        return QtGui.QDialog.exec_(self, *args, **kwargs)

    def cargarDatos(self):
        '''
        '''
        self.labelFechaPedido.setText(str(self._pedidoDeActuacion.getFechaRealizacion()))

        self.tableWidgetRepuestos.clearContents()
        self.tableWidgetRepuestos.setRowCount(len(self._pedidoDeActuacion.getRepuestosSolicitados()))
        fila = 0
        for repuesto in self._pedidoDeActuacion.getRepuestosSolicitados():
            columna = 0
            itemNombreTipoRepuesto = QtGui.QTableWidgetItem()
            itemNombreTipoRepuesto.setText(repuesto.getTipoDeRepuesto().getNombre())
            self.tableWidgetRepuestos.setItem(fila,columna,itemNombreTipoRepuesto)
            columna += 1
            itemDescripcionRepuesto = QtGui.QTableWidgetItem()
            itemDescripcionRepuesto.setText(repuesto.getTipoDeRepuesto().getDescripcion())
            self.tableWidgetRepuestos.setItem(fila,columna,itemDescripcionRepuesto)
            columna += 1
            itemCantidadRepuesto = QtGui.QTableWidgetItem()
            itemCantidadRepuesto.setText(str(repuesto.getCantidad()))
            self.tableWidgetRepuestos.setItem(fila,columna,itemCantidadRepuesto)
            fila += 1

    @QtCore.pyqtSlot()
    def on_pushButtonAceptar_clicked(self):
        self.accept()

    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        self.reject()
