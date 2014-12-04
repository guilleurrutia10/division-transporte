# -*- coding: utf-8 -*-
'''
Created on 13/11/2012

@author: urrutia
'''

from PyQt4 import QtCore, QtGui

from formularios.DialogCambiarDeSeccionUnEmpleado import Ui_DialogCambiarDeSeccionUnEmpleado
from formularios.DialogSeleccionarSeccionParaCambiarEmpleado import Ui_DialogSeleccionarUnaSeccion
from negocio.Division_Transporte import Division_Transporte
from Utiles_Dialogo import mostrarMensajeParaConfirmar


class DialogCambiardeSeccionunEmpleado(QtGui.QDialog, Ui_DialogCambiarDeSeccionUnEmpleado):
    '''
        dialogo para cambiar de seccion a un empleado de la Division.
    '''
    def __init__(self, parent = None):
        '''
        El dialogo posee:
            - lineEditFiltro
            - pushButtonFiltrar
            - pushButtonCambiar
            - tableWidgetEmpleados
            - pushButtonAceptar y pushButtonCancelar
        '''
        super(DialogCambiardeSeccionunEmpleado, self).__init__(parent)
        self.setupUi(self)
        self.cargarListaDeEmpleados()
        #Debo conectar los signals de la tabla:
        #self.tableWidgetEmpleados.conectarSignals()
        
    
        
    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        self.reject()
    
    @QtCore.pyqtSlot()
    def on_pushButtonCambiar_clicked(self):
        #Paso1: Recuperar el empleado que se quiere cambiar de Seccion:
        empleado_a_cambiar = self.tableWidgetEmpleados.getEmpleadoSeleccionado()
        #print 'Empleado a cambiar: %s' %(empleado_a_cambiar.quienSos())
        #Paso2: Recuperar todas las Secciones, menos en la que esté actualmente el empleado que se quiere cambiar.
        secciones_disponibles = Division_Transporte().getSeccionesParaCambiarEmpleado(empleado_a_cambiar) #print 'secciones totales: %d, \nsecciones disponibles: %d' %(len(Division_Transporte().getSecciones().values()),len(secciones_disponibles)) 
        #Paso3: Mostrar un Dialoguito ofreciendoles al usuario las secciones para que elija una...
        dialog = DialogSeleccionarSeccionParaCambiarEmpleado(secciones_disponibles, self)
        
        if dialog.exec_() == QtGui.QDialog.Accepted:
            msj = 'El empleado %s sera tranferido de la Seccion: %s a la Seccion: %s' %(empleado_a_cambiar.nombreCompleto(), Division_Transporte().getSeccionDeEmpleado(empleado_a_cambiar).getNombre(), dialog.getSeccion_Seleccionada().getNombre())
            #if mostrarMensajeParaConfirmar(self, msj, 'Tranferir empleado') == QtGui.QMessageBox.Accepted:
            if mostrarMensajeParaConfirmar(self, msj, 'Tranferir empleado') == 'Ok':
                #TODO: Paso4: Cambiar de seccion al empleado:
                print 'El usuario eligio esta Seccion: %s' %(dialog.getSeccion_Seleccionada())
                Division_Transporte().cambiarDeSeccionAEmpleado(empleado_a_cambiar, dialog.getSeccion_Seleccionada())
                seccc = dialog.getSeccion_Seleccionada() #Para debbugear...
                self.accept()
            else:
                print 'Anda el Rejected!!!!!'

        
    def cargarListaDeEmpleados(self):
        lista_de_secciones = Division_Transporte().getSeccionesQuePuedenTransferir()
        self.tableWidgetEmpleados.cargarConEmpleadosDeSecciones(lista_de_secciones)
        
        
class DialogSeleccionarSeccionParaCambiarEmpleado(QtGui.QDialog, Ui_DialogSeleccionarUnaSeccion):      
    '''
        dialogo para selccionar una seccion para transferir a un empleado de la Division.
    '''
    def __init__(self, secciones, parent = None):
        '''
        El dialogo posee:
            - lineEditFiltro
            - pushButtonFiltrar
            - pushButtonSeleccionar
            - tableWidgetSecciones --> de tipo TablaSecciones!
            - pushButtonCancelar
            
        Vars:
            - seccion_seleccionada
        '''
        super(DialogSeleccionarSeccionParaCambiarEmpleado, self).__init__(parent)
        self.setupUi(self)
        self.tableWidgetSecciones.cargarConSecciones(secciones)
        self.seccion_seleccionada = None
        
    def on_pushButtonSeleccionar_clicked(self):
        #Paso1: Recuperar la Seccion seleccionada:
        self.seccion_seleccionada = self.tableWidgetSecciones.getElementoSeleccionado() #print 'Seccion seleccionada: %s' %(self.seccion_seleccionada.getNombre())
    
    def getSeccion_Seleccionada(self):
        return self.seccion_seleccionada
    
