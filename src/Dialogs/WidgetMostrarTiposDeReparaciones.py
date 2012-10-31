'''
Created on 03/10/2012

@author: Usuario
'''
from PyQt4 import QtGui
from formularios.WidgetMostrarTiposDeReparaciones import Ui_WidgetMostrarTiposDeReparaciones

class WidgetMostrarTiposDeReparaciones(QtGui.QWidget, Ui_WidgetMostrarTiposDeReparaciones):
    '''
    classdocs
    '''
    def __init__(self, parent = None):
        '''
        Constructor
        '''
        super(WidgetMostrarTiposDeReparaciones, self).__init__(parent)
        self.setupUi(self)
