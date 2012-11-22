# -*- coding: utf-8 -*-
'''
Created on 22/11/2012

@author: urrutia
'''

from PyQt4 import QtCore, QtGui

from formularios.DialogBajaPersonal import Ui_DialogBajaPersonal
from formularios.DialogAsignarFechaDeBaja import Ui_DialogAsignarFechaBaja

class DialogBajaPersonal(QtGui.QDialog, Ui_DialogBajaPersonal):
    '''
    classdocs
    '''
    def __init__(self, parent = None):
        '''
        Constructor
        '''
        super(DialogBajaPersonal, self).__init__(parent)
        self.setupUi(self)
        self.cargaGrillaInicial()
        self.pushButtonCancelar
        self.pushButtonDarDeBaja
        
    def cargaGrillaInicial(self):
        print 'Cargar Grilla'
        
    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        '''
        '''
        self.close()
        
    @QtCore.pyqtSlot()
    def on_pushButtonDarDeBaja_clicked(self):
        '''
        '''
        dlgAsignarFecha = DialogAsignarFechaDeBaja()
        dlgAsignarFecha.exec_()
        
class DialogAsignarFechaDeBaja(QtGui.QDialog, Ui_DialogAsignarFechaBaja):
    '''
    classdocs
    '''
    def __init__(self, parent = None):
        '''
        Constructor
        '''
        super(DialogAsignarFechaDeBaja, self).__init__(parent)
        self.setupUi(self)
        
    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        '''
        '''
        self.close()
        
    @QtCore.pyqtSlot()
    def on_pushButtonAceptar_clicked(self):
        '''
        '''
        print 'Click sobre Aceptar'