# -*- coding: utf-8 -*-
'''
Created on 16/11/2012

@author: urrutia
'''

from PyQt4 import QtCore, QtGui

from formularios.WidgetListadoEmpleados import Ui_Form
from negocio.Division_Transporte import Division_Transporte

class WidgetListadoEmpleados(QtGui.QWidget, Ui_Form):
    
    def __init__(self, parent=None):
        super(WidgetListadoEmpleados, self).__init__(parent)
        self.setupUi(self)
        #Para evitar que se modifique la información presentada por la grilla.
        self.tableWidgetDatosEmpleados.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.empleados = None
        self.cargarGrillaInicial()
        
    def cargarGrillaEmpleadosSinAsignar(self, empleados):
        self.tableWidgetDatosEmpleados.clearContents()
        self.tableWidgetDatosEmpleados.setRowCount(len(empleados))
        #Indica la cantidad de columnas a llenar.
        print self.tableWidgetDatosEmpleados.horizontalHeader().count()
        fila = 0
        for empleado in empleados:
            columna = 0
            itemNombre = QtGui.QTableWidgetItem()
            itemNombre.setText(empleado.nombre)
            self.tableWidgetDatosEmpleados.setItem(fila, columna, itemNombre)
            columna += 1
            itemApellido = QtGui.QTableWidgetItem()
            itemApellido.setText(empleado.apellido)
            self.tableWidgetDatosEmpleados.setItem(fila, columna, itemApellido)
            columna += 1
            itemTipoDocumento = QtGui.QTableWidgetItem()
            itemTipoDocumento.setText(empleado.tipoDocumento.get_codigo_tipo_documento())
            self.tableWidgetDatosEmpleados.setItem(fila, columna, itemTipoDocumento)
            columna += 1
            itemDocumento = QtGui.QTableWidgetItem()
            itemDocumento.setText(empleado.documento)
            self.tableWidgetDatosEmpleados.setItem(fila, columna, itemDocumento)
            fila = fila + 1
    
    #===========================================================================
    # Por ahora la única vez que se consulta la BD es al cargar la grilla por
    # primera vez.
    #===========================================================================
    def cargarGrillaInicial(self):
        division = Division_Transporte()
        p = division.getEmpleados()
        self.empleados = p.values()
        self.empleados.sort(cmp=lambda x, y : cmp(x.nombre, y.nombre))
        self.cargarGrillaEmpleadosSinAsignar(self.empleados)
    
    @QtCore.pyqtSlot('QString')        
    def on_lineEditFiltroNombre_textChanged(self, cadena):
        filtro = unicode(cadena)        
        personal = filter(lambda p: unicode.lower(filtro) in unicode.lower(unicode(p.nombre)), self.empleados)
        personal.sort(cmp=lambda x, y : cmp(x.nombre, y.nombre))
        self.cargarGrillaEmpleadosSinAsignar(personal)
        
    @QtCore.pyqtSlot('QString')        
    def on_lineEditBuscarDocumento_textChanged(self, cadena):
        filtro = unicode(cadena)        
        personal = filter(lambda p: unicode.lower(filtro) in unicode.lower(unicode(p.documento)), self.empleados)
        personal.sort(cmp=lambda x, y : cmp(x.documento, y.documento))
        self.cargarGrillaEmpleadosSinAsignar(personal)
