'''
Created on 03/11/2012

@author: urrutia
'''

from PyQt4 import QtCore, QtGui
from formularios.DialogAsignarReparacion import Ui_DialogAsignarReparacion

class DialogAsignarReparacion(QtGui.QDialog, Ui_DialogAsignarReparacion):
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
        super(DialogAsignarReparacion, self).__init__(parent)
        self.setupUi(self)
        
    @QtCore.pyqtSlot()
    def on_pushButton_Cancelar_clicked(self):
        '''
        @version: 
        @author: 
        '''
        self.close()