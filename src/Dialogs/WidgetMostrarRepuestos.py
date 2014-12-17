# -*- coding: utf-8 -*-
'''
Created on 03/10/2012

@author: Usuario
'''
from PyQt4 import QtCore, QtGui

from formularios.WidgetMostrarRepuestos import Ui_FormMostrarRepuestos
from formularios.DialogModificarRepuesto import Ui_DialogMoficarRepuesto

from Utiles_Dialogo import mostrarMensajeOk
from negocio.Division_Transporte import Division_Transporte

class DialogModificarRepuesto(QtGui.QDialog, Ui_DialogMoficarRepuesto):
    '''
    classdocs
    '''
    def __init__(self, tipoRepuesto, parent = None):
        '''
        Constructor
        '''
        super(DialogModificarRepuesto, self).__init__(parent)
        self.setupUi(self)
        self.cargarDatosTipoRepuesto(tipoRepuesto)
        for label in self.findChildren(QtGui.QLabel):
            label.setObjectName('label')

    def cargarDatosTipoRepuesto(self, tipoRepuesto):
        self.lineEditCodigo.setModified(False)
        self.lineEditCodigo.setText(tipoRepuesto.getCodigo())
        self.lineEditNombreRepuesto.setText(tipoRepuesto.getNombre())
        self.plainTextEditDescripcion.setPlainText(tipoRepuesto.getDescripcion())
        
        
    @QtCore.pyqtSlot()
    def on_pushButtonAceptar_clicked(self):
        codigo = unicode(self.lineEditCodigo.text())
        nombre = unicode(self.lineEditNombreRepuesto.text())
        descripcion = unicode(self.plainTextEditDescripcion.toPlainText())
        Division_Transporte().modificarRepuesto(codigo, nombre, descripcion)
        mostrarMensajeOk(self, 'El repuesto ha sido modificado exitosamente', 'Tipo de Repuesto')
        self.accept()


class WidgetMostrarRepuestos(QtGui.QWidget, Ui_FormMostrarRepuestos):
    '''
    classdocs
    '''


    def __init__(self, parent = None):
        '''
        Constructor
        '''
        super(WidgetMostrarRepuestos, self).__init__(parent)
        self.setupUi(self)
        self.connect(self.pushButtonModificarRepuesto, QtCore.SIGNAL("pressed()"), self.abrirDialogModificarRepuesto)
        
    def abrirDialogModificarRepuesto(self):
        dlgModificarRepuesto= DialogModificarRepuesto(self)
        dlgModificarRepuesto.exec_()