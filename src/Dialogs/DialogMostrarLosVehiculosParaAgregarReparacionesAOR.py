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


class DialogMostrarLosVehiculosParaAgregarReparacionesAOR(QtGui.QDialog, Ui_DialogMostrarLosVehiculosParaAgregarReparacionesAOR):
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
        #self.listaDeVehiculos = WidgetListadoDeVehiculos.ListadoVehiculos(self.DIVISION.getVehiculos().values(), self.widget)
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
        print 'Click sobre aceptar'
        self.accept()

    @QtCore.pyqtSlot()
    def on_pushButtonAgregarReparacionesAOrden_clicked(self):
        '''
        @version: 
        @author: 
        '''
        if self.dominioVehiculo:
            print 'DOMINIO:', self.dominioVehiculo
            dlgRegistrarReparacionesVehiculo = DialogRegistrarReparaciones(self, self.DIVISION.getVehiculo(self.dominioVehiculo))
            try:
                dlgRegistrarReparacionesVehiculo.exec_()
#                 self.listaDeVehiculos.cargarGrilla(self.DIVISION.getVehiculosEnRevision())
                vehiculosEnRevision = self.DIVISION.getVehiculosEnRevision()
                self.listaDeVehiculos.tableWidgetListadoDeVehiculos.cargarConVehiculos(vehiculosEnRevision)
            except Excepcion_Orden_No_Esta_En_Revision, e:
                QtGui.QMessageBox.critical(self, 'Error', e.getMensaje())
        else:
            QtGui.QMessageBox.critical(self, 'Atencion', 'Debe seleccionar un Vehiculo para poder agregarle reparaciones')
            return

    def seleccionarCelda(self, fila, columna):
        self.dominioVehiculo = unicode(self.listaDeVehiculos.tableWidgetListadoDeVehiculos.item(fila, 0).text())
