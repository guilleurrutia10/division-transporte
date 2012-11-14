# -*- coding: utf-8 -*-
'''
Created on 03/10/2012

@author: Usuario
'''
from PyQt4 import QtCore, QtGui

from re import match

from formularios.DialogAltaRepuesto import Ui_DialogAltaRepuesto


class DialogAltaRepuesto(QtGui.QDialog, Ui_DialogAltaRepuesto):
    '''
    classdocs
    '''
    def __init__(self, parent = None):
        '''
        Constructor
        '''
        super(DialogAltaRepuesto, self).__init__(parent)
        self.setupUi(self)
        self.pushButtonCancelar
        
        #Validación a medida que se escribe en el lineEdit        
        self.lineEditDescRepuesto.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[A-Za-z]+'),self))
        self.lineEditNombreRepuesto.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[A-Za-z]+'),self))
        
        
    @QtCore.pyqtSlot('QString')
    def on_lineEditNombreRepuesto_textEdited(self, cadena):
        print 'El texto cambio................... %s' %cadena
    
    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        self.close()    
    
    @QtCore.pyqtSlot()
    def on_pushButtonAceptar_accepted(self):
        print 'Click sobre Aceptar'
        if not match('', self.lineEditDescRepuesto.text()):
            descripcion = unicode(self.lineEditDescRepuesto.text())
        else:
            msgBox = QtGui.QMessageBox(self)
            msgBox.setText('Debe ingresar la descripcion del repuesto.')
            msgBox.show()
            self.lineEditDescRepuesto.clear()
            self.lineEditDescRepuesto.setFocus()