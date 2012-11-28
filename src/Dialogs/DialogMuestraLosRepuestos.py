# -*- coding: utf-8 -*-
'''
Created on 31/10/2012

@author: alum
'''

from PyQt4 import QtCore, QtGui

from formularios.DialogMuestraLosRepuestos import Ui_Dialog
from negocio.Division_Transporte import Division_Transporte

class DialogMuestraLosRepuestos(QtGui.QDialog, Ui_Dialog):
    '''
    classdocs
    '''
    def __init__(self, parent = None):
        '''
        Constructor
        '''
        super(DialogMuestraLosRepuestos, self).__init__(parent)
        self.setupUi(self)
        #Para evitar que se modifique la información presentada por la grilla.
        self.tableWidgetDatosRepuestos.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.repuestos = None
        self.cargarGrillaInicial()
        self.tableWidgetDatosRepuestos.connect(self.tableWidgetDatosRepuestos, QtCore.SIGNAL('cellClicked(int,int)'), self.seleccionarCelda)
        
    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        self.close()
        
    @QtCore.pyqtSlot('QString')
    def on_lineEditBuscarNombre_textChanged(self, cadena):
        filtro = unicode(cadena)
        #refrescar Grilla
        repuestos = filter( lambda p: unicode.lower(filtro) in unicode.lower(unicode(p.getNombre())), self.repuestos)
        self.cargarGrilla(repuestos)
        
    def cargarGrilla(self, repuestos):
        self.tableWidgetDatosRepuestos.clearContents()
        self.tableWidgetDatosRepuestos.setRowCount(len(repuestos))
        fila = 0
        for repuesto in repuestos:
            columna = 0
            miItemc1 = QtGui.QTableWidgetItem()
            miItemc1.setText(repuesto.getNombre())
            self.tableWidgetDatosRepuestos.setItem(fila,columna,miItemc1)
            columna += 1
            miItemc2 = QtGui.QTableWidgetItem()
            miItemc2.setText(repuesto.getDescripcion())
            self.tableWidgetDatosRepuestos.setItem(fila,columna,miItemc2)
            fila += 1
                
    def cargarGrillaInicial(self):
        division = Division_Transporte()
        rep = division.getRepuestos()
        self.repuestos = rep.values()
        self.repuestos.sort(cmp=lambda x,y : cmp(x.getNombre, y.getNombre))
        self.cargarGrilla(self.repuestos)
        
    def seleccionarCelda(self, fila, columna):
        print 'Celda Seleccionada fila %s columna %s' % (fila, columna)
        itemSeleccionado = self.tableWidgetDatosRepuestos.item(fila, 0)
        division = Division_Transporte()
        self.repuestoSeleccionado = division.getRepuesto(unicode(itemSeleccionado.text()))
        print self.repuestoSeleccionado
        
    @QtCore.pyqtSlot()
    def on_pushButtonModificarRepuesto_clicked(self):
        print 'Modificar repuesto'