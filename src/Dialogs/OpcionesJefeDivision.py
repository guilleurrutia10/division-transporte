# -*- coding: utf-8 -*-
'''
Created on 26/09/2012

@author: Usuario
'''
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from formularios.frm_opc_jefe_division import Ui_MainWindow
import PyQt4
import sys


class OpcionesJefeDivision(QtGui.QDialog):

    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
