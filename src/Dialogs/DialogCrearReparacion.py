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
       