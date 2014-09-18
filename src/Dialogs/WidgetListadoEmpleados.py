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
        # Para evitar que se modifique la información presentada por la grilla.
        self.tableWidgetDatosEmpleados.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.empleados = None
        self.cargarGrillaInicial()
        self.pushButtonToPDF.setObjectName('iconButton')

    # TODO: Utilizar utilies_formularios para la tabla de empleados.
    def cargarGrillaEmpleadosSinAsignar(self, empleados):
        self.tableWidgetDatosEmpleados.clearContents()
        self.tableWidgetDatosEmpleados.setRowCount(len(empleados))
        # Indica la cantidad de columnas a llenar.
        self.tableWidgetDatosEmpleados.horizontalHeader().count()
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
            columna += 1
            itemSeccion = QtGui.QTableWidgetItem()
            itemSeccion.setText('empleado.seccion')
            self.tableWidgetDatosEmpleados.setItem(fila, columna, itemSeccion)
            columna += 1
            itemFechaNac = QtGui.QTableWidgetItem()
            # TODO: Crear metodo para el string de fecha.
            # Para que imprima lindo.
            itemFechaNac.setText(empleado.imprimirFechaNacimiento())
            self.tableWidgetDatosEmpleados.setItem(fila, columna, itemFechaNac)
            columna += 1
            itemDomicilio = QtGui.QTableWidgetItem()
            itemDomicilio.setText(empleado.getDomicilio())
            self.tableWidgetDatosEmpleados.setItem(fila, columna, itemDomicilio)
            columna += 1
            itemEmail = QtGui.QTableWidgetItem()
            itemEmail.setText(empleado.getEmail())
            self.tableWidgetDatosEmpleados.setItem(fila, columna, itemEmail)
            columna += 1
            itemtelefono = QtGui.QTableWidgetItem()
            itemtelefono.setText(empleado.getTelefono())
            self.tableWidgetDatosEmpleados.setItem(fila, columna, itemtelefono)

            fila = fila + 1

    #===========================================================================
    # Por ahora la única vez que se consulta la BD es al cargar la grilla por
    # primera vez.
    #===========================================================================
    def cargarGrillaInicial(self):
        division = Division_Transporte()
        p = division.getEmpleados()
        self.empleados = p.values()
        self.empleados.sort(cmp=lambda x, y: cmp(x.nombre, y.nombre))
        self.cargarGrillaEmpleadosSinAsignar(self.empleados)

#     @QtCore.pyqtSlot('QString')
#     def on_lineEditFiltroNombre_textChanged(self, cadena):
#         filtro = unicode(cadena)
#         personal = filter(lambda p: unicode.lower(filtro) in unicode.lower(unicode(p.nombre)), self.empleados)
#         personal.sort(cmp=lambda x, y: cmp(x.nombre, y.nombre))
#         self.cargarGrillaEmpleadosSinAsignar(personal)

    # De esta manera queda un solo filtro para los strings...
    @QtCore.pyqtSlot('QString')
    def on_lineEditBuscarDocumento_textChanged(self, cadena):
        filtro = unicode(cadena).lower()
        personal = filter(lambda p: filtro in unicode(p.getDocumento()).lower()
                          or filtro in unicode(p.getNombre()).lower()
                          or filtro in unicode(p.getApellido()).lower(),
                          self.empleados)
        personal.sort(cmp=lambda x, y: cmp(x, y))
        self.cargarGrillaEmpleadosSinAsignar(personal)

    @QtCore.pyqtSlot('QDate')
    def on_dateEditFechaInicio_dateChanged(self, date):
        self.filtrarFechaNacimiento()

    @QtCore.pyqtSlot('QDate')
    def on_dateEditFechaFin_dateChanged(self, date):
        self.filtrarFechaNacimiento()

    # TODO: Falta tener en cuenta la fecha de baja y alta.
    def filtrarFechaNacimiento(self):
        personal = filter(lambda p: self.dateEditFechaInicio.date().toPyDate() <= p.getFechaNacimiento()
                          and self.dateEditFechaFin.date().toPyDate() >= p.getFechaNacimiento(),
                          self.empleados)
        personal.sort(cmp=lambda x, y: cmp(x, y))
        self.cargarGrillaEmpleadosSinAsignar(personal)
