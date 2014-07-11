# -*- coding: utf-8 -*-
'''
Created on 13/11/2012

@author: urrutia
'''

from PyQt4 import QtCore, QtGui

from formularios.DialogRemoverEmpleadoDeSeccion import Ui_DialogRemoverEmpleadoDeSeccion
from negocio.Division_Transporte import Division_Transporte
from Utiles_Dialogo import mostrarMensaje

class DialogRemoverEmpleadoDeSeccion(QtGui.QDialog, Ui_DialogRemoverEmpleadoDeSeccion):
    '''
    Dialog contiene:
        - lineEdit_condicionDeFiltro
        - pushButton_filtroSeccion
        - tableWidget_empleados
        - pushButton_removerEmpleados
        - pushButtonAceptar
        - pushButtonCancelar
        
    '''
    def __init__(self, parent = None):
        '''
        Constructor
        '''
        super(DialogRemoverEmpleadoDeSeccion, self).__init__(parent)
        self.setupUi(self)
        self.tableWidget_empleados.cargarConEmpleadosDeSecciones(Division_Transporte().getSeccionesQuePuedenTransferir())
        
    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        self.reject()

    @QtCore.pyqtSlot()
    def on_pushButton_removerEmpleados_clicked(self):
        empleado_seleccionado = self.tableWidget_empleados.getEmpleadoSeleccionado()
        msg = 'Desea remover al empleado \'%s\' de la seccion \'%s\'?' %(empleado_seleccionado.nombreCompleto(), Division_Transporte().getSeccionDeEmpleado(empleado_seleccionado).getNombre()) 
        mostrarMensaje(self, msg, 'Confirmar remover empleado')
        
    