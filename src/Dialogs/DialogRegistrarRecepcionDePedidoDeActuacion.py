# -*- coding: utf-8 -*-
'''
Created on 10/10/2012

@author: urrutia
'''

from PyQt4 import QtGui, QtCore
from datetime import date
import transaction

from formularios.DialogRegistrarRecepcionDePedidoDeActuacion import Ui_DialogRegistrarRecepcionDePedidoDeActuacion 
from formularios.DialogAsignarFechaRecepcionPedidoActuacion import Ui_DialogAsignarFechaRecepcionPedidoActuacion

from negocio.Division_Transporte import Division_Transporte


class DialogRegistrarRecepcionDePedidoDeActuacion(QtGui.QDialog, Ui_DialogRegistrarRecepcionDePedidoDeActuacion):
    def __init__(self, parent=None):
        '''
        Este dialogo va a manejar pedidos de actuacion.
        Se los va a pedir a la DIvision a traves de los vehiculos
        que estan esperando aprobacion.
        '''
        super(DialogRegistrarRecepcionDePedidoDeActuacion, self).__init__(parent)
        self.setupUi(self)
        self.tableWidget.connect(self.tableWidget, QtCore.SIGNAL('cellClicked(int,int)'), self.seleccionarCelda)
        self.DIVISION = Division_Transporte()
        self._pedidosDeActuacion = [vehiculo.getPedidoDeActuacion() for vehiculo in self.DIVISION.getVehiculosEsperandoAprobacion()] 
        self.cargarGrillaInicial()
        self._pedidoSeleccionado = None
        self._vehiculoDuenioPedido = None

    @QtCore.pyqtSlot()
    def on_pushButtonAceptar_clicked(self):
        print 'Click sobre aceptar'
        self.accept()

    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        self.reject()

    def cargarGrillaInicial(self):
        self._pedidosDeActuacion.sort()
        num = 1
        for pda in self._pedidosDeActuacion:
            pda.setNumeroPedido(num)
            num += 1
        transaction.commit()
        # self.cargarGrilla(self.pedidosDeActuacion)
        self.cargarGrilla()

    def cargarGrilla(self):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(self._pedidosDeActuacion))
        fila = 0
        for pedido in self._pedidosDeActuacion:
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
        self._pedidoSeleccionado = self._pedidosDeActuacion[fila]
        print 'PEDIDO: ', self._pedidoSeleccionado
        print item.text(), '(fila %s,col %s)' % (fila, columna)

    @QtCore.pyqtSlot()
    def on_pushButton_Registrar_clicked(self):
        try:
            if self._pedidoSeleccionado:
                # dlgAsignarFecha = DialogAsignarFechaRecepcionPedidoActuacion(self, self._pedidoSeleccionado)
                self._vehiculoDuenioPedido = filter(lambda vehiculo: vehiculo.pedidoDeActuacionTePertenece(self._pedidoSeleccionado), self.DIVISION.getVehiculosEsperandoAprobacion())
                self._vehiculoDuenioPedido = self._vehiculoDuenioPedido[0]
                # print 'Pertenece al vehiculo ', self._vehiculoDuenioPedido.getDominio() 
                dlgAsignarFecha = DialogAsignarFechaRecepcionPedidoActuacion(self, self._vehiculoDuenioPedido)
                if dlgAsignarFecha.exec_():
                    self._pedidosDeActuacion = [vehiculo.getPedidoDeActuacion() for vehiculo in self.DIVISION.getVehiculosEsperandoAprobacion()]
                    self.cargarGrillaInicial()
                    self.mostrarMensaje('La fecha se ha cargado correctamente. ;)', 'Fecha cargada')
                self._pedidoSeleccionado = None
            else:
                self.mostrarMensaje('Debe Seleccionar el Pedido.', 'Seleccionar Pedido')
        except AttributeError:
            self.mostrarMensaje('Debe Seleccionar el Pedido.', 'Seleccionar Pedido')

    '''
    TODO: Este método se repite en varios Dialogs.
    '''
    def mostrarMensaje(self, mensaje, titulo):
        msgBox = QtGui.QMessageBox(self)
        msgBox.setText(QtCore.QString.fromUtf8(mensaje))
        msgBox.setWindowTitle(QtCore.QString.fromUtf8(titulo))
        return msgBox.exec_()

class DialogAsignarFechaRecepcionPedidoActuacion(QtGui.QDialog, Ui_DialogAsignarFechaRecepcionPedidoActuacion):

    def __init__(self, parent=None, vehiculo = None):
        super(DialogAsignarFechaRecepcionPedidoActuacion, self).__init__(parent)
        self.setupUi(self)
        self._vehiculo = vehiculo
        # seteo de nombres de los Labels para el estilo
        self.label.setObjectName("label")
        self.label_3.setObjectName("label")
        self.label_5.setObjectName("label")
        self.label_6.setObjectName("label")
        # Por defecto se establece el campo Fecha con la fecha actual del sistema
        self.dateEditFechaRecepcioPedido.setDate(QtCore.QDate.currentDate())
        self.cargarRepuestos()

    def cargarRepuestos(self):
        # Provisorio, seguro es un tableWidget
        for reparacion in self._vehiculo.getReparaciones():
            for r in reparacion.getRepuestosUtilizados():
                repuesto = QtGui.QListWidgetItem()
                repuesto.setText(r.getTipoDeRepuesto().getNombre())
                repuesto.setTextAlignment(4)
                self.listWidget.addItem(repuesto)

    @QtCore.pyqtSlot()
    def on_pushButtonAceptar_clicked(self):
        # ahora recibe un objeto pedido de actuacion!
        fecha = self.dateEditFechaRecepcioPedido.date()
        unaFecha = date(day=fecha.toPyDate().day,
                        month=fecha.toPyDate().month,
                        year=fecha.toPyDate().year)
        print unaFecha, type(fecha.toPyDate())
        # TODO: atrapar excepción por fecha incorrecta????
        # try:
        resu = self._vehiculo.registrarRecepcionPedidoActuacion(unaFecha)
        # except FechaAnteriorARealizda:
        # mostrar msj
#        print "Exitosa? ", resu
        transaction.commit()
        self.accept()

    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        self.reject()
