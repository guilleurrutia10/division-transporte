#encoding: utf-8
'''
Created on 07/12/2014

@author: Usuario
'''

from PyQt4 import QtCore, QtGui
from datetime import date

from formularios.DialogoSeleccionarDiaAgenda import Ui_DialogAgendaDeSeccion
from formularios.DialogMostrarReportesAgendaPorRango import Ui_DialogMostrarReportesAgendaPorRango
from AyudaManejador import AyudaManejador
from negocio.Division_Transporte import Division_Transporte
from reportes import generarAgendaParaUnDia, generarAgendaParaRangoDias
from Utiles_Dialogo import compara_fechas_en_cadenas, mostrarMensaje, seleccionarCarpeta


class DialogoAgendaDeSeccion(QtGui.QDialog, Ui_DialogAgendaDeSeccion, AyudaManejador):
    '''
    Atributos:
        - self.dateEdit_Desde
        - self.dateEdit_Hasta
        - self.label_Desde
        - self.label_Hasta
        - self.checkBox_porRango
        - self.buttonBox
    '''
    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super(DialogoAgendaDeSeccion, self).__init__(parent)
        self.setupUi(self)
#         self.buttonBox.connect(self, QtCore.SIGNAL('accepted()'), self.aceptar)
        self.buttonBox.connect(self, QtCore.SIGNAL('rejected()'), self.cancelar)
        #self.checkBox_porRango.connect(self, QtCore.SIGNAL('toggled(bool)'), self.cambioEstadoCheckBox)
        QtCore.QObject.connect(self.checkBox_porRango, QtCore.SIGNAL("toggled(bool)"), self.cambioEstadoCheckBox)
        self._usuario = self.parent().usuario
        self._seccion = filter(lambda seccion: self._usuario.esJefeDeSeccion(seccion), Division_Transporte().getSecciones().values())
        self._seccion = self._seccion[0]

        hoy = date.today()
        self.dateEdit_Hasta.setDate((QtCore.QDate(hoy.year, hoy.month, hoy.day)))
        self.dateEdit_Hasta.setVisible(False)
        button = self.buttonBox.button(self.buttonBox.Ok)

    @QtCore.pyqtSlot()
#     def aceptar(self):
    def on_buttonBox_accepted(self):
        '''
        '''
        desde = self.dateEdit_Desde.date()
        hasta = self.dateEdit_Hasta.date()
        desde = '%s/%s/%s' % (desde.day(), desde.month(), desde.year())
        hasta = '%s/%s/%s' % (hasta.day(), hasta.month(), hasta.year())

        folder = seleccionarCarpeta(self)
        if not folder:
            mostrarMensaje(self, "Por favor, seleccione una carpeta de destino para generar los pdfs", 'Error al seleccionar carpeta destino')
            return
        if self.checkBox_porRango.isChecked():
            if (compara_fechas_en_cadenas(desde, hasta) == -1):# Solo si desde es menor que hasta
                self.generarAgendaParaRangoDias(desde, hasta, folder)
            else:
                mostrarMensaje(self, "Por favor, seleccione fecha desde menor que fecha hasta", 'Error al seleccionar fechas')
                return
        else:
            hasta = None
            generarAgendaParaUnDia(self._seccion, desde, folder)

    @QtCore.pyqtSlot()
    def cancelar(self):
        '''
        '''
        pass

    # @QtCore.pyqtSlot()
    def cambioEstadoCheckBox(self):
        if self.checkBox_porRango.isChecked():
            self.label_Desde.setText(QtGui.QApplication.translate("DialogAgendaDeSeccion", "Desde:", None, QtGui.QApplication.UnicodeUTF8))
            self.label_Hasta.setText(QtGui.QApplication.translate("DialogAgendaDeSeccion", "Hasta:", None, QtGui.QApplication.UnicodeUTF8))
            self.dateEdit_Hasta.setVisible(True)
            self.dateEdit_Hasta.setEnabled(True)
        else:
            self.label_Desde.setText(QtGui.QApplication.translate("DialogAgendaDeSeccion", "Día:", None, QtGui.QApplication.UnicodeUTF8))
            self.label_Hasta.setText(QtGui.QApplication.translate("DialogAgendaDeSeccion", "", None, QtGui.QApplication.UnicodeUTF8))
            self.dateEdit_Hasta.setEnabled(False)
            self.dateEdit_Hasta.setVisible(False)

    def generarAgendaParaRangoDias(self, desde, hasta, folder):
        reportes_generados = generarAgendaParaRangoDias(self._seccion, desde, hasta, folder)
        dlg_progreso_reportes = DialogMostrarReportesAgendaPorRango(self._seccion.getNombre(), reportes_generados)
        dlg_progreso_reportes.exec_()


class DialogMostrarReportesAgendaPorRango(QtGui.QDialog, Ui_DialogMostrarReportesAgendaPorRango, AyudaManejador):

    def __init__(self, nombreSeccion, reportes, parent=None):
        super(DialogMostrarReportesAgendaPorRango, self).__init__(parent)
        self.setupUi(self)
        self.reportes = reportes
        self.nombreSeccion = nombreSeccion
        self.run()

    def run(self):
        self.label.setText(self.label.text()+QtCore.QString(self.nombreSeccion))
        for reporte in self.reportes:
            item = QtGui.QListWidgetItem(reporte)
            self.listWidget_reportes.addItem(item)
            self.pushButton_aceptar

    @QtCore.pyqtSlot()
    def on_pushButton_aceptar_clicked(self):
        self.accept()
