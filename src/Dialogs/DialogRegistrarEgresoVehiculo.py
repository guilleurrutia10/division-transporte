# -*- coding: utf-8 -*-
'''
Created on 03/11/2012

@author: urrutia
'''

from PyQt4 import QtCore, QtGui

from formularios.DialogRegistrarEgresoVehiculo import Ui_DialogRegistraEgresoVehiculo
from formularios.DialogDatosEgresoVehiculo import Ui_DialogDatosEgresoVehiculo
import WidgetListadoDeVehiculos 

class DialogRegistrarEgresoVehiculo(QtGui.QDialog, Ui_DialogRegistraEgresoVehiculo):
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
        super(DialogRegistrarEgresoVehiculo, self).__init__(parent)
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
    def on_pushButtonRegistrarEgreso_clicked(self):
        '''
        @version: 
        @author: 
        '''
        self.close()
        dlgDatosIngreso = DialogDatosEgresoVehiculo()
        dlgDatosIngreso.exec_()
        
class DialogDatosEgresoVehiculo(QtGui.QDialog, Ui_DialogDatosEgresoVehiculo):
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
        super(DialogDatosEgresoVehiculo, self).__init__(parent)
        self.setupUi(self)
        
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
        self.setupUi(self)    