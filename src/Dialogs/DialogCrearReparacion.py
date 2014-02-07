# -*- coding: utf-8 -*-
'''
Created on 03/10/2012

@author: Usuario
'''
from PyQt4 import QtCore, QtGui

from formularios.DialogCrearReparacion import Ui_DialogCrearReparacion
from negocio.Division_Transporte import Division_Transporte
from negocio.excepciones.Excepcion_Orden_Posee_Reparacion import Excepcion_Orden_Posee_Reparacion

class DialogCrearReparacion(QtGui.QDialog, Ui_DialogCrearReparacion):
    '''
    Atributos:
    
    _tipoDeReparacionSeleccionado
    _repuestosSolicitados
    '''
    def __init__(self, parent = None):
        '''
        Constructor
        '''
        super(DialogCrearReparacion, self).__init__(parent)
        self.setupUi(self)
        self.llenarComboBoxTiposReparacion()
        self._tipoDeReparacionSeleccionado = None
        self._repuestosSolicitados = []
        self._ordenDeReparacion = None
    
    def llenarComboBoxTiposReparacion(self):
        '''
        Solicita al controlador Division_Transporte todos los tipos de Reparaciones
        disponibles para ofrecerlos al ususario en un hermoso comboBox.
        '''
        dvTrans = Division_Transporte()
        for i in dvTrans.getTipoReparaciones():
            self.comboBoxTipoDeReparacion.addItems(QtCore.QStringList(i))
        
    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        self.reject()
        
    def seleccionoAlgunRepuesto(self):
        return self._repuestosSolicitados != []
        
    @QtCore.pyqtSlot()
    def on_pushButtonAceptar_clicked(self):
        print 'Click sobre aceptar'
        if not self.seleccionoAlgunRepuesto():
            QtGui.QMessageBox.critical(self, 'Error', 'Debe seleccionar por lo menos un repuesto para crear una reparacion')
            return
        #crear la reparacion
        from negocio.Reparacion import Reparacion
        unaReparacion = Reparacion(self._tipoDeReparacionSeleccionado, str(self.lineEditDescripcion.text()), self._repuestosSolicitados)
        #TODO: Aca me quede, por las dudas...
        #self._ordenDeReparacion.getReparaciones().append(unaReparacion)
        try:
            self._ordenDeReparacion.addReparacion(unaReparacion)
        except Excepcion_Orden_Posee_Reparacion, e:
            QtGui.QMessageBox.critical(self, 'Error. No se agrego la Reparacion', e.getMensaje())
            return
        self.accept()
         
        
    def agregarRepuesto(self, unTipoDeRepuesto, cantidad):
        from negocio.RepuestoUtilizados import RepuestoUtilizados
        nuevoRepuesto = RepuestoUtilizados(unTipoDeRepuesto, cantidad)
        if nuevoRepuesto in self._repuestosSolicitados:
            # si ya existia hacemos un pop, lo modificamos y lo volvemos a agregar...
            self._repuestosSolicitados.pop(self._repuestosSolicitados.index(nuevoRepuesto))
        self._repuestosSolicitados.append(nuevoRepuesto)
        self.refrescarRepuestosSolicitados()
        self.comboBoxTipoDeReparacion.setEnabled(False)
        
    @QtCore.pyqtSlot()
    def on_pushButtonAgregarRepuesto_clicked(self):
        print 'Agregando repuesto.....'
        try:
            nombreRepuestoSeleccionado = self.tableWidgetRepuestosDisponibles.item(self.tableWidgetRepuestosDisponibles.currentItem().row(), 0).text() 
            repuestoSeleccionado = self._tipoDeReparacionSeleccionado.getRepuesto(nombreRepuestoSeleccionado)
                # la var _tipoDeReparacionSeleccionado posee el TdeRep seleccionado en el combo box.
            print repuestoSeleccionado
            if not self.lineEditCantidadRepuesto.text():
                QtGui.QMessageBox.critical(self, 'Error', 'Por favor ingrese la cantidad del repuesto seleccionado')
                return
            self.agregarRepuesto(repuestoSeleccionado.getTipoDeRepuesto(), int(self.lineEditCantidadRepuesto.text()))
        except AttributeError:
            QtGui.QMessageBox.critical(self, 'Error', 'Por favor seleccione un repuesto para agregar a la reparacion')
            return
        
    def on_comboBoxTipoDeReparacion_currentIndexChanged(self):
        print 'Cambio el combo: %s' % self.comboBoxTipoDeReparacion.currentText()
        self._tipoDeReparacionSeleccionado = self.buscarTipoReparacion(self.comboBoxTipoDeReparacion.currentText())
        #Obtenemos los repuestos requeridos por la reparacion seleccionada
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
    
    def setOrdenDeReparacion(self, unaOrden):
        self._ordenDeReparacion = unaOrden
