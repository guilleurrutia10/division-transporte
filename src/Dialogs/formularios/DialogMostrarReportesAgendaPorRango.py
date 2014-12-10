# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/DialogMostrarReportesAgendaPorRango.ui'
#
# Created: Tue Dec  9 22:46:32 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DialogMostrarReportesAgendaPorRango(object):
    def setupUi(self, DialogMostrarReportesAgendaPorRango):
        DialogMostrarReportesAgendaPorRango.setObjectName(_fromUtf8("DialogMostrarReportesAgendaPorRango"))
        DialogMostrarReportesAgendaPorRango.resize(453, 434)
        DialogMostrarReportesAgendaPorRango.setMaximumSize(QtCore.QSize(800, 600))
        self.verticalLayout = QtGui.QVBoxLayout(DialogMostrarReportesAgendaPorRango)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(DialogMostrarReportesAgendaPorRango)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.listWidget_reportes = QtGui.QListWidget(DialogMostrarReportesAgendaPorRango)
        self.listWidget_reportes.setObjectName(_fromUtf8("listWidget_reportes"))
        self.verticalLayout.addWidget(self.listWidget_reportes)
        self.pushButton_aceptar = QtGui.QPushButton(DialogMostrarReportesAgendaPorRango)
        self.pushButton_aceptar.setObjectName(_fromUtf8("pushButton_aceptar"))
        self.verticalLayout.addWidget(self.pushButton_aceptar)

        self.retranslateUi(DialogMostrarReportesAgendaPorRango)
        QtCore.QMetaObject.connectSlotsByName(DialogMostrarReportesAgendaPorRango)

    def retranslateUi(self, DialogMostrarReportesAgendaPorRango):
        DialogMostrarReportesAgendaPorRango.setWindowTitle(_translate("DialogMostrarReportesAgendaPorRango", "Mostrando Reportes Agenda por Rango", None))
        self.label.setText(_translate("DialogMostrarReportesAgendaPorRango", "Generando reportes para la sección: ", None))
        self.pushButton_aceptar.setText(_translate("DialogMostrarReportesAgendaPorRango", "Aceptar", None))

