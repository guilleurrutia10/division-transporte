'''
Created on 30/11/2012

@author: Usuario
'''
from PyQt4 import QtCore, QtGui

from formularios.DialogMostrarLosVehiculosParaAgregarReparacionesAOR import Ui_DialogMostrarLosVehiculosParaAgregarReparacionesAOR
import DialogRegistrarReparaciones
import WidgetListadoDeVehiculos
from negocio.Division_Transporte import Division_Transporte
from excepciones.Excepcion_Orden_No_Esta_En_Revision import Excepcion_Orden_No_Esta_En_Revision

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
        self.miWidget = WidgetListadoDeVehiculos.ListadoVehiculos(self.widget)
        self.miWidget.connect(self.miWidget.tableWidgetListadoDeVehiculos, QtCore.SIGNAL('cellClicked(int,int)'), self.seleccionarCelda)
        self.dominioVehiculo = None    
        
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
            dlgRegistrarReparacionesVehiculo = DialogRegistrarReparaciones.DialogRegistrarReparaciones()
            dlgRegistrarReparacionesVehiculo.setDominioVehiculo(self.dominioVehiculo)
            self.dominioVehiculo = None
            try:
                dlgRegistrarReparacionesVehiculo.exec_()
            except Excepcion_Orden_No_Esta_En_Revision, e:
                QtGui.QMessageBox.critical(self, 'Error', e.getMensaje())
        else:
            QtGui.QMessageBox.critical(self, 'Atencion', 'Debe seleccionar un Vehiculo para poder agregarle reparaciones')
            return
        
    def seleccionarCelda(self, fila, columna):
        self.dominioVehiculo = self.miWidget.tableWidgetListadoDeVehiculos.item(fila, 0)
        
