# -*- coding: utf-8 -*-
'''
Created on 13/11/2012

@author: urrutia
'''

from PyQt4 import QtCore, QtGui

from formularios.DialogCambiarDeSeccionUnEncargado import Ui_DialogCambiaDeSeccionUnEncargado


class DialogCambiarDeSeccionUnEncargado(QtGui.QDialog, Ui_DialogCambiaDeSeccionUnEncargado):
    '''
    classdocs
    '''
    def __init__(self, parent = None):
        '''
        Constructor
        '''
        super(DialogCambiarDeSeccionUnEncargado, self).__init__(parent)
        self.setupUi(self)
        
    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        self.close()