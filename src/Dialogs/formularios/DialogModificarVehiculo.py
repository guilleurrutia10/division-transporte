# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/DialogModificarVehiculo.ui'
#
# Created: Thu Sep 11 02:39:52 2014
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

class Ui_DialogModificarVehiculo(object):
    def setupUi(self, DialogModificarVehiculo):
        DialogModificarVehiculo.setObjectName(_fromUtf8("DialogModificarVehiculo"))
        DialogModificarVehiculo.resize(545, 254)
        DialogModificarVehiculo.setMinimumSize(QtCore.QSize(300, 180))
        DialogModificarVehiculo.setMaximumSize(QtCore.QSize(800, 600))
        self.verticalLayout = QtGui.QVBoxLayout(DialogModificarVehiculo)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(DialogModificarVehiculo)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEditDominio = QtGui.QLineEdit(self.groupBox)
        self.lineEditDominio.setObjectName(_fromUtf8("lineEditDominio"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditDominio)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEditMarca = QtGui.QLineEdit(self.groupBox)
        self.lineEditMarca.setObjectName(_fromUtf8("lineEditMarca"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEditMarca)
        self.lineEditRegistroInterno = QtGui.QLineEdit(self.groupBox)
        self.lineEditRegistroInterno.setObjectName(_fromUtf8("lineEditRegistroInterno"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEditRegistroInterno)
        self.lineEditChasisNro = QtGui.QLineEdit(self.groupBox)
        self.lineEditChasisNro.setObjectName(_fromUtf8("lineEditChasisNro"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEditChasisNro)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBoxButtonBox = QtGui.QGroupBox(DialogModificarVehiculo)
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

        self.retranslateUi(DialogModificarVehiculo)
        QtCore.QMetaObject.connectSlotsByName(DialogModificarVehiculo)

    def retranslateUi(self, DialogModificarVehiculo):
        DialogModificarVehiculo.setWindowTitle(_translate("DialogModificarVehiculo", "Modificar Vehiculo", None))
        self.groupBox.setTitle(_translate("DialogModificarVehiculo", "Modificar Vehículo", None))
        self.label.setText(_translate("DialogModificarVehiculo", "Dominio:", None))
        self.label_2.setText(_translate("DialogModificarVehiculo", "Marca:", None))
        self.label_3.setText(_translate("DialogModificarVehiculo", "Registro Interno:", None))
        self.label_4.setText(_translate("DialogModificarVehiculo", "Número de Chasis:", None))
        self.pushButtonAceptar.setText(_translate("DialogModificarVehiculo", "Aceptar", None))
        self.pushButtonCancelar.setText(_translate("DialogModificarVehiculo", "Cancelar", None))

