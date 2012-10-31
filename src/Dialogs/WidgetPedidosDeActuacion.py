'''
Created on 10/10/2012

@author: urrutia
'''

from PyQt4 import QtGui, QtCore
from formularios.WidgetPedidosDeActuacion import Ui_FormPedidoDeActuacion

class WidgetRegistrarPedidoDeActuacion(QtGui.QWidget, Ui_FormPedidoDeActuacion):
    def __init__(self, parent = None):
        super(WidgetRegistrarPedidoDeActuacion, self).__init__(parent)
        self.setupUi(self)
        self.connect(self.pushButton_Registrar, QtCore.SIGNAL("pressed()"), self.registrarFecha)
        
    def registrarFecha(self):
        print "Click sobre Registrar Fecha de Recepcion"