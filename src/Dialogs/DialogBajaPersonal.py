# -*- coding: utf-8 -*-
'''
Created on 22/11/2012

@author: urrutia
'''

from PyQt4 import QtCore, QtGui

from formularios.DialogBajaPersonal import Ui_DialogBajaPersonal
from formularios.DialogAsignarFechaDeBaja import Ui_DialogAsignarFechaBaja
from negocio.Division_Transporte import Division_Transporte

class DialogBajaPersonal(QtGui.QDialog, Ui_DialogBajaPersonal):
    '''
    classdocs
    '''
    def __init__(self, parent = None):
        '''
        Constructor
        '''
        super(DialogBajaPersonal, self).__init__(parent)
        self.setupUi(self)
        #Variable para mantener una lista con los empleados y evitar la consulta
        #continua a la BD.
        self.empleados = None
        self.cargaGrillaInicial()
        self.tableWidgetDatosEmpleados.connect(self.tableWidgetDatosEmpleados, QtCore.SIGNAL('cellClicked(int,int)'), self.celdaClickeada)
        
        
    def cargaGrillaInicial(self):
        print 'Cargar Grilla'
        division = Division_Transporte()
        personal = division.getEmpleadosSinAsignar()
        self.empleados = personal.values()
        self.empleados.sort(cmp=lambda x,y : cmp(x.nombre, y.nombre))
        self.cargarGrilla(self.empleados)
        
    def cargarGrilla(self, empleados):
        self.tableWidgetDatosEmpleados.clearContents()
        self.tableWidgetDatosEmpleados.setRowCount(len(empleados))
        fila = 0
        for empleado in empleados:
            columna = 0
            miItem1 = QtGui.QTableWidgetItem()
            miItem1.setText(empleado.nombre)
            self.tableWidgetDatosEmpleados.setItem(fila,columna,miItem1)
            columna += 1
            miItem2 = QtGui.QTableWidgetItem()
            miItem2.setText(empleado.apellido)
            self.tableWidgetDatosEmpleados.setItem(fila,columna,miItem2)
            columna += 1
            miItem3 = QtGui.QTableWidgetItem()
            miItem3.setText(empleado.tipoDocumento.get_codigo_tipo_documento())
            self.tableWidgetDatosEmpleados.setItem(fila,columna,miItem3)
            columna += 1
            miItem4 = QtGui.QTableWidgetItem()
            miItem4.setText(empleado.documento)
            self.tableWidgetDatosEmpleados.setItem(fila,columna,miItem4)
        
    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        '''
        '''
        self.close()
        
    @QtCore.pyqtSlot()
    def on_pushButtonDarDeBaja_clicked(self):
        '''
        '''
        dlgAsignarFecha = DialogAsignarFechaDeBaja()
        dlgAsignarFecha.exec_()
    
    @QtCore.pyqtSlot('QString')
    def on_lineEditBuscarNombre_textChanged(self, cadena):
        '''
        '''    
        filtro = unicode(cadena)
        values = self.empleados
        personal = filter(lambda p: unicode.lower(filtro) in unicode.lower(unicode(p.nombre)), values)
        personal.sort(cmp=lambda x,y : cmp(x.nombre, y.nombre))
        self.cargarGrilla(personal)
        
    @QtCore.pyqtSlot('QString')
    def on_lineEditBuscarDocumento_textChanged(self, cadena):
        '''
        '''    
        filtro = unicode(cadena)
        values = self.empleados
        personal = filter(lambda p: unicode.lower(filtro) in unicode.lower(unicode(p.documento)), values)
        personal.sort(cmp=lambda x,y : cmp(x.documento, y.documento))
        self.cargarGrilla(personal)
        
    def celdaClickeada(self, fila, columna):
        print 'Celda clickeada fila %s columna %s' %(fila,columna)
        
class DialogAsignarFechaDeBaja(QtGui.QDialog, Ui_DialogAsignarFechaBaja):
    '''
    classdocs
    '''
    def __init__(self, parent = None):
        '''
        Constructor
        '''
        super(DialogAsignarFechaDeBaja, self).__init__(parent)
        self.setupUi(self)
        
    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        '''
        '''
        self.close()
        
    @QtCore.pyqtSlot()
    def on_pushButtonAceptar_clicked(self):
        '''
        '''
        print 'Click sobre Aceptar'