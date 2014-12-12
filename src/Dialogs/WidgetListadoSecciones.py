# -*- coding: utf-8 -*-
'''
Created on 10/10/2012

@author: urrutia
'''
from PyQt4 import QtGui, QtCore

from formularios.WidgetListadoSecciones2 import Ui_FormListadoSecciones
from formularios.DlgSeleccionarReporteSeccion import Ui_Dialog
from negocio.Division_Transporte import Division_Transporte
from PyQt4.QtGui import QFileDialog
import csv
from Utiles_Dialogo import mostrarMensaje

class ListadoSecciones(QtGui.QWidget, Ui_FormListadoSecciones):
    def __init__(self, parent=None):
        super(ListadoSecciones, self).__init__(parent)
        self.setupUi(self)
        self.tableWidgetListadoSecciones.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
#        self.cargarGrillaInicial()
        self._secciones = Division_Transporte().getSecciones().values()
        self._secciones.sort(cmp=lambda x, y : cmp(x.nombre, y.nombre))
        self.tableWidgetListadoSecciones.cargarConSecciones(self._secciones)
        
#    def seleccionarSeccion(self):
#        print "Click sobre Seleccionar Seccion"
#
#        
#    def cargarGrillaInicial(self):
#        division = Division_Transporte()
#        secciones = division.getSecciones()
#        sec = secciones.values()
#        sec.sort(cmp=lambda x, y : cmp(x.nombre, y.nombre))
#        self.cargarGrillaEmpleadosSinAsignar(sec)
#        
#    def cargarGrillaEmpleadosSinAsignar(self, secciones):
#        fila = 0
#        self.tableWidgetListadoSecciones.clearContents()
#        self.tableWidgetListadoSecciones.setRowCount(len(secciones))
#        for seccion in secciones:
#            columna = 0
#            itemNombre = QtGui.QTableWidgetItem()
#            itemNombre.setText(seccion.nombre)
#            self.tableWidgetListadoSecciones.setItem(fila, columna, itemNombre)
#            columna += 1
#            itemCantidadEmpl = QtGui.QTableWidgetItem()
#            itemCantidadEmpl.setText(unicode(seccion.cantidadEmpleadosTotales()))
#            self.tableWidgetListadoSecciones.setItem(fila, columna, itemCantidadEmpl)
#       
#     columna += 1
#            itemEncargado = QtGui.QTableWidgetItem()
#            itemEncargado.setText(seccion.encargado.nombreCompleto())
#            self.tableWidgetListadoSecciones.setItem(fila, columna, itemEncargado)
#            columna += 1
#            itemCode = QtGui.QTableWidgetItem()
#            itemCode.setText(unicode(seccion.getCodigo()))
#            self.tableWidgetListadoSecciones.setItem(fila, columna, itemCode)
#
#            fila += 1
        
    @QtCore.pyqtSlot()
    def on_pushButtonReparacionesPorSeccion_clicked(self):
        DlgSeleccionarReporte = SeleccionarReporteDeSeccion(self, self._secciones)
        DlgSeleccionarReporte.exec_()
        

class SeleccionarReporteDeSeccion(QtGui.QDialog, Ui_Dialog):
    def __init__(self, parent=None, secciones=None):
        super(SeleccionarReporteDeSeccion, self).__init__(parent)
        self.setupUi(self)
        self._secciones = secciones
    
    def generarReporteCsv(self):
        print 'CSV'
    
        fileDialog = QFileDialog(caption=QtCore.QString.fromUtf8('Guardar Reparaciones por Seccion'))
        filename = fileDialog.getSaveFileName(parent=self)
        filename = '%s.csv'%filename
        with open(filename, 'w') as csvfile:
            fieldnames = ['Codigo de Seccion', 'Nombre de Seccion', 'Encargado', 'Cantidad de empleados', 'Cantidad de reparaciones']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for seccion in self._secciones:
                print seccion.dic_valores_csv()
                writer.writerow(seccion.dic_valores_csv())
                #print seccion.getTurnosTodos()
        self.limpiar_csv(filename)
        mostrarMensaje(self, 'Archivo %s generado con exito!'%filename, 'Reporte csv: Reparaciones por Seccion')
        
    def limpiar_csv(self, filename):
        '''
        Remueve las lineas en blanco que deja el proceso de escritura del archivo
        '''
        arch1 = open(filename, 'rb')
        nametemp = 'temp.csv'
        arch_output = open(nametemp, 'wb')
        writer = csv.writer(arch_output)
        for row in csv.reader(arch1):
            if row:
                writer.writerow(row)
        arch1.close()
        arch_output.close()
        import os
        os.remove(filename)
        os.rename(nametemp, filename)

    def generarReporteTorta(self):
        print 'TORTA'
        import matplotlib.pyplot as plt
        
        # The slices will be ordered and plotted counter-clockwise.
#        labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
        labels = [seccion.getNombre() for seccion in self._secciones]
#        sizes = [15, 30, 45, 10]
        sizes = [seccion.cantidadDeReparaciones() for seccion in self._secciones]
        colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
        colors = colors[:len(sizes)]
        explode = (0, 0.1, 0, 0) # only "explode" the 2nd slice (i.e. 'Hogs')
        explode = explode[:len(sizes)]
        
        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True)#s, startangle=90)
        # Set aspect ratio to be equal so that pie is drawn as a circle.
        plt.axis('equal')
        
        plt.show()    

    def generarAmbos(self):
        self.generarReporteCsv()
        self.generarReporteTorta()
        
    @QtCore.pyqtSlot()
    def on_buttonBox_accepted(self):
        generar = {
                   'ambos': self.generarAmbos,
                   'soloCsv': self.generarReporteCsv,
                   'soloTorta': self.generarReporteTorta
                   }
        if self.checkBoxCsv.isChecked() and self.checkBoxTorta.isChecked():
            generar['ambos']()
            return
        if self.checkBoxCsv.isChecked():
            generar['soloCsv']()
        if self.checkBoxTorta.isChecked():
            generar['soloTorta']()
        
