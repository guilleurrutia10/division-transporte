# -*- coding: utf-8 -*-
'''
Created on 03/10/2012

@author: Usuario
'''
from PyQt4 import QtCore, QtGui

from formularios.DialogCrearReparacion import Ui_DialogCrearReparacion

class DialogCrearReparacion(QtGui.QDialog, Ui_DialogCrearReparacion):
    '''
    classdocs
    '''
    def __init__(self, parent = None):
        '''
        Constructor
        '''
        super(DialogCrearReparacion, self).__init__(parent)
        self.setupUi(self)
        self.pushButtonAgregarRepuesto
        
    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        self.close()
        
    @QtCore.pyqtSlot()
    def on_pushButtonAceptar_clicked(self):
        print 'Click sobre aceptar'
    
    @QtCore.pyqtSlot()
    def on_pushButtonAgregarRepuesto_clicked(self):
        print 'Agregando repuesto.....'