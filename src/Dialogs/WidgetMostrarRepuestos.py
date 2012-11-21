# -*- coding: utf-8 -*-
'''
Created on 03/10/2012

@author: Usuario
'''
from PyQt4 import QtCore, QtGui

from formularios.WidgetMostrarRepuestos import Ui_FormMostrarRepuestos
from formularios.DialogModificarRepuesto import Ui_DialogMoficarRepuesto
from negocio.Division_Transporte import Division_Transporte

class DialogModificarRepuesto(QtGui.QDialog, Ui_DialogMoficarRepuesto):
    '''
    classdocs
    '''
    def __init__(self, parent = None):
        '''
        Constructor
        '''
        super(DialogModificarRepuesto, self).__init__(parent)
        self.setupUi(self)

class WidgetMostrarRepuestos(QtGui.QWidget, Ui_FormMostrarRepuestos):
    '''
    classdocs
    '''


    def __init__(self, parent = None):
        '''
        Constructor
        '''
        super(WidgetMostrarRepuestos, self).__init__(parent)
        self.setupUi(self)
        #Conectamos el boton Modificar Repuesto...
        self.connect(self.pushButtonModificarRepuesto, QtCore.SIGNAL("pressed()"), self.abrirDialogModificarRepuesto)
        
    def abrirDialogModificarRepuesto(self):
        print 'abriendo dialogo ModificarRepuesto'
        dlgModificarRepuesto= DialogModificarRepuesto(self)
        dlgModificarRepuesto.exec_()