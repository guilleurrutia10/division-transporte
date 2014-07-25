# -*- coding: utf-8 -*-
'''
Created on 03/11/2012

@author: urrutia
'''

from PyQt4 import QtCore, QtGui

from formularios.DialogRegistrarEgresoVehiculo import Ui_DialogRegistraEgresoVehiculo
from formularios.DialogDatosEgresoVehiculo import Ui_DialogDatosEgresoVehiculo
from WidgetListadoDeVehiculos import ListadoVehiculos 

from negocio.Division_Transporte import Division_Transporte

class DialogRegistrarEgresoVehiculo(QtGui.QDialog, Ui_DialogRegistraEgresoVehiculo):
    '''
    classdocs
    @version: 
    @author: 
    '''
    
    def __init__(self, parent=None):
        '''
        Constructor
        @version: 
        @author: 
        '''
        super(DialogRegistrarEgresoVehiculo, self).__init__(parent)
        self.setupUi(self)
#        WidgetListadoDeVehiculos.ListadoVehiculos(self.widget)
#         self.miWidget = ListadoVehiculos(self.widget)
        self.miWidget = ListadoVehiculos(Division_Transporte().getVehiculos().values())
        self.miWidget.connect(self.miWidget.tableWidgetListadoDeVehiculos, QtCore.SIGNAL('cellClicked(int,int)'), self.seleccionarCelda)
    
    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        '''
        @version: 
        @author: 
        '''
        self.reject()
    
    @QtCore.pyqtSlot()
    def on_pushButtonRegistrarEgreso_clicked(self):
        '''
        @version: 
        @author: 
        '''
        try:
            if self.itemDominio:
                dlgDatosIngreso = DialogDatosEgresoVehiculo()
                dlgDatosIngreso.itemDominio = self.itemDominio
                dlgDatosIngreso.exec_()
                self.itemDominio = None
            else:
                self.mostrarMensaje('Debe seleccionar un vehículo.', 'Seleccionar vehículo')
        except AttributeError:
            self.mostrarMensaje('Debe seleccionar un vehículo.', 'Seleccionar vehículo')
            
    def seleccionarCelda(self, fila, columna):
        print 'Celda seleccionada: %s,%s' % (fila, columna)
        self.itemDominio = self.miWidget.tableWidgetListadoDeVehiculos.item(fila, 0)
        
    '''
    TODO: Este método se repite en varios Dialogs.
    '''
    def mostrarMensaje(self, mensaje, titulo):
        msgBox = QtGui.QMessageBox(self)
        msgBox.setText(QtCore.QString.fromUtf8(mensaje))
        msgBox.setWindowTitle(QtCore.QString.fromUtf8(titulo))
        return msgBox.exec_()
        
class DialogDatosEgresoVehiculo(QtGui.QDialog, Ui_DialogDatosEgresoVehiculo):
    '''
    classdocs
    @version: 
    @author: 
    '''
    
    def __init__(self, parent=None):
        '''
        Constructor
        @version: 
        @author: 
        '''
        super(DialogDatosEgresoVehiculo, self).__init__(parent)
        self.setupUi(self)
        self.pushButtonCancelar
        
    @QtCore.pyqtSlot()
    def on_pushButtonAceptar_clicked(self):
        '''
        @version: 
        @author: 
        '''
        print 'Click sobre aceptar'
    
    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        '''
        @version: 
        @author: 
        '''
        self.reject()
