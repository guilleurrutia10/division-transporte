# -*- coding: utf-8 -*-
'''
Created on 03/10/2012

@author: Usuario
'''
from PyQt4 import QtCore, QtGui
import transaction

from formularios.DialogCrearReparacion import Ui_DialogCrearReparacion
from negocio.Division_Transporte import Division_Transporte
from negocio.excepciones.Excepcion_Orden_Posee_Reparacion import Excepcion_Orden_Posee_Reparacion
from negocio.Reparacion import Reparacion
from negocio.RepuestoUtilizados import RepuestoUtilizados
from negocio.excepciones.Except_NoHayReparacionesDisponibles import Except_NoHayReparacionesDisponibles


class DialogCrearReparacion(QtGui.QDialog, Ui_DialogCrearReparacion):
    '''
    Atributos:
    _tipoDeReparacionSeleccionado
    _repuestosSolicitados
    '''
    def __init__(self, parent=None, vehiculoSeleccionado=None):
        '''
        Constructor
        '''
        super(DialogCrearReparacion, self).__init__(parent)
        self.setupUi(self)
        self.DIVISION = Division_Transporte()
        self._tiposDeReparaciones = self.DIVISION.getTipoReparaciones()
        try:
            self._tipoDeReparacionSeleccionado = self._tiposDeReparaciones[0]
        except IndexError:
            raise Except_NoHayReparacionesDisponibles() 
        self.llenarComboBoxTiposReparacion()
#        self._tipoDeReparacionSeleccionado = None
        self._repuestosSolicitados = []
#        self._ordenDeReparacion = ordenDeReparacion
        self._vehiculoSeleccionado = vehiculoSeleccionado

    def llenarComboBoxTiposReparacion(self):
        '''
        Solicita al controlador Division_Transporte todos los tipos de Reparaciones
        disponibles para ofrecerlos al ususario en un hermoso comboBox.
        '''
        self.comboBoxTipoDeReparacion.clear()
        for tipoDeReparacion in self._tiposDeReparaciones:
            self.comboBoxTipoDeReparacion.addItems(QtCore.QStringList(tipoDeReparacion.getNombre()))

    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        self.reject()

    def seleccionoAlgunRepuesto(self):
        return self._repuestosSolicitados != []

    @QtCore.pyqtSlot()
    def on_pushButtonAceptar_clicked(self):
        '''
        Se acepta el dialogo:
        Creamos una nueva reaparacion con los datos ingresados:
            - Tipo de reparacion
            - Descripcion
            - Lista de repuestos.
        Esta reparacion creada, la agregamos a la orden de reparacion con la que el dialogo está trabajando
        '''
        if not self.seleccionoAlgunRepuesto():
            QtGui.QMessageBox.critical(self, 'Error', 'Debe seleccionar por lo menos un repuesto para crear una reparacion')
            return
        # Crear la reparacion
        unaReparacion = Reparacion(self._tipoDeReparacionSeleccionado, unicode(self.lineEditDescripcion.text()), self._repuestosSolicitados)
        try:
            self._vehiculoSeleccionado.obtenerOrdenDeReparacionEnCurso().addReparacion(unaReparacion)
            # Para saber de qué cliente debemos borrar las transacciones.
            transaction.get().setUser(self.DIVISION.zodb.getNombreUsuario(), '')
            transaction.commit()
        except Excepcion_Orden_Posee_Reparacion, e:
            QtGui.QMessageBox.critical(self, 'Error. No se agrego la Reparacion', e.getMensaje())
            return
        self.accept()

    def agregarRepuesto(self, unTipoDeRepuesto, cantidad):
        '''
        Crea un repuesto utilizado y lo agrega a una lista local del dialogo, para luego crear la reparacion
        '''
        nuevoRepuesto = RepuestoUtilizados(unTipoDeRepuesto, cantidad)
        if nuevoRepuesto in self._repuestosSolicitados:
            # si ya existia hacemos un pop, lo modificamos y lo volvemos a agregar...
            self._repuestosSolicitados.pop(self._repuestosSolicitados.index(nuevoRepuesto))
        self._repuestosSolicitados.append(nuevoRepuesto)
        self.refrescarRepuestosSolicitados()
        self.comboBoxTipoDeReparacion.setEnabled(False)

    @QtCore.pyqtSlot()
    def on_pushButtonAgregarRepuesto_clicked(self):
        '''
        Agrega repuestos a la lista local (intercambio de lugar en tablas en las tablas)
        '''
        try:
            nombreRepuestoSeleccionado = self.tableWidgetRepuestosDisponibles.item(self.tableWidgetRepuestosDisponibles.currentItem().row(), 0).text() 
            repuestoSeleccionado = self._tipoDeReparacionSeleccionado.getRepuesto(nombreRepuestoSeleccionado)
            # la var _tipoDeReparacionSeleccionado posee el TdeRep seleccionado en el combo box.
            if not self.lineEditCantidadRepuesto.text():
                QtGui.QMessageBox.critical(self, 'Error', 'Por favor ingrese la cantidad del repuesto seleccionado')
                return
            self.agregarRepuesto(repuestoSeleccionado.getTipoDeRepuesto(), int(self.lineEditCantidadRepuesto.text()))
        except AttributeError:
            QtGui.QMessageBox.critical(self, 'Error', 'Por favor seleccione un repuesto para agregar a la reparacion')
            return

    @QtCore.pyqtSlot('QString')
    def on_comboBoxTipoDeReparacion_currentIndexChanged(self, cadena):
        if not len(cadena):
            return
        try:
            print 'Cambio el combo: %s' % self.comboBoxTipoDeReparacion.currentText()
        except IndexError:
            print "Cualquiera"
            return
#        self._tipoDeReparacionSeleccionado = self.buscarTipoReparacion(self.comboBoxTipoDeReparacion.currentText())
        nombre_tReparacion_selecionado = unicode(self.comboBoxTipoDeReparacion.currentText())
        self._tipoDeReparacionSeleccionado = filter(lambda tR: tR.getNombre() == nombre_tReparacion_selecionado, self._tiposDeReparaciones)
        if not len(self._tipoDeReparacionSeleccionado):
            return
        self._tipoDeReparacionSeleccionado = self._tipoDeReparacionSeleccionado[0]
        # Obtenemos los repuestos requeridos por la reparacion seleccionada
        repuestos = self._tipoDeReparacionSeleccionado.getRepuestos()

        self.tableWidgetRepuestosDisponibles.clearContents()
        self.tableWidgetRepuestosDisponibles.setRowCount(len(repuestos))
        fila = 0
        for repuesto in repuestos:
            columna = 0
            itemNombreRepuesto = QtGui.QTableWidgetItem()
            itemNombreRepuesto.setText(repuesto.getTipoDeRepuesto().getNombre())
            self.tableWidgetRepuestosDisponibles.setItem(fila,columna,itemNombreRepuesto)
            columna += 1
            itemDescripcionRepuesto = QtGui.QTableWidgetItem()
            itemDescripcionRepuesto.setText(repuesto.getTipoDeRepuesto().getDescripcion())
            self.tableWidgetRepuestosDisponibles.setItem(fila,columna,itemDescripcionRepuesto)
            fila += 1

    def refrescarRepuestosSolicitados(self):
        self.tableWidgetRepuestosAsignados.clearContents()
        self.tableWidgetRepuestosAsignados.setRowCount(len(self._repuestosSolicitados))
        fila = 0
        for repuesto in self._repuestosSolicitados:
            columna = 0
            itemNombreRepuesto = QtGui.QTableWidgetItem()
            itemNombreRepuesto.setText(repuesto.getTipoDeRepuesto().getNombre())
            self.tableWidgetRepuestosAsignados.setItem(fila,columna,itemNombreRepuesto)
            columna += 1
            itemDescripcionRepuesto = QtGui.QTableWidgetItem()
            itemDescripcionRepuesto.setText(repuesto.getTipoDeRepuesto().getDescripcion())
            self.tableWidgetRepuestosAsignados.setItem(fila,columna,itemDescripcionRepuesto)
            columna += 1
            itemCantidadRepuesto = QtGui.QTableWidgetItem()
            itemCantidadRepuesto.setText(str(repuesto.getCantidad()))
            self.tableWidgetRepuestosAsignados.setItem(fila,columna,itemCantidadRepuesto)
            fila += 1

    def buscarTipoReparacion(self, unTipoDeReparacion):
        division = Division_Transporte()
        return division.getTipoReparacion(unicode(unTipoDeReparacion))
