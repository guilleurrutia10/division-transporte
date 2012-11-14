'''
Created on 10/11/2012

@author: urrutia
'''
from PyQt4 import QtGui, QtCore

from formularios.DialogAltaVehiculo import Ui_DialogAltaVehiculo

class DialogAltaVehiculo(QtGui.QDialog, Ui_DialogAltaVehiculo):
    '''
    classdocs
    '''

    def __init__(self, parent = None):
        '''
        '''
        super(DialogAltaVehiculo, self).__init__(parent)
        self.setupUi(self)
        
        self.lineEditDominio.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('[0-9]+'),self))
        self.connect(self.buttonBox, QtCore.SIGNAL('accepted()'),self.on_buttonBox_accepted)

    def testeo(self):
        msgBox = QtGui.QMessageBox(self)
        msgBox.setText('Error!!!!!!!!!!!!!!')
        msgBox.show()
        self.lineEditDominio.clear()
        self.lineEditDominio.setFocus()
        return
        
#    @QtCore.pyqtSlot()
    def on_buttonBox_accepted(self):
        print 'Click sobre aceptar......................'
        self.testeo()