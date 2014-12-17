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
from Dialogs.DialogoRegistrarFinTurno import DialogoRegistrarFinTurno
from Dialogs.DialogRegistrarEgresoVehiculo import DialogDatosEgresoVehiculo
from Dialogs.DialogoAgendaDeSeccion import DialogoAgendaDeSeccion

class MyListado(QtGui.QWidget, Ui_Form):
    def __init__(self, parent = None):
        super(MyListado, self).__init__(parent)
        self.setupUi(self)
        self.cargarGrillaEmpleadosSinAsignar()
        self.connect(self.tableWidgetDatosEmpleados, QtCore.SIGNAL('cellDoubleClicked(int,int)'), self.celdaClick)    
    
    def cargarGrillaEmpleadosSinAsignar(self):
        
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
                       'actionListados_de_Seccion': self.actionListados_de_Seccion,
                       'actionConsultar_agenda': self.actionConsultar_agenda
                       }
        
        #TODO: validar 12/12/13
        self.usuario = usuario
        self.habilitarMenues()
        self.setearUI()
    
    def habilitarMenues(self):
        permisos = self.usuario.getPermisos()
        for permiso in permisos:
            self.menues[permiso].setEnabled(True)

    def deshabilitarMenues(self):
        '''
        Para cuando cambia de usuario...
        '''
        for action in self.menues.values():
            action.setEnabled(False)

    def setearUI(self):
        #css:
        self.actionAlta_de_Seccion.setObjectName('action')
        self.actionAlta_de_Personal.setObjectName('action')
        
    @QtCore.pyqtSlot()
    def on_actionListado_triggered(self):
        self.setCentralWidget(MyListado(self))
        self.centralWidget().connect(self.centralWidget().tableWidgetDatosEmpleados,QtCore.SIGNAL('cellDoubleClicked(int,int)'), self.celdaClick)
        
    def celdaClick(self):
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
            self.setCentralWidget(MyOtroListado(self))
        
    @QtCore.pyqtSlot()
    def on_actionSobre_triggered(self):
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
        widgetListadoVehiculos = WidgetListadoDeVehiculos.ListadoVehiculos(Division_Transporte().getVehiculos().values(), self)
        widgetListadoVehiculos.pushButtonSeleccionar.hide()
        self.setCentralWidget(widgetListadoVehiculos)

    @QtCore.pyqtSlot()
    def on_actionListado_Vehiculos_en_Reparacion_por_Seccion_triggered(self):
        self.setCentralWidget(WidgetListadoDeVehiculos.Listado_Vehiculos_en_reparacion_por_Seccion(self))
        self.centralWidget().labelListadoVehiculos.setText(QtCore.QString.fromUtf8("Listado de Vehiculos en Reparacion por Seccion"))
    
    @QtCore.pyqtSlot()
    def on_actionListado_Vehiculos_Reparados_por_Seccion_2_triggered(self):
        self.setCentralWidget(WidgetListadoDeVehiculos.Listado_Vehiculos_Reparados_por_Seccion_2(self))
        self.centralWidget().labelListadoVehiculos.setText(QtCore.QString.fromUtf8("Listado de Vehiculos Reparados por Seccion"))
    
    @QtCore.pyqtSlot()
    def on_actionListado_Vehiculos_con_Reparaciones_Planificadas_2_triggered(self):
        self.setCentralWidget(WidgetMostrarReparacionesPorVehiculo.WidgetMostrarReparacionesPorVehiculoPlanificadas(Division_Transporte().getVehiculosEnPlanificacion(), self))
#         self.setCentralWidget(WidgetMostrarReparacionesPorVehiculo.WidgetMostrarReparacionesPorVehiculo(Division_Transporte().getVehiculosEnPlanificacion(), self))
#         self.setCentralWidget(WidgetListadoDeVehiculos.Listado_Vehiculos_con_Reparaciones_Planificadas(self))
#         self.centralWidget().labelListadoVehiculos.setText(QtCore.QString.fromUtf8("Listado de Vehiculos con Reparaciones Planificadas"))
        
    @QtCore.pyqtSlot()
    def on_actionListado_Vehiculos_con_Reparaciones_no_Planificadas_2_triggered(self):
        self.setCentralWidget(WidgetListadoDeVehiculos.Listado_Vehiculos_con_Reparaciones_no_Planificadas(self))
#         self.centralWidget().labelListadoVehiculos.setText(QtCore.QString.fromUtf8("Listado de Vehiculos con Reparaciones no Planificadas"))
        
    @QtCore.pyqtSlot()
    def on_actionListado_de_Reparaciones_Realizadas_a_un_Vehiculos_2_triggered(self):
        self.setCentralWidget(WidgetMostrarReparacionesPorVehiculo.WidgetMostrarReparacionesPorVehiculo(Division_Transporte().getVehiculosEnFinalizada(), self))
#         self.setCentralWidget(WidgetMostrarReparacionesPorVehiculo.WidgetMostrarReparacionesPorVehiculo(Division_Transporte().getVehiculosEnFinalizada(), self))
    
    @QtCore.pyqtSlot()
    def on_actionListado_de_Tipos_de_Reparaciones_de_la_Division_2_triggered(self):
        self.setCentralWidget(WidgetMostrarTiposDeReparaciones.WidgetMostrarTiposDeReparaciones(self))
    
    @QtCore.pyqtSlot()
    def on_actionPlanificar_Reparaciones_de_Vehiculo_triggered(self):
        vehiculos_sin_planificar = Division_Transporte().getVehiculosEnAprobada()
        self.setCentralWidget(WidgetListadoDeVehiculos.ListadoVehiculos(vehiculos_sin_planificar, self))
        self.centralWidget().pushButtonSeleccionar.connect(self.centralWidget().pushButtonSeleccionar, QtCore.SIGNAL('clicked()'), self.planificar)
        self.centralWidget().tableWidgetListadoDeVehiculos.connect(self.centralWidget().tableWidgetListadoDeVehiculos, QtCore.SIGNAL('cellDoubleClicked(int , int)'), self.planificar)
    
    def planificar(self):
        if self.centralWidget().tableWidgetListadoDeVehiculos.getVehiculoSeleccionado():
            dlgPlanificar = DialogoPlanificar(self, self.centralWidget().tableWidgetListadoDeVehiculos.getVehiculoSeleccionado()) 
            dlgPlanificar.exec_()
            self.centralWidget().tableWidgetListadoDeVehiculos.cargarConVehiculos(Division_Transporte().getVehiculosEnAprobada())
            
    @QtCore.pyqtSlot()
    def on_actionBaja_de_Personal_triggered(self):
        dlgBajaPersonal = DialogBajaPersonal.DialogBajaPersonal()
        dlgBajaPersonal.exec_()
        
    @QtCore.pyqtSlot()
    def on_actionModificacion_de_Repuesto_triggered(self):
        dlMuesRep = DialogMuestraLosRepuestos.DialogMuestraLosRepuestos()
        dlMuesRep.exec_()
    
    #Conectamos la accion Modificar Personal...
    @QtCore.pyqtSlot()
    def on_actionModificacion_de_Personal_triggered(self):
        from Dialogs.WidgetModificarPersonal import WidgetModificarPersonal
        self.setCentralWidget(WidgetModificarPersonal(self))
        
    @QtCore.pyqtSlot()
    def on_actionListados_de_Seccion_triggered(self):            
        self.setCentralWidget(WidgetListadoSecciones.ListadoSecciones(self))

    @QtCore.pyqtSlot()
    def on_actionListado_de_Repuestos_de_la_Division_triggered(self):
        self.setCentralWidget(WidgetListadoDeRepuestosUtilizados.ListadoRepustosUtilizados(self))
        
    @QtCore.pyqtSlot()
    def on_actionRegistrar_Recepcion_de_Pedido_de_Actuacion_triggered(self):
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
            debug= 'Ok'
        except IndexError:
            debug= 'No sos jefe de seccion'
            
    @QtCore.pyqtSlot()
    def on_actionRegistrar_Ingreso_de_Vehiculo_triggered(self):
        dlgRegIngVehiculo = DialogRegistrarIngresoVehiculo.DialogRegistrarIngresoVehiculo()
        dlgRegIngVehiculo.exec_()
        
    def keyPressEvent(self, e):
        
#        print 'Se presiono una tecla'
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
    def on_actionRemover_Empleado_de_Seccion_triggered(self):
        dlgRemoverEmpleado = DialogRemoverEmpleadoDeSeccion.DialogRemoverEmpleadoDeSeccion()
        dlgRemoverEmpleado.exec_()
        
    @QtCore.pyqtSlot()
    def on_actionRegistrar_Finalizacion_de_Reparacion_triggered(self):
        seccion = filter(lambda s: self.usuario.esJefeDeSeccion(s), Division_Transporte().getSecciones().values())
        try: 
            dlgFinTurno = DialogoRegistrarFinTurno(self, seccion[0])
            dlgFinTurno.exec_()
        except SinTurnosException:
            debug= 'Ok'
        except IndexError:
            debug= 'No sos jefe de seccion'

    @QtCore.pyqtSlot()
    def on_actionRegistrar_Egreso_triggered(self):
        vehiculos_para_egresar = Division_Transporte().getVehiculosParaEgreso()
        self.setCentralWidget(WidgetListadoDeVehiculos.ListadoVehiculos(vehiculos_para_egresar, self))
        self.centralWidget().pushButtonSeleccionar.connect(self.centralWidget().pushButtonSeleccionar, QtCore.SIGNAL('clicked()'), self.egresar)
    
    def egresar(self):
        if self.centralWidget().tableWidgetListadoDeVehiculos.getVehiculoSeleccionado():
            dlgEgresar = DialogDatosEgresoVehiculo(self, self.centralWidget().tableWidgetListadoDeVehiculos.getVehiculoSeleccionado()) 
            dlgEgresar.exec_()
            self.centralWidget().tableWidgetListadoDeVehiculos.cargarConVehiculos(Division_Transporte().getVehiculosParaEgreso())

    @QtCore.pyqtSlot()
    def on_actionAcerca_de_Division_de_Transporte_triggered(self):
        QtGui.QMessageBox.about(self, "Acerca de DivT", QtCore.QString.fromUtf8('<h1>DivT</h1><p>Aplicación desarrollada para Desarrollo de Software</p>'));

    @QtCore.pyqtSlot()
    def on_actionConsultar_agenda_triggered(self):            
        dlgAgenda = DialogoAgendaDeSeccion(self) 
        dlgAgenda.exec_()

    @QtCore.pyqtSlot()
    def on_actionCambiarDeUsuario_triggered(self):            
#        print 'DEBUG: Cambiando de usuario...'
        from mainLogin import MyLogin
        from Dialogs.Utiles_Dialogo import mostrarMensaje
        myLogin = MyLogin()
        if myLogin.exec_() == QtGui.QDialog.Accepted:
            self.usuario = QtGui.QApplication.instance().getUsuarioActual()
            self.deshabilitarMenues()
            self.habilitarMenues()
            mostrarMensaje(self, 'Cambio de usuario exitoso.', 'Cambio de usuario')
