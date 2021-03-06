# -*- coding: utf-8 -*-
'''
Created on 13/11/2012

@author: urrutia
'''

from PyQt4 import QtCore, QtGui
import transaction
from time import localtime

from formularios.DialogCambiarDeSeccionUnEncargado import Ui_DialogCambiaDeSeccionUnEncargado
from negocio.Division_Transporte import Division_Transporte
from FormContrasenaEncargado import DialogCrearUsuarioEncargado
from negocio.usuario import Usuario
from AyudaManejador import AyudaManejador


class DialogCambiarDeSeccionUnEncargado(QtGui.QDialog, Ui_DialogCambiaDeSeccionUnEncargado, AyudaManejador):
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
    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super(DialogCambiarDeSeccionUnEncargado, self).__init__(parent)
        self.setupUi(self)
        self._secciones = Division_Transporte().getSecciones().values()#secciones con las que trabajara el dialogo
        self.tableWidget_secciones.cargarConSecciones(self._secciones)
        self._empleados = Division_Transporte().getEmpleadosSinAsignar().values()#empleados con los que trabajara el empleado
        self.tableWidget_empleados.cargarConEmpleados(self._empleados)
        fecha = localtime()
        self.DIVISION = Division_Transporte()
        self.DIVISION.zodb.setFechaMinimaDeshacer(fecha)
        self.pushButton_filtroEmpleado.setVisible(False)
        self.pushButton_filtroEmpleado.setHidden(True)

    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        self.DIVISION.zodb.deshacerCommits()
        self.reject()

    @QtCore.pyqtSlot()
    def on_pushButtonAceptar_clicked(self):
        # 1)Tomar el empleado seleccionado
        empleado_que_va_a_ser_encargado = self.tableWidget_empleadoSeleccionado.getPrimerEmpleado()
        # 2)Pedir una contrasena para el nuevo encargado
        if not self.pedirPassEncargado(empleado_que_va_a_ser_encargado):
            return
        # 3)Crearle un nuevo usuario.
        usrNew = Usuario(unicode(empleado_que_va_a_ser_encargado.nombreCompletoUsr()), unicode(empleado_que_va_a_ser_encargado.getPassword()))
        usrNew.registrar('jefeSeccion')
        empleado_que_va_a_ser_encargado.setUsuario(usrNew)
        # 4)Tomar la seccion seleciconada
        seccion_seleccionada = self.tableWidget_seccionSeleccionada.getPrimeraSeccion()
        # 5)Decirle a la seccion seleccionada, reemplazarEncargado
        encargado_anterior = seccion_seleccionada.asignarNuevoEncargado(empleado_que_va_a_ser_encargado)
        Division_Transporte().eliminarEmpleadoDisponible(empleado_que_va_a_ser_encargado)
        # 6)Devolver el encargado anterior a empleado disponible
        Division_Transporte().borraUsuario(encargado_anterior)
        encargado_anterior.desregistrarUsuario()
        Division_Transporte().agregarEmpleadoDisponible(encargado_anterior)
        # 7)Commitear
        # Para saber de qué cliente debemos borrar las transacciones.
        transaction.get().setUser(self.DIVISION.zodb.getNombreUsuario(), '')
        transaction.commit()

    def pedirPassEncargado(self, encargado):
        '''
            Pide la password para el nuevo encargado.
            @return: True si pudo conseguir la pass de modo exitoso. False si se cancelo el dialogo.
        '''
        dialog = DialogCrearUsuarioEncargado(encargado.nombreCompletoUsr())
        while True:
            if dialog.exec_() == QtGui.QDialog.Accepted:
                if dialog.contrasenasValidas():
                    encargado.setPassword(dialog.getPassEncargado())
#                    print 'Pass Encargado: %s' % (dialog.getPassEncargado())
                    return True
                else:
                    dialog.preparar_para_volver_a_pedir()
            else:
                return False

    @QtCore.pyqtSlot()
    def on_pushButton_elegirEmpleado_clicked(self):
        # Cargamos la tabla de empleado seleccionado, con el empleado seleccionado... :O
        self.tableWidget_empleadoSeleccionado.cargarConEmpleados([self.tableWidget_empleados.getEmpleadoSeleccionado()])
        # Habilitamos el boton para remover seleccion:
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

    @QtCore.pyqtSlot('QString')
    def on_lineEdit_filtroEmpleado_textChanged(self, cadena):
        filtro = unicode(cadena).lower()
        personal = filter(lambda p: filtro in unicode(p.getDocumento()).lower()
                          or filtro in unicode(p.getNombre()).lower()
                          or filtro in unicode(p.getApellido()).lower()
                          or filtro in unicode(p.getEmail()).lower()
                          or filtro in unicode(p.getTelefono()).lower(),
                          self._empleados)
        personal.sort(cmp=lambda x, y: cmp(x, y))
        self.tableWidget_empleados.cargarConEmpleados(personal)

    @QtCore.pyqtSlot('QString')
    def on_lineEdit_filtroSeccion_textChanged(self, cadena):
        filtro = unicode(cadena).lower()
        secciones = filter(lambda seccion: filtro in unicode(seccion.getNombre()).lower(), self._secciones)
        self.tableWidget_secciones.cargarConSecciones(secciones)
