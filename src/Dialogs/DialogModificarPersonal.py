# -*- coding: utf-8 -*-
'''
Created on 03/10/2012

@author: Usuario
'''
from PyQt4 import QtCore, QtGui
from formularios.DialogModificarPersonal import Ui_DialogModificarPersonal


class DialogModificarPersonal(QtGui.QDialog, Ui_DialogModificarPersonal):
    '''
    classdocs
    '''
    def __init__(self, parent = None):
        '''
        Constructor
        '''
        super(DialogModificarPersonal, self).__init__(parent)
        self.setupUi(self)