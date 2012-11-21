# -*- coding: utf-8 -*-
'''
Created on 03/10/2012

@author: Usuario
'''
from PyQt4 import QtCore, QtGui
from formularios.WidgetBajaPersonal import Ui_FormBajaPersonal
from Dialogs import DialogModificarPersonal

class WidgetBajaPersonal(QtGui.QWidget, Ui_FormBajaPersonal):
    '''
    classdocs
    '''


    def __init__(self, parent = None):
        '''
        Constructor
        '''
        super(WidgetBajaPersonal, self).__init__(parent)
        self.setupUi(self)
        self.connect(self.pushButtonModificar, QtCore.SIGNAL("pressed()"), self.abrirDialogModificarPersonal)
       
    def abrirDialogModificarPersonal(self):
        print 'abriendo dialogo AsignarFechaReparacion'
        dlgModificarPersonal= DialogModificarPersonal.DialogModificarPersonal(self)
        dlgModificarPersonal.exec_()
        