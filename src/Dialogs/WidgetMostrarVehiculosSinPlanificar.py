# -*- coding: utf-8 -*-
'''
Created on 03/10/2012

@author: Usuario
'''
from PyQt4 import QtCore, QtGui
from formularios.WidgetMostrarVehiculosSinPlanificar import Ui_WidgetMostrarVehiculosSinPlanificar
from formularios.DialogPlanificarReparaciones import Ui_DialogPlanificarReparaciones
from formularios.DialogAsignarFechaReparacion import Ui_AsignarFechaReparacion

class DialogAsignarFechaReparacion(QtGui.QDialog, Ui_AsignarFechaReparacion):
    '''
    classdocs
    '''
    def __init__(self, parent = None):
        '''
        Constructor
        '''
        super(DialogAsignarFechaReparacion, self).__init__(parent)
        self.setupUi(self)


class DialogPlanificarReparaciones(QtGui.QDialog, Ui_DialogPlanificarReparaciones):
    '''
    classdocs
    '''
    def __init__(self, parent = None):
        '''
        Constructor
        '''
        super(DialogPlanificarReparaciones, self).__init__(parent)
        self.setupUi(self)
        self.connect(self.pushButtonPlanificarReparacion, QtCore.SIGNAL("pressed()"), self.abrirDialogAsignarFechaReparacion)
       
    def abrirDialogAsignarFechaReparacion(self):
        print 'abriendo dialogo AsignarFechaReparacion'
        dlgAsignarFechaReparacion = DialogAsignarFechaReparacion(self)
        dlgAsignarFechaReparacion.exec_()
    

class WidgetMostrarVehiculosSinPlanificar(QtGui.QWidget, Ui_WidgetMostrarVehiculosSinPlanificar):
    '''
    classdocs
    '''
    def __init__(self, parent = None):
        '''
        Constructor
        '''
        super(WidgetMostrarVehiculosSinPlanificar, self).__init__(parent)
        self.setupUi(self)
        #Conectamos el boton Planificar Reparaciones...
        self.connect(self.pushButtonPlanificarReparaciones, QtCore.SIGNAL("pressed()"), self.abrirDialogPlanificarReparaciones)
       
    def abrirDialogPlanificarReparaciones(self):
        print 'abriendo dialogo Planificar Reparaciones'
        dlgPlanificarReparaciones = DialogPlanificarReparaciones(self)
        dlgPlanificarReparaciones.exec_()

    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        '''
        @version: 
        @author: 
        '''
        self.close()