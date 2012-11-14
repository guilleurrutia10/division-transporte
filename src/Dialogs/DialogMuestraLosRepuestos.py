# -*- coding: utf-8 -*-
'''
Created on 31/10/2012

@author: alum
'''

from PyQt4 import QtCore, QtGui
from formularios.DialogMuestraLosRepuestos import Ui_Dialog

class DialogMuestraLosRepuestos(QtGui.QDialog, Ui_Dialog):
    '''
    classdocs
    '''
    def __init__(self, parent = None):
        '''
        Constructor
        '''
        super(DialogMuestraLosRepuestos, self).__init__(parent)
        self.setupUi(self)
        self.lineEditBuscarNombre
    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        self.close()
        
    @QtCore.pyqtSlot('QString')
    def on_lineEditBuscarNombre_textChanged(self, cadena):
        print 'Filtrar %s' %cadena
        #refrescar Grilla