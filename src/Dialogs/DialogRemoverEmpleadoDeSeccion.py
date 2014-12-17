# -*- coding: utf-8 -*-
'''
Created on 13/11/2012

@author: urrutia
'''

from PyQt4 import QtCore, QtGui

from formularios.DialogRemoverEmpleadoDeSeccion import Ui_DialogRemoverEmpleadoDeSeccion
from negocio.Division_Transporte import Division_Transporte
from Utiles_Dialogo import mostrarMensaje, Mensaje
from PyQt4.QtGui import QMessageBox

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
        secciondelempleadoseleccionado = Division_Transporte().getSeccionDeEmpleado(empleado_seleccionado)
        msg = 'Desea remover al empleado \'%s\' de la seccion \'%s\'?' %(empleado_seleccionado.nombreCompleto(), secciondelempleadoseleccionado.getNombre()) 
        #mostrarMensaje(self, msg, 'Confirmar remover empleado')
        msjConfirmar = Mensaje(self, msg, "Confirmar remover")
        msjConfirmar.agregarBotonCancelar()
        msjConfirmar.setCritical()
        retorno = msjConfirmar.exec_()
        if retorno == QMessageBox.Cancel:
            debug= "DEBUG: Cancelar accion remover empleado de seccion"
            return
        if retorno == QMessageBox.Ok:
            msg = 'El empleado \'%s\' ha sido removido de la seccion \'%s\'' %(empleado_seleccionado.nombreCompleto(), secciondelempleadoseleccionado.getNombre())
            Division_Transporte().nuevoEmpleadoDisponible(empleado_seleccionado)
            secciondelempleadoseleccionado.removerEmpleado(empleado_seleccionado)
            mostrarMensaje(self, msg, 'Empleado removido')
        self.refrescarTabla()
        
    def refrescarTabla(self):
        self.tableWidget_empleados.cargarConEmpleadosDeSecciones(Division_Transporte().getSeccionesQuePuedenTransferir())