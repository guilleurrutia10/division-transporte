# -*- coding: utf-8 -*-
'''
Created on 10/10/2012

@author: urrutia
'''
from PyQt4 import QtGui, QtCore

from formularios.WidgetListadoDeRepuestosUtilizados import Ui_FormRepuestosUtilizados
from negocio.Division_Transporte import Division_Transporte


class ListadoRepustosUtilizados(QtGui.QWidget, Ui_FormRepuestosUtilizados):
    '''
    Clase utilizada para el listado de los repuestos utilizados en la División
    Se trata de aquellos repuestos que han formado parte de las reparaciones
    finalizadas en cada vehículo que tenga al menos una orden de reparación
    finalizada.

    Atributos:
    - self.tableWidget
        Código, Nombre, Descripción, Número Pedido de Actuación,
        Número Orden de Reparación, Dominio del Vehículo
    -
    '''
    def __init__(self, parent=None):
        super(ListadoRepustosUtilizados, self).__init__(parent)
        self.setupUi(self)
        division = Division_Transporte()
        # Se obtienen los vehículos con al menos una orden de reparación
        # finalizada.
        self.vehiculos = division.getVehiculosEnFinalizada()
        self.cargarRepuestoUtilizados(self.vehiculos)
        self.tableWidgetRepuestos.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)

    def cargarRepuestoUtilizados(self, vehiculos):
        '''
        Se carga el tableWidgetRepuestos con los repuestos utilizados.
        '''
        self.tableWidgetRepuestos.clearContents()
        fila = 0
        for v in vehiculos:
            for orden in v.getOrdenesDeReparacionFinalizadas():
                for reparacion in orden.getReparaciones():
                    for repuesto in reparacion.getRepuestosUtilizados():
                        filas = self.tableWidgetRepuestos.rowCount() + len(reparacion.getRepuestosUtilizados())
                        self.tableWidgetRepuestos.setRowCount(filas)
                        columna = 0
                        itemCodigo = QtGui.QTableWidgetItem()
                        itemCodigo.setText(repuesto.getTipoDeRepuesto().getCodigo())
                        self.tableWidgetRepuestos.setItem(fila, columna, itemCodigo)
                        columna += 1
                        item = QtGui.QTableWidgetItem()
                        item.setText(repuesto.getTipoDeRepuesto().getNombre())
                        self.tableWidgetRepuestos.setItem(fila, columna, item)
                        columna += 1
                        item = QtGui.QTableWidgetItem()
                        item.setText(repuesto.getTipoDeRepuesto().getDescripcion())
                        self.tableWidgetRepuestos.setItem(fila, columna, item)
                        columna += 1
                        item = QtGui.QTableWidgetItem()
                        codigoPedido = orden.getPedidoDeActuacion().getNumeroPedido()
                        #item.setText(QtCore.QString.number(codigoPedido))
                        item.setText(unicode(codigoPedido))
                        self.tableWidgetRepuestos.setItem(fila, columna, item)
                        columna += 1
                        item = QtGui.QTableWidgetItem()
                        codigoReparacion = orden.getCodigoOrdenReparacion()
                        #item.setText(QtCore.QString.number(codigoReparacion))
                        item.setText(codigoReparacion)
                        self.tableWidgetRepuestos.setItem(fila, columna, item)
                        columna += 1
                        item = QtGui.QTableWidgetItem()
                        item.setText(v.getDominio())
                        self.tableWidgetRepuestos.setItem(fila, columna, item)
                        fila += 1
