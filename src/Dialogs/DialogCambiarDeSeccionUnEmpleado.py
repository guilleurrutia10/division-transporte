# -*- coding: utf-8 -*-
'''
Created on 13/11/2012

@author: urrutia
'''

from PyQt4 import QtCore, QtGui

from formularios.DialogCambiarDeSeccionUnEmpleado import Ui_DialogCambiarDeSeccionUnEmpleado


class DialogCambiardeSeccionunEmpleado(QtGui.QDialog, Ui_DialogCambiarDeSeccionUnEmpleado):
    '''
    classdocs
    '''
    def __init__(self, parent = None):
        '''
        Constructor
        '''
        super(DialogCambiardeSeccionunEmpleado, self).__init__(parent)
        self.setupUi(self)
        
    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        self.reject()