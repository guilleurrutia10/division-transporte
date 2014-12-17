# -*- coding: utf-8 -*-
'''
Created on 03/10/2012

@author: Usuario
'''
from PyQt4 import QtCore, QtGui

from formularios.DialogModificarPersonal import Ui_DialogModificarPersonal
from negocio.Division_Transporte import Division_Transporte
from Utiles_Dialogo import MensajeCritico, mostrarMensaje
from negocio.excepciones.ExcepcionObjetoExiste import ExcepcionObjetoExiste

class DialogModificarPersonal(QtGui.QDialog, Ui_DialogModificarPersonal):
    '''
    classdocs
    Elementos:
        - lineEditNombre
        - lineEditApellido
        - comboBoxTipoDocumento
        - lineEditNroDocumento
        - dateEditFechaNacimiento
        - lineEditDomicilio
        - lineEditTelefono
        - lineEditEmail
        - pushButtonAceptar
        - pushButtonCancelar
    '''
    def __init__(self, parent=None, empleado_a_modificar=None):
        '''
        Constructor
        '''
        super(DialogModificarPersonal, self).__init__(parent)
        self.setupUi(self)
        self._empleado = empleado_a_modificar
#        print 'DEBUG Debo Modificar Empleado %s'%self._empleado.nombreCompleto()
        #Guardamos los QDAtos para utilizar luego sus metodos de comparacion y saber si han sido modificados
        self.qDatosEmpleado= {'nombre':QtCore.QString(self._empleado.getNombre()),
                              'apellido':QtCore.QString(self._empleado.getApellido()),
                              'nrodocumento':QtCore.QString(self._empleado.getDocumento()),
                              'fechanacimiento': QtCore.QDate(self._empleado.getFechaNacimiento())
                              }
        self.lineEditNombre.setText(self.qDatosEmpleado['nombre'])
        self.lineEditApellido.setText(self.qDatosEmpleado['apellido'])
        self.lineEditNroDocumento.setText(self.qDatosEmpleado['nrodocumento'])
        self.dateEditFechaNacimiento.setDate(self.qDatosEmpleado['fechanacimiento'])
        textodomicilio = self._empleado.getDomicilio() 
        if not textodomicilio: textodomicilio = '-'
        self.qDatosEmpleado.update({'domicilio':QtCore.QString(textodomicilio)})
        self.lineEditDomicilio.setText(self.qDatosEmpleado['domicilio'])
        textoemail = unicode(self._empleado.getEmail())
        if not textoemail: textoemail = '-'
        self.qDatosEmpleado.update({'email':QtCore.QString(textoemail)})
        self.lineEditEmail.setText(self.qDatosEmpleado['email'])
        textotelefono = self._empleado.getTelefono()
        if not textotelefono: textotelefono = '-'
        self.qDatosEmpleado.update({'telefono':QtCore.QString(textotelefono)})
        self.lineEditTelefono.setText(self.qDatosEmpleado['telefono'])
        self.comboBoxTipoDocumento.clear()
        currentItem= 0
        for index, tipodocumento in enumerate(Division_Transporte().getTipoDeDocumentos()):
            item = QtCore.QStringList(tipodocumento)
            if self._empleado.getTipoDocumento().get_codigo_tipo_documento() == tipodocumento: currentItem = index 
            self.comboBoxTipoDocumento.addItems(item)
#        print 'DEBUG: Current index %d'%currentItem
        self.qDatosEmpleado.update({'tipodocumento':currentItem})
        self.comboBoxTipoDocumento.setCurrentIndex(currentItem)
        
    @QtCore.pyqtSlot()
    def on_pushButtonAceptar_clicked(self):
        if not self.seActualizoAlgunValor():
            msg = 'Ningun datos del empleado \'%s\' han sido modificado' %self._empleado.nombreCompleto()
            mostrarMensaje(self, msg, 'No actualizar')
            self.reject()
            return

        msjConfirmar = MensajeCritico(self, 'Confirma los cambios realizados?', 'Confirmar cambios')
        respuesta = msjConfirmar.exec_()
        if respuesta == QtGui.QMessageBox.Cancel:
#            print "DEBUG: Cancelar accion"
            self.reject()
        if respuesta == QtGui.QMessageBox.Ok:
            try:
                Division_Transporte().modificarEmpleado(self._empleado, self.getValoresActualizados())
                msg = 'Los datos del empleado \'%s\' han sido actualizados' %self._empleado.nombreCompleto()
                mostrarMensaje(self, msg, 'Operacion exitosa!')
                self.accept()
            except ExcepcionObjetoExiste:
                mostrarMensaje(self, 'Ya existe un empleado con los datos ingresados.\nNo se van a actualizar los datos', 'No se pueden actualizar los datos')
                return

    def seActualizoAlgunValor(self):
        '''
        Devuelve True si algun valor fue modificado
        '''
        #Lo siguiente es para legibilidad:
        valores = []
        valores.append(self.qDatosEmpleado['nombre'] != self.lineEditNombre.text())
        valores.append(self.qDatosEmpleado['apellido'] != self.lineEditApellido.text())
        valores.append(self.qDatosEmpleado['domicilio'] != self.lineEditDomicilio.text())
        valores.append(self.qDatosEmpleado['email'] != self.lineEditEmail.text())
        valores.append(self.qDatosEmpleado['nrodocumento'] != self.lineEditNroDocumento.text())
        valores.append(self.qDatosEmpleado['telefono'] != self.lineEditTelefono.text())
        valores.append(self.qDatosEmpleado['fechanacimiento'] != self.dateEditFechaNacimiento.date())
        valores.append(self.qDatosEmpleado['tipodocumento'] != self.comboBoxTipoDocumento.currentIndex())
        return True in valores 
                
    def getValoresActualizados(self):
        return {'nombre': unicode(self.lineEditNombre.text()),
                'apellido':unicode(self.lineEditApellido.text()),
                'nrodocumento': unicode(self.lineEditNroDocumento.text()),
                'tipodocumento': unicode(self.comboBoxTipoDocumento.currentText()),
                'fechanacimiento':self.dateEditFechaNacimiento.date().toPyDate(),
                'domicilio': unicode(self.lineEditDomicilio.text()),
                'telefono': unicode(self.lineEditTelefono.text()),
                'email':unicode(self.lineEditEmail.text())
                } 

    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        '''
        '''
        self.reject()
