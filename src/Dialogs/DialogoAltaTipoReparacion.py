# -*- coding: utf-8 -*-
'''
Created on 18/07/2014

@author: Usuario
'''
from PyQt4 import QtCore, QtGui
from formularios.DlgAltaTipoReparacion import Ui_DialogAltaTipoReparacion
from negocio.Division_Transporte import Division_Transporte
from Utiles_Dialogo import mostrarMensaje
from negocio.RepuestoRequeridos import RepuestoRequeridos
from negocio.TipoDeReparacion import TipoDeReparacion
import transaction
class DialogoAltaTipoReparacion(QtGui.QDialog, Ui_DialogAltaTipoReparacion):
    '''
    Elementos:
        lineEditNombre
        lineEditDescripcion
        comboBoxSeccion
        tableWidgetRepuestosSinAsignar
        tableWidgetRepuestosAsignados
        pushButtonAsignarRepuesto
        pushButtonDesasignarRepuesto
        pushButtonAceptar
        pushButtonCancelar
        lineEditCantidad
    '''

    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super(DialogoAltaTipoReparacion, self).__init__(parent)
        self.setupUi(self)
        self.DIVISION = Division_Transporte()
        self.tableWidgetRepuestosAsignados.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.tableWidgetRepuestosSinAsignar.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self._secciones = self.DIVISION.getSecciones().values()
        self._repuestosSinAsignar = self.DIVISION.getTipoRepuestos().values()
        self._repuestosAsignados = []
        self.tableWidgetRepuestosSinAsignar.cargarConRepuestos(self._repuestosSinAsignar)
        
        for seccion in self._secciones:
            self.comboBoxSeccion.addItems(QtCore.QStringList(seccion.getNombre()))
            
        #seteo de nombres de los Labels para el estilo 
        self.label.setObjectName("label")
        self.label_2.setObjectName("label")
        self.label_3.setObjectName("label")
        self.label_4.setObjectName("label")
        self.label_5.setObjectName("label")
        self.label_7.setObjectName("label")



    @QtCore.pyqtSlot()
    def on_pushButtonAsignarRepuesto_clicked(self):
        
        if not self.tableWidgetRepuestosSinAsignar.getRepuestoSeleccionado():
            mostrarMensaje(self, 'Debe seleccionar un repuesto.', 'Seleccionar')
            return
        try:
            cantidad_de_repuesto = int(self.lineEditCantidad.text())
        except ValueError:
            mostrarMensaje(self, 'Debe ingresar la cantidad del repuesto.', 'Seleccionar')
            return
        self._repuestosAsignados.append(RepuestoRequeridos(self.tableWidgetRepuestosSinAsignar.getRepuestoSeleccionado(),cantidad_de_repuesto))
        self._repuestosSinAsignar.remove(self.tableWidgetRepuestosSinAsignar.getRepuestoSeleccionado())        
        self.tableWidgetRepuestosAsignados.cargarConRepuestos(self._repuestosAsignados)
        self.tableWidgetRepuestosSinAsignar.cargarConRepuestos(self._repuestosSinAsignar)

    @QtCore.pyqtSlot()
    def on_pushButtonDesasignarRepuesto_clicked(self):
        if not self.tableWidgetRepuestosAsignados.getRepuestoSeleccionado():
            mostrarMensaje(self, 'Debe Seleccionar un Empleado.', 'Seleccionar')
            return

        self._repuestosSinAsignar.append(self.tableWidgetRepuestosAsignados.getRepuestoSeleccionado().getTipoDeRepuesto())
        self._repuestosAsignados.remove(self.tableWidgetRepuestosAsignados.getRepuestoSeleccionado())        
        self.tableWidgetRepuestosAsignados.cargarConRepuestos(self._repuestosAsignados)
        self.tableWidgetRepuestosSinAsignar.cargarConRepuestos(self._repuestosSinAsignar)
        
    @QtCore.pyqtSlot()
    def on_pushButtonAceptar_clicked(self):
        
        nombreTipoReparacion = unicode(self.lineEditNombre.text())
        if len(nombreTipoReparacion) == 0:
            mostrarMensaje(self, 'Debe ingresar el nombre del tipo de reparaci�n', 'Ingresar nombre del tipo de reparaci�n')
            return
        descripcionTipoReparacion = unicode(self.lineEditDescripcion.text())
        if not self._repuestosAsignados:
            mostrarMensaje(self, 'No se han cargado repuestos al Tipo de Reparacion.', 'Error al cargar repuestos')
            return

        #Repuestos Requeridos ok.        
        #crear tipo de reparacion
        tReparacion = TipoDeReparacion(nombreTipoReparacion, descripcionTipoReparacion, self._repuestosAsignados)
        #tomar la seccion ingresada y appendearle el tipo de reparacion creado
        nombre_seccion_seleccionada = unicode(self.comboBoxSeccion.currentText())
        seccionSeleccionada = filter(lambda s: s.getNombre() == nombre_seccion_seleccionada, self._secciones)
        seccionSeleccionada = seccionSeleccionada[0]
        seccionSeleccionada.agregarTipoDeReparacion(tReparacion)  
        
        if mostrarMensaje(self, 'El tipo de reparacion se ha creado exitosamente!\nSe agrego a la seccion indicada', 'Creacion exitosa'):
            transaction.commit()
            self.accept()
