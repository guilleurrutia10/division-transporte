'''
Created on 29/07/2014

@author: LeoMorales
'''
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QString
import transaction

from formularios.DlgFinalizarTurno import Ui_DialogoFinalizarTurno
from Utiles_Dialogo import mostrarMensaje, compara_fechas_en_cadenas
from negocio.excepciones.SinTurnosException import SinTurnosException
from AyudaManejador import AyudaManejador


class DialogoRegistrarFinTurno(QtGui.QDialog, Ui_DialogoFinalizarTurno, AyudaManejador):
    '''
    Atributos:
        self._seccion
        self._fechaSeleccionada
        self._horaSeleccionada
        self._turnoSeleccionado
    '''
    def __init__(self, parent=None, seccion=None):
        '''
        Constructor
        '''
        super(DialogoRegistrarFinTurno, self).__init__(parent)
        self.setupUi(self)
        self._seccion = seccion
        # Variable para ignorar los cambios en los combo en el momento de carga de los mismos...
        self._todoCargado = False
        self.inicializar()

    def inicializar(self):
        # omboBoxFecha:
        dias_con_turnos = list(self._seccion.getDiasEnLosQueHayTurnoAsignado())
        dias_con_turnos.sort(cmp=compara_fechas_en_cadenas)
        for dia in dias_con_turnos:
            self.comboBoxFecha.addItems(QtCore.QStringList(dia))
        try:
            self._fechaSeleccionada = dias_con_turnos[0]
        except IndexError:
            mostrarMensaje(self, 'Su seccion no posee turnos asignados', 'Sin turnos asignados')
            raise SinTurnosException("No turnos!")

        #comboBoxHora:
        self._horaSeleccionada = self.refrescarComboHora()

        #Inicializar turno:
        self._turnoSeleccionado = self._seccion.getTurnoDeFechaHora(self._fechaSeleccionada,self._horaSeleccionada)

        #Label dominio:
        self.labelDominio.setText(QString(self._turnoSeleccionado.getVehiculo().getDominio()))

        #Tabla de reparaciones:
        self.tableWidgetReparaciones.cargarConReparaciones(self._turnoSeleccionado.getReparaciones())

        #Tabla de empleados asignados:
        self.tableWidgetEmpleados.cargarConEmpleados(self._turnoSeleccionado.getEmpleadosAsignados())

        self.tableWidgetReparaciones.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.tableWidgetEmpleados.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)

        #Css:
        self.labelFecha.setObjectName('label')
        self.labelHora.setObjectName('label')
        self.labelVehiculo.setObjectName('label')
        self.label_2.setObjectName('label')
        self.labelReparaciones.setObjectName('label')

        self._todoCargado = True

    def refrescarComboHora(self):
        '''
        @precondition: self._fechaSeleccionada esta cargada.
        Valiendose de la fecha seleccionada, refresca el combo de hora.
        Ademas devuelve el primer valor de la lista de sus valores.
        Siempre va a poder buscar horas xq sino en primer termino nunca se podria haber elegido
        la fecha seleccionada.
        '''
        self.comboBoxHora.clear()
        horas = self._seccion.getHorasEnLosQueHayTurnoAsignados(self._fechaSeleccionada)
        for hora in horas:
            self.comboBoxHora.addItems(QtCore.QStringList(str(hora)))
        return horas[0]

    def on_comboBoxFecha_currentIndexChanged(self):
        if not self._todoCargado:
            return
        self._fechaSeleccionada = unicode(self.comboBoxFecha.currentText())
        self._horaSeleccionada = self.refrescarComboHora()
        self._turnoSeleccionado = self._seccion.getTurnoDeFechaHora(self._fechaSeleccionada,self._horaSeleccionada)
        self.refrescarDatosTurno()

    def on_comboBoxHora_currentIndexChanged(self):
        if not self._todoCargado:
            return
        self._horaSeleccionada = self.comboBoxHora.currentText().toInt()
        self._turnoSeleccionado = self._seccion.getTurnoDeFechaHora(self._fechaSeleccionada,self._horaSeleccionada)
        self.refrescarDatosTurno()

    def refrescarDatosTurno(self):
        '''
        Primero setear el turno y luego llamar a este metodo
        '''
        self.labelDominio.setText(QString(self._turnoSeleccionado.getVehiculo().getDominio()))
        self.tableWidgetReparaciones.cargarConReparaciones(self._turnoSeleccionado.getReparaciones())
        self.tableWidgetEmpleados.cargarConEmpleados(self._turnoSeleccionado.getEmpleadosAsignados())
        
    @QtCore.pyqtSlot()
    def on_pushButtonFinalizar_clicked(self):
        self._turnoSeleccionado.finalizar(unicode(self.plainTextEditObservaciones.toPlainText()))
        transaction.commit()
        self.accept()
        
    @QtCore.pyqtSlot()
    def on_pushButtonSalir_clicked(self):
        self.reject()