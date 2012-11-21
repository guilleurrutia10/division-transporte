# -*- coding: utf-8 -*-
'''
Created on 03/10/2012

@author: Usuario
'''
from PyQt4 import QtGui
from formularios.WidgetMostrarReparacionesPorVehiculo import Ui_WidgetMostrarReparacionesPorVehiculo

class WidgetMostrarReparacionesPorVehiculo(QtGui.QWidget, Ui_WidgetMostrarReparacionesPorVehiculo):
    '''
    classdocs
    '''


    def __init__(self, parent = None):
        '''
        Constructor
        '''
        super(WidgetMostrarReparacionesPorVehiculo, self).__init__(parent)
        self.setupUi(self)
        