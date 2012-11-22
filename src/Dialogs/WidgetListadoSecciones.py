# -*- coding: utf-8 -*-
'''
Created on 10/10/2012

@author: urrutia
'''
from PyQt4 import QtGui, QtCore

from formularios.WidgetListadoSecciones2 import Ui_FormListadoSecciones
from negocio.Division_Transporte import Division_Transporte

class ListadoSecciones(QtGui.QWidget, Ui_FormListadoSecciones):
    def __init__(self, parent = None):
        super(ListadoSecciones, self).__init__(parent)
        self.setupUi(self)
        self.cargarGrillaInicial()
        
    def seleccionarSeccion(self):
        print "Click sobre Seleccionar Seccion"
        
    def cargarGrillaInicial(self):
        division = Division_Transporte()
        secciones = division.getSecciones()
        sec = secciones.values()
        sec.sort(cmp=lambda x,y : cmp(x.nombre, y.nombre))
        self.cargarGrilla(sec)
        
    def cargarGrilla(self, secciones):
        fila = 0
        columna = 0
        self.tableWidgetListadoSecciones.setRowCount(len(secciones))
        for seccion in secciones:
            miItem1 = QtGui.QTableWidgetItem()
            miItem1.setText(seccion.nombre)
            self.tableWidgetListadoSecciones.setItem(fila,columna,miItem1)
            columna += 1
            miItem2 = QtGui.QTableWidgetItem()
            miItem2.setText(unicode(seccion.cantidadEmpleados()))
            self.tableWidgetListadoSecciones.setItem(fila,columna,miItem2)
            columna += 1
            miItem3 = QtGui.QTableWidgetItem()
            miItem3.setText(seccion.encargado.nombre)
            self.tableWidgetListadoSecciones.setItem(fila,columna,miItem3)