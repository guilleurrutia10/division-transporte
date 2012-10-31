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