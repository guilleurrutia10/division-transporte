# -*- coding: utf-8 -*-
'''
Created on 03/10/2012

@author: Usuario
'''
from PyQt4 import QtCore, QtGui
from formularios.DialogAltaSeccion import Ui_DialogAltaSeccion
from negocio.Division_Transporte import Division_Transporte
from copy import deepcopy

class DialogAltaSeccion(QtGui.QDialog, Ui_DialogAltaSeccion):
    '''
    classdocs
    '''
    def __init__(self, parent = None):
        '''
        Constructor
        '''
        super(DialogAltaSeccion, self).__init__(parent)
        self.setupUi(self)
        self._filaEmpleadoSinAsignar = None
        self._filaEmpleadoAsignados = None
        self._encargado = None
        self.validacionesLineEdit()
        self.cargarGrilla()
        
    def validacionesLineEdit(self):
        self.lineEditNombreSeccion.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[A-Za-z]+'),self))
        self.tableWidgetEmpleadosSinAsignar.connect(self.tableWidgetEmpleadosSinAsignar, QtCore.SIGNAL('cellClicked(int,int)'), self.on_tableWidgetEmpleadosSinAsignar_cellClicked)
        self.tableWidgetEmpleadosAsignados.connect(self.tableWidgetEmpleadosAsignados, QtCore.SIGNAL('cellClicked(int,int)'), self.on_tableWidgetEmpleadosAsignados_cellClicked)
        self.pushButtonAsignarComoEncargado
        
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
            print 'No se han cargado empleados a la Seccion'
            return
        try:
            assert not(self._encargado is None)
        except AssertionError:
            print 'No se ha asignado el Encargado de la Seccion'
            return
        print 'Cargando Seccion.... Realizar todavía'
        nombreSeccion = unicode(self.lineEditNombreSeccion.text())
        division = Division_Transporte()
        empleados = {}
        #Armar un diccionario de empleados con las filas a excepción del encargado.
        for fila in range(self.tableWidgetEmpleadosAsignados.rowCount()):
            item = self.tableWidgetEmpleadosAsignados.item(fila, 0)
            empleado = deepcopy(division.getEmpleado(unicode(item.text())))
            if empleado == self._encargado:
                continue
            empleados[empleado.documento] = empleado
            print empleado.documento
        #Deepcopy xq el objeto que trataba de almacenar de nuevo ya se encontraba 
        #en algún lugar de la BD.
        division.agregarSecciones(nombreSeccion, empleados, deepcopy(self._encargado))
        if self.mostrarMensaje('La Sección se ha cargado exitosamente! :)', 'Cargando'):
            self.accept()
        
    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        self.close()
        
    def cargarGrilla(self):
        #=======================================================================
        # Acordarse de realizar el filtrado de aquellos empleados que no se 
        # encuentran asignados a ninguna sección. Pedirselo a la División a través
        # del método -- Division.getEmpleadosSinAsignar() --
        #=======================================================================
        division = Division_Transporte()
        empleados = division.getEmpleadosSinAsignar()
        fila = 0
        self.tableWidgetEmpleadosSinAsignar.setRowCount(len(empleados))
        for clave,empl in empleados.iteritems():
#            print '%s,%s'%(fila, columna), clave, empl
            columna = 0
            miItem1 = QtGui.QTableWidgetItem()
            miItem1.setText(unicode(empl.documento))
            self.tableWidgetEmpleadosSinAsignar.setItem(fila,columna,miItem1)
            columna += 1
            miItem2 = QtGui.QTableWidgetItem()
            miItem2.setText(unicode(empl.nombre))
            self.tableWidgetEmpleadosSinAsignar.setItem(fila,columna,miItem2)
            fila += 1
    
#    @QtCore.pyqtSlot('int,int')
    def on_tableWidgetEmpleadosSinAsignar_cellClicked(self, fila, columna):
        print fila, ',' , columna
        self._filaEmpleadoSinAsignar = {}
        item1 = QtGui.QTableWidgetItem()
        item = self.tableWidgetEmpleadosSinAsignar.item(fila, 0)
        item1.setText(item.text())
        self._filaEmpleadoSinAsignar[item1.text()] = item1
        print item.text()
        item2 = QtGui.QTableWidgetItem()
        item = self.tableWidgetEmpleadosSinAsignar.item(fila, 1)
        print item.text()
        item2.setText(item.text())
        self._filaEmpleadoSinAsignar[item2.text()] = item2
        self._filaEmpleadoSinAsignar['fila'] = fila
    
    def on_tableWidgetEmpleadosAsignados_cellClicked(self, fila, columna):
        print fila, ',' , columna
        self._filaEmpleadoAsignados = {}
        item1 = QtGui.QTableWidgetItem()
        item = self.tableWidgetEmpleadosAsignados.item(fila, 0)
        item1.setText(item.text())
        self._filaEmpleadoAsignados['documento'] = item1
#        self._filaEmpleadoSinAsignar[item1.text()] = item1
        print item.text()
        item2 = QtGui.QTableWidgetItem()
        item = self.tableWidgetEmpleadosAsignados.item(fila, 1)
        print item.text()
        item2.setText(item.text())
        self._filaEmpleadoAsignados['nombre'] = item2
#        self._filaEmpleadoSinAsignar[item2.text()] = item2
        self._filaEmpleadoAsignados['fila'] = fila
    
    @QtCore.pyqtSlot()
    def on_pushButtonAsignarEmpleado_clicked(self):
        print 'Asignando empleado'
        try:
            assert not(self._filaEmpleadoSinAsignar is None)
        except AssertionError:
            self.mostrarMensaje('Debe Seleccionar un Empleado.', 'Seleccionar')
            return
        fila = self.tableWidgetEmpleadosAsignados.rowCount()
        col = 0
        cantFilas = self.tableWidgetEmpleadosAsignados.rowCount() + 1
        self.tableWidgetEmpleadosAsignados.setRowCount(cantFilas)
        for clave, valor in self._filaEmpleadoSinAsignar.iteritems():
            if clave is 'fila':
                self.tableWidgetEmpleadosSinAsignar.removeRow(valor)
                continue
            self.tableWidgetEmpleadosAsignados.setItem(fila,col,valor)
            col +=1
        self._filaEmpleadoSinAsignar.clear()
        self._filaEmpleadoSinAsignar = None
        print self._filaEmpleadoSinAsignar
    
    @QtCore.pyqtSlot()
    def on_pushButtonDesasignarEmpleado_clicked(self):
        '''
        TODO: Mejorar la modularizacion.
        '''
        print 'Desasignando empleado'
        try:
            assert not(self._filaEmpleadoAsignados is None)
        except AssertionError:
            self.mostrarMensaje('Debe Seleccionar un Empleado.', 'Seleccionar')
            return
        fila = self.tableWidgetEmpleadosSinAsignar.rowCount()
        col = 0
        cantFilas = self.tableWidgetEmpleadosSinAsignar.rowCount() + 1
        self.tableWidgetEmpleadosSinAsignar.setRowCount(cantFilas)
        for clave, valor in self._filaEmpleadoAsignados.iteritems():
            if clave is 'fila':
                self.tableWidgetEmpleadosAsignados.removeRow(valor)
                continue
            self.tableWidgetEmpleadosSinAsignar.setItem(fila,col,valor)
            col +=1
        self._filaEmpleadoAsignados.clear() 
        self._filaEmpleadoAsignados = None
        print self._filaEmpleadoAsignados
        
    @QtCore.pyqtSlot()
    def on_pushButtonAsignarComoEncargado_clicked(self):
        print 'Asignando Encargado'
        try:
            assert not(self._filaEmpleadoAsignados is None)
        except AssertionError:
            self.mostrarMensaje('Debe Seleccionar un Empleado.', 'Seleccionar')
            return
        itemDocumento = self._filaEmpleadoAsignados['documento']
        division = Division_Transporte()
        self._encargado = division.getEmpleado(unicode(itemDocumento.text()))
        self._filaEmpleadoAsignados.clear() 
        self._filaEmpleadoAsignados = None
        print self._filaEmpleadoAsignados
        self.mostrarMensaje('El encargado %s se cargado correctamente. :)'%self._encargado.nombre, 'Cargando Encargado')
        
    '''
    TODO: Este método se repite en varios Dialogs.
    '''
    def mostrarMensaje(self, mensaje, titulo):
        msgBox = QtGui.QMessageBox(self)
        msgBox.setText(QtCore.QString.fromUtf8(mensaje))
        msgBox.setWindowTitle(QtCore.QString.fromUtf8(titulo))
        return msgBox.exec_()