# -*- coding: utf-8 -*-
'''
Created on 10/10/2012

@author: urrutia
'''
from PyQt4 import QtGui, QtCore

from formularios.WidgetListadoSecciones2 import Ui_FormListadoSecciones
from negocio.Division_Transporte import Division_Transporte

class ListadoSecciones(QtGui.QWidget, Ui_FormListadoSecciones):
    def __init__(self, parent=None):
        super(ListadoSecciones, self).__init__(parent)
        self.setupUi(self)
        self.tableWidgetListadoSecciones.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.cargarGrillaInicial()
        
    def seleccionarSeccion(self):
        print "Click sobre Seleccionar Seccion"
        
    def cargarGrillaInicial(self):
        division = Division_Transporte()
        secciones = division.getSecciones()
        sec = secciones.values()
        sec.sort(cmp=lambda x, y : cmp(x.nombre, y.nombre))
        self.cargarGrillaEmpleadosSinAsignar(sec)
        
    def cargarGrillaEmpleadosSinAsignar(self, secciones):
        fila = 0
        self.tableWidgetListadoSecciones.clearContents()
        self.tableWidgetListadoSecciones.setRowCount(len(secciones))
        for seccion in secciones:
            columna = 0
            itemNombre = QtGui.QTableWidgetItem()
            itemNombre.setText(seccion.nombre)
            self.tableWidgetListadoSecciones.setItem(fila, columna, itemNombre)
            columna += 1
            itemCantidadEmpl = QtGui.QTableWidgetItem()
            itemCantidadEmpl.setText(unicode(seccion.cantidadEmpleadosTotales()))
            self.tableWidgetListadoSecciones.setItem(fila, columna, itemCantidadEmpl)
            columna += 1
            itemEncargado = QtGui.QTableWidgetItem()
            itemEncargado.setText(seccion.encargado.nombreCompleto())
            self.tableWidgetListadoSecciones.setItem(fila, columna, itemEncargado)
            columna += 1
            itemCode = QtGui.QTableWidgetItem()
            itemCode.setText(unicode(seccion.getCodigo()))
            self.tableWidgetListadoSecciones.setItem(fila, columna, itemCode)

            fila += 1
            