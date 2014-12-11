# -*- coding: utf-8 -*-
'''
Created on 22/11/2012

@author: urrutia
'''

from PyQt4 import QtCore, QtGui

from formularios.DialogBajaPersonal import Ui_DialogBajaPersonal
from formularios.DialogAsignarFechaDeBaja import Ui_DialogAsignarFechaBaja
from negocio.Division_Transporte import Division_Transporte
from Utiles_Dialogo import Mensaje, mostrarMensaje
from datetime import date
            
class DialogBajaPersonal(QtGui.QDialog, Ui_DialogBajaPersonal):
    '''
    Elementos:
        - tableWidgetDatosEmpleados
        - pushButtonCancelar
        - pushButtonDarDeBaja
    '''
    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super(DialogBajaPersonal, self).__init__(parent)
        self.setupUi(self)
        # Variable para mantener una lista con los empleados y evitar la
        # consulta continua a la BD.
        self.empleados = None
        self.refrescarTabla()
        self.tableWidgetDatosEmpleados.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        
        self.tableWidgetDatosEmpleados.connect(self.tableWidgetDatosEmpleados, QtCore.SIGNAL('cellClicked(int,int)'), self.celdaClickeada)

        self._empleadoSeleccionado = None

    def refrescarTabla(self):
        self.empleados = self.obtenerListaEmpleados()
        self.empleados.sort(cmp=lambda x, y: cmp(x.nombre, y.nombre))
        #self.cargaGrillaInicial()
        self.tableWidgetDatosEmpleados.cargarConEmpleados(self.empleados)

    def cargaGrillaInicial(self):
        self.empleados = self.obtenerListaEmpleados()
        self.empleados.sort(cmp=lambda x, y: cmp(x.nombre, y.nombre))
        self.cargarGrilla(self.empleados)

    def cargarGrilla(self, empleados):
        self.tableWidgetDatosEmpleados.clearContents()
        self.tableWidgetDatosEmpleados.setRowCount(len(empleados))
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
            # Tener en cuenta a posterior.....
#             columna += 1
#             itemSeccion = QtGui.QTableWidgetItem()
#             itemSeccion.setText(empleado.getSeccion)
#             self.tableWidgetDatosEmpleados.setItem(fila, columna, itemSeccion)
#             columna += 1
#             itemFechaNac = QtGui.QTableWidgetItem()
#             itemFechaNac.setText(empleado.getFechaNacimiento())
#             self.tableWidgetDatosEmpleados.setItem(fila, columna, itemFechaNac)
#             columna += 1
#             itemDomicilio = QtGui.QTableWidgetItem()
#             itemDomicilio.setText(empleado.getDomicilio())
#             self.tableWidgetDatosEmpleados.setItem(fila, columna, itemDomicilio)
#             columna += 1
#             itemMail = QtGui.QTableWidgetItem()
#             itemMail.setText(empleado.getEmail())
#             self.tableWidgetDatosEmpleados.setItem(fila, columna, itemMail)
#             columna += 1
#             itemTelefono = QtGui.QTableWidgetItem()
#             itemTelefono.setText(empleado.getTelefono())
#             self.tableWidgetDatosEmpleados.setItem(fila, columna, itemTelefono)

            fila += 1

    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        '''
        '''
        self.reject()

    @QtCore.pyqtSlot()
    def on_pushButtonDarDeBaja_clicked(self):
        '''
        '''
        try:
            if self.itemDocumento:
#                dlgAsignarFecha = DialogAsignarFechaDeBaja(self._empleadoSeleccionado)
                dlgAsignarFecha = DialogAsignarFechaDeBaja(self.tableWidgetDatosEmpleados.getElementoSeleccionado())
                self.itemDocumento = None
                dlgAsignarFecha.exec_()
                self.refrescarTabla()
            else:
                self.mostrarMensaje('Debe Seleccionar un Empleado.', 'Seleccionar Empleado')
        except AttributeError, e:
            print e
            self.mostrarMensaje('Debe Seleccionar un Empleado.', 'Seleccionar Empleado')

#    @QtCore.pyqtSlot('QString')
#    def on_lineEditBuscarNombre_textChanged(self, cadena):
#        '''
#        '''
#        filtro = unicode(cadena)
#        personal = filter(lambda p: unicode.lower(filtro) in unicode.lower(unicode(p.nombre)), self.empleados)
#        personal.sort(cmp=lambda x, y: cmp(x.nombre, y.nombre))
##        self.cargarGrilla(personal)
#        self.tableWidgetDatosEmpleados.cargarConEmpleados(personal)

    def filtrame(self, filtrovalue, persona):
        return unicode.lower(filtrovalue) in unicode.lower(unicode(persona.documento)) or unicode.lower(filtrovalue) in unicode.lower(unicode(persona.nombre)) or unicode.lower(filtrovalue) in unicode.lower(unicode(persona.getApellido()))
    
    @QtCore.pyqtSlot('QString')
    def on_lineEditBuscarDocumento_textChanged(self, cadena):
        '''
        Filtra por nombre, apellido y nro de documento
        '''
        filtro = unicode(cadena)
        personal = filter(lambda p: self.filtrame(filtro, p), self.empleados)
        personal.sort(cmp=lambda x, y: cmp(x.documento, y.documento))
        self.cargarGrilla(personal)
        self.tableWidgetDatosEmpleados.cargarConEmpleados(personal)

    def celdaClickeada(self, fila, columna):
        print 'Celda clickeada fila %s columna %s' % (fila, columna)
        self.itemDocumento = self.tableWidgetDatosEmpleados.item(fila, 3)
        documento = self.itemDocumento.text()
        empleados = Division_Transporte().getEmpleados().values()
        for e in empleados:
            if e.getDocumento() == documento:
                self._empleadoSeleccionado = e
                return

    '''
    TODO: Se ha repetido este mismo método en varias de las clsase Dialogos.
    '''
    def mostrarMensaje(self, mensaje, titulo):
        '''
        Función que muestra un pequeña ventana con información relevante.
        '''
        msgBox = QtGui.QMessageBox(self)
        msgBox.setText(QtCore.QString.fromUtf8(mensaje))
        msgBox.setWindowTitle(QtCore.QString.fromUtf8(titulo))
        return msgBox.exec_()

    def obtenerListaEmpleados(self):
        division = Division_Transporte()
        personal = division.getEmpleadosSinAsignar()
        return personal.values()


class DialogAsignarFechaDeBaja(QtGui.QDialog, Ui_DialogAsignarFechaBaja):
    '''
    Elementos
        - calendarWidgetRegistrarBaja
        - pushButtonAceptar
        - pushButtonCancelar
    '''
    def __init__(self, empleado=None, parent=None):
        '''
        Constructor
        '''
        super(DialogAsignarFechaDeBaja, self).__init__(parent)
        self.setupUi(self)
        self._empleado = empleado
        hoy = date.today()
        fecha_tope_bajo = self._empleado.getFechaAlta()
        #self.calendarWidgetRegistrarBaja.setMaximumDate(QtCore.QDate(hoy.year, hoy.month, hoy.day))
        self.calendarWidgetRegistrarBaja.setSelectedDate(QtCore.QDate(hoy.year, hoy.month, hoy.day))
        self.calendarWidgetRegistrarBaja.setMinimumDate(QtCore.QDate(fecha_tope_bajo.year, fecha_tope_bajo.month, fecha_tope_bajo.day))
        self._fechaSeleccionada = None

    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        '''
        Método que se llama al realizar click sobre el botón Cancelar.
        '''
        self.reject()

    @QtCore.pyqtSlot('QDate')
    def on_calendarWidgetRegistrarBaja_clicked(self, date):
        '''
        Método que se llama cuando se hace click sobre el calendario
        para seleccionar una fecha de baja.
        '''
#         from PyQt4.QtCore import QDate
        # QDate.toPyDate() -> datetime.date
        print date.toPyDate().__str__()

    @QtCore.pyqtSlot()
    def on_pushButtonAceptar_clicked(self):
        '''
        Método que se llama al realizar click sobre el botón Aceptar.
        '''
#        print 'Click sobre Aceptar'
#        print self._empleado
        # TODO: Dar de Baja (OK)
        msg = 'Desea remover al empleado \'%s\' de la Division?' %(self._empleado.nombreCompleto())
        msjConfirmar = Mensaje(self, msg, "Confirmar eliminar")
        msjConfirmar.agregarBotonCancelar()
        msjConfirmar.setCritical()
        retorno = msjConfirmar.exec_()
        if retorno == QtGui.QMessageBox.Cancel:
            print "DEBUG: Cancelar accion remover empleado de seccion"
            self.reject()
        if retorno == QtGui.QMessageBox.Ok:
            self._fechaSeleccionada = self.calendarWidgetRegistrarBaja.selectedDate()
            self._fechaSeleccionada = date(self._fechaSeleccionada.year(), self._fechaSeleccionada.month(), self._fechaSeleccionada.day())
            self._empleado.setFechaBaja(self._fechaSeleccionada)
            Division_Transporte().bajaEmpleado(self._empleado)
            msg = 'El empleado \'%s\' ha sido removido de la Division' %(self._empleado.nombreCompleto())
            print 'DEBUG: ', msg
            mostrarMensaje(self, msg, 'Empleado removido')
            self.accept()

    
    def getFechaSeleccionada(self):
        return self._fechaSeleccionada