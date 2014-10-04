'''
Created on 11/02/2014

@author: LeoMorales

USO:

        dialog = DialogCrearUsuarioEncargado("NOMBRE DE ENCARGADO!")
        while True:
            if dialog.exec_() == QtGui.QDialog.Accepted:
                if dialog.contrasenasValidas():
                    self._encargado.setPassword(dialog.getPassEncargado())
                    break
                else:
                    dialog.preparar_para_volver_a_pedir()
            else:
                #Salio por reject
                break

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
        return unicode(self.lineEditPassword.text())

#    @QtCore.pyqtSlot()
#    def on_pushButtonOk_clicked(self):
#        #comparar contrasenas:
#        print self.lineEditPassword.text(), ' == ', self.lineEditPassword2.text(), '?'
#        while self.lineEditPassword.text() != self.lineEditPassword2.text(): 
#            self.labelMsgError.setText("Las claves no coinciden, ingrese nuevamente")
#            self.lineEditPassword.setFocus()
#        self.accept()

    def contrasenasValidas(self):
        return unicode(self.lineEditPassword.text()) == unicode(self.lineEditPassword2.text())
    
    def preparar_para_volver_a_pedir(self, mensaje= "Las claves no coinciden, ingrese nuevamente"):
        self.lineEditPassword.clear()
        self.lineEditPassword2.clear()
        self.lineEditPassword.setFocus()
        self.labelMsgError.setText(mensaje)

if __name__ == '__main__':        
    print 'Hola'
    dialoguito = DialogCrearUsuarioEncargado("Juan")
    dialoguito.exec_()
    