# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/DialogAsignarFechaDeBaja.ui'
#
# Created: Sun Aug  3 23:50:05 2014
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

class Ui_DialogAsignarFechaBaja(object):
    def setupUi(self, DialogAsignarFechaBaja):
        DialogAsignarFechaBaja.setObjectName(_fromUtf8("DialogAsignarFechaBaja"))
        DialogAsignarFechaBaja.resize(498, 294)
        DialogAsignarFechaBaja.setMaximumSize(QtCore.QSize(593, 300))
        self.gridLayout_2 = QtGui.QGridLayout(DialogAsignarFechaBaja)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.groupBox = QtGui.QGroupBox(DialogAsignarFechaBaja)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.calendarWidgetRegistrarBaja = QtGui.QCalendarWidget(self.groupBox)
        self.calendarWidgetRegistrarBaja.setObjectName(_fromUtf8("calendarWidgetRegistrarBaja"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.calendarWidgetRegistrarBaja)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBoxButtonBox = QtGui.QGroupBox(DialogAsignarFechaBaja)
        self.groupBoxButtonBox.setTitle(_fromUtf8(""))
        self.groupBoxButtonBox.setObjectName(_fromUtf8("groupBoxButtonBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBoxButtonBox)
        self.gridLayout.setContentsMargins(9, 9, 9, 8)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButtonAceptar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonAceptar.setObjectName(_fromUtf8("pushButtonAceptar"))
        self.gridLayout.addWidget(self.pushButtonAceptar, 0, 1, 1, 1)
        self.pushButtonCancelar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonCancelar.setObjectName(_fromUtf8("pushButtonCancelar"))
        self.gridLayout.addWidget(self.pushButtonCancelar, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBoxButtonBox, 1, 0, 1, 1)

        self.retranslateUi(DialogAsignarFechaBaja)
        QtCore.QMetaObject.connectSlotsByName(DialogAsignarFechaBaja)

    def retranslateUi(self, DialogAsignarFechaBaja):
        DialogAsignarFechaBaja.setWindowTitle(_translate("DialogAsignarFechaBaja", "Asignar Fecha de Baja", None))
        self.groupBox.setTitle(_translate("DialogAsignarFechaBaja", "Registrar Fecha de Baja", None))
        self.pushButtonAceptar.setText(_translate("DialogAsignarFechaBaja", "Aceptar", None))
        self.pushButtonCancelar.setText(_translate("DialogAsignarFechaBaja", "Cancelar", None))

