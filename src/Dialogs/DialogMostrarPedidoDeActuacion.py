# -*- coding: utf-8 -*-
'''
Created on 03/10/2012

@author: Usuario
'''
from PyQt4 import QtCore, QtGui
from formularios.DialogMostrarPedidoDeActuacion import Ui_DialogMostrarPedidoDeActuacion

from Dialogs import DialogCrearReparacion
from negocio.Division_Transporte import Division_Transporte
from negocio.excepciones.Excepcion_Orden_No_Esta_En_Revision import Excepcion_Orden_No_Esta_En_Revision
from PyQt4.Qwt5.qplt import QString

class DialogMostrarPedidoDeActuacion(QtGui.QDialog, Ui_DialogMostrarPedidoDeActuacion):
    '''
    Atributos:
    
    - vehiculoSeleccionado
    
    En tiempo de ejecucion, el dialogo posee una nueva variable:
    Mejor seteamos...
        - dominioVehiculo.
    '''
    def __init__(self, parent = None):
        '''
        Constructor
        '''
        super(DialogMostrarPedidoDeActuacion, self).__init__(parent)
        self.setupUi(self)
        self._pedidoDeActuacion = None
    
    def setPedidoDeActuacion(self, pedidoDeActuacion):
        self._pedidoDeActuacion = pedidoDeActuacion
        
    def exec_(self, *args, **kwargs):
        self.cargarDatos(self._pedidoDeActuacion)
        return QtGui.QDialog.exec_(self, *args, **kwargs)
    
    def cargarDatos(self, unPedidoDeActuacion):
        '''
        '''
        self.labelFechaPedido.setText(str(unPedidoDeActuacion.getFechaRealizacion()))
        
        self.tableWidgetRepuestos.clearContents()
        self.tableWidgetRepuestos.setRowCount(len(unPedidoDeActuacion.getRepuestosSolicitados()))
        fila = 0
        for repuesto in unPedidoDeActuacion.getRepuestosSolicitados():
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
        print 'Click sobre aceptar'
        self.accept()
    
    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        self.reject()