# -*- coding: utf-8 -*-
'''
Created on 13/11/2012

@author: urrutia
'''

from PyQt4 import QtCore, QtGui

from formularios.DialogRemoverEmpleadoDeSeccion import Ui_Dialog

class DialogRemoverEmpleadoDeSeccion(QtGui.QDialog, Ui_Dialog):
    '''
    classdocs
    '''
    def __init__(self, parent = None):
        '''
        Constructor
        '''
        super(DialogRemoverEmpleadoDeSeccion, self).__init__(parent)
        self.setupUi(self)
        
    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        self.close()