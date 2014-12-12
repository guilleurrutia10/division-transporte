# -*- coding: utf-8 -*-
'''
Created on 03/10/2012

@author: Usuario
'''
from PyQt4 import QtGui, QtCore

from formularios.WidgetMostrarReparacionesPorVehiculo import Ui_WidgetMostrarReparacionesPorVehiculo
from negocio.Division_Transporte import Division_Transporte
from AyudaManejador import AyudaManejador


class WidgetMostrarReparacionesPorVehiculo(QtGui.QWidget, Ui_WidgetMostrarReparacionesPorVehiculo, AyudaManejador):
    '''
    classdocs
    '''

    def __init__(self, vehiculos, parent=None):
        '''
        Constructor
        self.dateEditHasta
        self.dateEditDesde
        
        '''
        super(WidgetMostrarReparacionesPorVehiculo, self).__init__(parent)
        self.setupUi(self)
        self._vehiculos = vehiculos

        #self.tableWidgetVehiculos = ListadoVehiculos(Division_Transporte().getVehiculosEnFinalizada(), self)
        #Para evitar que se modifique la información presentada en la tabla
        self.tableWidgetVehiculos.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.tableWidgetReparaciones.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)

        self.tableWidgetVehiculos.cargarConVehiculos(vehiculos)
#         self.tableWidgetVehiculos.cargarConVehiculos(Division_Transporte().getVehiculosEnFinalizada())
#         self.tableWidgetVehiculos.cargarConVehiculos(Division_Transporte().getVehiculos().values())

        self.tableWidgetVehiculos.connect(self.tableWidgetVehiculos, QtCore.SIGNAL('cellClicked(int , int)'), self.mostrarReparaciones)
#        self.dateEdit.setCalendarPopup(True)
#        self.dateEdit_2.setCalendarPopup(True)
        self.reparacionesOrdenadas = {}


    def mostrarReparaciones(self, fila, columna):
        '''
        '''
        print 'Debo mostrar las reparaciones para el vehiculo: '
        print self.tableWidgetVehiculos.getVehiculoEn(fila).getDominio()
        vehiculo = self.tableWidgetVehiculos.getVehiculoEn(fila)
        self.reparacionesOrdenadas = vehiculo.getReparacionesFinalizadasOrdenadasPorOrdenReparacion()
#        for rep in vehiculo.getReparacionesFinalizadas():
#            reparaciones.extend(rep)
        self.tableWidgetReparaciones.cargarConReparacionesDeOrdenes(self.reparacionesOrdenadas)
#         self.tableWidgetReparaciones.cargarConReparaciones(vehiculo.getReparacionesFinalizadas())

    @QtCore.pyqtSlot('QDate')
    def on_dateEditDesde_dateChanged(self, date):
        self.filtrarFechaFinalizacionDeReparacion()

    @QtCore.pyqtSlot('QDate')
    def on_dateEditHasta_dateChanged(self, date):
        self.filtrarFechaFinalizacionDeReparacion()

    def reparacionEntreFechas(self, reparacion):
        return self.dateEditDesde.date().toPyDate() <= reparacion.getFechaFin() <= self.dateEditHasta.date().toPyDate()
     
    # TODO: Falta tener en cuenta la fecha de fin de las reparaciones.(OK)
    def filtrarFechaFinalizacionDeReparacion(self):
        '''
            Tenemos que enviar un diccionario de la siguiente forma:
            - {'ORD0001':[Rep1, Rep2,.., RepN],
                ...
              }
        '''
        todas_las_reparaciones = {k:[] for k in self.reparacionesOrdenadas}
        {todas_las_reparaciones[ordenname].append(reparacion) 
         for ordenname, reparaciones in self.reparacionesOrdenadas.iteritems() 
         for reparacion in reparaciones if self.reparacionEntreFechas(reparacion)}
        #Limpiamos:
        todas_las_reparaciones = {ord_name:lrep for ord_name,lrep in todas_las_reparaciones.iteritems() if lrep}
        self.tableWidgetReparaciones.cargarConReparacionesDeOrdenes(todas_las_reparaciones)

    def on_lineEdit_textChanged(self, cadena):
        filtro = unicode(cadena).lower()
        coches = filter(lambda v: filtro in unicode.lower(unicode(v.getDominio()))
                or filtro in unicode.lower(unicode(v.getMarca()))
                or filtro in unicode.lower(unicode(v.getRegistroInterno()))
                or filtro in unicode.lower(unicode(v.getNumeroChasis())),
                self._vehiculos)
        coches.sort(cmp=lambda x, y: cmp(x, y))
        self.tableWidgetVehiculos.cargarConVehiculos(coches)


class WidgetMostrarReparacionesPorVehiculoPlanificadas(WidgetMostrarReparacionesPorVehiculo):

    def mostrarReparaciones(self, fila, columna):
        vehiculo = self.tableWidgetVehiculos.getVehiculoEn(fila)
        reparaciones = []
#         for rep in vehiculo.getReparacionesPlanificadas():
#             reparaciones.app(rep)
        self.tableWidgetReparaciones.cargarConReparaciones(vehiculo.getReparacionesPlanificadas())
#        self.tableWidgetReparaciones.cargarConReparaciones(vehiculo.getReparacionesFinalizadas())
    