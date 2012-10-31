'''
Created on 10/10/2012

@author: urrutia
'''
from PyQt4 import QtGui, QtCore
from formularios.WidgetListadoSecciones import Ui_FormListadoSecciones

class ListadoSecciones(QtGui.QWidget, Ui_FormListadoSecciones):
    def __init__(self, parent = None):
        super(ListadoSecciones, self).__init__(parent)
        self.setupUi(self)
#        self.connect(self.pushButtonSeleccionar, QtCore.SIGNAL("pressed()"), self.seleccionarSeccion)
        
    def seleccionarSeccion(self):
        print "Click sobre Seleccionar Seccion"