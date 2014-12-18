# -*- coding: utf-8 -*-
'''
Created on 14/11/2012

@author: urrutia
'''

from PyQt4 import QtCore, QtGui
from re import match

from formularios.DialogMostrarLosVehiculosParaModificar import Ui_DialogMostrarLosVehiculosParaModificar
from formularios.DialogModificarVehiculo import Ui_DialogModificarVehiculo
from WidgetListadoDeVehiculos import ListadoVehiculos
from negocio.Division_Transporte import Division_Transporte
from AyudaManejador import AyudaManejador


class DialogMostrarLosVehiculosParaModificar(QtGui.QDialog, Ui_DialogMostrarLosVehiculosParaModificar, AyudaManejador):
    '''
    classdocs
    Elementos:
        - tableWidgetListadoDeVehiculos
        - pushButtonHecho
    '''
    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super(DialogMostrarLosVehiculosParaModificar, self).__init__(parent)
        self.setupUi(self)
        self.miWidget = ListadoVehiculos(Division_Transporte().getVehiculos().values(), self.widget)
        self.miWidget.connect(self.miWidget.tableWidgetListadoDeVehiculos, QtCore.SIGNAL('cellClicked(int,int)'), self.seleccionarCelda)
        self.vehiculoSeleccionado = None
        # Se oculta el botón.
        self.miWidget.pushButtonSeleccionar.hide()
        # Layout que contiene el widget central
        self.verticalLayout_2.addWidget(self.miWidget)

    #===========================================================================
    # Tratando de agarrar el evento de Seleccionar un Vehiculos de la grilla
    # y utilizarlo para retomar sus datos de la BD para mostrarlos en el 
    # modificar.
    #===========================================================================
    def seleccionarCelda(self, row, column):
        self.vehiculoSeleccionado = self.miWidget.tableWidgetListadoDeVehiculos.getVehiculoSeleccionado()

    @QtCore.pyqtSlot()
    def on_pushButtonModificarDatosDeVehiculo_clicked(self):
        '''
        '''
        if not self.vehiculoSeleccionado: # == None
            self.mostrarMensaje(self.trUtf8('Debe seleccionar un Vehículo.'),
                                self.trUtf8('Ingresar Vehículo'))
            return
        dlgModificar = DialogModificarVehiculo(vehiculoSeleccionado=self.vehiculoSeleccionado)
        dlgModificar.exec_()
        self.vehiculoSeleccionado = None
        vehiculos = Division_Transporte().getVehiculos().values()
        self.miWidget.tableWidgetListadoDeVehiculos.cargarConVehiculos(vehiculos)

    '''
    TODO: Este método se repite en varios Dialogs.
    '''
    def mostrarMensaje(self, mensaje, titulo):
        msgBox = QtGui.QMessageBox(self)
        msgBox.setText(mensaje)
        #msgBox.setText(QtCore.QString.fromUtf8(mensaje))
        msgBox.setWindowTitle(titulo)
        #msgBox.setWindowTitle(QtCore.QString.fromUtf8(titulo))
        return msgBox.exec_()

    #===========================================================================
    # Evento que se dispara cada vez que el Dialog toma el Foco
    #===========================================================================
    def showEvent(self, e):
        return


class DialogModificarVehiculo(QtGui.QDialog, Ui_DialogModificarVehiculo, AyudaManejador):
    '''
    classdocs
    '''
    def __init__(self, parent=None, vehiculoSeleccionado=None):
        '''
        Constructor
        '''
        super(DialogModificarVehiculo, self).__init__(parent)
        self.setupUi(self)
        self.auto = vehiculoSeleccionado
        self.cargarLineEdit()
        for label in self.findChildren(QtGui.QLabel):
            label.setObjectName('label')

    def cargarLineEdit(self):
        self.lineEditDominio.setText(self.auto.dominio)
        self.lineEditDominio.setReadOnly(True)
        self.lineEditDominio.setModified(False)
        self.lineEditRegistroInterno.setText(self.auto.registroInterno)
        self.lineEditChasisNro.setText(self.auto.numeroChasis)
        self.lineEditMarca.setText(self.auto.marca)
        self.lineEditMarca.setFocus()
        return

    # Se agrega la validación al completar los campos.
    def validacionesLineEdit(self):
        '''
        Se cargan las expresiones regulares para validar
        la entrada de los diferentes lineEdits del diálogo.
        '''
#         dominioRegExp = QtCore.QRegExp('[A-Z|a-z]{3}[0-9]{3}')
#         validadorRegExp = QtGui.QRegExpValidator(dominioRegExp, self)
#         self.lineEditDominio.setValidator(validadorRegExp)
        marcaRegExp = QtCore.QRegExp('[A-Z|a-z]+')
        validadorRegExp = QtGui.QRegExpValidator(marcaRegExp, self)
        self.lineEditMarca.setValidator(validadorRegExp)
        registroInternoRegExp = QtCore.QRegExp('[0-9]+')
        validadorRegExp = QtGui.QRegExpValidator(registroInternoRegExp, self)
        self.lineEditRegistroInterno.setValidator(validadorRegExp)
        numChasisRegExp = QtCore.QRegExp('[0-9]+')
        validadorRegExp = QtGui.QRegExpValidator(numChasisRegExp, self)
        self.lineEditChasisNro.setValidator(validadorRegExp)

    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        '''
        '''
        self.reject()

    # Se agregan los TextChanged para evitar comprobaciones extensas
    # en la acción Aceptar.
    @QtCore.pyqtSlot('QString')
    def on_lineEditMarca_textChanged(self, cadena):
        self.lineEditMarca.setModified(False)
        if cadena != self.auto.getMarca():
#         if cadena != self._vehiculo.getMarca():
            self.lineEditMarca.setModified(True)

    @QtCore.pyqtSlot('QString')
    def on_lineEditRegistroInterno_textChanged(self, cadena):
        self.lineEditRegistroInterno.setModified(False)
        if cadena != self.auto.getRegistroInterno():
            self.lineEditRegistroInterno.setModified(True)

    @QtCore.pyqtSlot('QString')
    def on_lineEditChasisNro_textChanged(self, cadena):
        self.lineEditChasisNro.setModified(False)
        if cadena != self.auto.getNumeroChasis():
            self.lineEditChasisNro.setModified(True)

    def evaluarCamposIngresados(self):
        if not match('[a-z|A-Z]+', self.lineEditMarca.text()):
            self.mostrarMensaje(self.trUtf8('Debe ingresar la Marca del vehículo.Debe ser un valor alfabético.'),
                                self.trUtf8('Ingresar Marca'))
            self.lineEditMarca.clear()
            self.lineEditMarca.setFocus()
            return
        if not match('[0-9]+', self.lineEditRegistroInterno.text()):
            self.mostrarMensaje(self.trUtf8('Debe ingresar el Registro Interno del vehículo. Debe ser un valor numérico.'),
                                self.trUtf8('Ingresar Registro Interno'))
            self.lineEditRegistroInterno.clear()
            self.lineEditRegistroInterno.setFocus()
            return
        if not match('[0-9]+', self.lineEditChasisNro.text()):
            self.mostrarMensaje(self.trUtf8('Debe ingresar el Número de Chasis del vehículo. Debe ser un valor numérico.'),
                                self.trUtf8('Ingresar Número de Chasis'))
            self.lineEditChasisNro.clear()
            self.lineEditChasisNro.setFocus()
            return
        return True

    @QtCore.pyqtSlot()
    def on_pushButtonAceptar_clicked(self):
        if not (self.lineEditMarca.isModified() or self.lineEditRegistroInterno.isModified() or self.lineEditChasisNro.isModified()):
            self.mostrarMensaje(self.trUtf8(u'No se modificó ningún atributo del vehículo'),
                                self.trUtf8(u'Modificación de Vehículo'))
            return
        else:
            if not self.evaluarCamposIngresados():
                return
            division = Division_Transporte()
            dominio = unicode(self.lineEditDominio.text())
            marca = unicode(self.lineEditMarca.text())
            registroInterno = unicode(self.lineEditRegistroInterno.text())
            nroChasis = unicode(self.lineEditChasisNro.text())
#             # Se le pide a la Division que modifique el informacion del vehiculo.
            division.modificarVehiculo(dominio, marca, registroInterno, nroChasis)

            if self.mostrarMensaje(self.trUtf8('El vehiculo se ha modificado correctamente!!! :)'),
                                   self.trUtf8('Ingresando Vehículo')):
                self.accept()

    '''
    TODO: Este método se repite en varios Dialogs.
    '''
    def mostrarMensaje(self, mensaje, titulo):
        msgBox = QtGui.QMessageBox(self)
        msgBox.setText(mensaje)
        #msgBox.setText(QtCore.QString.fromUtf8(mensaje))
        msgBox.setWindowTitle(titulo)
        #msgBox.setWindowTitle(QtCore.QString.fromUtf8(titulo))
        return msgBox.exec_()
