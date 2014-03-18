# -*- coding: utf-8 -*-
'''
Created on 13/11/2012

@author: urrutia
'''

from PyQt4 import QtCore, QtGui

from formularios.DialogCambiarDeSeccionUnEncargado import Ui_DialogCambiaDeSeccionUnEncargado
from negocio.Division_Transporte import Division_Transporte

class DialogCambiarDeSeccionUnEncargado(QtGui.QDialog, Ui_DialogCambiaDeSeccionUnEncargado):
    '''
        El Dialogo contiene:
            - lineEdit_filtroEmpleado
            - pushButton_filtroEmpleado
            - tableWidget_empleados
            - pushButton_elegirEmpleado
            - pushButton_removerEmpleado
            - tableWidget_empleadoSeleccionado
        
            - lineEdit_filtroSeccion
            - pushButton_filtroSeccion
            - tableWidget_secciones
            - pushButton_elegirSeccion
            - pushButton_removerSeccion
            - tableWidget_seccionSeleccionada
        
            - pushButtonAceptar
            - pushButtonCancelar
    '''
    def __init__(self, parent = None):
        '''
        Constructor
        '''
        super(DialogCambiarDeSeccionUnEncargado, self).__init__(parent)
        self.setupUi(self)
        self.tableWidget_secciones.cargarConSecciones(Division_Transporte().getSecciones().values())
        self.tableWidget_empleados.cargarConEmpleados(Division_Transporte().getEmpleadosSinAsignar().values()) 
        
    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        self.reject()
        
    @QtCore.pyqtSlot()
    def on_pushButton_elegirEmpleado_clicked(self):
        #Cargamos la tabla de empleado seleccionado, con el empleado seleccionado... :O
        self.tableWidget_empleadoSeleccionado.cargarConEmpleados([self.tableWidget_empleados.getEmpleadoSeleccionado()])
        #Habilitamos el boton para remover seleccion:
        self.pushButton_removerEmpleado.setEnabled(True)
        self.pushButton_elegirEmpleado.setEnabled(False)
        
    @QtCore.pyqtSlot()
    def on_pushButton_elegirSeccion_clicked(self):
        #Cargamos la tabla de empleado seleccionado, con el empleado seleccionado... :O
        self.tableWidget_seccionSeleccionada.cargarConSecciones([self.tableWidget_secciones.getSeccionSeleccionada()])
        #Habilitamos el boton para remover seleccion:
        self.pushButton_removerSeccion.setEnabled(True)
        #Deshabilitamos el boton para seleccionar:
        self.pushButton_elegirSeccion.setEnabled(False)

    @QtCore.pyqtSlot()
    def on_pushButton_removerEmpleado_clicked(self):
        self.tableWidget_empleadoSeleccionado.cargarConEmpleados([])
        self.pushButton_removerEmpleado.setEnabled(False)
        self.pushButton_elegirEmpleado.setEnabled(True)
        
    @QtCore.pyqtSlot()
    def on_pushButton_removerSeccion_clicked(self):
        self.tableWidget_seccionSeleccionada.cargarConSecciones([])
        self.pushButton_removerSeccion.setEnabled(False)
        self.pushButton_elegirSeccion.setEnabled(True)
        