# -*- coding: utf-8 -*-
'''
Created on 10/10/2012

@author: urrutia
'''

from PyQt4 import QtGui, QtCore

from formularios.WidgetListadoDeVehiculos import Ui_FormListadoVehiculos
from negocio.Division_Transporte import Division_Transporte

'''@todo: lo que sigue............ ;p'''
#===============================================================================
# Crear clases similares con los nombres significativos correspondientes, por ejemplo
# ListadoVehiculosSinReparaciones para evitar grandes sentencias condicionales...
#===============================================================================
class ListadoVehiculos(QtGui.QWidget, Ui_FormListadoVehiculos):
    def __init__(self, parent = None):
        super(ListadoVehiculos, self).__init__(parent)
        self.setupUi(self)
        self.cargarGrillaInicial()
    
    @QtCore.pyqtSlot('QString')
    def on_lineEditBuscar_textChanged(self, cadena):
        print 'Iniciando filtrado......................'
        print '%s' %self.lineEditBuscar.text()
        filtro = unicode(self.lineEditBuscar.text())
        division = Division_Transporte()
        vehiculos = division.getVehiculos()
        values = vehiculos.values()
        
        coches = filter(lambda p: unicode.lower(filtro) in unicode.lower(p.dominio), values)
        coches.sort(cmp=lambda x,y : cmp(x.dominio, y.dominio))
        self.cargarGrilla(coches)
            
    def cargarGrilla(self, vehiculos):
        self.tableWidgetListadoDeVehiculos.clearContents()
        self.tableWidgetListadoDeVehiculos.setRowCount(len(vehiculos))
        fila = 0
        for vehiculo in vehiculos:
            columna = 0
            miItem1 = QtGui.QTableWidgetItem()
            miItem1.setText(vehiculo.dominio)
            self.tableWidgetListadoDeVehiculos.setItem(fila,columna,miItem1)
            columna += 1
            miItem2 = QtGui.QTableWidgetItem()
            miItem2.setText(vehiculo.marca)
            self.tableWidgetListadoDeVehiculos.setItem(fila,columna,miItem2)
            columna += 1
            miItem3 = QtGui.QTableWidgetItem()
            miItem3.setText(vehiculo.registroInterno)
            self.tableWidgetListadoDeVehiculos.setItem(fila,columna,miItem3)
            columna += 1
            miItem4 = QtGui.QTableWidgetItem()
            miItem4.setText(vehiculo.numeroChasis)
            self.tableWidgetListadoDeVehiculos.setItem(fila,columna,miItem4)
            columna += 1
            miItem5 = QtGui.QTableWidgetItem()
            miItem5.setText(vehiculo.comisaria)
            self.tableWidgetListadoDeVehiculos.setItem(fila,columna,miItem5)
            fila += 1
    
    def cargarGrillaInicial(self):
        division = Division_Transporte()
        vehiculos = division.getVehiculos()
        coches = vehiculos.values()
        coches.sort(cmp=lambda x,y : cmp(x.dominio, y.dominio))
        self.cargarGrilla(coches)
        

class Listado_Vehiculos_en_reparacion_por_Seccion(QtGui.QWidget, Ui_FormListadoVehiculos):
    def __init__(self, parent = None):
        super(Listado_Vehiculos_en_reparacion_por_Seccion, self).__init__(parent)
        self.setupUi(self)
        
class Listado_Vehiculos_con_Reparaciones_Planificadas(QtGui.QWidget, Ui_FormListadoVehiculos):
    def __init__(self, parent = None):
        super(Listado_Vehiculos_con_Reparaciones_Planificadas, self).__init__(parent)
        self.setupUi(self)
        
class Listado_Vehiculos_con_Reparaciones_no_Planificadas(QtGui.QWidget, Ui_FormListadoVehiculos):
    def __init__(self, parent = None):
        super(Listado_Vehiculos_con_Reparaciones_no_Planificadas, self).__init__(parent)
        self.setupUi(self)
        
class Listado_Vehiculos_de_la_Division_2(QtGui.QWidget, Ui_FormListadoVehiculos):
    def __init__(self, parent = None):
        super(Listado_Vehiculos_de_la_Division_2, self).__init__(parent)
        self.setupUi(self)
        
class Listado_Vehiculos_con_Reparaciones_Planificadas_2(QtGui.QWidget, Ui_FormListadoVehiculos):
    def __init__(self, parent = None):
        super(ListadoVehiculos, self).__init__(parent)
        self.setupUi(self)
        
class Listado_Vehiculos_Reparados_por_Seccion_2(QtGui.QWidget, Ui_FormListadoVehiculos):
    def __init__(self, parent = None):
        super(Listado_Vehiculos_Reparados_por_Seccion_2, self).__init__(parent)
        self.setupUi(self)