# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/DialogModificarRepuesto.ui'
#
# Created: Thu Sep 11 23:02:59 2014
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

class Ui_DialogMoficarRepuesto(object):
    def setupUi(self, DialogMoficarRepuesto):
        DialogMoficarRepuesto.setObjectName(_fromUtf8("DialogMoficarRepuesto"))
        DialogMoficarRepuesto.resize(500, 300)
        DialogMoficarRepuesto.setMinimumSize(QtCore.QSize(400, 200))
        DialogMoficarRepuesto.setMaximumSize(QtCore.QSize(500, 300))
        self.verticalLayout = QtGui.QVBoxLayout(DialogMoficarRepuesto)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(DialogMoficarRepuesto)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.lineEditNombreRepuesto = QtGui.QLineEdit(self.groupBox)
        self.lineEditNombreRepuesto.setObjectName(_fromUtf8("lineEditNombreRepuesto"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEditNombreRepuesto)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEditCodigo = QtGui.QLineEdit(self.groupBox)
        self.lineEditCodigo.setReadOnly(True)
        self.lineEditCodigo.setPlaceholderText(_fromUtf8(""))
        self.lineEditCodigo.setObjectName(_fromUtf8("lineEditCodigo"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditCodigo)
        self.plainTextEditDescripcion = QtGui.QPlainTextEdit(self.groupBox)
        self.plainTextEditDescripcion.setObjectName(_fromUtf8("plainTextEditDescripcion"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.plainTextEditDescripcion)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBoxButtonBox = QtGui.QGroupBox(DialogMoficarRepuesto)
        self.groupBoxButtonBox.setMinimumSize(QtCore.QSize(271, 41))
        self.groupBoxButtonBox.setMaximumSize(QtCore.QSize(16777215, 41))
        self.groupBoxButtonBox.setTitle(_fromUtf8(""))
        self.groupBoxButtonBox.setObjectName(_fromUtf8("groupBoxButtonBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBoxButtonBox)
        self.gridLayout_2.setContentsMargins(9, 9, 9, 8)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pushButtonAceptar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonAceptar.setObjectName(_fromUtf8("pushButtonAceptar"))
        self.gridLayout_2.addWidget(self.pushButtonAceptar, 0, 1, 1, 1)
        self.pushButtonCancelar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonCancelar.setObjectName(_fromUtf8("pushButtonCancelar"))
        self.gridLayout_2.addWidget(self.pushButtonCancelar, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxButtonBox)

        self.retranslateUi(DialogMoficarRepuesto)
        QtCore.QObject.connect(self.pushButtonCancelar, QtCore.SIGNAL(_fromUtf8("clicked()")), DialogMoficarRepuesto.reject)
        QtCore.QObject.connect(self.pushButtonCancelar, QtCore.SIGNAL(_fromUtf8("pressed()")), DialogMoficarRepuesto.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogMoficarRepuesto)

    def retranslateUi(self, DialogMoficarRepuesto):
        DialogMoficarRepuesto.setWindowTitle(_translate("DialogMoficarRepuesto", "Modificar Repuesto", None))
        self.groupBox.setTitle(_translate("DialogMoficarRepuesto", "Modificar Repuesto", None))
        self.label_2.setText(_translate("DialogMoficarRepuesto", "Descripción:", None))
        self.label.setText(_translate("DialogMoficarRepuesto", "Nombre:", None))
        self.label_3.setText(_translate("DialogMoficarRepuesto", "Código:", None))
        self.pushButtonAceptar.setText(_translate("DialogMoficarRepuesto", "Aceptar", None))
        self.pushButtonCancelar.setText(_translate("DialogMoficarRepuesto", "Cancelar", None))

