# -*- coding: utf-8 -*-
'''
Created on 16/11/2012

@author: urrutia
'''

from PyQt4 import QtCore, QtGui

from formularios.WidgetListadoEmpleados import Ui_Form

class WidgetListadoEmpleados(QtGui.QWidget, Ui_Form):
    def __init__(self, parent = None):
        super(WidgetListadoEmpleados, self).__init__(parent)
        self.setupUi(self)