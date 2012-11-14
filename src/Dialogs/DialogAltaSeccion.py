# -*- coding: utf-8 -*-
'''
Created on 03/10/2012

@author: Usuario
'''
from PyQt4 import QtCore, QtGui
from formularios.DialogAltaSeccion import Ui_DialogAltaSeccion


class DialogAltaSeccion(QtGui.QDialog, Ui_DialogAltaSeccion):
    '''
    classdocs
    '''
    def __init__(self, parent = None):
        '''
        Constructor
        '''
        super(DialogAltaSeccion, self).__init__(parent)
        self.setupUi(self)
