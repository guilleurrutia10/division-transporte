# -*- coding: utf-8 -*-
'''
Created on 20/07/2014

@author: LeoMorales
'''

from PyQt4 import QtCore, QtGui
from formularios.DlgPlanificar import Ui_DialogPlanificar
from datetime import date
from Utiles_Dialogo import mostrarMensaje
from negocio.Turno import Turno
import transaction

class DialogoPlanificar(QtGui.QDialog, Ui_DialogPlanificar):
    '''
    classdocs
    '''
    def __init__(self, parent = None, vehiculo_a_planificar= None):
        '''
        Constructor
        
        Observacion:
        Forma de trabajo: cada elemento de la UI que puede cambiar dinamicamente
        tiene asociada un lista, luego existen metodos que refrescan dichos componentes,
        valiendose de las listas.
        '''
        super(DialogoPlanificar, self).__init__(parent)
        self.setupUi(self)
        self._vehiculo = vehiculo_a_planificar
        self._secciones_del_vehiculo = self._vehiculo.obtenerOrdenDeReparacionEnCurso().getSeccionesDeLasReparaciones()
        self._seccionSeleccionada = self._secciones_del_vehiculo[0] #Por defecto, la primer seccion del combo box.
        self._todoCargado = False #Para que al principio no se pase automaticamente a la 2da pestana (al cargar el combo box)
        self._reparaciones_asignadas = []
        self._reparaciones_sin_asignar = []
        self.seteoUi()
        

    def seteoUi(self):
        #Css
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
        
        #Seteamos el nombre del label de seccion por si se pasa a la 2da pestana directamente al abrir...
        self.label_2.setText(self._seccionSeleccionada.getNombre())
        
        #Setamos las reparaciones disponibles, y refrescamos
        self._reparaciones_sin_asignar = self._vehiculo.obtenerOrdenDeReparacionEnCurso().getReparacionesClasificadas()[self._seccionSeleccionada.getNombre()]
        self.refrescarTablas()
        
        #Seteamos la fecha del turno predefinida con la fecha de hoy:
        hoy = date.today()
        self.dateEditFechaTurno.setDate((QtCore.QDate(hoy.year, hoy.month, hoy.day)))
        self.dateEditFechaTurno.setMinimumDate((QtCore.QDate(hoy.year, hoy.month, hoy.day)))
        
        self._todoCargado = True
            
    def refrescarComboSecciones(self):
        #Lo usan varios metodos...
        #Limpiamos y cargamos el combo
        self.comboBoxSecciones.clear()
        for seccion in self._secciones_del_vehiculo:
            self.comboBoxSecciones.addItems(QtCore.QStringList(seccion.getNombre()))
        #seteamos la seccion de trabajo con la primera de las disponibles
        self._seccionSeleccionada = self._secciones_del_vehiculo[0]
    
    
    def on_comboBoxSecciones_currentIndexChanged(self):
        if not self._todoCargado:
            return
        try:
            print 'Cambio el combo: %s' % self.comboBoxSecciones.currentText()
        except IndexError:
            print "No tendria que se posible!"
            return
        nombre_seccion_selecionado = unicode(self.comboBoxSecciones.currentText())
        self._seccionSeleccionada = filter(lambda s: s.getNombre() == nombre_seccion_selecionado, self._secciones_del_vehiculo)
        try:
            self._seccionSeleccionada = self._seccionSeleccionada[0]
        except IndexError:
            self._seccionSeleccionada = self._secciones_del_vehiculo[0]
        #seteamos el label de la tab2...
        self.label_2.setText(nombre_seccion_selecionado)
        #Setamos las reparaciones disponibles, y refrescamos
        self._reparaciones_sin_asignar = self._vehiculo.obtenerOrdenDeReparacionEnCurso().getReparacionesClasificadas()[self._seccionSeleccionada.getNombre()]
        self.refrescarTablas()

        #cambiamos a tab2...
        self.tabWidget.setCurrentIndex(1)
        
    def on_dateEditFechaTurno_dateChanged(self):
        self.refrescarComboHoras()

    def refrescarComboHoras(self):
        #Lo utilizan varios metodos
        f = self.dateEditFechaTurno.date()
        fecha = '%s/%s/%s' %(f.day(), f.month(), f.year())
        print 'Fecha: ', fecha
        self.comboBoxHoraTurno.clear()
        horas = []
        horas.extend(self._seccionSeleccionada.getHorasSinTurnoParaElDia(fecha))
        horas.sort()
        for hora in horas:
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
    def on_pushButton_2_clicked(self):
        #TODO: PushButton_2 --> PushButtonCrearTurno!!
        #seccion.tieneTurnoLibreParaFechaHora('fechaSeleccionada', 'HoraSeleccionada') #Siempre True, Porque el dialogo no muestra opciones ocupadas
        f = self.dateEditFechaTurno.date()
        fecha = '%s/%s/%s' %(f.day(), f.month(), f.year())
        hora = int(self.comboBoxHoraTurno.currentText())
        turno_creado = Turno(self._seccionSeleccionada, self._vehiculo, fecha, hora, self._reparaciones_asignadas)
        #Registrar el turno creado:
        self._seccionSeleccionada.registrarTurno(turno_creado)
        transaction.commit()#Para que turno quede en tabla de turnos...
        self._vehiculo.agregarTurnoAlPlan(turno_creado)
        transaction.commit()#Para que turno quede en el plan...
        mostrarMensaje(self, "Turno creado con exito:\nDia: %s %d horas\nVehiculo: %s\nSeccion: %s"%(fecha, hora, self._vehiculo.getDominio(), self._seccionSeleccionada.getNombre()), 'Turno')
        if self._vehiculo.tieneTodasLasReparacionesPlanificadas():
            mostrarMensaje(self, "El vehiculo ya posee todas sus reparaciones planificadas\nOk para finalizar, Cancel para deshacer", 'Fin planificacion')
            return
            
        #todavia le quedan reparaciones para la seccion seleccionada?
        if self._vehiculo.getReparacionesSinPlanificarDeLaSeccion(self._seccionSeleccionada.getNombre()):
            #yes
            self._reparaciones_sin_asignar = self._vehiculo.getReparacionesSinPlanificarDeLaSeccion(self._seccionSeleccionada.getNombre())
            self._reparaciones_asignadas = []
            self.refrescarTablas()
            self.refrescarComboHoras()
        else:
            #No
            #Pero igualmente quedan reparaciones de otras secciones (sino hubiera cortado mas arriba)
            self._reparaciones_asignadas = []#Sino, se puede dar el caso en que quede con basura!
            self._secciones_del_vehiculo = self._vehiculo.obtenerOrdenDeReparacionEnCurso().getSeccionesDeLasReparaciones()
            self.refrescarComboSecciones()
            self._seccionSeleccionada = self._secciones_del_vehiculo[0]
            self._reparaciones_sin_asignar = self._vehiculo.getReparacionesSinPlanificarDeLaSeccion(self._seccionSeleccionada.getNombre())
            self.refrescarComboHoras()
            #cambiamos a tab1...
            self.tabWidget.setCurrentIndex(0)

    def aceptar(self):
        print 'Aceptar!!'
        if self._vehiculo.tieneTodasLasReparacionesPlanificadas():#verificar xq pude hacer click en aceptar sin haber terminado...
            self._vehiculo.planificacionFinalizada()
            transaction.commit()

    def cancelar(self):
        #No tirar commits a lo loco
        transaction.abort()
        #Y ademas:
        #alvehiculo.decirleQuePongaTodasSusReparacionesCOmoNoPlanificadas!
