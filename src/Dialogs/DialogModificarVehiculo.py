# -*- coding: utf-8 -*-
'''
Created on 14/11/2012

@author: urrutia
'''

from PyQt4 import QtCore, QtGui

from formularios.DialogMostrarLosVehiculosParaModificar import Ui_DialogMostrarLosVehiculosParaModificar
from formularios.DialogModificarVehiculo import Ui_DialogModificarVehiculo
from WidgetListadoDeVehiculos import ListadoVehiculos
from negocio.Division_Transporte import Division_Transporte

#global item, x ahora para contener información del vehículo seleccionado.
itemglobal = None

class DialogMostrarLosVehiculosParaModificar(QtGui.QDialog, Ui_DialogMostrarLosVehiculosParaModificar):
    '''
    classdocs
    '''
    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super(DialogMostrarLosVehiculosParaModificar, self).__init__(parent)
        self.setupUi(self)
        self.miWidget = ListadoVehiculos(Division_Transporte().getVehiculos().values(), self.widget)
        self.miWidget.connect(self.miWidget.tableWidgetListadoDeVehiculos, QtCore.SIGNAL('cellClicked(int,int)'), self.seleccionarCelda)
        self.itemParaModificar = None
    
    #===========================================================================
    # Tratando de agarrar el evento de Seleccionar un Vehiculos de la grilla
    # y utilizarlo para retomar sus datos de la BD para mostrarlos en el 
    # modificar.
    #===========================================================================
    def seleccionarCelda(self, row, column):
        print row, ',' , column
#        item = QtGui.QTableWidgetItem()
        item = self.miWidget.tableWidgetListadoDeVehiculos.item(row, 0)
        print item.text()
        self.itemParaModificar = item
        global itemglobal
        itemglobal = item
        
    @QtCore.pyqtSlot()
    def on_pushButtonAceptar_clicked(self):
        self.accept()
        
    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        '''
        '''
        self.reject()
    
    @QtCore.pyqtSlot()
    def on_pushButtonModificarDatosDeVehiculo_clicked(self):
        '''
        '''
        try:
            global itemglobal
            assert not(itemglobal is None)
        except AssertionError:
            self.mostrarMensaje('Debe seleccionar un Vehículo.', 'Ingresar Vehículo')
            return
        dlgModificar = DialogModificarVehiculo()
        dlgModificar.exec_()
        itemglobal = None
        self.miWidget.cargarGrilla(Division_Transporte().getVehiculos().values())
#        self.miWidget.cargarGrillaInicial()
    
    '''
    TODO: Este método se repite en varios Dialogs.
    '''
    def mostrarMensaje(self, mensaje, titulo):
        msgBox = QtGui.QMessageBox(self)
        msgBox.setText(QtCore.QString.fromUtf8(mensaje))
        msgBox.setWindowTitle(QtCore.QString.fromUtf8(titulo))
        return msgBox.exec_()
    
    #===========================================================================
    # Evento que se dispara cada vez que el Dialog toma el Foco
    #===========================================================================
    def showEvent(self, e):
        print 'Se tomo el foco', self.isVisible()
                
        

class DialogModificarVehiculo(QtGui.QDialog, Ui_DialogModificarVehiculo):
    '''
    classdocs
    '''
    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super(DialogModificarVehiculo, self).__init__(parent)
        self.setupUi(self)
        self.auto = None
        global itemglobal
        self.item = itemglobal
        self.cargarLineEdit()
    
    def cargarLineEdit(self):
        division = Division_Transporte()
        self.auto = division.getVehiculo(unicode(self.item.text()))
        
        self.lineEditDominio.setText(self.auto.dominio)
        #TODO: El dominio es el único que no puede cambiar????
        self.lineEditDominio.setReadOnly (True)
        self.lineEditDominio.setModified(False)
        self.lineEditRegistroInterno.setText(self.auto.registroInterno)
        self.lineEditChasisNro.setText(self.auto.numeroChasis)
        self.lineEditMarca.setText(self.auto.marca)
        return

    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        '''
        '''
        self.reject()
    
    @QtCore.pyqtSlot()
    def on_pushButtonAceptar_clicked(self):
        print 'Click sobre aceptar'
        # Se comprueba burdamente que los haya cambiado al menos un LineEdit.
        if (self.lineEditDominio.text() == self.auto.dominio) and (self.lineEditMarca.text() == self.auto.marca) and (self.lineEditChasisNro.text() == self.auto.numeroChasis) and (self.lineEditRegistroInterno.text() == self.auto.registroInterno):
            self.mostrarMensaje('No se modificó ningún atributo del vehículo', 'Modificación de Vehículo')
            return
        else:
            '''TODO: Crear método ModificarVehiculo()'''
            division = Division_Transporte()
            dominio = unicode(self.lineEditDominio.text())
            marca = unicode(self.lineEditMarca.text())
            registroInterno = unicode(self.lineEditRegistroInterno.text())
            nroChasis = unicode(self.lineEditChasisNro.text())
            # Se le pide a la Division que modifique el informacion del vehiculo.
            division.modificarVehiculo(dominio, marca, registroInterno, nroChasis)
            
            if self.mostrarMensaje('El vehiculo se ha modificado correctamente!!! :)', 'Ingresando Vehiculo'):
                self.accept()
    
    '''
    TODO: Este método se repite en varios Dialogs.
    '''
    def mostrarMensaje(self, mensaje, titulo):
        msgBox = QtGui.QMessageBox(self)
        msgBox.setText(QtCore.QString.fromUtf8(mensaje))
        msgBox.setWindowTitle(QtCore.QString.fromUtf8(titulo))
        return msgBox.exec_()
