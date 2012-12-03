# -*- coding: utf-8 -*-
'''
Created on 03/10/2012

@author: Usuario
'''
from PyQt4 import QtCore, QtGui
from formularios.DialogRegistrarReparaciones import Ui_DialogRegistrarReparaciones
from Dialogs import DialogCrearReparacion

class DialogRegistrarReparaciones(QtGui.QDialog, Ui_DialogRegistrarReparaciones):
    '''
    classdocs
    '''
    def __init__(self, parent = None):
        '''
        Constructor
        '''
        super(DialogRegistrarReparaciones, self).__init__(parent)
        self.setupUi(self)
        #Conectamos el boton Agregar Reparaciones...
        self.connect(self.pushButtonAgregarReparacion, QtCore.SIGNAL("pressed()"), self.abrirDialogCrearReparacion)
        self.pushButtonBuscarVehiculo
    def abrirDialogCrearReparacion(self):
        print 'abriendo dialogo Crear Reparacion'
        dlgCrearReparacion = DialogCrearReparacion.DialogCrearReparacion(self)
        dlgCrearReparacion.exec_()
        
    @QtCore.pyqtSlot()
    def on_pushButtonAceptar_clicked(self):
        print 'Click sobre aceptar'
    
    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        self.reject()
        
    @QtCore.pyqtSlot()
    def on_pushButtonBuscarVehiculo_clicked(self):
        print 'Buscando............'