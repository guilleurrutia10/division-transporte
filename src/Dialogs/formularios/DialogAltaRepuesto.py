# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/DialogAltaRepuesto.ui'
#
# Created: Wed Sep 10 22:00:17 2014
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

class Ui_DialogAltaRepuesto(object):
    def setupUi(self, DialogAltaRepuesto):
        DialogAltaRepuesto.setObjectName(_fromUtf8("DialogAltaRepuesto"))
        DialogAltaRepuesto.resize(495, 200)
        DialogAltaRepuesto.setMinimumSize(QtCore.QSize(300, 140))
        DialogAltaRepuesto.setMaximumSize(QtCore.QSize(600, 200))
        self.verticalLayout = QtGui.QVBoxLayout(DialogAltaRepuesto)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(DialogAltaRepuesto)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEditNombreRepuesto = QtGui.QLineEdit(self.groupBox)
        self.lineEditNombreRepuesto.setObjectName(_fromUtf8("lineEditNombreRepuesto"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditNombreRepuesto)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEditDescRepuesto = QtGui.QLineEdit(self.groupBox)
        self.lineEditDescRepuesto.setObjectName(_fromUtf8("lineEditDescRepuesto"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEditDescRepuesto)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBoxButtonBox = QtGui.QGroupBox(DialogAltaRepuesto)
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

        self.retranslateUi(DialogAltaRepuesto)
        QtCore.QMetaObject.connectSlotsByName(DialogAltaRepuesto)

    def retranslateUi(self, DialogAltaRepuesto):
        DialogAltaRepuesto.setWindowTitle(_translate("DialogAltaRepuesto", "Alta Repuesto", None))
        self.groupBox.setTitle(_translate("DialogAltaRepuesto", "Nuevo Repuesto", None))
        self.label.setText(_translate("DialogAltaRepuesto", "Nombre Repuesto:", None))
        self.lineEditNombreRepuesto.setToolTip(_translate("DialogAltaRepuesto", "Indica el nombre del repuesto", None))
        self.label_2.setText(_translate("DialogAltaRepuesto", "Descripción Repuesto:", None))
        self.lineEditDescRepuesto.setToolTip(_translate("DialogAltaRepuesto", "Indica la descripción del repuesto", None))
        self.pushButtonAceptar.setText(_translate("DialogAltaRepuesto", "Aceptar", None))
        self.pushButtonCancelar.setText(_translate("DialogAltaRepuesto", "Cancelar", None))

