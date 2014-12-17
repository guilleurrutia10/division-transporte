# -*- coding: utf-8 -*-
'''
Created on 20/07/2014

@author: LeoMorales
'''

from PyQt4 import QtCore, QtGui
import transaction
from datetime import date
from time import localtime

from formularios.DlgPlanificar import Ui_DialogPlanificar
from Utiles_Dialogo import mostrarMensaje
from negocio.Turno import Turno
from negocio.Division_Transporte import Division_Transporte
from reportes import generarHojaDeRuta
from PyQt4.QtGui import QFileDialog

class DialogoPlanificar(QtGui.QDialog, Ui_DialogPlanificar):
    '''
    classdocs
    '''
    def __init__(self, parent=None, vehiculo_a_planificar=None):
        '''
        Constructor

        Observación:
        Forma de trabajo: cada elemento de la UI que puede cambiar dinamicamente
        tiene asociada un lista, luego existen metodos que refrescan dichos componentes,
        valiendose de las listas.
        '''
        super(DialogoPlanificar, self).__init__(parent)
        self.setupUi(self)
        self._vehiculo = vehiculo_a_planificar
        self._secciones_del_vehiculo = self._vehiculo.obtenerOrdenDeReparacionEnCurso().getSeccionesDeLasReparaciones()
        self._seccionSeleccionada = self._secciones_del_vehiculo[0] # Por defecto, la primer sección del combo box.
        self._todoCargado = False # Para que al principio no se pase automáticamente a la 2da pestaña (al cargar el combo box)
        self._reparaciones_asignadas = []
        self._reparaciones_sin_asignar = []
        self.seteoUi()
        # Cargamos la mínima fecha a tener en cuenta.
        # A partir de esta fecha podemos deshacer commits.
        self.DIVISION = Division_Transporte()
        self.DIVISION.zodb.setFechaMinimaDeshacer(localtime())

    def seteoUi(self):
        # Css
        self.label.setObjectName("label")
        self.label_2.setObjectName("label")
        self.labelFecha.setObjectName("label")
        self.labelHora.setObjectName("label")
        self.labelReparaciones.setObjectName("label")
        self.labelReparacionesAsignadas.setObjectName("label")
        self.labelSeccion.setObjectName("label")
        self.pushButtonAsignarReparacion.setObjectName('button')
        self.pushButtonDesasignarReparacion.setObjectName('button')

        self.buttonBox.connect(self, QtCore.SIGNAL('accepted()'), self.aceptar)
        self.buttonBox.connect(self, QtCore.SIGNAL('rejected()'), self.cancelar)

        self.comboBoxHoraTurno.clear()
        self.refrescarComboSecciones()

        # Seteamos el nombre del label de seccion por si se pasa a la 2da pestana directamente al abrir...
        self.label_2.setText(self._seccionSeleccionada.getNombre())

        # Setamos las reparaciones disponibles, y refrescamos
        self._reparaciones_sin_asignar = self._vehiculo.obtenerOrdenDeReparacionEnCurso().getReparacionesClasificadas()[self._seccionSeleccionada.getNombre()]
        self.refrescarTablas()

        # Seteamos la fecha del turno predefinida con la fecha de hoy:
#        hoy = date.today()
#        fecharecepcion = self._vehiculo.getPedidoDeActuacion().getFechaRecepcion()
        fecharecepcion = self._vehiculo.getPedidoDeActuacion().getFechaRealizacion()
        self.dateEditFechaTurno.setDate((QtCore.QDate(fecharecepcion.year, fecharecepcion.month, fecharecepcion.day)))
        self.dateEditFechaTurno.setMinimumDate((QtCore.QDate(fecharecepcion.year, fecharecepcion.month, fecharecepcion.day)))
        #Popup verdadero:
        self.dateEditFechaTurno.setCalendarPopup(True)
        self._todoCargado = True

    def refrescarComboSecciones(self):
        # Lo usan varios métodos...
        # Limpiamos y cargamos el combo
        self.comboBoxSecciones.clear()
        for seccion in self._secciones_del_vehiculo:
            self.comboBoxSecciones.addItems(QtCore.QStringList(seccion.getNombre()))
        # Seteamos la sección de trabajo con la primera de las disponibles
        self._seccionSeleccionada = self._secciones_del_vehiculo[0]

    def on_comboBoxSecciones_currentIndexChanged(self):
        if not self._todoCargado:
            return
        try:
#            print 'Cambio el combo: %s' % self.comboBoxSecciones.currentText()
            uncurrentitemm = self.comboBoxSecciones.currentText()
        except IndexError:
#            print "No tendria que se posible!"
            return
        nombre_seccion_selecionado = unicode(self.comboBoxSecciones.currentText())
        self._seccionSeleccionada = filter(lambda s: s.getNombre() == nombre_seccion_selecionado, self._secciones_del_vehiculo)
        try:
            self._seccionSeleccionada = self._seccionSeleccionada[0]
        except IndexError:
            self._seccionSeleccionada = self._secciones_del_vehiculo[0]
        # Seteamos el label de la tab2...
        self.label_2.setText(nombre_seccion_selecionado)
        # Setamos las reparaciones disponibles, y refrescamos
        self._reparaciones_sin_asignar = self._vehiculo.obtenerOrdenDeReparacionEnCurso().getReparacionesClasificadas()[self._seccionSeleccionada.getNombre()]
        self.refrescarTablas()

        # Cambiamos a tab2...
        self.tabWidget.setCurrentIndex(1)

    def on_dateEditFechaTurno_dateChanged(self):
        self.refrescarComboHoras()

    def refrescarComboHoras(self):
        # Lo utilizan varios métodos
        f = self.dateEditFechaTurno.date()
        fecha = '%s/%s/%s' % (f.day(), f.month(), f.year())
#        print 'Fecha: ', fecha
        self.comboBoxHoraTurno.clear()
        horas = []
        horas.extend(self._seccionSeleccionada.getHorasSinTurnoParaElDia(fecha))
        horas.sort()
        horasEnLosQueElVehiculoYaEstaOcupado = self._vehiculo.horasOcupadasParaElDia(fecha)
        for hora in horas:
            if hora not in horasEnLosQueElVehiculoYaEstaOcupado:
                self.comboBoxHoraTurno.addItems(QtCore.QStringList(str(hora)))

    def refrescarTablas(self):
        self.pushButtonAsignarReparacion.setEnabled(True)
        self.pushButtonDesasignarReparacion.setEnabled(True)
        if not self._reparaciones_asignadas:
            self.pushButtonDesasignarReparacion.setEnabled(False)
        if not self._reparaciones_sin_asignar:
            self.pushButtonAsignarReparacion.setEnabled(False)
        self.tableWidgetReparacionesAsignadas.cargarConReparaciones(self._reparaciones_asignadas)
        self.tableWidgetReparacionesSinAsignar.cargarConReparaciones(self._reparaciones_sin_asignar)

    @QtCore.pyqtSlot()
    def on_pushButtonAsignarReparacion_clicked(self):
        if not self.tableWidgetReparacionesSinAsignar.getReparacionSeleccionada():
            mostrarMensaje(self, 'Debe seleccionar un repuesto.', 'Seleccionar')
            return
        self._reparaciones_asignadas.append(self.tableWidgetReparacionesSinAsignar.getReparacionSeleccionada())
        self._reparaciones_sin_asignar.remove(self.tableWidgetReparacionesSinAsignar.getReparacionSeleccionada())
        self.refrescarTablas()

    @QtCore.pyqtSlot()
    def on_pushButtonDesasignarReparacion_clicked(self):
 
        if not self.tableWidgetReparacionesAsignadas.getReparacionSeleccionada():
            mostrarMensaje(self, 'Debe seleccionar un repuesto.', 'Seleccionar')
            return
        self._reparaciones_sin_asignar.append(self.tableWidgetReparacionesAsignadas.getReparacionSeleccionada())
        self._reparaciones_asignadas.remove(self.tableWidgetReparacionesAsignadas.getReparacionSeleccionada())
        self.refrescarTablas()

    @QtCore.pyqtSlot()
    def on_PushButtonCrearTurno_clicked(self):
        # TODO: [ok] PushButton_2 --> PushButtonCrearTurno!!
        # seccion.tieneTurnoLibreParaFechaHora('fechaSeleccionada', 'HoraSeleccionada') #Siempre True, Porque el dialogo no muestra opciones ocupadas
        f = self.dateEditFechaTurno.date()
        fecha = '%s/%s/%s' %(f.day(), f.month(), f.year())
        hora = int(self.comboBoxHoraTurno.currentText())
        # TODO [ok]: Ver que se pueden crear turnos con detalles de plan vacíos.
        # Además, puedo agregar varios turnos para una única reparación.

        # Si == 0 mostrar debe registrar reparación
        if len(self._reparaciones_asignadas) == 0:
            mostrarMensaje(self, self.trUtf8('Debe seleccionar al menos una reparación para registrar el turno'), self.trUtf8('Truno'))
            return
        codigo_turno = self.DIVISION.getGestorDeCodigos().nextCodigoTurno()
        turno_creado = Turno(codigo_turno, self._seccionSeleccionada, self._vehiculo, fecha, hora, self._reparaciones_asignadas)
        # Registrar el turno creado:
        self._seccionSeleccionada.registrarTurno(turno_creado)
        # Para saber de qué cliente debemos borrar las transacciones.
        transaction.get().setUser(self.DIVISION.zodb.getNombreUsuario(), '')
        transaction.commit()# Para que turno quede en tabla de turnos...
        self._vehiculo.agregarTurnoAlPlan(turno_creado)
        # Para saber de qué cliente debemos borrar las transacciones.
        transaction.get().setUser(self.DIVISION.zodb.getNombreUsuario(), '')
        transaction.commit()# Para que turno quede en el plan...
#         mostrarMensaje(self,
#                        self.trUtf8("Turno creado con éxito:\nDía: %s %d horas\nVehículo: %s\nSección: %s"%(fecha, hora, self._vehiculo.getDominio(), self._seccionSeleccionada.getNombre()),
#                        self.trUtf8('Turno')))
        mostrarMensaje(self, "Turno creado con exito:\nDia: %s %d horas\nVehiculo: %s\nSeccion: %s"%(fecha, hora, self._vehiculo.getDominio(), self._seccionSeleccionada), 'Turno')
        if self._vehiculo.tieneTodasLasReparacionesPlanificadas():
#             mostrarMensaje(self,
#                            self.trUtf8("El vehículo ya posee todas sus reparaciones planificadas\nOk para finalizar, Cancel para deshacer"),
#                            self.trUtf8('Fin planificación'))
            mostrarMensaje(self,"El vehiculo ya posee todas sus reparaciones planificadas\nOk para finalizar, Cancel para deshacer", 'Fin planificación')
            return

        # Todavía le quedan reparaciones para la sección seleccionada?
        if self._vehiculo.getReparacionesSinPlanificarDeLaSeccion(self._seccionSeleccionada.getNombre()):
            # yes
            self._reparaciones_sin_asignar = self._vehiculo.getReparacionesSinPlanificarDeLaSeccion(self._seccionSeleccionada.getNombre())
            self._reparaciones_asignadas = []
            self.refrescarTablas()
            self.refrescarComboHoras()
        else:
            # No
            # Pero igualmente quedan reparaciones de otras secciones (sino hubiera cortado más arriba)
            self._reparaciones_asignadas = []# Sino, se puede dar el caso en que quede con basura!
            self._secciones_del_vehiculo = self._vehiculo.obtenerOrdenDeReparacionEnCurso().getSeccionesDeLasReparaciones()
            self.refrescarComboSecciones()
            self._seccionSeleccionada = self._secciones_del_vehiculo[0]
            self._reparaciones_sin_asignar = self._vehiculo.getReparacionesSinPlanificarDeLaSeccion(self._seccionSeleccionada.getNombre())
            self.refrescarComboHoras()
            # cambiamos a tab1...
            self.tabWidget.setCurrentIndex(0)

    def aceptar(self):
        if self._vehiculo.tieneTodasLasReparacionesPlanificadas():# Verificar xq pude hacer click en aceptar sin haber terminado...
            self._vehiculo.planificacionFinalizada()#En este punto, la OR esta PLANIFICADA.
            self.mostrarHojaDeRuta()
            # Para saber de qué cliente debemos borrar las transacciones.
            transaction.get().setUser(self.DIVISION.zodb.getNombreUsuario(), '')
            transaction.commit()
#            print "DEBUG: Orden de reparacion planificada: %s"%self._vehiculo.obtenerOrdenDeReparacionEnCurso()
        else:
            # Se eliminan los turnos registrados anteriormente
            self.DIVISION.zodb.deshacerCommits()
            mostrarMensaje(self, self.trUtf8('No se registraron todos los trunos. Se van a eliminar los cambios realizados'),
                           self.trUtf8('Planificar'))

    def cancelar(self):
        self.DIVISION.zodb.deshacerCommits()
        #TODO [OK]: No tirar commits a lo loco. Ahora se deshacen los commits parciales.
        transaction.abort()
        #Y ademas:
        #alvehiculo.decirleQuePongaTodasSusReparacionesCOmoNoPlanificadas!

    def mostrarHojaDeRuta(self):
        '''
        Primer paso para generar el reporte hoja de ruta:
        '''
        #turnos_ordenados = self._vehiculo.getTurnosOrdenados()
        fileDialog = QFileDialog(caption=QtCore.QString.fromUtf8('Guardar Orden de Reparación'))
        filename = fileDialog.getSaveFileName(parent=self)
        generarHojaDeRuta(self._vehiculo, filename)