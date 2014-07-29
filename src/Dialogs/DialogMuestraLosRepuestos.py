# -*- coding: utf-8 -*-
'''
Created on 31/10/2012

@author: alum
'''

from PyQt4 import QtCore, QtGui

from formularios.DialogMuestraLosRepuestos import Ui_Dialog
from negocio.Division_Transporte import Division_Transporte

from WidgetMostrarRepuestos import DialogModificarRepuesto
from Utiles_Dialogo import mostrarMensaje

class DialogMuestraLosRepuestos(QtGui.QDialog, Ui_Dialog):
    '''
    classdocs
    '''
    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super(DialogMuestraLosRepuestos, self).__init__(parent)
        self.setupUi(self)
        #Para evitar que se modifique la información presentada por la grilla.
        self.tableWidgetDatosRepuestos.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.repuestos = None
        self.cargarGrillaInicial()
        self.tableWidgetDatosRepuestos.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.tableWidgetDatosRepuestos.connect(self.tableWidgetDatosRepuestos, QtCore.SIGNAL('cellClicked(int,int)'), self.seleccionarCelda)
        
        self.repuestoSeleccionado = None
        
    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        self.reject()
        
    @QtCore.pyqtSlot('QString')
    def on_lineEditBuscarNombre_textChanged(self, cadena):
        filtro = unicode(cadena).lower()
        #Se aplica un filtro sobre los campos Nombre, Descripcion y codigo
        repuestos = filter(lambda p: filtro in unicode.lower(unicode(p.getNombre())) or filtro in unicode.lower(unicode(p.getDescripcion())) or filtro in unicode.lower(unicode(p.getCodigo())), self.repuestos)
        #refrescar Grilla
        self.cargarGrilla(repuestos)
         
    def cargarGrilla(self, repuestos):
        self.tableWidgetDatosRepuestos.clearContents()
        self.tableWidgetDatosRepuestos.setRowCount(len(repuestos))
        fila = 0
        for repuesto in repuestos:
            columna = 0
            itemCodigo = QtGui.QTableWidgetItem()
            itemCodigo.setText(repuesto.getCodigo())
            self.tableWidgetDatosRepuestos.setItem(fila, columna, itemCodigo)
            columna += 1
            itemNombre = QtGui.QTableWidgetItem()
            itemNombre.setText(repuesto.getNombre())
            self.tableWidgetDatosRepuestos.setItem(fila, columna, itemNombre)
            columna += 1
            itemDescripcion = QtGui.QTableWidgetItem()
            itemDescripcion.setText(repuesto.getDescripcion())
            self.tableWidgetDatosRepuestos.setItem(fila, columna, itemDescripcion)
            fila += 1
                 
    def cargarGrillaInicial(self):
        division = Division_Transporte()
        rep = division.getRepuestos()
        self.repuestos = rep.values()
        self.repuestos.sort(cmp=lambda x, y : cmp(x.getNombre, y.getNombre))
        self.cargarGrilla(self.repuestos)
         
    def seleccionarCelda(self, fila, columna):
        print 'Celda Seleccionada fila %s columna %s' % (fila, columna)
        itemSeleccionado = self.tableWidgetDatosRepuestos.item(fila, 0)
        division = Division_Transporte()
        self.repuestoSeleccionado = division.getRepuesto(unicode(itemSeleccionado.text()))
        print self.repuestoSeleccionado
        
    @QtCore.pyqtSlot()
    def on_pushButtonModificarRepuesto_clicked(self):
        if self.repuestoSeleccionado:
            dlgModificarRepuesto = DialogModificarRepuesto(self.repuestoSeleccionado)
            dlgModificarRepuesto.exec_()
            self.cargarGrilla(Division_Transporte().getRepuestos().values())
        else:
            mostrarMensaje(self, 'Debe seleccionar un Tipo de Repuesto', 'Tipo de Repuesto')
