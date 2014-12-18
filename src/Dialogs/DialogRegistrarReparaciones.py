# -*- coding: utf-8 -*-
'''
Created on 03/10/2012

@author: Usuario
'''
import transaction
from PyQt4 import QtCore, QtGui
from time import localtime

from formularios.DialogRegistrarReparaciones import Ui_DialogRegistrarReparaciones
from DialogCrearReparacion import DialogCrearReparacion
from negocio.Division_Transporte import Division_Transporte
from negocio.excepciones.Excepcion_Orden_No_Esta_En_Revision import Excepcion_Orden_No_Esta_En_Revision
from DialogMostrarPedidoDeActuacion import DialogMostrarPedidoDeActuacion
from negocio.excepciones.Except_NoHayReparacionesDisponibles import Except_NoHayReparacionesDisponibles
from Utiles_Dialogo import mostrarMensaje
from reportes import imprimirPedidoDeActuacion
from Utiles_Dialogo import Mensaje
from AyudaManejador import AyudaManejador


class DialogRegistrarReparaciones(QtGui.QDialog, Ui_DialogRegistrarReparaciones, AyudaManejador):
    '''
    Atributos:

    - vehiculoSeleccionado

    En tiempo de ejecucion, el dialogo posee una nueva variable:
    Mejor seteamos...
        - dominioVehiculo.

    Recibe como parametro el objeto vehiculo con el cual se va a trabajar
    '''
    def __init__(self, parent=None, vehiculoSeleccionado=None):
        '''
        Constructor
        '''
        super(DialogRegistrarReparaciones, self).__init__(parent)
        self.setupUi(self)
        # Conectamos el boton Agregar Reparaciones...
        self.connect(self.pushButtonAgregarReparacion, QtCore.SIGNAL("pressed()"), self.abrirDialogCrearReparacion)
        self.vehiculoSeleccionado = vehiculoSeleccionado
        self.DIVISION = Division_Transporte()
        # Cargamos la mínima fecha a tener en cuenta.
        # A partir de esta fecha podemos deshacer commits.
        fecha = localtime()
        self.DIVISION.zodb.setFechaMinimaDeshacer(fecha)
        self.prepararCss()

    def exec_(self, *args, **kwargs):
        self.completarLabelsOR()
        #TODO: Quitar de aca
        #self.cargarListaReparaciones(self.ordenDeReparacion.getReparaciones())
        self.cargarListaReparaciones(self.vehiculoSeleccionado.getOrdenDeReparacionEnCurso().getReparaciones())
        return QtGui.QDialog.exec_(self, *args, **kwargs)

    def cargarListaReparaciones(self, reparaciones):
        self.tableWidgetReparaciones.clearContents()
        self.tableWidgetReparaciones.setRowCount(len(reparaciones))
        fila = 0
        for reparacion in reparaciones:
            columna = 0
            itemCodigoTipo = QtGui.QTableWidgetItem()
            itemCodigoTipo.setText(reparacion.getTipoDeReparacion().getCodigo())
            self.tableWidgetReparaciones.setItem(fila,columna,itemCodigoTipo)
            columna += 1
            itemNombreTipo = QtGui.QTableWidgetItem()
            itemNombreTipo.setText(reparacion.getTipoDeReparacion().getNombre())
            self.tableWidgetReparaciones.setItem(fila,columna,itemNombreTipo)
            columna += 1
            itemDescripcion = QtGui.QTableWidgetItem()
            itemDescripcion.setText(reparacion.getCodigo())
            self.tableWidgetReparaciones.setItem(fila,columna,itemDescripcion)
            columna += 1
            itemDescripcion = QtGui.QTableWidgetItem()
            itemDescripcion.setText(reparacion.getDescripcion())
            self.tableWidgetReparaciones.setItem(fila,columna,itemDescripcion)
            fila += 1

    def completarLabelsOR(self):
        try:
            ordenDeReparacion = self.vehiculoSeleccionado.getOrdenDeReparacionEnCurso()
        except Excepcion_Orden_No_Esta_En_Revision, e:
            raise Excepcion_Orden_No_Esta_En_Revision(e.getMensaje())

        # Completar los labels:
        self.labelChoferAsignado.setText(ordenDeReparacion.getChofer())
        self.labelIdOrden.setText(unicode(ordenDeReparacion.getCodigoOrdenReparacion()))
        self.labelFechaOrden.setText(ordenDeReparacion.getFecha().ctime())
        self.labelKilometraje.setText(unicode(ordenDeReparacion.getKilometrajeActual()))
        self.labelEquipamiento.setText(ordenDeReparacion.getEquipamiento())
        self.labelCombustible.setText(unicode(ordenDeReparacion.getCombustibleActual()))
        self.labelComisaria.setText(ordenDeReparacion.getComisaria())

    def prepararCss(self):
        self.label.setObjectName("label")
        self.label_2.setObjectName("label")
        self.label_3.setObjectName("label")
        self.label_6.setObjectName("label")
        self.label_8.setObjectName("label")
        self.label_10.setObjectName("label")
        self.label_11.setObjectName("label")
        self.label_12.setObjectName("label")

    def buscarVehiculo(self):
        return self.DIVISION.getVehiculo(self.dominioVehiculo)

    def abrirDialogCrearReparacion(self):
        try:
            dlgCrearReparacion = DialogCrearReparacion(self, self.vehiculoSeleccionado)
        except Except_NoHayReparacionesDisponibles:
            mostrarMensaje(self, "La división no tiene tipos de repaciones disponibles", "No se pueden agregar reparaciones")
            return
        # A partir de esta sentencia, dlgCrearReparacion posee una OR:
        if dlgCrearReparacion.exec_():
            # Toma la variable ordenDeReparacion generada en tiempo de ejecucion
            # por el metodo completarLabelsOR()
            self.cargarListaReparaciones(self.vehiculoSeleccionado.getOrdenDeReparacionEnCurso().getReparaciones()) # Este dialogo trabaja con VEHICULO!!

    @QtCore.pyqtSlot()
    def on_pushButtonAceptar_clicked(self):
        if not self.vehiculoSeleccionado.getOrdenDeReparacionEnCurso().getReparaciones():
            QtGui.QMessageBox.critical(self, 'Error', 'Debe agregar por lo menos una reparación al Vehículo para generar un Pedido de Actuación')
            return
        # 1ro Recuperamos el vehiculo, ok, el dialogo ya trabaja con un vehiculo
        # directamente le decimos que genere el pedido
        self.vehiculoSeleccionado.generarPedidoDeActuacion()
        self.mostrarPedidoDeActuacion(self.vehiculoSeleccionado.obtenerOrdenDeReparacionEnCurso().getPedidoDeActuacion())
        self.imprimirPedidoActuacion()
        # Para saber de qué cliente debemos borrar las transacciones.
        transaction.get().setUser(self.DIVISION.zodb.getNombreUsuario(), '')
        transaction.commit()
        self.accept()

    def mostrarPedidoDeActuacion(self, unPedidoDeActuacion):
        '''
        '''
        dlgMostrarPedido = DialogMostrarPedidoDeActuacion(self, unPedidoDeActuacion)
        dlgMostrarPedido.exec_()

    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        # Deshacemos los commits realizados.
        self.DIVISION.zodb.deshacerCommits()
        self.reject()

    @QtCore.pyqtSlot()
    def on_pushButtonBuscarVehiculo_clicked(self):
        pass

    def imprimirPedidoActuacion(self):
        # TODO: obtener datos a imprimir
        # datosImprimir = .....
        orden = self.vehiculoSeleccionado.obtenerOrdenDeReparacionEnCurso()
        pedido = orden.getPedidoDeActuacion()
        repuestosSolicitados = pedido.getRepuestosSolicitados()
        repuestosImprimir = []
        for rep in repuestosSolicitados:
            tipoRepuesto = rep.getTipoDeRepuesto()
            repuestosImprimir.append([str(repuestosSolicitados.index(rep)) ,str(rep.getCantidad()), tipoRepuesto.getDescripcion()])
#        print repuestosImprimir
        # TODO: Armar método obtener nombre archivo
        # nombreArchivo = .....
        fileDialog = QtGui.QFileDialog(caption=QtCore.QString.fromUtf8('Guardar Pedido de Actuación'))
        fileDialog.setAcceptMode(QtGui.QFileDialog.AcceptSave)
        if fileDialog.exec_() == QtGui.QFileDialog.AcceptSave:
            for filename in fileDialog.selectedFiles():
#                print 'Imprimiendo: %s' % filename
                aux = filename
        else:
            return
        imprimirPedidoDeActuacion(pedido._nroDePedido, repuestosImprimir, unicode(filename))
        m = Mensaje(self)
        m.setTitle('PDF')
        m.setMensaje(u'El archivo pdf ha sido generado con éxito. Se encuentra ubicado en %s.pdf' % filename)
        m.setInformative()
        m.exec_()
