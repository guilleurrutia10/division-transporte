# -*- coding: utf-8 -*-
'''
Created on 03/10/2012

@author: Usuario
'''
from PyQt4 import QtCore, QtGui

from formularios.DialogAltaSeccion import Ui_DialogAltaSeccion
from negocio.Division_Transporte import Division_Transporte

class DialogAltaSeccion(QtGui.QDialog, Ui_DialogAltaSeccion):
    '''
    classdocs
    '''
    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super(DialogAltaSeccion, self).__init__(parent)
        self.setupUi(self)
        self.tableWidgetEmpleadosAsignados.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.tableWidgetEmpleadosSinAsignar.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self._encargado = None
        self.filaSeleccionadaAsignados = None
        self.filaSeleccionadaSinAsignar = None
        self.empleadosAsignado = []
        self.empleadosSinAsignar = []
        self.validacionesLineEdit()
        self.conectarSignals()
        self.cargarGrillaInicial()
        
    def validacionesLineEdit(self):
        self.lineEditNombreSeccion.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[A-Za-z]+'), self))
    
    def conectarSignals(self):
        self.tableWidgetEmpleadosSinAsignar.connect(self.tableWidgetEmpleadosSinAsignar, QtCore.SIGNAL('cellClicked(int,int)'), self.celdaClickeada_on_tableWidgetEmpleadosSinAsignar)
        self.tableWidgetEmpleadosAsignados.connect(self.tableWidgetEmpleadosAsignados, QtCore.SIGNAL('cellClicked(int,int)'), self.celdaClickeada_on_tableWidgetEmpleadosAsignados)
        
    @QtCore.pyqtSlot()
    def on_pushButtonAceptar_clicked(self):
        print 'Click sobre Aceptar'
        nombreSeccion = unicode(self.lineEditNombreSeccion.text())
        if len(nombreSeccion) is 0:
            self.mostrarMensaje('Debe ingresar el nombre de la Sección', 'Ingresar Sección')
            return
        try:
            assert not(self.tableWidgetEmpleadosAsignados.rowCount() < 2)
        except AssertionError:
            self.mostrarMensaje('No se han cargado empleados a la Seccion. Debe cargar al menos dos.', 'Cargar Empleados')
            return
        try:
            assert not(self._encargado is None)
        except AssertionError:
            self.mostrarMensaje('No se ha asignado el Encargado de la Seccion.', 'Cargar encargados')
            return
        print 'Cargando Seccion.... Realizar todavía'
        self.cargarSeccion(nombreSeccion)
        if self.mostrarMensaje('La Sección se ha cargado exitosamente! :)', 'Cargando'):
            self.accept()
        
    def cargarSeccion(self, nombreSeccion):
        empleados = []
        for fila in xrange(self.tableWidgetEmpleadosAsignados.columnCount()):
            itemDocumento = self.tableWidgetEmpleadosAsignados.item(fila, 0)
            if  itemDocumento.text() == self._encargado:
                continue
            empleados.append(unicode(itemDocumento.text()))
        division = Division_Transporte()
        division.agregarSecciones(nombreSeccion, empleados, self._encargado)
            
    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        self.reject()
    
    def cargarGrillaInicial(self):
        self.empleados = self.obtenerListaEmpleadosSinAsignar()
        empleados = sorted(self.empleados, cmp=lambda x, y : cmp(x.documento, y.documento))
        self.cargarGrillaEmpleadosSinAsignar(empleados)
    
    def cargarGrillaEmpleadosSinAsignar(self, empleados):
        fila = 0
        self.tableWidgetEmpleadosSinAsignar.clearContents()
        self.tableWidgetEmpleadosSinAsignar.setRowCount(len(empleados))
        for empleado in empleados:
            columna = 0
            itemDocumento = QtGui.QTableWidgetItem()
            itemDocumento.setText(unicode(empleado.documento))
            self.tableWidgetEmpleadosSinAsignar.setItem(fila, columna, itemDocumento)
            columna += 1
            itemNombre = QtGui.QTableWidgetItem()
            itemNombre.setText(unicode(empleado.nombre))
            self.tableWidgetEmpleadosSinAsignar.setItem(fila, columna, itemNombre)
            fila += 1
    
    def obtenerListaEmpleadosSinAsignar(self):
        division = Division_Transporte()
        personal = division.getEmpleadosSinAsignar()
        return personal.values()
    
    def celdaClickeada_on_tableWidgetEmpleadosSinAsignar(self, fila, columna):
        self.filaSeleccionadaSinAsignar = fila
    
    def celdaClickeada_on_tableWidgetEmpleadosAsignados(self, fila, columna):
        self.filaSeleccionadaAsignados = fila
    
    @QtCore.pyqtSlot()
    def on_pushButtonAsignarEmpleado_clicked(self):
        try:
            assert not self.filaSeleccionadaSinAsignar is None
        except AssertionError:
            self.mostrarMensaje('Debe Seleccionar un Empleado.', 'Seleccionar')
            return
        documento = self.tableWidgetEmpleadosSinAsignar.item(self.filaSeleccionadaSinAsignar, 0).text()
        self.tableWidgetEmpleadosSinAsignar.removeRow(self.filaSeleccionadaSinAsignar)
        division = Division_Transporte()
        empleado = division.getEmpleado(unicode(documento))
        self.empleadosAsignado.append(empleado)
        self.empleados.remove(empleado)
        self.cargarGrillaEmpleadosAsignados(self.empleadosAsignado)
        self.filaSeleccionadaSinAsignar = None
    
    @QtCore.pyqtSlot()
    def on_pushButtonDesasignarEmpleado_clicked(self):
        try:
            assert not self.filaSeleccionadaAsignados is None
        except AssertionError:
            self.mostrarMensaje('Debe Seleccionar un Empleado.', 'Seleccionar')
            return
        documento = self.tableWidgetEmpleadosAsignados.item(self.filaSeleccionadaAsignados, 0).text()
        self.tableWidgetEmpleadosAsignados.removeRow(self.filaSeleccionadaAsignados)
        division = Division_Transporte()
        empleado = division.getEmpleado(unicode(documento))
        self.empleados.append(empleado)
        self.empleadosAsignado.remove(empleado)
        self.cargarGrillaEmpleadosSinAsignar(self.empleados)
        self.filaSeleccionadaAsignados = None
        if self._encargado == empleado.documento:
            self._encargado = None

    @QtCore.pyqtSlot()
    def on_pushButtonAsignarComoEncargado_clicked(self):
        print 'Asignando Encargado'
        try:
            if self._encargado:
                self.mostrarMensaje('Ya seleccionó el encargado.', 'Selección de encargado')
                return
            assert not((self.filaSeleccionadaAsignados is None))
        except AssertionError:
            self.mostrarMensaje('Debe Seleccionar un Empleado.', 'Seleccionar')
            return
        documento = self.tableWidgetEmpleadosAsignados.item(self.filaSeleccionadaAsignados, 0).text()
        nombre = self.tableWidgetEmpleadosAsignados.item(self.filaSeleccionadaAsignados, 1).text()
        self._encargado = unicode(documento)
        self.filaSeleccionadaAsignados = None
        self.mostrarMensaje('El encargado %s se cargado correctamente. :)' % nombre, 'Cargando Encargado')
        
    '''
    TODO: Este método se repite en varios Dialogs.
    '''
    def mostrarMensaje(self, mensaje, titulo):
        msgBox = QtGui.QMessageBox(self)
        msgBox.setText(QtCore.QString.fromUtf8(mensaje))
        msgBox.setWindowTitle(QtCore.QString.fromUtf8(titulo))
        return msgBox.exec_()
    
    def cargarGrillaEmpleadosAsignados(self, empleados):
        fila = 0
        self.tableWidgetEmpleadosAsignados.clearContents()
        self.tableWidgetEmpleadosAsignados.setRowCount(len(empleados))
        for empleado in empleados:
            columna = 0
            itemDocumento = QtGui.QTableWidgetItem()
            itemDocumento.setText(unicode(empleado.documento))
            self.tableWidgetEmpleadosAsignados.setItem(fila, columna, itemDocumento)
            columna += 1
            itemNombre = QtGui.QTableWidgetItem()
            itemNombre.setText(unicode(empleado.nombre))
            self.tableWidgetEmpleadosAsignados.setItem(fila, columna, itemNombre)
            fila += 1
