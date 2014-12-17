# -*- coding: utf-8 -*-
'''
Created on 13/12/2014

@author: LeoMorales
'''
from PyQt4 import QtCore, QtGui
from formularios.WidgetModificarPersonal import Ui_WidgetModificarPersonal
from DialogModificarPersonal import DialogModificarPersonal
from negocio.Division_Transporte import Division_Transporte

class WidgetModificarPersonal(QtGui.QWidget, Ui_WidgetModificarPersonal):
    '''
    classdocs
    '''

    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super(WidgetModificarPersonal, self).__init__(parent)
        self.setupUi(self)
        self.connect(self.pushButtonModificar, QtCore.SIGNAL("pressed()"), self.abrirDialogModificarPersonal)
        self.connect(self.tableWidgetEmpleados, QtCore.SIGNAL('cellDoubleClicked(int,int)'), self.dobleClick)
        self._empleados = Division_Transporte().getEmpleados().values()
        self.tableWidgetEmpleados.cargarConEmpleadosParaModificar(self._empleados)

    def abrirDialogModificarPersonal(self):
        #Enviarle el empleado al dialogo...
#        print 'DEBUG: Modificar %s'%self.tableWidgetEmpleados.getElementoSeleccionado().nombreCompleto()
        dlgModificarPersonal = DialogModificarPersonal(self, self.tableWidgetEmpleados.getElementoSeleccionado())
        dlgModificarPersonal.exec_()
        #Cuando vuelve actualizamos la tabla
        self._empleados = Division_Transporte().getEmpleados().values()
        self.tableWidgetEmpleados.cargarConEmpleadosParaModificar(self._empleados)

    def dobleClick(self, uno, dos):
        self.abrirDialogModificarPersonal()
        
    @QtCore.pyqtSlot('QString')
    def on_lineEditBuscarNombre_textChanged(self, cadena):
        filtro = unicode(cadena).lower()
        personal = filter(lambda p: filtro in unicode(p.getDocumento()).lower()
                          or filtro in unicode(p.getNombre()).lower()
                          or filtro in unicode(p.getApellido()).lower()
                          or filtro in unicode(p.getEmail()).lower()
                          or filtro in unicode(p.getTelefono()).lower(),
                          self._empleados)
        personal.sort(cmp=lambda x, y: cmp(x, y))
        #self.cargarGrillaEmpleadosSinAsignar(personal)
        self.tableWidgetEmpleados.cargarConEmpleadosParaModificar(personal)
