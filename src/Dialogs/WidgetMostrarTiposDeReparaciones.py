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
    def __init__(self, parent = None):
        '''
        Constructor
        '''
        super(WidgetMostrarTiposDeReparaciones, self).__init__(parent)
        self.setupUi(self)
        #Para evitar que se modifique la información presentada por la grilla.
        self.tableWidgetTipoReparacionesDivision.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.cargarGrillaInicial()
        
    def cargarGrilla(self, tiposReparaciones):
        self.tableWidgetTipoReparacionesDivision.clearContents()
        self.tableWidgetTipoReparacionesDivision.setRowCount(len(tiposReparaciones))
        fila = 0
        for reparacion in tiposReparaciones:
            columna = 0
            miItem1 = QtGui.QTableWidgetItem()
            miItem1.setText(reparacion.getNombre())
            self.tableWidgetTipoReparacionesDivision.setItem(fila, columna, miItem1)
            columna += 1
            miItem2 = QtGui.QTableWidgetItem()
            miItem2.setText(unicode(reparacion.getDescipcion()))
            self.tableWidgetTipoReparacionesDivision.setItem(fila, columna, miItem2)
            fila += 1
            
    def cargarGrillaInicial(self):
        division = Division_Transporte()
        tiposReparaciones = division.getTipoReparaciones()
        self.tiposReparaciones = tiposReparaciones.values()
        self.tiposReparaciones.sort(cmp=lambda x,y : cmp(x, y))
        self.cargarGrilla(self.tiposReparaciones)
        
    @QtCore.pyqtSlot('QString')
    def on_lineEditNombreTipoReparacion_textChanged(self, cadena):
        filtro = unicode(cadena)
        tiposReparaciones = filter(lambda reparacion: unicode.lower(filtro) in unicode.lower(unicode(reparacion.getNombre())), self.tiposReparaciones)
        tiposReparaciones.sort(cmp=lambda x,y : cmp(x, y))
        self.cargarGrilla(tiposReparaciones)