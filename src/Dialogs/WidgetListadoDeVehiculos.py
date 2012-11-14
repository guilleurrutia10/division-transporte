# -*- coding: utf-8 -*-
'''
Created on 10/10/2012

@author: urrutia
'''

from PyQt4 import QtGui, QtCore

from formularios.WidgetListadoDeVehiculos import Ui_FormListadoVehiculos

'''@todo: lo que sigue............ ;p'''
#===============================================================================
# Crear clases similares con los nombres significativos correspondientes, por ejemplo
# ListadoVehiculosSinReparaciones para evitar grandes sentencias condicionales...
#===============================================================================
class ListadoVehiculos(QtGui.QWidget, Ui_FormListadoVehiculos):
    def __init__(self, parent = None):
        super(ListadoVehiculos, self).__init__(parent)
        self.setupUi(self)
        self.cargarGrilla()
    
    @QtCore.pyqtSlot('QString')
    def on_lineEditBuscar_textChanged(self, string):
        print 'Iniciando filtrado......................'
        print '%s' %self.lineEditBuscar.text()
    
    #=======================================================================
    # Esto es un ejemplo, según el filtrado se mostrarán o no ciertos
    # vehículos 
    #=======================================================================
    def cargarGrilla(self):
        from negocio import Division_Transporte
        division = Division_Transporte.Division_Transporte()
        vehiculos = division.getVehiculos()
        
        self.tableWidgetListadoDeVehiculos.setRowCount(len(vehiculos))
        row = 0
        for coche in vehiculos:
            col = 0
            miItem1 = QtGui.QTableWidgetItem()
            miItem1.setText(vehiculos[coche].dominio)
            self.tableWidgetListadoDeVehiculos.setItem(row,col,miItem1)
            col+=1
            miItem2 = QtGui.QTableWidgetItem()
            miItem2.setText(vehiculos[coche].marca)
            self.tableWidgetListadoDeVehiculos.setItem(row,col,miItem2)
            col+=1
            miItem3 = QtGui.QTableWidgetItem()
            miItem3.setText(vehiculos[coche].registroInterno)
            self.tableWidgetListadoDeVehiculos.setItem(row,col,miItem3)
            col+=1
            miItem4 = QtGui.QTableWidgetItem()
            miItem4.setText(vehiculos[coche].numeroChasis)
            self.tableWidgetListadoDeVehiculos.setItem(row,col,miItem4)
            col+=1
            miItem5 = QtGui.QTableWidgetItem()
            miItem5.setText(vehiculos[coche].comisaria)
            self.tableWidgetListadoDeVehiculos.setItem(row,col,miItem5)
            row+=1

class Listado_Vehiculos_en_reparacion_por_Seccion(QtGui.QWidget, Ui_FormListadoVehiculos):
    def __init__(self, parent = None):
        super(ListadoVehiculos, self).__init__(parent)
        self.setupUi(self)
        
class Listado_Vehiculos_con_Reparaciones_Planificadas(QtGui.QWidget, Ui_FormListadoVehiculos):
    def __init__(self, parent = None):
        super(ListadoVehiculos, self).__init__(parent)
        self.setupUi(self)
        
class Listado_Vehiculos_con_Reparaciones_no_Planificadas(QtGui.QWidget, Ui_FormListadoVehiculos):
    def __init__(self, parent = None):
        super(ListadoVehiculos, self).__init__(parent)
        self.setupUi(self)
        
class Listado_Vehiculos_de_la_Division_2(QtGui.QWidget, Ui_FormListadoVehiculos):
    def __init__(self, parent = None):
        super(ListadoVehiculos, self).__init__(parent)
        self.setupUi(self)
        
class Listado_Vehiculos_con_Reparaciones_Planificadas_2(QtGui.QWidget, Ui_FormListadoVehiculos):
    def __init__(self, parent = None):
        super(ListadoVehiculos, self).__init__(parent)
        self.setupUi(self)
        
class Listado_Vehiculos_Reparados_por_Seccion_2(QtGui.QWidget, Ui_FormListadoVehiculos):
    def __init__(self, parent = None):
        super(ListadoVehiculos, self).__init__(parent)
        self.setupUi(self)