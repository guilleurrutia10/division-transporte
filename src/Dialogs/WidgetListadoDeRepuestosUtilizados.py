'''
Created on 10/10/2012

@author: urrutia
'''
from PyQt4 import QtGui
from formularios.WidgetListadoDeRepuestosUtilizados import Ui_FormRepuestosUtilizados

class ListadoRepustosUtilizados(QtGui.QWidget, Ui_FormRepuestosUtilizados):
    def __init__(self, parent = None):
        super(ListadoRepustosUtilizados, self).__init__(parent)
        self.setupUi(self)