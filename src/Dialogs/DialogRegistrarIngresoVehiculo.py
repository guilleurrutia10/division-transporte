# -*- coding: utf-8 -*-
'''
Created on 03/11/2012

@author: urrutia
'''

from PyQt4 import QtCore, QtGui
from re import match

from formularios.DialogRegistrarIngresoVehiculo import Ui_DialogRegistrarIngresoVehiculo
from formularios.DialogDatosIngresoVehiculo import Ui_DialogIngresoVehiculo 
import WidgetListadoDeVehiculos

from negocio.Division_Transporte import Division_Transporte
from excepciones.ExcepcionPoseeOrdenReparacionEnCurso import ExcepcionPoseeOrdenReparacionEnCurso

global itemglobal
itemglobal = None

class DialogRegistrarIngresoVehiculo(QtGui.QDialog, Ui_DialogRegistrarIngresoVehiculo):
    '''
    classdocs
    @version: 
    @author: 
    '''
    
    def __init__(self, parent = None):
        '''
        Constructor
        @version: 
        @author: 
        '''
        super(DialogRegistrarIngresoVehiculo, self).__init__(parent)
        self.setupUi(self)
        self.miWidget = WidgetListadoDeVehiculos.ListadoVehiculos(self.widget)
        self.miWidget.connect(self.miWidget.tableWidgetListadoDeVehiculos, QtCore.SIGNAL('cellClicked(int,int)'), self.seleccionarCelda)
        self.miWidget.connect(self.miWidget.tableWidgetListadoDeVehiculos, QtCore.SIGNAL('cellEntered(int,int)'), self.seleccionarCelda)
        self.miWidget.connect(self.miWidget.tableWidgetListadoDeVehiculos, QtCore.SIGNAL('cellPressed(int,int)'), self.seleccionarCelda)
        
    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        '''
        @version: 
        @author: 
        '''
        self.reject()
        
    @QtCore.pyqtSlot()
    def on_pushButtonAceptar_clicked(self):
        '''
        @version: 
        @author: 
        '''
        print 'Click sobre aceptar'
        self.accept()
    
    @QtCore.pyqtSlot()
    def on_pushButtonRegistrarNuevoIngreso_clicked(self):
        '''
        @version: 
        @author: 
        '''
        '''
        TODO: Obtener algún indicio de que el vehiculo seleccionado tiene Orden de
        Reparacion en Curso.
        '''
        if itemglobal:
            dlgDatosIngreso = DialogDatosIngresoVehiculo()
            dlgDatosIngreso.exec_()
        else:
            self.mostrarMensaje('Debe seleccionar un Vehiculo.', 'Seleccionar Vehiculo')
        
    def seleccionarCelda(self, fila, columna):
        itemVehiculo = self.miWidget.tableWidgetListadoDeVehiculos.item(fila, 0)
        global itemglobal
        itemglobal = itemVehiculo
        
    '''
    TODO: Este método se repite en varios Dialogs.
    '''
    def mostrarMensaje(self, mensaje, titulo):
        msgBox = QtGui.QMessageBox(self)
        msgBox.setText(QtCore.QString.fromUtf8(mensaje))
        msgBox.setWindowTitle(QtCore.QString.fromUtf8(titulo))
        return msgBox.exec_()
        
class DialogDatosIngresoVehiculo(QtGui.QDialog, Ui_DialogIngresoVehiculo):
    '''
    classdocs
    @version: 
    @author: 
    '''
    
    def __init__(self, parent = None):
        '''
        Constructor
        @version: 
        @author: 
        '''
        super(DialogDatosIngresoVehiculo, self).__init__(parent)
        self.setupUi(self)
        self.validacionesLineEdit()
        cadena = self.lineEditKilometraje.validator().regExp()
        print cadena.pattern()
#        QtCore.QRegExp.pattern()
        
    #Validación a medida que se escribe en el lineEdit
    def validacionesLineEdit(self):
        self.lineEditKilometraje.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[0-9]+'),self))
        self.lineEditCombustible.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[0-9]+'),self))
        self.lineEditEquipamiento.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[a-zA-Z]+'),self))
        self.lineEditReparacion.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[a-zA-Z]+'),self))
        self.lineEditComisaria.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[a-zA-Z]+'),self))
        self.lineEditLocalidad.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[a-zA-Z]+'),self))
            
    @QtCore.pyqtSlot()
    def on_pushButtonAceptar_clicked(self):
        '''
        @version: 
        @author: 
        '''
        print 'Click sobre aceptar'
        global itemglobal
        print itemglobal.text()
        try:
            assert self.testearDialogo() is True
            self.registrarIngresoVehiculo()
            print 'Imprimiendo Orden-......'
            self.mostrarMensaje('Orden de Reparación Creada. :)', 'Creando Orden de Reparación')
            self.accept()
        except AssertionError:
            return
        except ExcepcionPoseeOrdenReparacionEnCurso, e:
            self.mostrarMensaje(e.getMensaje(), 'ERROR!')
            self.reject()
    
    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        '''
        @version: 
        @author: 
        '''
        self.reject()
    
    def registrarIngresoVehiculo(self):
        dominio = unicode(itemglobal.text())
        division = Division_Transporte()
        vehiculo = division.getVehiculo(dominio)
        
        kilometrajeActual = unicode(self.lineEditKilometraje.text())
        combustibleActual = unicode(self.lineEditCombustible.text())
        equipamiento = unicode(self.lineEditEquipamiento.text())
        reparacion = unicode(self.lineEditReparacion.text())
        comisaria = unicode(self.lineEditComisaria.text())
        localidad = unicode(self.lineEditLocalidad.text())
        
        division.registrarIngresoDeVehiculo(vehiculo.dominio, kilometrajeActual, combustibleActual, equipamiento, reparacion, comisaria, localidad)
        
    def testearDialogo(self):
        if not match('[0-9]+', self.lineEditKilometraje.text()):
            self.mostrarMensaje('Debe ingresar el kilometraje.', 'Ingresar Kilometraje')
            self.lineEditKilometraje.clear()
            self.lineEditKilometraje.setFocus()
            return
        if not match('[0-9]+', self.lineEditCombustible.text()):
            self.mostrarMensaje('Debe ingresar el Combustible','Ingresar Combustible' )
            self.lineEditCombustible.clear()
            self.lineEditCombustible.setFocus()
            return
        if not match('[a-zA-Z]+', self.lineEditReparacion.text()):
            self.mostrarMensaje('Debe ingresar la reparacion solicitada', 'Ingresar reparacion')
            self.lineEditReparacion.clear()
            self.lineEditReparacion.setFocus()
        if not match('[a-zA-Z]+', self.lineEditComisaria.text()):
            self.mostrarMensaje('Debe ingresar la Comisaria solicitada', 'Ingresar Comisaria')
            self.lineEditComisaria.clear()
            self.lineEditComisaria.setFocus()
        if not match('[a-zA-Z]+', self.lineEditLocalidad.text()):
            self.mostrarMensaje('Debe ingresar la Localidad solicitada', 'Ingresar Localidad')
            self.lineEditLocalidad.clear()
            self.lineEditLocalidad.setFocus()
        return True
            
    '''
    TODO: Este método se repite en varios Dialogs.
    '''
    def mostrarMensaje(self, mensaje, titulo):
        msgBox = QtGui.QMessageBox(self)
        msgBox.setText(QtCore.QString.fromUtf8(mensaje))
        msgBox.setWindowTitle(QtCore.QString.fromUtf8(titulo))
        return msgBox.exec_()