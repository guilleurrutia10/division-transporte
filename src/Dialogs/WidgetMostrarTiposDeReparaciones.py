# -*- coding: utf-8 -*-
'''
Created on 03/10/2012

@author: Usuario
'''
from PyQt4 import QtGui, QtCore

from formularios.WidgetMostrarTiposDeReparaciones import Ui_WidgetMostrarTiposDeReparaciones
from negocio.Division_Transporte import Division_Transporte


class WidgetMostrarTiposDeReparaciones(QtGui.QWidget, Ui_WidgetMostrarTiposDeReparaciones):
    '''
    classdocs
    '''
    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super(WidgetMostrarTiposDeReparaciones, self).__init__(parent)
        self.setupUi(self)
        # Para evitar que se modifique la información presentada por la grilla.
        self.tableWidgetTipoReparacionesDivision.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.cargarGrillaInicial()

    def cargarGrilla(self, tiposReparaciones):
        self.tableWidgetTipoReparacionesDivision.clearContents()
        self.tableWidgetTipoReparacionesDivision.setRowCount(len(tiposReparaciones))
        fila = 0
        for reparacion in tiposReparaciones:
            columna = 0
            itemCodigo = QtGui.QTableWidgetItem()
            itemCodigo.setText(reparacion.getCodigo())
            self.tableWidgetTipoReparacionesDivision.setItem(fila, columna, itemCodigo)
            columna += 1
            itemNombre = QtGui.QTableWidgetItem()
            itemNombre.setText(reparacion.getNombre())
            self.tableWidgetTipoReparacionesDivision.setItem(fila, columna, itemNombre)
            columna += 1
            itemDescripcion = QtGui.QTableWidgetItem()
            itemDescripcion.setText(unicode(reparacion.getDescipcion()))
            self.tableWidgetTipoReparacionesDivision.setItem(fila, columna, itemDescripcion)
            columna += 1
            seccion = Division_Transporte().seccion_a_la_que_pertenece(reparacion)
            itemSeccion = QtGui.QTableWidgetItem()
            itemSeccion.setText(unicode(seccion.getNombre()))
            self.tableWidgetTipoReparacionesDivision.setItem(fila, columna, itemSeccion)
            columna += 1
            itemTiempoEstimado = QtGui.QTableWidgetItem()
            itemTiempoEstimado.setText(unicode(reparacion.getTiempoEstimado()))
            self.tableWidgetTipoReparacionesDivision.setItem(fila, columna, itemTiempoEstimado)

            fila += 1

    def cargarGrillaInicial(self):
        division = Division_Transporte()
        # TODO: Tener en cuenta si alguna seccion no posee tiposDeReparaciones asignadas.
        self.tiposReparaciones = division.getTipoReparaciones()
#         self.tiposReparaciones = tiposReparaciones.values()
        self.tiposReparaciones.sort(cmp=lambda x, y: cmp(x, y))
        self.cargarGrilla(self.tiposReparaciones)

    @QtCore.pyqtSlot('QString')
    def on_lineEditNombreTipoReparacion_textChanged(self, cadena):
        filtro = unicode(cadena)
        tiposReparaciones = filter(lambda reparacion: unicode.lower(filtro) in unicode.lower(unicode(reparacion.getNombre())), self.tiposReparaciones)
        tiposReparaciones.sort(cmp=lambda x, y: cmp(x, y))
        self.cargarGrilla(tiposReparaciones)
