# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui

from formularios.MainWindowExample import Ui_MainWindow
from formularios.WidgetListadoEmpleados import Ui_Form


#===============================================================================
# Import Dialogos
#===============================================================================
from Dialogs import DialogModificarVehiculo,DialogAltaPersonal,DialogRegistrarReparaciones,DialogAltaRepuesto,DialogAltaSeccion, DialogModificarPersonal, DialogMuestraLosRepuestos
from Dialogs import DialogSeleccionarSeccion, DialogRegistrarIngresoVehiculo, DialogAltaVehiculo
#===============================================================================
# import widgets
#===============================================================================
from Dialogs import WidgetMostrarReparacionesPorVehiculo,WidgetMostrarTiposDeReparaciones,WidgetMostrarVehiculosSinPlanificar,WidgetBajaPersonal
from Dialogs import WidgetListadoSecciones, WidgetListadoDeRepuestosUtilizados, WidgetListadoDeVehiculos

from Dialogs import DialogCambiarDeSeccionUnEmpleado, DialogCambiarDeSeccionUnEncargado, DialogRegistrarEgresoVehiculo, DialogRemoverEmpleadoDeSeccion
from Dialogs import DialogRegistrarRecepcionDePedidoDeActuacion

class MyListado(QtGui.QWidget, Ui_Form):
    def __init__(self, parent = None):
        super(MyListado, self).__init__(parent)
        self.setupUi(self)
        self.cargarGrilla()
        self.connect(self.tableWidgetDatosEmpleados, QtCore.SIGNAL('cellDoubleClicked(int,int)'), self.celdaClick)    
    
    def cargarGrilla(self):
        
        print "Cargando Grilla"
        from negocio import Division_Transporte
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
        

class ListadoEmpleados(QtGui.QWidget, Ui_Form):
    def __init__(self, parent = None):
        super(ListadoEmpleados, self).__init__(parent)
        self.setupUi(self)
        
MyOtroListado = MyListado

class MyMainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        
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
        print 'abriendo dialogo Alta Vehiculo'
        dlgAltaVehiculo = DialogAltaVehiculo.DialogAltaVehiculo(self)
        dlgAltaVehiculo.exec_()
    
    #Conectamos la accion modificar vehiculo...
    @QtCore.pyqtSlot()
    def on_actionModificacion_de_Vehiculo_triggered(self):
        print 'abriendo dialogo Modificar Vehiculo'
        dlgModificarVehiculo = DialogModificarVehiculo.DialogMostrarLosVehiculosParaModificar(self) 
        dlgModificarVehiculo.exec_()
        
    #Conectamos la accion Verificar_Reparaciones_Necesarias_del_Vehiculo...
    @QtCore.pyqtSlot()
    def on_actionVerificar_Reparaciones_Necesarias_del_Vehiculo_triggered(self):
        print 'abriendo dialogo Verificar_Reparaciones_Necesarias_del_Vehiculo'
        dlgRegistrarReparaciones = DialogRegistrarReparaciones.DialogRegistrarReparaciones(self)
        dlgRegistrarReparaciones.exec_()
    
    #Conectamos la accion Alta Personal...
    @QtCore.pyqtSlot()
    def on_actionAlta_de_Personal_triggered(self):
        print 'abriendo dialogo Alta Personal'
        dlgAltaPersonal = DialogAltaPersonal.DialogAltaPersonal(self)
        dlgAltaPersonal.exec_()
    
    #Conectamos la accion Alta Repuesto...
    @QtCore.pyqtSlot()
    def on_actionAlta_de_Repuesto_triggered(self):
        print 'abriendo dialogo Alta Repuesto'
        dlgAltaRepuesto = DialogAltaRepuesto.DialogAltaRepuesto(self)
        dlgAltaRepuesto.exec_()
    
    #Conectamos la accion Alta Repuesto...
    @QtCore.pyqtSlot()
    def on_actionAlta_de_Seccion_triggered(self):
        print 'abriendo dialogo Alta Repuesto'
        dlgAltaSeccion = DialogAltaSeccion.DialogAltaSeccion(self)
        dlgAltaSeccion.exec_()
    
        
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
        print 'agregando widget listado Personas'
        self.setCentralWidget(ListadoEmpleados(self))
        
    @QtCore.pyqtSlot()
    def on_actionListado_Vehiculos_de_la_Division_2_triggered(self):
        print 'agregando widget listado Vehiculos'
        self.setCentralWidget(WidgetListadoDeVehiculos.ListadoVehiculos(self))

    @QtCore.pyqtSlot()
    def on_actionListado_Vehiculos_en_Reparacion_por_Seccion_triggered(self):
        print 'agregando widget listado de Vehiculos'
        self.setCentralWidget(WidgetListadoDeVehiculos.Listado_Vehiculos_en_reparacion_por_Seccion(self))
        self.centralWidget().labelListadoVehiculos.setText(QtCore.QString.fromUtf8("Listado de Vehiculos en Reparacion por Seccion"))
    
    @QtCore.pyqtSlot()
    def on_actionListado_Vehiculos_Reparados_por_Seccion_2_triggered(self):
        print 'agregando widget listado de Vehiculos'
        self.setCentralWidget(WidgetListadoDeVehiculos.Listado_Vehiculos_Reparados_por_Seccion_2(self))
        self.centralWidget().labelListadoVehiculos.setText(QtCore.QString.fromUtf8("Listado de Vehiculos Reparados por Seccion"))
    
    @QtCore.pyqtSlot()
    def on_actionListado_Vehiculos_con_Reparaciones_Planificadas_2_triggered(self):
        print 'agregando widget listado de Vehiculos'
        self.setCentralWidget(WidgetListadoDeVehiculos.Listado_Vehiculos_con_Reparaciones_Planificadas(self))
        self.centralWidget().labelListadoVehiculos.setText(QtCore.QString.fromUtf8("Listado de Vehiculos con Reparaciones Planificadas"))
        
    @QtCore.pyqtSlot()
    def on_actionListado_Vehiculos_con_Reparaciones_no_Planificadas_2_triggered(self):
        print 'agregando widget listado de Vehiculos'
        self.setCentralWidget(WidgetListadoDeVehiculos.Listado_Vehiculos_con_Reparaciones_no_Planificadas(self))
        self.centralWidget().labelListadoVehiculos.setText(QtCore.QString.fromUtf8("Listado de Vehiculos con Reparaciones no Planificadas"))
        
    @QtCore.pyqtSlot()
    def on_actionListado_de_Reparaciones_Realizadas_a_un_Vehiculos_2_triggered(self):
        print 'agregando widget listado Vehiculos'
        self.setCentralWidget(WidgetMostrarReparacionesPorVehiculo.WidgetMostrarReparacionesPorVehiculo(self))
    
    @QtCore.pyqtSlot()
    def on_actionListado_de_Tipos_de_Reparaciones_de_la_Division_2_triggered(self):
        print 'agregando widget listado Vehiculos'
        self.setCentralWidget(WidgetMostrarTiposDeReparaciones.WidgetMostrarTiposDeReparaciones(self))
    
    @QtCore.pyqtSlot()
    def on_actionPlanificar_Reparaciones_de_Vehiculo_triggered(self):
        print 'agregando widget listado Vehiculos'
        self.setCentralWidget(WidgetMostrarVehiculosSinPlanificar.WidgetMostrarVehiculosSinPlanificar(self))
    
    @QtCore.pyqtSlot()
    def on_actionBaja_de_Personal_triggered(self):
        print 'agregando widget baja personal'
        self.setCentralWidget(WidgetBajaPersonal.WidgetBajaPersonal(self))
        
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
        print 'agregando widget Seleccionar Sección'
        dlgSelecSec = DialogSeleccionarSeccion.DialogSeleccionarSeccion()
        dlgSelecSec.exec_()
        
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