# -*- coding: utf-8 -*-
'''
Created on 03/10/2012

@author: Usuario
'''
from PyQt4 import QtCore, QtGui
from formularios.DialogRegistrarReparaciones import Ui_DialogRegistrarReparaciones
from Dialogs import DialogCrearReparacion
from negocio.Division_Transporte import Division_Transporte
from excepciones.Excepcion_Orden_No_Esta_En_Revision import Excepcion_Orden_No_Esta_En_Revision
from Dialogs.DialogMostrarPedidoDeActuacion import DialogMostrarPedidoDeActuacion

class DialogRegistrarReparaciones(QtGui.QDialog, Ui_DialogRegistrarReparaciones):
    '''
    Atributos:
    
    - vehiculoSeleccionado
    
    En tiempo de ejecucion, el dialogo posee una nueva variable:
    Mejor seteamos...
        - dominioVehiculo.
    '''
    def __init__(self, parent = None):
        '''
        Constructor
        '''
        super(DialogRegistrarReparaciones, self).__init__(parent)
        self.setupUi(self)
        #Conectamos el boton Agregar Reparaciones...
        self.connect(self.pushButtonAgregarReparacion, QtCore.SIGNAL("pressed()"), self.abrirDialogCrearReparacion)
        self.vehiculoSeleccionado = None
        self.dominioVehiculo = None
    
    def setDominioVehiculo(self, unDominio):
        self.dominioVehiculo = unDominio
            
    def exec_(self, *args, **kwargs):
        self.completarLabelsOR()
        #TODO: Quitar de aca
        self.cargarListaReparaciones(self.ordenDeReparacion.getReparaciones())
        return QtGui.QDialog.exec_(self, *args, **kwargs)
        
    def cargarListaReparaciones(self, reparaciones):
        self.tableWidgetReparaciones.clearContents()
        self.tableWidgetReparaciones.setRowCount(len(reparaciones))
        fila = 0
        for reparacion in reparaciones:
            columna = 0
            itemNombreTipo = QtGui.QTableWidgetItem()
            itemNombreTipo.setText(reparacion.getTipoDeReparacion().getNombre())
            self.tableWidgetReparaciones.setItem(fila,columna,itemNombreTipo)
            columna += 1
            itemDescripcion = QtGui.QTableWidgetItem()
            itemDescripcion.setText(reparacion.getDescripcion())
            self.tableWidgetReparaciones.setItem(fila,columna,itemDescripcion)
            fila += 1
    
        
    def completarLabelsOR(self):
        print self.dominioVehiculo.text()
        self.vehiculoSeleccionado = self.buscarVehiculo()
        try:
            ordenDeReparacion = self.vehiculoSeleccionado.getOrdenDeReparacionEnCurso()
        except Excepcion_Orden_No_Esta_En_Revision, e:
            raise Excepcion_Orden_No_Esta_En_Revision(e.getMensaje())
            
        
        #Completar los labels:
        self.labelChoferAsignado.setText(ordenDeReparacion.getChofer())
        self.labelIdOrden.setText(unicode(ordenDeReparacion.getCodigoOrdenReparacion()))
        self.labelFechaOrden.setText(ordenDeReparacion.getFecha().ctime())
        self.labelKilometraje.setText(unicode(ordenDeReparacion.getKilometrajeActual()))
        self.labelEquipamiento.setText(ordenDeReparacion.getEquipamiento())
        self.labelCombustible.setText(unicode(ordenDeReparacion.getCombustibleActual()))
        self.labelComisaria.setText(ordenDeReparacion.getComisaria())
        
        self.ordenDeReparacion = ordenDeReparacion
        
    def buscarVehiculo(self):
        division = Division_Transporte()
        return division.getVehiculo(unicode(self.dominioVehiculo.text()))
    
    def abrirDialogCrearReparacion(self):
        print 'abriendo dialogo Crear Reparacion'
        dlgCrearReparacion = DialogCrearReparacion.DialogCrearReparacion(self)
        #A partir de esta sentencia, dlgCrearReparacion posee una OR:
        dlgCrearReparacion.setOrdenDeReparacion(self.ordenDeReparacion)
        if dlgCrearReparacion.exec_():
            #Toma la variable ordenDeReparacion generada en tiempo de ejecucion
            #por el metodo completarLabelsOR()
            self.cargarListaReparaciones(self.ordenDeReparacion.getReparaciones())
        
        
    @QtCore.pyqtSlot()
    def on_pushButtonAceptar_clicked(self):
        print 'Click sobre aceptar'
        if self.ordenDeReparacion.getReparaciones() == []:
            QtGui.QMessageBox.critical(self, 'Error', 'Debe agregar por lo menos una Reparacion al Vehiculo para generar un Pedido de Actuacion')
            return
        division = Division_Transporte()
        division.registrarReparaciones(self.vehiculoSeleccionado)
        vehiculo = self.buscarVehiculo()
        self.mostrarPedidoDeActuacion(vehiculo.dameOrdenDeReparacionEnCurso().getPedidoDeActuacion())
        self.accept()
    
    def mostrarPedidoDeActuacion(self, unPedidoDeActuacion):
        '''
        '''
        #TODO [ok]: Aca ahora imprimimos algo, pero debemos mostrar un nuevo dialogo...
        dlgMostrarPedido = DialogMostrarPedidoDeActuacion()
        dlgMostrarPedido.setPedidoDeActuacion(unPedidoDeActuacion)
        dlgMostrarPedido.exec_()
            
        
    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        self.reject()
        
    @QtCore.pyqtSlot()
    def on_pushButtonBuscarVehiculo_clicked(self):
        print 'Buscando............'