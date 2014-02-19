'''
Created on 11/02/2014

@author: LeoMorales
'''
from PyQt4 import QtGui

from formularios.FormContrasenaEncargado import Ui_DialogCrearUsuarioEncargado

class DialogCrearUsuarioEncargado(QtGui.QDialog, Ui_DialogCrearUsuarioEncargado):
    
    '''
        Dialogo para pedirle al empleado administrativo la contrasena para crearle un Usuario al Empleado asignado
        como encargado de una Seccion.
    '''
    def __init__(self, nombreUsr, parent=None):
        '''
        Constructor
        '''
        super(DialogCrearUsuarioEncargado, self).__init__(parent)
        self.setupUi(self)
        self.label_nombreUsrEncargado.setText(nombreUsr)
        
    def getPassEncargado(self):
        return unicode(self.linePassword.text())

if __name__ == '__main__':        
    print 'Hola'
    dialoguito = DialogCrearUsuarioEncargado()