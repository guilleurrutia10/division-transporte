# -*- coding: utf-8 -*-
'''
Created on 10/10/2012

@author: urrutia
'''

from PyQt4 import QtGui, QtCore

from formularios.DialogRegistrarRecepcionDePedidoDeActuacion import Ui_DialogRegistrarRecepcionDePedidoDeActuacion 
from formularios.DialogAsignarFechaRecepcionPedidoActuacion import Ui_DialogAsignarFechaRecepcionPedidoActuacion

from negocio.Division_Transporte import Division_Transporte

class DialogRegistrarRecepcionDePedidoDeActuacion(QtGui.QDialog, Ui_DialogRegistrarRecepcionDePedidoDeActuacion):
    def __init__(self, parent=None):
        super(DialogRegistrarRecepcionDePedidoDeActuacion, self).__init__(parent)
        self.setupUi(self)
        self.cargarGrillaInicial()
        self.pushButtonCancelar
        self.tableWidget.connect(self.tableWidget, QtCore.SIGNAL('cellClicked(int,int)'), self.seleccionarCelda)

    @QtCore.pyqtSlot()
    def on_pushButton_Registrar_clicked(self):
        try:
            if self.itemNumeroPedido:
                dlgAsignarFecha = DialogAsignarFechaRecepcionPedidoActuacion()
                dlgAsignarFecha.itemNumeroPedido = self.itemNumeroPedido
                dlgAsignarFecha.exec_()
                self.itemNumeroPedido = None
            else:
                self.mostrarMensaje('Debe Seleccionar el Pedido.', 'Seleccionar Pedido')
        except AttributeError:
            self.mostrarMensaje('Debe Seleccionar el Pedido.', 'Seleccionar Pedido')
            
    @QtCore.pyqtSlot()
    def on_pushButtonAceptar_clicked(self):
        print 'Click sobre aceptar'
        
    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        self.reject()
        
    def cargarGrillaInicial(self):
        division = Division_Transporte()
        self.pedidosDeActuacion = division.getPedidoActuacionSinFechaRecepcion()
        from pprint import pprint
        pprint(self.pedidosDeActuacion)
        num = 1
        for i in self.pedidosDeActuacion:
            i.setNumeroPedido(num)
            num += 1
        self.cargarGrilla(self.pedidosDeActuacion)
        
    def cargarGrilla(self, pedidosDeActuacion):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(pedidosDeActuacion))
        fila = 0
        for pedido in pedidosDeActuacion:
            columna = 0
            itemNumeroPedido = QtGui.QTableWidgetItem()
            itemNumeroPedido.setText(str(pedido.getNumeroPedido()))
            self.tableWidget.setItem(fila, columna, itemNumeroPedido)
            columna += 1
            itemFechaRealizacion = QtGui.QTableWidgetItem()
            itemFechaRealizacion.setText(pedido.getFechaRealizacion().ctime())
            self.tableWidget.setItem(fila, columna, itemFechaRealizacion)
            fila += 1
            
    def seleccionarCelda(self, fila, columna):
        item = self.tableWidget.item(fila, 0)
        self.itemNumeroPedido = unicode(item.text())
        print item.text(), '(fila %s,col %s)' % (fila, columna)
        
    '''
    TODO: Este método se repite en varios Dialogs.
    '''
    def mostrarMensaje(self, mensaje, titulo):
        msgBox = QtGui.QMessageBox(self)
        msgBox.setText(QtCore.QString.fromUtf8(mensaje))
        msgBox.setWindowTitle(QtCore.QString.fromUtf8(titulo))
        return msgBox.exec_()

class DialogAsignarFechaRecepcionPedidoActuacion(QtGui.QDialog, Ui_DialogAsignarFechaRecepcionPedidoActuacion):
    
    def __init__(self, parent=None):
        super(DialogAsignarFechaRecepcionPedidoActuacion, self).__init__(parent)
        self.setupUi(self)
    
    @QtCore.pyqtSlot()
    def on_pushButtonAceptar_clicked(self):
        # itemNumeroPedido, variable recibida por el Dialog anterior...
        print 'Click sobre aceptar'
        fecha = self.dateEditFechaRecepcioPedido.date()
        from datetime import date
        unaFecha = date(day=fecha.toPyDate().day, month=fecha.toPyDate().month, year=fecha.toPyDate().year)
        print unaFecha, type(fecha.toPyDate())
        division = Division_Transporte()
        division.registrarRecepcionPedidoDeActuacion(int(self.itemNumeroPedido), unaFecha)
        
    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        self.reject()
