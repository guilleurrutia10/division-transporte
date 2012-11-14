# -*- coding: utf-8 -*-
'''
Created on 02/11/2012

@author: urrutia
'''

from PyQt4 import QtCore, QtGui

from formularios.DialogSeleccionarSeccion import Ui_Dialog_SeleccionarSeccion

import WidgetListadoSecciones, DialogAsignarReparacion

class DialogSeleccionarSeccion(QtGui.QDialog, Ui_Dialog_SeleccionarSeccion):
    '''
    classdocs
    '''


    def __init__(self, parent = None):
        '''
        Constructor
        '''
        super(DialogSeleccionarSeccion, self).__init__(parent)
        self.setupUi(self)
        WidgetListadoSecciones.ListadoSecciones(self.widget_SeleccionarSeccion)
        
    @QtCore.pyqtSlot()
    def on_pushButton_Seleccionar_clicked(self):
        print "Click sobre Seleccionar"
        self.close()
        dlgSelecSec = DialogAsignarReparacion.DialogAsignarReparacion()
        dlgSelecSec.exec_()
    
    @QtCore.pyqtSlot()
    def on_pushButton_Cancelar_clicked(self):
        self.close()