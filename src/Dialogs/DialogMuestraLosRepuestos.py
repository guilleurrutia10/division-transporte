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
        self.cargarGrillaInicial()
        
    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        self.close()
        
    @QtCore.pyqtSlot('QString')
    def on_lineEditBuscarNombre_textChanged(self, cadena):
        print 'Filtrar %s' %cadena
        #refrescar Grilla
        
    def cargarGrilla(self, repuestos):
        self.tableWidgetDatosRepuestos.clearContents()
        self.tableWidgetDatosRepuestos.setRowCount(len(repuestos))
        fila = 0
        for rep in repuestos:
            columna = 0
            miItemc1 = QtGui.QTableWidgetItem()
            miItemc1.setText(rep.getNombre())
            self.tableWidgetDatosRepuestos.setItem(fila,columna,miItemc1)
            columna += 1
            miItemc2 = QtGui.QTableWidgetItem()
            miItemc2.setText(rep.getDescripcion())
            self.tableWidgetDatosRepuestos.setItem(fila,columna,miItemc2)
                
    def cargarGrillaInicial(self):
        division = Division_Transporte()
        rep = division.getRepuestos()
        repuestos = rep.values()
        repuestos.sort(cmp=lambda x,y : cmp(x.nombre, y.nombre))
        self.cargarGrilla(repuestos)