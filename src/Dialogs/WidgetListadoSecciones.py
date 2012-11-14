# -*- coding: utf-8 -*-
'''
Created on 10/10/2012

@author: urrutia
'''
from PyQt4 import QtGui, QtCore
from formularios.WidgetListadoSecciones2 import Ui_FormListadoSecciones

class ListadoSecciones(QtGui.QWidget, Ui_FormListadoSecciones):
    def __init__(self, parent = None):
        super(ListadoSecciones, self).__init__(parent)
        self.setupUi(self)
        
    def seleccionarSeccion(self):
        print "Click sobre Seleccionar Seccion"