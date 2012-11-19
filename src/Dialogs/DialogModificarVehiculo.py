# -*- coding: utf-8 -*-
'''
Created on 14/11/2012

@author: urrutia
'''

from PyQt4 import QtCore, QtGui

from formularios.DialogMostrarLosVehiculosParaModificar import Ui_DialogMostrarLosVehiculosParaModificar
from formularios.DialogModificarVehiculo import Ui_DialogModificarVehiculo
import WidgetListadoDeVehiculos
from negocio.Division_Transporte import Division_Transporte

#global item, x ahora para contener información del vehículo seleccionado.
itemglobal = None

class DialogMostrarLosVehiculosParaModificar(QtGui.QDialog, Ui_DialogMostrarLosVehiculosParaModificar):
    '''
    classdocs
    '''
    def __init__(self, parent = None):
        '''
        Constructor
        '''
        super(DialogMostrarLosVehiculosParaModificar, self).__init__(parent)
        self.setupUi(self)
        self.miWidget = WidgetListadoDeVehiculos.ListadoVehiculos(self.widget)
        self.miWidget.connect(self.miWidget.tableWidgetListadoDeVehiculos, QtCore.SIGNAL('cellClicked(int,int)'), self.probando)
        self.itemParaModificar = None
#        miWidget.connect(miWidget.tableWidgetListadoDeVehiculos, QtCore.SIGNAL('itemClicked(QTableWidgetItem *)'), self.celdaClickeada)
#        miWidget.connect(miWidget.tableWidgetListadoDeVehiculos, QtCore.SIGNAL('cellDoubleClicked(int,int)'), self.celdaClickeada)

#    @QtCore.pyqtSlot('QTableWidgetItem *')
#    def on_table_itemClicked(self, item):
#        print 'Se clickeo sobre un item %s'% QtGui.QTableWidgetItem(item).text()
#        row = QtGui.QTableWidgetItem(item).row()
#        print 'fila:', row
#        return
        
    def celdaClickeada(self, *item):
        print 'Se clickeo sobre un item %s'% QtGui.QTableWidgetItem(*item).text()
        row = QtGui.QTableWidgetItem(*item).row()
        print 'fila:', row
        QtGui.QTableWidgetItem(*item).setText('hola')
        return
    
    #===========================================================================
    # Tratando de agarrar el evento de Seleccionar un Vehiculos de la grilla
    # y utilizarlo para retomar sus datos de la BD para mostrarlos en el 
    # modificar.
    #===========================================================================
    def probando(self, row, column):
        print row, ',' , column
        fila = row
        item = QtGui.QTableWidgetItem()
        item = self.miWidget.tableWidgetListadoDeVehiculos.item(row, 0)
        print item.text()
        self.itemParaModificar = item
        global itemglobal
        itemglobal = item
        
    @QtCore.pyqtSlot()
    def on_pushButtonAceptar_clicked(self):
        pass
        
    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        '''
        '''
        self.close()
    
    @QtCore.pyqtSlot()
    def on_pushButtonModificarDatosDeVehiculo_clicked(self):
        '''
        '''
        try:
            global itemglobal
            assert not(itemglobal is None)
        except AssertionError:
            return
        dlgModificar = DialogModificarVehiculo()
        if dlgModificar.exec_():
            self.miWidget.cargarGrilla()
        return
    
    #===========================================================================
    # Evento que se dispara cada vez que el Dialog toma el Foco
    #===========================================================================
    def showEvent(self, e):
        print 'Se tomo el foco', self.isVisible()
                
        

class DialogModificarVehiculo(QtGui.QDialog, Ui_DialogModificarVehiculo):
    '''
    classdocs
    '''
    def __init__(self, parent = None):
        '''
        Constructor
        '''
        super(DialogModificarVehiculo, self).__init__(parent)
        self.setupUi(self)
        self.auto = None
        global itemglobal
        self.item = itemglobal
        self.cargarLineEdit()
    
    #===========================================================================
    # Se cargan los LineEdit con la información del Vehícuo seleccionado
    #===========================================================================
    def cargarLineEdit(self):
        division = Division_Transporte()
        vehiculos = division.getVehiculos()
        # self.item: variable que contiene la informacion del dominio del 
        # vehiculo selecciionado. 
        dominio = unicode(self.item.text())
        # Se busca en la BD el Vehiculo seleccionado.
        tutu = vehiculos[dominio]
        self.auto = tutu
        # Se cargan.....
        self.lineEditDominio.setText(tutu.dominio)
        self.lineEditRegistroInterno.setText(tutu.registroInterno)
        self.lineEditChasisNro.setText(tutu.numeroChasis)
        self.lineEditMarca.setText(tutu.marca)
        return
    
    @QtCore.pyqtSlot()
    def on_pushButtonAceptar_clicked(self):
        print 'Click sobre aceptar'
        # Se comprueba burdamente que los haya cambiado al menos un LineEdit.
        if (self.lineEditDominio.text() is self.auto.dominio):
            if (self.lineEditRegistroInterno is self.auto.marca):
                if (self.lineEditChasisNro is self.auto.numeroChasis):
                    if (self.lineEditRegistroInterno is self.auto.registroInterno):
                        return
        else:
            division = Division_Transporte()
            dominio = unicode(self.lineEditDominio.text())
            marca = unicode(self.lineEditMarca.text())
            registroInterno = unicode(self.lineEditRegistroInterno.text())
            nroChasis = unicode(self.lineEditChasisNro.text())
            # Se le pide a la Division que modifique el informacion del vehiculo.
            division.modificarVehiculo(dominio, marca, registroInterno, nroChasis)
            msgBox = QtGui.QMessageBox(self)
            msgBox.setWindowTitle(QtCore.QString.fromUtf8('Ingresando Vehiculo'))
            msgBox.setText(QtCore.QString.fromUtf8('El vehiculo se ha modificado correctamente!!! :)'))
            if msgBox.exec_():
                # Evento que lanza el ButtonBox, creo?
                self.accept()
    
    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        '''
        '''
        self.close()