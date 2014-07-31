'''
Created on 22/07/2014

@author: LeoMorales
'''

from PyQt4 import QtCore, QtGui

from formularios.DlgAsignarReparaciones import Ui_DialogoAsignarReparaciones
from negocio.Division_Transporte import Division_Transporte
from PyQt4.Qwt5.qplt import QString
from Utiles_Dialogo import mostrarMensaje, compara_fechas_en_cadenas
from negocio.excepciones.SinTurnosException import SinTurnosException

class DialogoAsignarReparaciones(QtGui.QDialog, Ui_DialogoAsignarReparaciones):
    '''
    classdocs
    '''
    def __init__(self, parent = None, seccion= None):
        '''
        Constructor
        '''
        super(DialogoAsignarReparaciones, self).__init__(parent)
        self.setupUi(self)
        self.buttonBox.connect(self, QtCore.SIGNAL('accepted()'), self.aceptar)
        self.buttonBox.connect(self, QtCore.SIGNAL('rejected()'), self.cancelar)
        self._seccion = seccion
        dias_con_turnos = list(self._seccion.getDiasEnLosQueHayTurnoSinAsignar())
        dias_con_turnos.sort(cmp=compara_fechas_en_cadenas)
        for dia in dias_con_turnos:
            self.comboBoxFecha.addItems(QtCore.QStringList(dia))
        try:
            self._fechaSeleccionada = dias_con_turnos[0]
        except IndexError:
            mostrarMensaje(self, 'Su seccion no posee turnos sin asignar', 'Sin turnos no asignados')
            raise SinTurnosException("No turnos!")
        self._horaSeleccionada = self.refrescarComboHora()
        self._turnoSeleccionado = self._seccion.getTurnoDeFechaHora(self._fechaSeleccionada,self._horaSeleccionada )
        self.refrescarDatosTurno()
#        self.refrescarReparaciones()
#        self._empleadosSinAsignar = self._seccion.getEmpleados().values()
        self._empleadosSinAsignar = self._seccion.getEmpleados()
        self._empleadosAsignados = []
        self.refrescarTablasEmpleados()
    
    def on_comboBoxFecha_currentIndexChanged(self):
        self._fechaSeleccionada = unicode(self.comboBoxFecha.currentText())
        self._horaSeleccionada = self.refrescarComboHora()
        self._turnoSeleccionado = self._seccion.getTurnoDeFechaHora(self._fechaSeleccionada,self._horaSeleccionada)
        self.refrescarDatosTurno()

    def on_comboBoxHora_currentIndexChanged(self):
#        self._horaSeleccionada = int(self.comboBoxHora.currentText())
        self._horaSeleccionada = self.comboBoxHora.currentText().toInt()
        self._turnoSeleccionado = self._seccion.getTurnoDeFechaHora(self._fechaSeleccionada,self._horaSeleccionada)
        self.refrescarDatosTurno()
        
    def refrescarComboHora(self):
        '''
        Refresca el combo y ademas devuelve el primer valor de la lista de sus valores'''
        self.comboBoxHora.clear()
        horas = self._seccion.getHorasEnLosQueHayTurnoSinAsignar(self._fechaSeleccionada)
        for hora in horas:
            self.comboBoxHora.addItems(QtCore.QStringList(str(hora)))
        return horas[0]

    def refrescarTablasEmpleados(self):
        '''
        Modo de uso:
        Primero setear las listas con los valores que se quieran,
        luego invocar este metodo
        '''
        self.pushButtonAsignar.setEnabled(True)
        self.pushButtonDesasignar.setEnabled(True)
        if not self._empleadosAsignados:
            self.pushButtonDesasignar.setEnabled(False)
        if not self._empleadosSinAsignar:
            self.pushButtonAsignar.setEnabled(False)
        self.tableWidgetEmpleadosAsignados.cargarConEmpleados(self._empleadosAsignados)
        self.tableWidgetEmpleadosDisponibles.cargarConEmpleados(self._empleadosSinAsignar)
    
    def refrescarDatosTurno(self):
        '''
        Primero setear el turno y luego llamar a este metodo
        '''
        self.labelDominio.setText(QString(self._turnoSeleccionado.getVehiculo().getDominio()))
        self._reparacionesTurno = self._turnoSeleccionado.getReparaciones()
        self.tableWidgetReparaciones.cargarConReparaciones(self._reparacionesTurno)

    @QtCore.pyqtSlot()
    def on_pushButtonAsignar_clicked(self):
        if not self.tableWidgetEmpleadosDisponibles.getEmpleadoSeleccionado():
            mostrarMensaje(self, 'Debe seleccionar un empleado.', 'Seleccionar')
            return
        self._empleadosAsignados.append(self.tableWidgetEmpleadosDisponibles.getEmpleadoSeleccionado())
        self._empleadosSinAsignar.remove(self.tableWidgetEmpleadosDisponibles.getEmpleadoSeleccionado())        
        self.refrescarTablasEmpleados()
    
    @QtCore.pyqtSlot()
    def on_pushButtonDesasignar_clicked(self):
        
        if not self.tableWidgetEmpleadosAsignados.getEmpleadoSeleccionado():
            mostrarMensaje(self, 'Debe seleccionar un empleado.', 'Seleccionar')
            return
        self._empleadosSinAsignar.append(self.tableWidgetEmpleadosAsignados.getEmpleadoSeleccionado())
        self._empleadosAsignados.remove(self.tableWidgetEmpleadosAsignados.getEmpleadoSeleccionado())        
        self.refrescarTablasEmpleados()
        
    def aceptar(self):
        mostrarMensaje(self,
                       'Turno: %s %dhs.\nSe asignaron los siguientes empleados:\n%s'%(self._fechaSeleccionada,
                                                                                      self._horaSeleccionada,
                                                                                      '\n'.join([e.getNombre() for e in self._empleadosAsignados])),
                       'Asignacion finalizada'
                       )
        self._turnoSeleccionado.asignarEmpleados(self._empleadosAsignados)

    def cancelar(self):
        #No tirar commits a lo loco
        #Y ademas:
        #alvehiculo.decirleQuePongaTodasSusReparacionesCOmoNoPlanificadas!
        pass
    
