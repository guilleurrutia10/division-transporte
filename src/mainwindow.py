# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui

from formularios.MainWindowExample import Ui_MainWindow
from formularios.WidgetListadoEmpleados import Ui_Form
from formularios.DialogAltaVehiculo import Ui_DialogAltaVehiculo


#===============================================================================
# Import Dialogos
#===============================================================================
from Dialogs import DialogModificarVehiculo,DialogAltaPersonal,DialogRegistrarReparaciones,DialogAltaRepuesto,DialogAltaSeccion, DialogModificarPersonal, DialogMuestraLosRepuestos
#===============================================================================
# import widgets
#===============================================================================
from Dialogs import WidgetMostrarReparacionesPorVehiculo,WidgetMostrarTiposDeReparaciones,WidgetMostrarVehiculosSinPlanificar,WidgetBajaPersonal
from Dialogs import WidgetPedidosDeActuacion, WidgetListadoSecciones, WidgetListadoDeRepuestosUtilizados, WidgetListadoDeVehiculos

class MyListado(QtGui.QWidget, Ui_Form):
    def __init__(self, parent = None):
        super(MyListado, self).__init__(parent)
        self.setupUi(self)
        self.cargarGrilla()
#        self.connect(self.tableWidgetDatosEmpleados, QtCore.SIGNAL('cellDoubleClicked(int,int)'), self.celdaClick)
    
    def cargarGrilla(self):
        
        print "Cargando Grilla"
#        from negocio.Empleado import Empleado
        from adminBaseDatos import Local
#        personita = Local.mostrarEmpleado('1')
#        
#        self.tableWidgetDatosEmpleados.setRowCount(1)
#        miItemc1 = QtGui.QTableWidgetItem()
#        miItemc2 = QtGui.QTableWidgetItem()
#        miItemc1.setText(personita.nombre)
#        miItemc2.setText(personita.apellido)
#        self.tableWidgetDatosEmpleados.setItem(0,0,miItemc1)
#        self.tableWidgetDatosEmpleados.setItem(0,1,miItemc2)
        p = Local.mostrarEmpleados()
        
        if p.__len__() != 0:
            self.tableWidgetDatosEmpleados.setRowCount(p.__len__())
            row = 0
            for i in p:
                miItemc1 = QtGui.QTableWidgetItem()
                miItemc2 = QtGui.QTableWidgetItem()
                miItemc3 = QtGui.QTableWidgetItem()
                miItemc1.setText(i.nombre)
                miItemc2.setText(i.apellido)
                miItemc3.setText(i.documento)
                self.tableWidgetDatosEmpleados.setItem(row,0,miItemc1)
                self.tableWidgetDatosEmpleados.setItem(row,1,miItemc2)
                self.tableWidgetDatosEmpleados.setItem(row,2,miItemc3)
                row = row + 1
    
    def celdaClick(self):
        print "Click sobre una celda"
        self.close()
        

class ListadoEmpleados(QtGui.QWidget, Ui_Form):
    def __init__(self, parent = None):
        super(ListadoEmpleados, self).__init__(parent)
        self.setupUi(self)

class DialogAltaVehiculo(QtGui.QDialog, Ui_DialogAltaVehiculo):
    def __init__(self, parent = None):
        super(DialogAltaVehiculo, self).__init__(parent)
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
        #Cosas Nuevas
        #---------- Probando ----------------------
        self.centralWidget().connect(self.centralWidget().tableWidgetDatosEmpleados,QtCore.SIGNAL('cellDoubleClicked(int,int)'), self.celdaClick)
        
    def celdaClick(self):
        print "Click sobre una celda"
        self.centralWidget().close()
        self.setCentralWidget(DialogModificarPersonal.DialogModificarPersonal(self))
    
    @QtCore.pyqtSlot()
    def on_actionAlta_de_Vehiculo_triggered(self):
        print 'abriendo dialogo Alta Vehiculo'
        dlgAltaVehiculo = DialogAltaVehiculo(self)
        dlgAltaVehiculo.exec_()
    
    #Conectamos la accion modificar vehiculo...
    @QtCore.pyqtSlot()
    def on_actionModificacion_de_Vehiculo_triggered(self):
        print 'abriendo dialogo Modificar Vehiculo'
        dlgModificarVehiculo = DialogModificarVehiculo.DialogModificarVehiculo(self) 
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
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, QtGui.QDockWidget('my dock', self))
        
        
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
#        self.setCentralWidget(WidgetMostrarReparacionesPorVehiculo.WidgetMostrarReparacionesPorVehiculo(self))

    @QtCore.pyqtSlot()
    def on_actionListado_Vehiculos_en_Reparacion_por_Seccion_triggered(self):
        print 'agregando widget listado de Vehiculos'
        self.setCentralWidget(WidgetListadoDeVehiculos.ListadoVehiculos(self))
        self.centralWidget().labelListadoVehiculos.setText("Listado de Vehiculos en Reparacion por Seccion")
    
    @QtCore.pyqtSlot()
    def on_actionListado_Vehiculos_Reparados_por_Seccion_2_triggered(self):
        print 'agregando widget listado de Vehiculos'
        self.setCentralWidget(WidgetListadoDeVehiculos.ListadoVehiculos(self))
        self.centralWidget().labelListadoVehiculos.setText("Listado de Vehiculos Reparados por Seccion")
    
    @QtCore.pyqtSlot()
    def on_actionListado_Vehiculos_con_Reparaciones_Planificadas_2_triggered(self):
        print 'agregando widget listado de Vehiculos'
        self.setCentralWidget(WidgetListadoDeVehiculos.ListadoVehiculos(self))
        self.centralWidget().labelListadoVehiculos.setText("Listado de Vehiculos con Reparaciones Planificadas")
        
    @QtCore.pyqtSlot()
    def on_actionListado_Vehiculos_con_Reparaciones_no_Planificadas_2_triggered(self):
        print 'agregando widget listado de Vehiculos'
        self.setCentralWidget(WidgetListadoDeVehiculos.ListadoVehiculos(self))
        self.centralWidget().labelListadoVehiculos.setText("Listado de Vehiculos con Reparaciones no Planificadas")
        
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
#        self.setCentralWidget(WidgetMostrarRepuestos.WidgetMostrarRepuestos(self))
    
    #Conectamos la accion Modificar Personal...
    @QtCore.pyqtSlot()
    def on_actionModificacion_de_Personal_triggered(self):
        print 'agregando Widget'
        self.setCentralWidget(WidgetBajaPersonal.WidgetBajaPersonal(self))
        
    @QtCore.pyqtSlot()
    def on_actionListados_de_Seccion_triggered(self):            
        print 'agregando Widget Listado de Secciones'
        self.setCentralWidget(WidgetListadoSecciones.ListadoSecciones(self))
        self.centralWidget().pushButton_2_Cancelar.hide()
        self.centralWidget().pushButtonSeleccionar.hide()

    @QtCore.pyqtSlot()
    def on_actionListado_de_Repuestos_de_la_Division_triggered(self):
        print 'agregando widget listado de repustos utilizados'
        self.setCentralWidget(WidgetListadoDeRepuestosUtilizados.ListadoRepustosUtilizados(self))
        
    @QtCore.pyqtSlot()
    def on_actionRegistrar_Recepcion_de_Pedido_de_Actuacion_triggered(self):
        print 'agregando widget Registro Pedido de Actuacion'
        self.setCentralWidget(WidgetPedidosDeActuacion.WidgetRegistrarPedidoDeActuacion(self))
    
    @QtCore.pyqtSlot()
    def on_actionAsignar_Reparacion_triggered(self):
        print 'agregando widget Registro Pedido de Actuacion'
        self.setCentralWidget(WidgetListadoSecciones.ListadoSecciones(self))
        self.centralWidget().connect(self.centralWidget().pushButtonSeleccionar, QtCore.SIGNAL("pressed()"), self.seleccionarSeccion)
    
    def seleccionarSeccion(self):
        print "Click sobre Seleccionar Seccion"
        self.centralWidget().close()
        self.setCentralWidget(WidgetMostrarReparacionesPorVehiculo.WidgetMostrarReparacionesPorVehiculo(self))
        self.centralWidget().connect(self.centralWidget().tableWidgetReparaciones, QtCore.SIGNAL('cellDoubleClicked(int,int)'), self.celdaReparacionClick)
        self.centralWidget().tableWidgetReparaciones.setRowCount(1)
        self.centralWidget().label_3.setText("Reparaciones Necesarias")
        
    def celdaReparacionClick(self):
        print "Click", "."*50
        
        
    def keyPressEvent(self, e):
        
        if e.key() == QtCore.Qt.Key_F1:
            self.on_actionAlta_de_Personal_triggered()
        if e.key() == (QtCore.Qt.Key_F2):
            self.on_actionListado_triggered()