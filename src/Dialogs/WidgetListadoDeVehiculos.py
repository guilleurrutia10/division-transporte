'''
Created on 10/10/2012

@author: urrutia
'''

from PyQt4 import QtGui

from formularios.WidgetListadoDeVehiculos import Ui_FormListadoVehiculos

class ListadoVehiculos(QtGui.QWidget, Ui_FormListadoVehiculos):
    def __init__(self, parent = None):
        super(ListadoVehiculos, self).__init__(parent)
        self.setupUi(self)