# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui

#from formularios.MainWindowExample import Ui_MainWindow
from Dialogs.formularios.MainWindowExample import Ui_MainWindow
#from formularios.WidgetListadoEmpleados import Ui_Form
#from negocio.Division_Transporte import Division_Transporte
from Dialogs.formularios.WidgetListadoEmpleados import Ui_Form
from Dialogs.negocio.Division_Transporte import Division_Transporte

#===============================================================================
# Import Dialogos
#===============================================================================
from Dialogs import DialogModificarVehiculo, \
                    DialogAltaPersonal,\
                    DialogRegistrarReparaciones,\
                    DialogAltaRepuesto,\
                    DialogAltaSeccion,\
                    DialogModificarPersonal,\
                    DialogMuestraLosRepuestos,\
                    DialogSeleccionarSeccion,\
                    DialogRegistrarIngresoVehiculo,\
                    DialogAltaVehiculo
#===============================================================================
# import widgets
#===============================================================================
from Dialogs import WidgetMostrarReparacionesPorVehiculo,WidgetMostrarTiposDeReparaciones,WidgetMostrarVehiculosSinPlanificar,WidgetBajaPersonal
from Dialogs import WidgetListadoSecciones, WidgetListadoDeRepuestosUtilizados, WidgetListadoDeVehiculos, WidgetListadoEmpleados

from Dialogs import DialogCambiarDeSeccionUnEmpleado, DialogCambiarDeSeccionUnEncargado, DialogRegistrarEgresoVehiculo, DialogRemoverEmpleadoDeSeccion
from Dialogs import DialogRegistrarRecepcionDePedidoDeActuacion, DialogBajaPersonal

from Dialogs.DialogoAltaTipoReparacion import DialogoAltaTipoReparacion
from Dialogs.DialogoPlanificar import DialogoPlanificar 
from Dialogs.DialogoAsignarReparaciones import DialogoAsignarReparaciones
from Dialogs.negocio.excepciones.SinTurnosException import SinTurnosException

class MyListado(QtGui.QWidget, Ui_Form):
    def __init__(self, parent = None):
        super(MyListado, self).__init__(parent)
        self.setupUi(self)
        self.cargarGrillaEmpleadosSinAsignar()
        self.connect(self.tableWidgetDatosEmpleados, QtCore.SIGNAL('cellDoubleClicked(int,int)'), self.celdaClick)    
    
    def cargarGrillaEmpleadosSinAsignar(self):
        
        print "Cargando Grilla"
        from Dialogs.negocio import Division_Transporte
        division = Division_Transporte.Division_Transporte()
        p = division.getEmpleados()
        
        if p.__len__() != 0:
            self.tableWidgetDatosEmpleados.setRowCount(p.__len__())
            row = 0
            for i in p:
                miItemc1 = QtGui.QTableWidgetItem()
                miItemc2 = QtGui.QTableWidgetItem()
                miItemc3 = QtGui.QTableWidgetItem()
#                miItemc4 = QtGui.QTableWidgetItem()
                miItemc1.setText(p[i].nombre)
                miItemc2.setText(p[i].apellido)
                miItemc3.setText(p[i].documento)
#                miItemc4.setText(p[i].tipoDocumento)
                self.tableWidgetDatosEmpleados.setItem(row,0,miItemc1)
                self.tableWidgetDatosEmpleados.setItem(row,1,miItemc2)
                self.tableWidgetDatosEmpleados.setItem(row,3,miItemc3)
#                self.tableWidgetDatosEmpleados.setItem(row,4,miItemc4)
                row = row + 1
    
    def celdaClick(self):
        print "Click sobre una celda"
        self.close()
        
MyOtroListado = MyListado

class MyMainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, usuario, parent = None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        #CSS:
        self.setObjectName("window")
        self.menues = {'actionAlta_de_Vehiculo': self.actionAlta_de_Vehiculo,
                       'actionRegistrar_Ingreso_de_Vehiculo': self.actionRegistrar_Ingreso_de_Vehiculo,
                       'actionRegistrar_Egreso': self.actionRegistrar_Egreso,
                       'actionModificacion_de_Vehiculo': self.actionModificacion_de_Vehiculo,
                       'actionVerificar_Reparaciones_Necesarias_del_Vehiculo': self.actionVerificar_Reparaciones_Necesarias_del_Vehiculo,
                       'actionPlanificar_Reparaciones_de_Vehiculo': self.actionPlanificar_Reparaciones_de_Vehiculo,
                       'actionListado_Vehiculos_de_la_Division_2': self.actionListado_Vehiculos_de_la_Division_2,
                       'actionListado_de_Reparaciones_Realizadas_a_un_Vehiculos_2': self.actionListado_de_Reparaciones_Realizadas_a_un_Vehiculos_2,
                       'actionListado_Vehiculos_con_Reparaciones_Planificadas_2': self.actionListado_Vehiculos_con_Reparaciones_Planificadas_2,
                       'actionListado_Vehiculos_con_Reparaciones_no_Planificadas_2': self.actionListado_Vehiculos_con_Reparaciones_no_Planificadas_2,
                       'actionListado_Vehiculos_en_Reparacion_por_Seccion': self.actionListado_Vehiculos_en_reparacion_por_Seccion,
                       'actionListado_Vehiculos_Reparados_por_Seccion_2': self.actionListado_Vehiculos_Reparados_por_Seccion_2,
                       'actionListado_de_Tipos_de_Reparaciones_de_la_Division_2': self.actionListado_de_Tipos_de_Reparaciones_de_la_Division_2,
                       'actionAlta_de_Personal': self.actionAlta_de_Personal,
                       'actionBaja_de_Personal': self.actionBaja_de_Personal,
                       'actionModificacion_de_Personal': self.actionModificacion_de_Personal,
                       'actionCambiar_de_Seccion_a_un_Empleado': self.actionCambiar_de_Seccion_a_un_Empleado,
                       'actionCambiar_el_Encargado_de_una_Seccion': self.actionCambiar_el_Encargado_de_una_Seccion,
                       'actionRemover_Empleado_de_Seccion': self.actionRemover_Empleado_de_Seccion,
                       'actionListado_de_Personal_de_la_Division': self.actionListado_de_Personal_de_la_Division,
                       'actionAlta_de_Repuesto': self.actionAlta_de_Repuesto,
                       'actionModificacion_de_Repuesto': self.actionModificacion_de_Repuesto,
                       'actionRegistrar_Recepcion_de_Pedido_de_Actuacion': self.actionRegistrar_Recepcion_de_Pedido_de_Actuacion,
                       'actionListado_de_Repuestos_de_la_Division': self.actionListado_de_Repuestos_de_la_Division,
                       'actionAlta_de_Seccion': self.actionAlta_de_Seccion,
                       'actionAlta_Tipo_de_Reparacion': self.actionAlta_Tipo_de_Reparacion,
                       'actionAsignar_Reparacion': self.actionAsignar_Reparacion,
                       'actionRegistrar_Finalizacion_de_Reparacion': self.actionRegistrar_Finalizacion_de_Reparacion,
                       'actionListados_de_Seccion': self.actionListados_de_Seccion}
        
        #TODO: validar 12/12/13
        self.usuario = usuario
        self.habilitarMenues()
        self.setearUI()
    
    def habilitarMenues(self):
        permisos = self.usuario.getPermisos()
        for permiso in permisos:
            self.menues[permiso].setEnabled(True)

    def setearUI(self):
        #css:
        self.actionAlta_de_Seccion.setObjectName('action')
        self.actionAlta_de_Personal.setObjectName('action')
        
    @QtCore.pyqtSlot()
    def on_actionListado_triggered(self):
        print 'agregando listado'
        self.setCentralWidget(MyListado(self))
        self.centralWidget().connect(self.centralWidget().tableWidgetDatosEmpleados,QtCore.SIGNAL('cellDoubleClicked(int,int)'), self.celdaClick)
        
    def celdaClick(self):
        print "Click sobre una celda"
        self.centralWidget().close()
        self.setCentralWidget(DialogModificarPersonal.DialogModificarPersonal(self))
    
    @QtCore.pyqtSlot()
    def on_actionAlta_de_Vehiculo_triggered(self):
        dlgAltaVehiculo = DialogAltaVehiculo.DialogAltaVehiculo(self)
        dlgAltaVehiculo.exec_()
    
    #Conectamos la accion modificar vehiculo...
    @QtCore.pyqtSlot()
    def on_actionModificacion_de_Vehiculo_triggered(self):
        dlgModificarVehiculo = DialogModificarVehiculo.DialogMostrarLosVehiculosParaModificar(self) 
        dlgModificarVehiculo.exec_()
        
    #Conectamos la accion Verificar_Reparaciones_Necesarias_del_Vehiculo...
    @QtCore.pyqtSlot()
    def on_actionVerificar_Reparaciones_Necesarias_del_Vehiculo_triggered(self):
        print 'abriendo dialogo Verificar_Reparaciones_Necesarias_del_Vehiculo'
        from Dialogs.DialogMostrarLosVehiculosParaAgregarReparacionesAOR import DialogMostrarLosVehiculosParaAgregarReparacionesAOR
        dlgRegistrarReparaciones = DialogMostrarLosVehiculosParaAgregarReparacionesAOR(self)
        dlgRegistrarReparaciones.exec_()
    
    #Conectamos la accion Alta Personal...
    @QtCore.pyqtSlot()
    def on_actionAlta_de_Personal_triggered(self):
        dlgAltaPersonal = DialogAltaPersonal.DialogAltaPersonal(self)
        dlgAltaPersonal.exec_()
    
    #Conectamos la accion Alta Repuesto...
    @QtCore.pyqtSlot()
    def on_actionAlta_de_Repuesto_triggered(self):
        print 'abriendo dialogo Alta Repuesto'
        dlgAltaRepuesto = DialogAltaRepuesto.DialogAltaRepuesto(self)
        dlgAltaRepuesto.exec_()
    
    #Conectamos la accion Alta Seccion...
    @QtCore.pyqtSlot()
    def on_actionAlta_de_Seccion_triggered(self):
        dlgAltaSeccion = DialogAltaSeccion.DialogAltaSeccion(self)
        dlgAltaSeccion.exec_()
    
    #Conectamos la accion Alta Tipo de Reparacion...
    @QtCore.pyqtSlot()
    def on_actionAlta_Tipo_de_Reparacion_triggered(self):
        dlgAltaTipoReparacion = DialogoAltaTipoReparacion(self)
        dlgAltaTipoReparacion.exec_()
        
    @QtCore.pyqtSlot(bool)
    def on_actionAyuda_triggered(self, check):
        if check:
            print 'agregando otro listado'
            self.setCentralWidget(MyOtroListado(self))
        
    @QtCore.pyqtSlot()
    def on_actionSobre_triggered(self):
        print 'agregando dock'
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, QtGui.QDockWidget(QtCore.QString.fromUtf8('my dock'), self))
        
        
#===============================================================================
# Conexion de Widgets:
#===============================================================================
    @QtCore.pyqtSlot()
    def on_actionListado_de_Personal_de_la_Division_triggered(self):
        self.setCentralWidget(WidgetListadoEmpleados.WidgetListadoEmpleados(self))
    
    #Agregada la lista de vehículos a listar
    @QtCore.pyqtSlot()
    def on_actionListado_Vehiculos_de_la_Division_2_triggered(self):
        print 'DIV 2: agregando widget listado Vehiculos'
        self.setCentralWidget(WidgetListadoDeVehiculos.ListadoVehiculos(Division_Transporte().getVehiculos().values(), self))

    @QtCore.pyqtSlot()
    def on_actionListado_Vehiculos_en_Reparacion_por_Seccion_triggered(self):
        print 'En reparacion: agregando widget listado de Vehiculos'
        self.setCentralWidget(WidgetListadoDeVehiculos.Listado_Vehiculos_en_reparacion_por_Seccion(self))
        self.centralWidget().labelListadoVehiculos.setText(QtCore.QString.fromUtf8("Listado de Vehiculos en Reparacion por Seccion"))
    
    @QtCore.pyqtSlot()
    def on_actionListado_Vehiculos_Reparados_por_Seccion_2_triggered(self):
        print 'Reparados: agregando widget listado de Vehiculos'
        self.setCentralWidget(WidgetListadoDeVehiculos.Listado_Vehiculos_Reparados_por_Seccion_2(self))
        self.centralWidget().labelListadoVehiculos.setText(QtCore.QString.fromUtf8("Listado de Vehiculos Reparados por Seccion"))
    
    @QtCore.pyqtSlot()
    def on_actionListado_Vehiculos_con_Reparaciones_Planificadas_2_triggered(self):
        print 'Planificados: agregando widget listado de Vehiculos'
        self.setCentralWidget(WidgetMostrarReparacionesPorVehiculo.WidgetMostrarReparacionesPorVehiculo(Division_Transporte().getVehiculosEnPlanificacion(), self))
#         self.setCentralWidget(WidgetListadoDeVehiculos.Listado_Vehiculos_con_Reparaciones_Planificadas(self))
#         self.centralWidget().labelListadoVehiculos.setText(QtCore.QString.fromUtf8("Listado de Vehiculos con Reparaciones Planificadas"))
        
    @QtCore.pyqtSlot()
    def on_actionListado_Vehiculos_con_Reparaciones_no_Planificadas_2_triggered(self):
        self.setCentralWidget(WidgetListadoDeVehiculos.Listado_Vehiculos_con_Reparaciones_no_Planificadas(self))
#         self.centralWidget().labelListadoVehiculos.setText(QtCore.QString.fromUtf8("Listado de Vehiculos con Reparaciones no Planificadas"))
        
    @QtCore.pyqtSlot()
    def on_actionListado_de_Reparaciones_Realizadas_a_un_Vehiculos_2_triggered(self):
        print 'Reparaciones realizadas: agregando widget listado Vehiculos'
        self.setCentralWidget(WidgetMostrarReparacionesPorVehiculo.WidgetMostrarReparacionesPorVehiculo(Division_Transporte().getVehiculosEnFinalizada(), self))
    
    @QtCore.pyqtSlot()
    def on_actionListado_de_Tipos_de_Reparaciones_de_la_Division_2_triggered(self):
        print 'Tipos de Reparaciones: agregando widget listado Vehiculos'
        self.setCentralWidget(WidgetMostrarTiposDeReparaciones.WidgetMostrarTiposDeReparaciones(self))
    
    @QtCore.pyqtSlot()
    def on_actionPlanificar_Reparaciones_de_Vehiculo_triggered(self):
        print 'Planificar reapraciones: agregando widget listado Vehiculos'
        vehiculos_sin_planificar = Division_Transporte().getVehiculosEnAprobada()
        self.setCentralWidget(WidgetListadoDeVehiculos.ListadoVehiculos(vehiculos_sin_planificar, self))
        self.centralWidget().pushButtonSeleccionar.connect(self.centralWidget().pushButtonSeleccionar, QtCore.SIGNAL('clicked()'), self.planificar)
    
    def planificar(self):
        if self.centralWidget().tableWidgetListadoDeVehiculos.getVehiculoSeleccionado():
            dlgPlanificar = DialogoPlanificar(self, self.centralWidget().tableWidgetListadoDeVehiculos.getVehiculoSeleccionado()) 
            dlgPlanificar.exec_()
            self.centralWidget().tableWidgetListadoDeVehiculos.cargarConVehiculos(Division_Transporte().getVehiculosEnAprobada())
            
    @QtCore.pyqtSlot()
    def on_actionBaja_de_Personal_triggered(self):
        print 'agregando Dialog baja personal'
        dlgBajaPersonal = DialogBajaPersonal.DialogBajaPersonal()
        dlgBajaPersonal.exec_()
        
    @QtCore.pyqtSlot()
    def on_actionModificacion_de_Repuesto_triggered(self):
        print 'agregando widget baja personal'
        dlMuesRep = DialogMuestraLosRepuestos.DialogMuestraLosRepuestos()
        dlMuesRep.exec_()
    
    #Conectamos la accion Modificar Personal...
    @QtCore.pyqtSlot()
    def on_actionModificacion_de_Personal_triggered(self):
        print 'agregando Widget'
        self.setCentralWidget(WidgetBajaPersonal.WidgetBajaPersonal(self))
        
    @QtCore.pyqtSlot()
    def on_actionListados_de_Seccion_triggered(self):            
        print 'agregando Widget Listado de Secciones'
        self.setCentralWidget(WidgetListadoSecciones.ListadoSecciones(self))

    @QtCore.pyqtSlot()
    def on_actionListado_de_Repuestos_de_la_Division_triggered(self):
        print 'agregando widget listado de repustos utilizados'
        self.setCentralWidget(WidgetListadoDeRepuestosUtilizados.ListadoRepustosUtilizados(self))
        
    @QtCore.pyqtSlot()
    def on_actionRegistrar_Recepcion_de_Pedido_de_Actuacion_triggered(self):
        print 'agregando Dialog Registro Pedido de Actuacion'
        dlgRegistrarPedidoActuacion = DialogRegistrarRecepcionDePedidoDeActuacion.DialogRegistrarRecepcionDePedidoDeActuacion()
        dlgRegistrarPedidoActuacion.exec_()
    
    @QtCore.pyqtSlot()
    def on_actionAsignar_Reparacion_triggered(self):
        #Tomar la seccion correspondiente y abrir el dialogo
        seccion = filter(lambda s: self.usuario.esJefeDeSeccion(s), Division_Transporte().getSecciones().values())
        try: 
            dlgAsignarReparaciones = DialogoAsignarReparaciones(self, seccion[0])
            dlgAsignarReparaciones.exec_()
        except SinTurnosException:
            print 'Ok'
        except IndexError:
            print 'No sos jefe de seccion'
    @QtCore.pyqtSlot()
    def on_actionRegistrar_Ingreso_de_Vehiculo_triggered(self):
        dlgRegIngVehiculo = DialogRegistrarIngresoVehiculo.DialogRegistrarIngresoVehiculo()
        dlgRegIngVehiculo.exec_()
        
    def keyPressEvent(self, e):
        
        print 'Se presiono una tecla'
        if e.key() == QtCore.Qt.Key_F1:
            self.on_actionAlta_de_Personal_triggered()
        if e.key() == (QtCore.Qt.Key_F2):
            self.on_actionListado_triggered()
    
    #===========================================================================
    # Nuevos Dialogs
    #===========================================================================
    
    @QtCore.pyqtSlot()
    def on_actionCambiar_de_Seccion_a_un_Empleado_triggered(self):
        dlgCambiarSeccionEmpleado = DialogCambiarDeSeccionUnEmpleado.DialogCambiardeSeccionunEmpleado()
        dlgCambiarSeccionEmpleado.exec_()
        
    @QtCore.pyqtSlot()
    def on_actionCambiar_el_Encargado_de_una_Seccion_triggered(self):
        dlgCambiarSeccionEmpleado = DialogCambiarDeSeccionUnEncargado.DialogCambiarDeSeccionUnEncargado()
        dlgCambiarSeccionEmpleado.exec_()
        
    @QtCore.pyqtSlot()
    def on_actionRegistrar_Egreso_triggered(self):
        dlgRegistrarEgreso = DialogRegistrarEgresoVehiculo.DialogRegistrarEgresoVehiculo()
        dlgRegistrarEgreso.exec_()
        
    @QtCore.pyqtSlot()
    def on_actionRemover_Empleado_de_Seccion_triggered(self):
        dlgRemoverEmpleado = DialogRemoverEmpleadoDeSeccion.DialogRemoverEmpleadoDeSeccion()
        dlgRemoverEmpleado.exec_()