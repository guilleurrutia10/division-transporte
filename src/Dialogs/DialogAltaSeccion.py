# -*- coding: utf-8 -*-
'''
Created on 03/10/2012

@author: Usuario
'''
from PyQt4 import QtCore, QtGui

from formularios.DialogAltaSeccion import Ui_DialogAltaSeccion
from negocio.Division_Transporte import Division_Transporte
from FormContrasenaEncargado import DialogCrearUsuarioEncargado

from Utiles_Dialogo import mostrarMensaje

COLUMNA_DNI = 0

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
        self.filaSeleccionadaAsignados = None
        self.filaSeleccionadaSinAsignar = None
        self.empleadosAsignados = [] #Lista que contendra todos los objetos Empleado que estan siendo asignados a la nueva seccion,
        self.empleadosSinSeccion = [] #Lista que contendra todos los objetos Empleado que estan disponibles para la nueva seccion,
        self.validacionesLineEdit()
        self.conectarSignals()
        self.cargarGrillaInicial()
        #objeto Empleado asignado como Encargado de la nueva Seccion
        self._encargado = None
        #Desactivado al principio!
        self.pushButtonDesasignarEncargado.setDisabled(True)
        
    def validacionesLineEdit(self):
        self.lineEditNombreSeccion.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[A-Za-z]+'), self))
    
    def conectarSignals(self):
        self.tableWidgetEmpleadosSinAsignar.connect(self.tableWidgetEmpleadosSinAsignar, QtCore.SIGNAL('cellClicked(int,int)'), self.celdaClickeada_on_tableWidgetEmpleadosSinAsignar)
        self.tableWidgetEmpleadosAsignados.connect(self.tableWidgetEmpleadosAsignados, QtCore.SIGNAL('cellClicked(int,int)'), self.celdaClickeada_on_tableWidgetEmpleadosAsignados)
        
    @QtCore.pyqtSlot()
    def on_pushButtonAceptar_clicked(self):
        
        nombreSeccion = unicode(self.lineEditNombreSeccion.text())
        if len(nombreSeccion) is 0:
            mostrarMensaje(self, 'Debe ingresar el nombre de la Sección', 'Ingresar Sección')
            return
        try:
            assert not(self.tableWidgetEmpleadosAsignados.rowCount() < 2)
        except AssertionError:
            mostrarMensaje(self, 'No se han cargado empleados a la Seccion. Debe cargar al menos dos.', 'Error al cargar empleados')
            return
        try:
            assert not(self._encargado is None)
        except AssertionError:
            mostrarMensaje(self, 'No se ha asignado el Encargado de la Seccion.', 'Error al cargar encargado')
            return
        print 'Cargando la nueva Seccion...'
        
        self._encargado.setPassword('') #Seteamos una variable dinamica en el encargado
        self.pedirPassEncargado()
        if self._encargado.getPassword() == '': return
        #while self._encargado.getPassword() == '':
        #    self.pedirPassEncargado()
        
        #agregarSeccion se va a encargar tmb de registrar el Usuario del encargado y registrarlo...
        Division_Transporte().agregarSeccion(nombreSeccion, self.empleadosAsignados , self._encargado)
        
        if mostrarMensaje(self, 'La Sección se ha cargado exitosamente! :)', 'Cargando'):
            self.accept()
    
    def pedirPassEncargado(self):
        '''
            Crea un Usuario nuevo para que el Encargado de la Seccion pueda logearse como tal.
            @precondition: self._encargado != None.
        '''
        dialog = DialogCrearUsuarioEncargado(self._encargado.nombreCompletoUsr())
        
        if dialog.exec_() == QtGui.QDialog.Accepted:
            self._encargado.setPassword(dialog.getPassEncargado())
            print 'Pass Encargado: %s' % (dialog.getPassEncargado())
        
         
    
    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        self.reject()
    
    def cargarGrillaInicial(self):
        self.empleadosSinSeccion = self.obtenerListaEmpleadosSinAsignar()
        self.empleadosSinSeccion = sorted(self.empleadosSinSeccion, cmp=lambda x, y : cmp(x.documento, y.documento))
        self.tableWidgetEmpleadosSinAsignar.cargarGrilla(self.empleadosSinSeccion)
        
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
            mostrarMensaje(self, 'Debe Seleccionar un Empleado.', 'Seleccionar')
            return
        documento = self.tableWidgetEmpleadosSinAsignar.item(self.filaSeleccionadaSinAsignar, COLUMNA_DNI).text()
        self.tableWidgetEmpleadosSinAsignar.removeRow(self.filaSeleccionadaSinAsignar)
        division = Division_Transporte()
        empleado = division.getEmpleado(unicode(documento))
        self.empleadosAsignados.append(empleado)
        self.empleadosSinSeccion.remove(empleado)
        self.tableWidgetEmpleadosAsignados.cargarGrilla(self.empleadosAsignados)
        self.filaSeleccionadaSinAsignar = None
    
    @QtCore.pyqtSlot()
    def on_pushButtonDesasignarEmpleado_clicked(self):
        try:
            assert not self.filaSeleccionadaAsignados is None
        except AssertionError:
            mostrarMensaje(self, 'Debe Seleccionar un Empleado.', 'Seleccionar')
            return
        documento = self.tableWidgetEmpleadosAsignados.item(self.filaSeleccionadaAsignados, COLUMNA_DNI).text()
        self.tableWidgetEmpleadosAsignados.removeRow(self.filaSeleccionadaAsignados)
        division = Division_Transporte()
        empleado = division.getEmpleado(unicode(documento))
        self.empleadosSinSeccion.append(empleado)
        self.empleadosAsignados.remove(empleado)
        self.tableWidgetEmpleadosSinAsignar.cargarGrilla(self.empleadosSinSeccion)
        self.filaSeleccionadaAsignados = None

    @QtCore.pyqtSlot()
    def on_pushButtonAsignarComoEncargado_clicked(self):
        print 'Asignando Encargado'
        try:
            #El boton directamente esta desactivado cuando ya se asigno un encargado!
            assert not((self.filaSeleccionadaSinAsignar is None))
        except AssertionError:
            mostrarMensaje(self, 'Debe Seleccionar un Empleado.', 'Seleccionar')
            return
        #documentoDelEncargado = self.tableWidgetEmpleadosAsignados.item(self.filaSeleccionadaSinAsignar, 0).text()
        documentoDelEncargado = self.tableWidgetEmpleadosSinAsignar.item(self.filaSeleccionadaSinAsignar, 0).text()
        #Paso1, setear el encargado de la seccion
        self._encargado = Division_Transporte().getEmpleado(unicode(documentoDelEncargado))
        #Paso2, refrescar la grilla del encargado
        #self.cargarGrillaEmpleados(self.tableWidgetEncargadoAsignado, [self._encargado])
        self.tableWidgetEncargadoAsignado.cargarGrilla([self._encargado])
        #Paso3, remover al encargados de los empleados disponibles y de la grilla
        self.empleadosSinSeccion.remove(self._encargado)
        self.tableWidgetEmpleadosSinAsignar.removeRow(self.filaSeleccionadaSinAsignar)
        #Paso4, desactivar el boton de asignar encargado y activar el de desasignacion
        self.pushButtonAsignarComoEncargado.setDisabled(True)
        self.pushButtonDesasignarEncargado.setDisabled(False)
        
        self.filaSeleccionadaSinAsignar = None
        #mostrarMensaje(self, 'El encargado %s se cargado correctamente. :)' % self._encargado.nombre, 'Cargando Encargado')

    @QtCore.pyqtSlot()
    def on_pushButtonDesasignarEncargado_clicked(self):
        #Paso1, devolver al encargado a la lista de empleados disponibles
        self.empleadosSinSeccion.append(self._encargado)
        #Paso2, Refrescar grilla empleados disponibles
        #self.cargarGrillaEmpleados(self.tableWidgetEmpleadosSinAsignar, self.empleados)
        self.tableWidgetEmpleadosSinAsignar.cargarGrilla(self.empleadosSinSeccion)
        #Paso3, setear el encargado de la seccion
        self._encargado = None
        #Paso4, refrescar la grilla del encargado
        #self.cargarGrillaEmpleados(self.tableWidgetEncargadoAsignado, [])
        self.tableWidgetEncargadoAsignado.cargarGrilla([])
        
        #Paso5, desactivar el boton de desasignar encargado y activar el de asignacion
        self.pushButtonAsignarComoEncargado.setDisabled(False)
        self.pushButtonDesasignarEncargado.setDisabled(True)


## -*- coding: utf-8 -*-
#'''
#Created on 03/10/2012
#
#@author: Usuario
#'''
#from PyQt4 import QtCore, QtGui
#
#from formularios.DialogAltaSeccion import Ui_DialogAltaSeccion
#from negocio.Division_Transporte import Division_Transporte
#
#from Utiles_Dialogo import mostrarMensaje
#COLUMNA_DNI = 0
#
#class DialogAltaSeccion(QtGui.QDialog, Ui_DialogAltaSeccion):
#    '''
#    classdocs
#    '''
#    def __init__(self, parent=None):
#        '''
#        Constructor
#        '''
#        super(DialogAltaSeccion, self).__init__(parent)
#        self.setupUi(self)
#        self.tableWidgetEmpleadosAsignados.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
#        self.tableWidgetEmpleadosSinAsignar.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
#        self._dni_encargado = None
#        self.filaSeleccionadaAsignados = None
#        self.filaSeleccionadaSinAsignar = None
#        self.empleadosAsignado = []
#        self.empleadosSinAsignar = []
#        self.validacionesLineEdit()
#        self.conectarSignals()
#        self.cargarGrillaInicial()
#        #Encargado
#        self._encargado = None
#        
#    def validacionesLineEdit(self):
#        self.lineEditNombreSeccion.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[A-Za-z]+'), self))
#    
#    def conectarSignals(self):
#        self.tableWidgetEmpleadosSinAsignar.connect(self.tableWidgetEmpleadosSinAsignar, QtCore.SIGNAL('cellClicked(int,int)'), self.celdaClickeada_on_tableWidgetEmpleadosSinAsignar)
#        self.tableWidgetEmpleadosAsignados.connect(self.tableWidgetEmpleadosAsignados, QtCore.SIGNAL('cellClicked(int,int)'), self.celdaClickeada_on_tableWidgetEmpleadosAsignados)
#        
#    @QtCore.pyqtSlot()
#    def on_pushButtonAceptar_clicked(self):
#        
#        nombreSeccion = unicode(self.lineEditNombreSeccion.text())
#        if len(nombreSeccion) is 0:
#            mostrarMensaje(self, 'Debe ingresar el nombre de la Sección', 'Ingresar Sección')
#            return
#        try:
#            assert not(self.tableWidgetEmpleadosAsignados.rowCount() < 2)
#        except AssertionError:
#            mostrarMensaje(self, 'No se han cargado empleados a la Seccion. Debe cargar al menos dos.', 'Error al cargar empleados')
#            return
#        try:
#            assert not(self._dni_encargado is None)
#        except AssertionError:
#            mostrarMensaje(self, 'No se ha asignado el Encargado de la Seccion.', 'Error al cargar encargado')
#            return
#        print 'Cargando Seccion.... Realizar todavía'
#        
#        empleados_dni = self.get_dni_empleados(nombreSeccion)
#        division = Division_Transporte()
#        division.agregarSecciones(nombreSeccion, empleados_dni , self._dni_encargado)
#        
#        if mostrarMensaje(self, 'La Sección se ha cargado exitosamente! :)', 'Cargando'):
#            self.accept()
#        
#    def get_dni_empleados(self, nombreSeccion):
#        """
#            Devuelve una lista con los nros de dni de los empleados seleccionados para la seccion
#        """
#        empleados = []
#        for fila in xrange(self.tableWidgetEmpleadosAsignados.columnCount()):
#            itemDocumento = self.tableWidgetEmpleadosAsignados.item(fila, COLUMNA_DNI)
#            if  itemDocumento.text() == self._dni_encargado:
#                continue
#            empleados.append(unicode(itemDocumento.text()))
#        
#        return empleados
#        #division = Division_Transporte()
#        #division.agregarSecciones(nombreSeccion, empleados, self._dni_encargado)
#            
#    @QtCore.pyqtSlot()
#    def on_pushButtonCancelar_clicked(self):
#        self.reject()
#    
#    def cargarGrillaInicial(self):
#        self.empleados = self.obtenerListaEmpleadosSinAsignar()
#        empleados = sorted(self.empleados, cmp=lambda x, y : cmp(x.documento, y.documento))
#        self.cargarGrillaEmpleadosSinAsignar(empleados)
#    
#    def cargarGrillaEmpleadosSinAsignar(self, empleados):
#        fila = 0
#        self.tableWidgetEmpleadosSinAsignar.clearContents()
#        self.tableWidgetEmpleadosSinAsignar.setRowCount(len(empleados))
#        for empleado in empleados:
#            columna = 0
#            itemDocumento = QtGui.QTableWidgetItem()
#            itemDocumento.setText(unicode(empleado.documento))
#            self.tableWidgetEmpleadosSinAsignar.setItem(fila, columna, itemDocumento)
#            columna += 1
#            itemNombre = QtGui.QTableWidgetItem()
#            itemNombre.setText(unicode(empleado.nombre))
#            self.tableWidgetEmpleadosSinAsignar.setItem(fila, columna, itemNombre)
#            fila += 1
#
#    def cargarGrillaEmpleadosAsignados(self, empleados):
#        fila = 0
#        self.tableWidgetEmpleadosAsignados.clearContents()
#        self.tableWidgetEmpleadosAsignados.setRowCount(len(empleados))
#        for empleado in empleados:
#            columna = 0
#            itemDocumento = QtGui.QTableWidgetItem()
#            itemDocumento.setText(unicode(empleado.documento))
#            self.tableWidgetEmpleadosAsignados.setItem(fila, columna, itemDocumento)
#            columna += 1
#            itemNombre = QtGui.QTableWidgetItem()
#            itemNombre.setText(unicode(empleado.nombre))
#            self.tableWidgetEmpleadosAsignados.setItem(fila, columna, itemNombre)
#            fila += 1
#
#    #TODO: Podriamos usar este, generico, en lugar de los dos de arriba, llamar cargarGrillaEmpleados(self.tableWidgetEmpleadosAsignados/self.tableWidgetEmpleadosSinAsignar, empleados) 
#    def cargarGrillaEmpleados(self, grilla, empleados):
#        fila = 0
#        grilla.clearContents()
#        grilla.setRowCount(len(empleados))
#        for empleado in empleados:
#            columna = 0
#            itemDocumento = QtGui.QTableWidgetItem()
#            itemDocumento.setText(unicode(empleado.documento))
#            grilla.setItem(fila, columna, itemDocumento)
#            columna += 1
#            itemNombre = QtGui.QTableWidgetItem()
#            itemNombre.setText(unicode(empleado.nombre))
#            grilla.setItem(fila, columna, itemNombre)
#            fila += 1
#    
#    def obtenerListaEmpleadosSinAsignar(self):
#        division = Division_Transporte()
#        personal = division.getEmpleadosSinAsignar()
#        return personal.values()
#    
#    def celdaClickeada_on_tableWidgetEmpleadosSinAsignar(self, fila, columna):
#        self.filaSeleccionadaSinAsignar = fila
#    
#    def celdaClickeada_on_tableWidgetEmpleadosAsignados(self, fila, columna):
#        self.filaSeleccionadaAsignados = fila
#    
#    @QtCore.pyqtSlot()
#    def on_pushButtonAsignarEmpleado_clicked(self):
#        try:
#            assert not self.filaSeleccionadaSinAsignar is None
#        except AssertionError:
#            mostrarMensaje(self, 'Debe Seleccionar un Empleado.', 'Seleccionar')
#            return
#        documento = self.tableWidgetEmpleadosSinAsignar.item(self.filaSeleccionadaSinAsignar, 0).text()
#        self.tableWidgetEmpleadosSinAsignar.removeRow(self.filaSeleccionadaSinAsignar)
#        division = Division_Transporte()
#        empleado = division.getEmpleado(unicode(documento))
#        self.empleadosAsignado.append(empleado)
#        self.empleados.remove(empleado)
#        self.cargarGrillaEmpleadosAsignados(self.empleadosAsignado)
#        self.filaSeleccionadaSinAsignar = None
#    
#    @QtCore.pyqtSlot()
#    def on_pushButtonDesasignarEmpleado_clicked(self):
#        try:
#            assert not self.filaSeleccionadaAsignados is None
#        except AssertionError:
#            mostrarMensaje(self, 'Debe Seleccionar un Empleado.', 'Seleccionar')
#            return
#        documento = self.tableWidgetEmpleadosAsignados.item(self.filaSeleccionadaAsignados, 0).text()
#        self.tableWidgetEmpleadosAsignados.removeRow(self.filaSeleccionadaAsignados)
#        division = Division_Transporte()
#        empleado = division.getEmpleado(unicode(documento))
#        self.empleados.append(empleado)
#        self.empleadosAsignado.remove(empleado)
#        self.cargarGrillaEmpleadosSinAsignar(self.empleados)
#        self.filaSeleccionadaAsignados = None
#        if self._dni_encargado == empleado.documento:
#            self._dni_encargado = None
#
#    @QtCore.pyqtSlot()
#    def on_pushButtonAsignarComoEncargado_clicked(self):
#        print 'Asignando Encargado'
#        try:
#            # Esto ya no es necesario, hay que desactivar el boton directamente, cuando ya se asigno un encargado!
#            #if self._dni_encargado:
#            #    mostrarMensaje(self, 'Ya seleccionó el encargado.', 'Selección de encargado')
#            #    return
#            #assert not((self.filaSeleccionadaAsignados is None))
#            assert not((self.filaSeleccionadaSinAsignar is None))
#        except AssertionError:
#            mostrarMensaje(self, 'Debe Seleccionar un Empleado.', 'Seleccionar')
#            return
#        #documentoDelEncargado = self.tableWidgetEmpleadosAsignados.item(self.filaSeleccionadaSinAsignar, 0).text()
#        documentoDelEncargado = self.tableWidgetEmpleadosSinAsignar.item(self.filaSeleccionadaSinAsignar, 0).text()
#        #Paso1, setear el encargado de la seccion
#        self._encargado = Division_Transporte().getEmpleado(unicode(documentoDelEncargado))
#        #Paso2, refrescar la grilla del encargado
#        self.cargarGrillaEmpleados(self.tableWidgetEncargadoAsignado, [self._encargado])
#        #Paso3, remover al encargados de los empleados disponibles y de la grilla
#        self.empleados.remove(self._encargado)
#        self.tableWidgetEmpleadosSinAsignar.removeRow(self.filaSeleccionadaSinAsignar)
#        #Paso4, desactivar el boton de asignar encargado y activar el de desasignacion
#        self.pushButtonAsignarComoEncargado.setDisabled(True)
#        self.pushButtonDesasignarEncargado.setDisabled(False)
#        
#        #nombre = self.tableWidgetEmpleadosAsignados.item(self.filaSeleccionadaAsignados, 1).text()
#        self._dni_encargado = unicode(documentoDelEncargado)
#        self.filaSeleccionadaSinAsignar = None
#        mostrarMensaje(self, 'El encargado %s se cargado correctamente. :)' % self._encargado.nombre, 'Cargando Encargado')
#
#    @QtCore.pyqtSlot()
#    def on_pushButtonDesasignarEncargado_clicked(self):
#        #Paso1, devolver al encargado a la lista de empleados disponibles
#        self.empleados.append(self._encargado)
#        #Paso2, Refrescar grilla empleados disponibles
#        self.cargarGrillaEmpleados(self.tableWidgetEmpleadosSinAsignar, self.empleados)
#        #Paso3, setear el encargado de la seccion
#        self._encargado = None
#        #Paso4, refrescar la grilla del encargado
#        self.cargarGrillaEmpleados(self.tableWidgetEncargadoAsignado, [])
#        
#        #Paso5, desactivar el boton de desasignar encargado y activar el de asignacion
#        self.pushButtonAsignarComoEncargado.setDisabled(False)
#        self.pushButtonDesasignarEncargado.setDisabled(True)
#        
#         
#    '''
#    TODO[OK]: Este método se repite en varios Dialogs.
#    
#    def mostrarMensaje(self, mensaje, titulo):
#        msgBox = QtGui.QMessageBox(self)
#        msgBox.setText(QtCore.QString.fromUtf8(mensaje))
#        msgBox.setWindowTitle(QtCore.QString.fromUtf8(titulo))
#        return msgBox.exec_()
#    '''