# -*- coding: utf-8 -*-
'''
Created on 10/10/2012

@author: urrutia
'''

from PyQt4 import QtGui, QtCore

from formularios.WidgetListadoDeVehiculos import Ui_FormListadoVehiculos
from formularios.WidgetMostrarReparacionesVehiculo import Ui_WidgetMostrarReparacionesPorVehiculo

from negocio.Division_Transporte import Division_Transporte
# from pyfits.util import deprecated
from reportes import imprimirListadoVehiculos
from Utiles_Dialogo import Mensaje


'''TODO: lo que sigue............ ;p'''
#===============================================================================
# Crear clases similares con los nombres significativos correspondientes, por ejemplo
# ListadoVehiculosSinReparaciones para evitar grandes sentencias condicionales...
#===============================================================================
class ListadoVehiculos(QtGui.QWidget, Ui_FormListadoVehiculos):
    def __init__(self, vehiculosParaListar, parent=None):
        super(ListadoVehiculos, self).__init__(parent)
        self.setupUi(self)
        # Para evitar que se modifique la información presentada por la grilla.
        self.tableWidgetListadoDeVehiculos.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.vehiculos = vehiculosParaListar
        # self.cargarGrilla(self.vehiculos)
        self.tableWidgetListadoDeVehiculos.cargarConVehiculos(self.vehiculos)
        # Reaccionamos al doble clic:
        self.tableWidgetListadoDeVehiculos.connect(self.tableWidgetListadoDeVehiculos, QtCore.SIGNAL('cellDoubleClicked(int , int)'), self.planificarVehiculo)
        self.pushButtonToPdf.setObjectName('iconButton')

    def planificarVehiculo(self, fila, columna):
        '''
        Planificar vehiculo
        '''
#        print 'selecciono el vehiculo: %d\n Coordenadas: (%d, %d)' %(fila, fila, columna)
        debug= self.tableWidgetListadoDeVehiculos.getVehiculoEn(fila).getDominio()

    @QtCore.pyqtSlot()
    def on_pushButtonToPdf_clicked(self):
        fileDialog = QtGui.QFileDialog(caption=QtCore.QString.fromUtf8('Guardar Listado de Vehículos'))
        fileDialog.setAcceptMode(QtGui.QFileDialog.AcceptSave)
        if fileDialog.exec_() == QtGui.QFileDialog.AcceptSave:
            for filename in fileDialog.selectedFiles():
                debug= 'Imprimiendo: %s' % filename
        else:
            return
        cabeceraVehiculos = ['',
                             'Dominio',
                             'Marca',
                             'Registro Interno',
                             u'Número de Chasis'
                             ]
        imprimirListadoVehiculos(cabeceraVehiculos, self.vehiculos, filename=unicode(filename))
        m = Mensaje(self)
        m.setTitle('PDF')
        m.setMensaje(u'El archivo pdf ha sido generado con éxito. Se encuentra ubicado en %s.pdf' % filename)
        m.setInformative()
        m.exec_()

    @QtCore.pyqtSlot('QString')
    def on_lineEditBuscar_textChanged(self, cadena):
        filtro = unicode(self.lineEditBuscar.text()).lower()
        coches = filter(lambda v: filtro in unicode.lower(unicode(v.getDominio()))
                        or filtro in unicode.lower(unicode(v.getMarca()))
                        or filtro in unicode.lower(unicode(v.getRegistroInterno()))
                        or filtro in unicode.lower(unicode(v.getNumeroChasis())),
                        self.vehiculos)
        # El método de comparación por igual está sobrecargado en la clase Legajo.
        coches.sort(cmp=lambda x, y: cmp(x, y))
        self.tableWidgetListadoDeVehiculos.cargarConVehiculos(coches)


from formularios.DlgPlanificar_1 import Ui_DlgPlanificar_1


class DialogPlanificar_1(QtGui.QDialog, Ui_DlgPlanificar_1):
    '''
    Atributos:

        _vehiculo: al cual vamos a planificar

    '''
    def __init__(self, parent=None, vehiculoSeleccionado=None):
        '''
        Constructor
        '''
        super(DialogPlanificar_1, self).__init__(parent)
        self.setupUi(self)
        self._vehiculo = vehiculoSeleccionado


class Listado_Vehiculos_en_reparacion_por_Seccion(QtGui.QWidget, Ui_FormListadoVehiculos):
    def __init__(self, parent=None):
        super(Listado_Vehiculos_en_reparacion_por_Seccion, self).__init__(parent)
        self.setupUi(self)


#TODO: Deprecated
class Listado_Vehiculos_con_Reparaciones_Planificadas(QtGui.QWidget, Ui_FormListadoVehiculos):
    def __init__(self, parent=None):
        super(Listado_Vehiculos_con_Reparaciones_Planificadas, self).__init__(parent)
        self.setupUi(self)


# class Listado_Vehiculos_con_Reparaciones_no_Planificadas(QtGui.QWidget, Ui_FormListadoVehiculos):
class Listado_Vehiculos_con_Reparaciones_no_Planificadas(QtGui.QWidget, Ui_WidgetMostrarReparacionesPorVehiculo):
    def __init__(self, parent=None):
        super(Listado_Vehiculos_con_Reparaciones_no_Planificadas, self).__init__(parent)
        self.setupUi(self)
#         self.widgetCentral = ListadoVehiculos(Division_Transporte().getVehiculosEnAprobada(), self)
        self.tableWidgetVehiculos.cargarConVehiculos(Division_Transporte().getVehiculosEnAprobada())
        self.tableWidgetVehiculos.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.tableWidgetReparaciones.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self._ultimoVehiculoSeleccionado = None

        self.tableWidgetVehiculos.connect(self.tableWidgetVehiculos, QtCore.SIGNAL('cellClicked(int , int)'), self.mostrarReparaciones)

    def mostrarReparaciones(self, fila, columna):
        vehiculoSeleccionado = self.tableWidgetVehiculos.getVehiculoEn(fila)
        print 'Vehiculo seleccionado: ', vehiculoSeleccionado.getDominio()
        if vehiculoSeleccionado != self._ultimoVehiculoSeleccionado:
            self._ultimoVehiculoSeleccionado = vehiculoSeleccionado
            self.cargarConReparaciones(vehiculoSeleccionado.dameOrdenDeReparacionEnCurso())

    def cargarConReparaciones(self, reparaciones):
        self.tableWidgetReparaciones.cargarConReparaciones(reparaciones)


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
