# -*- coding: utf-8 -*-
'''
Created on 03/11/2012

@author: urrutia
'''

from PyQt4 import QtCore, QtGui

from formularios.DialogRegistrarIngresoVehiculo import Ui_DialogRegistrarIngresoVehiculo
from formularios.DialogDatosIngresoVehiculo import Ui_DialogIngresoVehiculo 
import WidgetListadoDeVehiculos

class DialogRegistrarIngresoVehiculo(QtGui.QDialog, Ui_DialogRegistrarIngresoVehiculo):
    '''
    classdocs
    @version: 
    @author: 
    '''
    
    def __init__(self, parent = None):
        '''
        Constructor
        @version: 
        @author: 
        '''
        super(DialogRegistrarIngresoVehiculo, self).__init__(parent)
        self.setupUi(self)
        WidgetListadoDeVehiculos.ListadoVehiculos(self.widget)
        
    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        '''
        @version: 
        @author: 
        '''
        self.close()
    
    @QtCore.pyqtSlot()
    def on_pushButtonRegistrarNuevoIngreso_clicked(self):
        '''
        @version: 
        @author: 
        '''
        self.close()
        dlgDatosIngreso = DialogDatosIngresoVehiculo()
        dlgDatosIngreso.exec_()
        
class DialogDatosIngresoVehiculo(QtGui.QDialog, Ui_DialogIngresoVehiculo):
    '''
    classdocs
    @version: 
    @author: 
    '''
    
    def __init__(self, parent = None):
        '''
        Constructor
        @version: 
        @author: 
        '''
        super(DialogDatosIngresoVehiculo, self).__init__(parent)
        self.setupUi(self)
        self.buttonBox = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Cancel)
        #Validación a medida que se escribe en el lineEdit
        self.lineEditKilometraje.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[0-9]+'),self))
        self.lineEditCombustible.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[0-9]+'),self))
        self.lineEditEquipamiento.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[a-zA-Z]+'),self))
        self.lineEditReparacion.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[a-zA-Z]+'),self))
        self.lineEditComisaria.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[a-zA-Z]+'),self))
        self.lineEditLocalidad.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[a-zA-Z]+'),self))
        
    @QtCore.pyqtSlot()
    def on_buttonBox_accepted(self):
        '''
        @version: 
        @author: 
        '''
        print 'Click sobre aceptar'
    
    @QtCore.pyqtSlot()
    def on_buttonBox_rejected(self):
        '''
        @version: 
        @author: 
        '''
        self.close()