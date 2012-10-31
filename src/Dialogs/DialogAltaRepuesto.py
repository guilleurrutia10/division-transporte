'''
Created on 03/10/2012

@author: Usuario
'''
from PyQt4 import QtCore, QtGui
from formularios.DialogAltaRepuesto import Ui_DialogAltaRepuesto


class DialogAltaRepuesto(QtGui.QDialog, Ui_DialogAltaRepuesto):
    '''
    classdocs
    '''
    def __init__(self, parent = None):
        '''
        Constructor
        '''
        super(DialogAltaRepuesto, self).__init__(parent)
        self.setupUi(self)
    