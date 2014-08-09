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

#global item, x ahora para contener información del vehículo seleccionado.
itemglobal = None


class DialogMostrarLosVehiculosParaModificar(QtGui.QDialog, Ui_DialogMostrarLosVehiculosParaModificar):
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
        self.itemParaModificar = None
        # Se oculta.
        self.miWidget.pushButtonSeleccionar.hide()

    #===========================================================================
    # Tratando de agarrar el evento de Seleccionar un Vehiculos de la grilla
    # y utilizarlo para retomar sus datos de la BD para mostrarlos en el 
    # modificar.
    #===========================================================================
    def seleccionarCelda(self, row, column):
        print row, ',' , column
#        item = QtGui.QTableWidgetItem()
        item = self.miWidget.tableWidgetListadoDeVehiculos.item(row, 0)
        print item.text()
        self.itemParaModificar = item
        global itemglobal
        itemglobal = item
#         dominio = unicode(item.text())
#         vehiculoSeleccionado = Division_Transporte().getVehiculo(dominio)
        vehiculo = self.miWidget.tableWidgetListadoDeVehiculos.getVehiculoSeleccionado()

#     @QtCore.pyqtSlot()
#     def on_pushButtonAceptar_clicked(self):
#         self.accept()
# 
#     @QtCore.pyqtSlot()
#     def on_pushButtonCancelar_clicked(self):
#         '''
#         '''
#         self.reject()

    @QtCore.pyqtSlot()
    def on_pushButtonModificarDatosDeVehiculo_clicked(self):
        '''
        '''
        try:
            global itemglobal
            assert not(itemglobal is None)
        except AssertionError:
            self.mostrarMensaje('Debe seleccionar un Vehículo.', 'Ingresar Vehículo')
            return
        # TODO: Se debe enviar el vehículo a modificar.
        dlgModificar = DialogModificarVehiculo()
        dlgModificar.exec_()
        itemglobal = None
#         self.miWidget.cargarGrilla(Division_Transporte().getVehiculos().values())
        vehiculos = Division_Transporte().getVehiculos().values()
        self.miWidget.tableWidgetListadoDeVehiculos.cargarConVehiculos(vehiculos)
#        self.miWidget.cargarGrillaInicial()

    '''
    TODO: Este método se repite en varios Dialogs.
    '''
    def mostrarMensaje(self, mensaje, titulo):
        msgBox = QtGui.QMessageBox(self)
        msgBox.setText(QtCore.QString.fromUtf8(mensaje))
        msgBox.setWindowTitle(QtCore.QString.fromUtf8(titulo))
        return msgBox.exec_()

    #===========================================================================
    # Evento que se dispara cada vez que el Dialog toma el Foco
    #===========================================================================
    def showEvent(self, e):
        print 'Se tomo el foco', self.isVisible()


class DialogModificarVehiculo(QtGui.QDialog, Ui_DialogModificarVehiculo):
    '''
    classdocs
    '''
    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super(DialogModificarVehiculo, self).__init__(parent)
        self.setupUi(self)
        self.auto = None
        global itemglobal
        self.item = itemglobal
        self.cargarLineEdit()

    def cargarLineEdit(self):
        division = Division_Transporte()
        self.auto = division.getVehiculo(unicode(self.item.text()))

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
            self.mostrarMensaje('Debe ingresar la Marca del vehículo.Debe ser alfabético.', 'Ingresar Marca')
            self.lineEditMarca.clear()
            self.lineEditMarca.setFocus()
            return
        if not match('[0-9]+', self.lineEditRegistroInterno.text()):
            self.mostrarMensaje('Debe ingresar el Registro Interno del vehículo.Debe ser numérico.', 'Ingresar Registro Interno')
            self.lineEditRegistroInterno.clear()
            self.lineEditRegistroInterno.setFocus()
            return
        if not match('[0-9]+', self.lineEditChasisNro.text()):
            self.mostrarMensaje('Debe ingresar el Número de Chasis del vehículo.Debe ser numérico.', 'Ingresar Número de Chasis')
            self.lineEditChasisNro.clear()
            self.lineEditChasisNro.setFocus()
            return
        return True

    # TODO: Falta testear para que no haya campos vacíos
    @QtCore.pyqtSlot()
    def on_pushButtonAceptar_clicked(self):
        # Se comprueba burdamente que los haya cambiado al menos un LineEdit.
        print 'Marca modificado ', self.lineEditMarca.isModified()
        print 'R.I modificado ', self.lineEditRegistroInterno.isModified()
        print 'Chasis modificado ', self.lineEditChasisNro.isModified()
#         if (self.lineEditMarca.text() == self.auto.marca) and (self.lineEditChasisNro.text() == self.auto.numeroChasis) and (self.lineEditRegistroInterno.text() == self.auto.registroInterno):
#             self.mostrarMensaje('No se modificó ningún atributo del vehículo', 'Modificación de Vehículo')
#             return
        if not (self.lineEditMarca.isModified() or self.lineEditRegistroInterno.isModified() or self.lineEditChasisNro.isModified()):
            self.mostrarMensaje('No se modificó ningún atributo del vehículo', 'Modificación de Vehículo')
            return
        else:
            if not self.evaluarCamposIngresados():
                return
            # TODO: es necesario agregar el método modificarVehiculo o se
            # puede realizar el commit acá mismo.
            division = Division_Transporte()
            dominio = unicode(self.lineEditDominio.text())
            marca = unicode(self.lineEditMarca.text())
            registroInterno = unicode(self.lineEditRegistroInterno.text())
            nroChasis = unicode(self.lineEditChasisNro.text())
#             # Se le pide a la Division que modifique el informacion del vehiculo.
            division.modificarVehiculo(dominio, marca, registroInterno, nroChasis)

            if self.mostrarMensaje('El vehiculo se ha modificado correctamente!!! :)', 'Ingresando Vehiculo'):
                self.accept()

    '''
    TODO: Este método se repite en varios Dialogs.
    '''
    def mostrarMensaje(self, mensaje, titulo):
        msgBox = QtGui.QMessageBox(self)
        msgBox.setText(QtCore.QString.fromUtf8(mensaje))
        msgBox.setWindowTitle(QtCore.QString.fromUtf8(titulo))
        return msgBox.exec_()
