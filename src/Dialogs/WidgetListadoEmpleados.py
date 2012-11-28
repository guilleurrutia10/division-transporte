# -*- coding: utf-8 -*-
'''
Created on 16/11/2012

@author: urrutia
'''

from PyQt4 import QtCore, QtGui

from formularios.WidgetListadoEmpleados import Ui_Form
from negocio.Division_Transporte import Division_Transporte

class WidgetListadoEmpleados(QtGui.QWidget, Ui_Form):
    
    def __init__(self, parent = None):
        super(WidgetListadoEmpleados, self).__init__(parent)
        self.setupUi(self)
        #Para evitar que se modifique la información presentada por la grilla.
        self.tableWidgetDatosEmpleados.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.empleados = None
        self.cargarGrillaInicial()
        
    def cargarGrilla(self, empleados):
        self.tableWidgetDatosEmpleados.clearContents()
        self.tableWidgetDatosEmpleados.setRowCount(len(empleados))
        fila = 0
        for empleado in empleados:
            columna = 0
            miItemc1 = QtGui.QTableWidgetItem()
            miItemc1.setText(empleado.nombre)
            self.tableWidgetDatosEmpleados.setItem(fila,columna,miItemc1)
            columna += 1
            miItemc2 = QtGui.QTableWidgetItem()
            miItemc2.setText(empleado.apellido)
            self.tableWidgetDatosEmpleados.setItem(fila,columna,miItemc2)
            columna += 1
            miItemc3 = QtGui.QTableWidgetItem()
            miItemc3.setText(empleado.tipoDocumento.get_codigo_tipo_documento())
            self.tableWidgetDatosEmpleados.setItem(fila,columna,miItemc3)
            columna += 1
            miItemc4 = QtGui.QTableWidgetItem()
            miItemc4.setText(empleado.documento)
            self.tableWidgetDatosEmpleados.setItem(fila,columna,miItemc4)
            fila = fila + 1
    
    #===========================================================================
    # Por ahora la única vez que se consulta la BD es al cargar la grilla por
    # primera vez.
    #===========================================================================
    def cargarGrillaInicial(self):
        division = Division_Transporte()
        p = division.getEmpleados()
        self.empleados = p.values()
        self.empleados.sort(cmp=lambda x,y : cmp(x.nombre, y.nombre))
        self.cargarGrilla(self.empleados)
    
    @QtCore.pyqtSlot('QString')        
    def on_lineEditFiltroNombre_textChanged(self, cadena):
        filtro = unicode(cadena)
#        division = Division_Transporte()
#        empleados = division.getEmpleados()
#        values = empleados.values()
        
        personal = filter(lambda p: unicode.lower(filtro) in unicode.lower(unicode(p.nombre)), self.empleados)
        personal.sort(cmp=lambda x,y : cmp(x.nombre, y.nombre))
        self.cargarGrilla(personal)
        
    @QtCore.pyqtSlot('QString')        
    def on_lineEditBuscarDocumento_textChanged(self, cadena):
        filtro = unicode(cadena)
#        division = Division_Transporte()
#        empleados = division.getEmpleados()
#        values = empleados.values()
        
        personal = filter(lambda p: unicode.lower(filtro) in unicode.lower(unicode(p.documento)), self.empleados)
        personal.sort(cmp=lambda x,y : cmp(x.documento, y.documento))
        self.cargarGrilla(personal) 