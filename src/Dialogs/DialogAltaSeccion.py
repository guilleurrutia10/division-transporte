# -*- coding: utf-8 -*-
'''
Created on 03/10/2012

@author: Usuario
'''
from PyQt4 import QtCore, QtGui

from formularios.DialogAltaSeccion import Ui_DialogAltaSeccion
from negocio.Division_Transporte import Division_Transporte
from FormContrasenaEncargado import DialogCrearUsuarioEncargado

from Utiles_Dialogo import mostrarMensaje
from AyudaManejador import AyudaManejador
COLUMNA_DNI = 0


class DialogAltaSeccion(QtGui.QDialog, Ui_DialogAltaSeccion, AyudaManejador):
    '''
    classdocs
    '''
    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super(DialogAltaSeccion, self).__init__(parent)
        self.setupUi(self)
        self.DIVISION = Division_Transporte()
        self.tableWidgetEmpleadosAsignados.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.tableWidgetEmpleadosSinAsignar.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.empleadosAsignados = [] #Lista que contendra todos los objetos Empleado que estan siendo asignados a la nueva seccion,
        self.empleadosSinSeccion = [] #Lista que contendra todos los objetos Empleado que estan disponibles para la nueva seccion,
        self.validacionesLineEdit()
        self.cargarGrillaInicial()
        # Objeto Empleado asignado como Encargado de la nueva Seccion
        self._encargado = None
        # Desactivado al principio!
        self.pushButtonDesasignarEncargado.setDisabled(True)

        #seteo de nombres de los Labels para el estilo 
        self.label.setObjectName("label")
        self.label_2.setObjectName("label")
        self.label_3.setObjectName("label")
        self.label_4.setObjectName("label")

    def validacionesLineEdit(self):
        self.lineEditNombreSeccion.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[A-Za-z]+'), self))

    def conectarSignals(self):
        self.tableWidgetEmpleadosSinAsignar.connect(self.tableWidgetEmpleadosSinAsignar, QtCore.SIGNAL('cellClicked(int,int)'), self.celdaClickeada_on_tableWidgetEmpleadosSinAsignar)
        self.tableWidgetEmpleadosAsignados.connect(self.tableWidgetEmpleadosAsignados, QtCore.SIGNAL('cellClicked(int,int)'), self.celdaClickeada_on_tableWidgetEmpleadosAsignados)

    @QtCore.pyqtSlot()
    def on_pushButtonAceptar_clicked(self):
        nombreSeccion = unicode(self.lineEditNombreSeccion.text())
        if len(nombreSeccion) is 0:
            mostrarMensaje(self, 'Debe ingresar el nombre de la Sección', 'Ingresar Sección')
            return
        # Se comprueba si se han asignado al menos dos empleados a la Sección
        if self.tableWidgetEmpleadosAsignados.rowCount() < 2:
            mostrarMensaje(self, 'No se han cargado suficientes empleados a la Seccion. Debe cargar al menos dos.', 'Error al cargar empleados')
            return
        # Se comprueba que se haya asignado un encargado a la Sección
        if not self._encargado:
            mostrarMensaje(self, 'No se ha asignado el Encargado de la Seccion.', 'Error al cargar encargado')
            return
##        print 'Cargando la nueva Seccion...'

        #self._encargado.setPassword('') #Seteamos una variable dinamica en el encargado
        self.pedirPassEncargado()
        if self._encargado.getPassword() == '': return
        #while self._encargado.getPassword() == '':
        #    self.pedirPassEncargado()

        #agregarSeccion se va a encargar tmb de registrar el Usuario del encargado y registrarlo...
        #Division_Transporte().agregarSeccion(nombreSeccion, self.empleadosAsignados , self._encargado)
        self.DIVISION.agregarSeccion(nombreSeccion, self.empleadosAsignados , self._encargado)

        if mostrarMensaje(self, 'La Sección se ha cargado exitosamente! :)', 'Cargando'):
            self.accept()

    def pedirPassEncargado(self):
        '''
            Crea un Usuario nuevo para que el Encargado de la Seccion pueda logearse como tal.
            @precondition: self._encargado != None.
        '''
        dialog = DialogCrearUsuarioEncargado(self._encargado.nombreCompletoUsr(), self)
        while True:
            if dialog.exec_() == QtGui.QDialog.Accepted:
                if dialog.contrasenasValidas():
                    self._encargado.setPassword(dialog.getPassEncargado())
#                    print 'Pass Encargado: %s' % (dialog.getPassEncargado())
                    break
                else:
#                    dialog.lineEditPassword.clear()
#                    dialog.lineEditPassword2.clear()
#                    dialog.lineEditPassword.setFocus()
#                    dialog.labelMsgError.setText("Las claves no coinciden, ingrese nuevamente")
                    dialog.preparar_para_volver_a_pedir()
            else:
                break
         
   
#        if dialog.exec_() == QtGui.QDialog.Accepted:
#            self._encargado.setPassword(dialog.getPassEncargado())
##            print 'Pass Encargado: %s' % (dialog.getPassEncargado())

    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        self.reject()

    def cargarGrillaInicial(self):
        self.empleadosSinSeccion = self.obtenerListaEmpleadosSinAsignar()
        self.empleadosSinSeccion = sorted(self.empleadosSinSeccion, cmp=lambda x, y : cmp(x.documento, y.documento))
        self.tableWidgetEmpleadosSinAsignar.cargarConEmpleados(self.empleadosSinSeccion)

    def obtenerListaEmpleadosSinAsignar(self):
        personal = self.DIVISION.getEmpleadosSinAsignar()
        return personal.values()

    def celdaClickeada_on_tableWidgetEmpleadosSinAsignar(self, fila, columna):
        self.filaSeleccionadaSinAsignar = fila

    def celdaClickeada_on_tableWidgetEmpleadosAsignados(self, fila, columna):
        self.filaSeleccionadaAsignados = fila

    @QtCore.pyqtSlot()
    def on_pushButtonAsignarEmpleado_clicked(self):
        if not self.tableWidgetEmpleadosSinAsignar.getEmpleadoSeleccionado():
            mostrarMensaje(self, 'Debe Seleccionar un Empleado.', 'Seleccionar')
            return

        self.empleadosSinSeccion.remove(self.tableWidgetEmpleadosSinAsignar.getEmpleadoSeleccionado())
        self.empleadosAsignados.append(self.tableWidgetEmpleadosSinAsignar.getEmpleadoSeleccionado())
        self.tableWidgetEmpleadosAsignados.cargarConEmpleados(self.empleadosAsignados)
        self.tableWidgetEmpleadosSinAsignar.cargarConEmpleados(self.empleadosSinSeccion)

    @QtCore.pyqtSlot()
    def on_pushButtonDesasignarEmpleado_clicked(self):
        if not self.tableWidgetEmpleadosAsignados.getEmpleadoSeleccionado():
            mostrarMensaje(self, 'Debe Seleccionar un Empleado.', 'Seleccionar')
            return
        self.empleadosAsignados.remove(self.tableWidgetEmpleadosAsignados.getEmpleadoSeleccionado())
        self.empleadosSinSeccion.append(self.tableWidgetEmpleadosAsignados.getEmpleadoSeleccionado())
        self.tableWidgetEmpleadosAsignados.cargarConEmpleados(self.empleadosAsignados)
        self.tableWidgetEmpleadosSinAsignar.cargarConEmpleados(self.empleadosSinSeccion)

    @QtCore.pyqtSlot()
    def on_pushButtonAsignarComoEncargado_clicked(self):
        if not self.tableWidgetEmpleadosSinAsignar.getEmpleadoSeleccionado(): 
            mostrarMensaje(self, 'Debe Seleccionar un Empleado.', 'Seleccionar')
            return

        # Paso1, setear el encargado de la seccion
        self._encargado = self.tableWidgetEmpleadosSinAsignar.getEmpleadoSeleccionado()
        # Paso2, refrescar la grilla del encargado
        self.tableWidgetEncargadoAsignado.cargarConEmpleados([self._encargado])
        # Paso3, remover al encargado de los empleados disponibles y de la grilla
        self.empleadosSinSeccion.remove(self._encargado)
        self.tableWidgetEmpleadosSinAsignar.cargarConEmpleados(self.empleadosSinSeccion)
        # Paso4, desactivar el boton de asignar encargado y activar el de desasignacion
        self.pushButtonAsignarComoEncargado.setDisabled(True)
        self.pushButtonDesasignarEncargado.setDisabled(False)

        self.filaSeleccionadaSinAsignar = None

    @QtCore.pyqtSlot()
    def on_pushButtonDesasignarEncargado_clicked(self):
        # Paso1, devolver al encargado a la lista de empleados disponibles
        self.empleadosSinSeccion.append(self._encargado)
        # Paso2, Refrescar grilla empleados disponibles
        self.tableWidgetEmpleadosSinAsignar.cargarConEmpleados(self.empleadosSinSeccion)
        # Paso3, setear el encargado de la seccion
        self._encargado = None
        # Paso4, refrescar la grilla del encargado
        self.tableWidgetEncargadoAsignado.cargarConEmpleados([])

        # Paso5, desactivar el boton de desasignar encargado y activar el de asignacion
        self.pushButtonAsignarComoEncargado.setDisabled(False)
        self.pushButtonDesasignarEncargado.setDisabled(True)
