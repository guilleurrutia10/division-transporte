# -*- coding: utf-8 -*-
'''
Created on 03/10/2012

@author: Usuario
'''
from PyQt4 import QtGui, QtCore

from formularios.WidgetMostrarReparacionesPorVehiculo import Ui_WidgetMostrarReparacionesPorVehiculo
from negocio.Division_Transporte import Division_Transporte

class WidgetMostrarReparacionesPorVehiculo(QtGui.QWidget, Ui_WidgetMostrarReparacionesPorVehiculo):
    '''
    classdocs
    '''


    def __init__(self, vehiculos, parent = None):
        '''
        Constructor
        '''
        super(WidgetMostrarReparacionesPorVehiculo, self).__init__(parent)
        self.setupUi(self)
        
        #self.tableWidgetVehiculos = ListadoVehiculos(Division_Transporte().getVehiculosEnFinalizada(), self)
        #Para evitar que se modifique la información presentada en la tabla
        self.tableWidgetVehiculos.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.tableWidgetReparaciones.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        
        self.tableWidgetVehiculos.cargarConVehiculos(vehiculos)
#         self.tableWidgetVehiculos.cargarConVehiculos(Division_Transporte().getVehiculosEnFinalizada())
#         self.tableWidgetVehiculos.cargarConVehiculos(Division_Transporte().getVehiculos().values())
        
        self.tableWidgetVehiculos.connect(self.tableWidgetVehiculos, QtCore.SIGNAL('cellClicked(int , int)'), self.mostrarReparaciones)
        
    
    def mostrarReparaciones(self, fila, columna):
        '''
        '''
        print 'Debo mostrar las reparaciones para el vehiculo: '
        print self.tableWidgetVehiculos.getVehiculoEn(fila).getDominio()
        vehiculo = self.tableWidgetVehiculos.getVehiculoEn(fila)
        reparaciones = []
        for rep in vehiculo.getReparacionesFinalizadas():
            reparaciones.extend(rep)
        self.tableWidgetReparaciones.cargarConReparaciones(reparaciones)
#         self.tableWidgetReparaciones.cargarConReparaciones(vehiculo.getReparacionesFinalizadas())