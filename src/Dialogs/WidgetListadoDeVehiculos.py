# -*- coding: utf-8 -*-
'''
Created on 10/10/2012

@author: urrutia
'''

from PyQt4 import QtGui, QtCore

from formularios.WidgetListadoDeVehiculos import Ui_FormListadoVehiculos
from negocio.Division_Transporte import Division_Transporte

'''TODO: lo que sigue............ ;p'''
#===============================================================================
# Crear clases similares con los nombres significativos correspondientes, por ejemplo
# ListadoVehiculosSinReparaciones para evitar grandes sentencias condicionales...
#===============================================================================
class ListadoVehiculos(QtGui.QWidget, Ui_FormListadoVehiculos):
    def __init__(self, parent=None):
        super(ListadoVehiculos, self).__init__(parent)
        self.setupUi(self)
        #Para evitar que se modifique la información presentada por la grilla.
        self.tableWidgetListadoDeVehiculos.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.cargarGrillaInicial()
    
    @QtCore.pyqtSlot('QString')
    def on_lineEditBuscar_textChanged(self, cadena):
        filtro = unicode(self.lineEditBuscar.text())        
        coches = filter(lambda p: unicode.lower(filtro) in unicode.lower(unicode(p.dominio)), self.vehiculos)
        #El método de comparación por igual está sobrecargado en la clase Legajo.
        coches.sort(cmp=lambda x, y : cmp(x, y))
#        coches.sort(cmp=lambda x,y : cmp(x.dominio, y.dominio))
        self.cargarGrilla(coches)
            
    def cargarGrilla(self, vehiculos):
        self.tableWidgetListadoDeVehiculos.clearContents()
        self.tableWidgetListadoDeVehiculos.setRowCount(len(vehiculos))
        fila = 0
        for vehiculo in vehiculos:
            columna = 0
            itemDominio = QtGui.QTableWidgetItem()
            itemDominio.setText(vehiculo.dominio)
            self.tableWidgetListadoDeVehiculos.setItem(fila, columna, itemDominio)
            columna += 1
            itemMarca = QtGui.QTableWidgetItem()
            itemMarca.setText(vehiculo.marca)
            self.tableWidgetListadoDeVehiculos.setItem(fila, columna, itemMarca)
            columna += 1
            itemRegistroInterno = QtGui.QTableWidgetItem()
            itemRegistroInterno.setText(vehiculo.registroInterno)
            self.tableWidgetListadoDeVehiculos.setItem(fila, columna, itemRegistroInterno)
            columna += 1
            itemNumeroChasis = QtGui.QTableWidgetItem()
            itemNumeroChasis.setText(vehiculo.numeroChasis)
            self.tableWidgetListadoDeVehiculos.setItem(fila, columna, itemNumeroChasis)
            columna += 1
            itemComisaria = QtGui.QTableWidgetItem()
            itemComisaria.setText(vehiculo.comisaria)
            self.tableWidgetListadoDeVehiculos.setItem(fila, columna, itemComisaria)
            #columna += 1
            #itemModelo = QtGui.QTableWidgetItem()
            #itemModelo.setText(vehiculo.marca)
            #self.tableWidgetListadoDeVehiculos.setItem(fila, columna, itemModelo)
            fila += 1
            
    
    def cargarGrillaInicial(self):
        division = Division_Transporte()
        vehiculos = division.getVehiculos()
        self.vehiculos = vehiculos.values()
        self.vehiculos.sort(cmp=lambda x, y : cmp(x.dominio, y.dominio))
        self.cargarGrilla(self.vehiculos)
    '''
    TODO: cambiar por un refrescar grilla.
    '''
    @QtCore.pyqtSlot()
    def on_pushButtonRefrescar_clicked(self):
        self.lineEditBuscar.clear()
        self.cargarGrillaInicial()

class Listado_Vehiculos_en_reparacion_por_Seccion(QtGui.QWidget, Ui_FormListadoVehiculos):
    def __init__(self, parent=None):
        super(Listado_Vehiculos_en_reparacion_por_Seccion, self).__init__(parent)
        self.setupUi(self)
        
class Listado_Vehiculos_con_Reparaciones_Planificadas(QtGui.QWidget, Ui_FormListadoVehiculos):
    def __init__(self, parent=None):
        super(Listado_Vehiculos_con_Reparaciones_Planificadas, self).__init__(parent)
        self.setupUi(self)
        
class Listado_Vehiculos_con_Reparaciones_no_Planificadas(QtGui.QWidget, Ui_FormListadoVehiculos):
    def __init__(self, parent=None):
        super(Listado_Vehiculos_con_Reparaciones_no_Planificadas, self).__init__(parent)
        self.setupUi(self)
        
class Listado_Vehiculos_de_la_Division_2(QtGui.QWidget, Ui_FormListadoVehiculos):
    def __init__(self, parent=None):
        super(Listado_Vehiculos_de_la_Division_2, self).__init__(parent)
        self.setupUi(self)
        
class Listado_Vehiculos_con_Reparaciones_Planificadas_2(QtGui.QWidget, Ui_FormListadoVehiculos):
    def __init__(self, parent=None):
        super(ListadoVehiculos, self).__init__(parent)
        self.setupUi(self)
        
class Listado_Vehiculos_Reparados_por_Seccion_2(QtGui.QWidget, Ui_FormListadoVehiculos):
    def __init__(self, parent=None):
        super(Listado_Vehiculos_Reparados_por_Seccion_2, self).__init__(parent)
        self.setupUi(self)
