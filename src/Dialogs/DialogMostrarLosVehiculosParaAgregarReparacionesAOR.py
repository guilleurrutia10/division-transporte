'''
Created on 30/11/2012

@author: Usuario
'''
from PyQt4 import QtCore, QtGui

from formularios.DialogMostrarLosVehiculosParaAgregarReparacionesAOR import Ui_DialogMostrarLosVehiculosParaAgregarReparacionesAOR
from DialogRegistrarReparaciones import DialogRegistrarReparaciones
from WidgetListadoDeVehiculos import ListadoVehiculos
from negocio.Division_Transporte import Division_Transporte
from negocio.excepciones.Excepcion_Orden_No_Esta_En_Revision import Excepcion_Orden_No_Esta_En_Revision
from AyudaManejador import AyudaManejador


class DialogMostrarLosVehiculosParaAgregarReparacionesAOR(QtGui.QDialog, Ui_DialogMostrarLosVehiculosParaAgregarReparacionesAOR, AyudaManejador):
    '''
    Dialogo que muestra todos los vehiculos de la Division y brinda
    la posibilidad de registrarle sus reparaciones.

    @version: 
    @author: 
    '''

    def __init__(self, parent=None):
        '''
        Constructor
        @version: 
        @author: 
        '''
        super(DialogMostrarLosVehiculosParaAgregarReparacionesAOR, self).__init__(parent)
        self.setupUi(self)
        self.DIVISION = Division_Transporte()
        self.listaDeVehiculos = ListadoVehiculos(self.DIVISION.getVehiculosEnRevision(), self.widget)
        self.listaDeVehiculos.connect(self.listaDeVehiculos.tableWidgetListadoDeVehiculos, QtCore.SIGNAL('cellClicked(int,int)'), self.seleccionarCelda)
        self.dominioVehiculo = None
        self.listaDeVehiculos.pushButtonSeleccionar.hide()
        # Layout que contiene el widget central
        self.verticalLayout_2.addWidget(self.listaDeVehiculos)

    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        '''
        @version: 
        @author: 
        '''
        self.close()

    @QtCore.pyqtSlot()
    def on_pushButtonAceptar_clicked(self):
        '''
        @version: 
        @author: 
        '''
        self.accept()

    @QtCore.pyqtSlot()
    def on_pushButtonAgregarReparacionesAOrden_clicked(self):
        '''
        @version: 
        @author: 
        '''
        if self.dominioVehiculo:
            dlgRegistrarReparacionesVehiculo = DialogRegistrarReparaciones(self, self.DIVISION.getVehiculo(self.dominioVehiculo))
            try:
                dlgRegistrarReparacionesVehiculo.exec_()
                vehiculosEnRevision = self.DIVISION.getVehiculosEnRevision()
                self.listaDeVehiculos.tableWidgetListadoDeVehiculos.cargarConVehiculos(vehiculosEnRevision)
            except Excepcion_Orden_No_Esta_En_Revision, e:
                QtGui.QMessageBox.critical(self, 'Error', e.getMensaje())
        else:
            QtGui.QMessageBox.critical(self, 'Atencion', 'Debe seleccionar un Vehiculo para poder agregarle reparaciones')
            return

    def seleccionarCelda(self, fila, columna):
        self.dominioVehiculo = unicode(self.listaDeVehiculos.tableWidgetListadoDeVehiculos.getVehiculoSeleccionado().getDominio())
