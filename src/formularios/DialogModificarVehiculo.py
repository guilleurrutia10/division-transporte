# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogModificarVehiculo.ui'
#
# Created: Wed Nov 21 16:16:50 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogModificarVehiculo(object):
    def setupUi(self, DialogModificarVehiculo):
        DialogModificarVehiculo.setObjectName(_fromUtf8("DialogModificarVehiculo"))
        DialogModificarVehiculo.resize(300, 180)
        DialogModificarVehiculo.setMinimumSize(QtCore.QSize(300, 180))
        DialogModificarVehiculo.setMaximumSize(QtCore.QSize(300, 180))
        DialogModificarVehiculo.setWindowTitle(QtGui.QApplication.translate("DialogModificarVehiculo", "Modificar Vehiculo", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(DialogModificarVehiculo)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(DialogModificarVehiculo)
        self.groupBox.setTitle(QtGui.QApplication.translate("DialogModificarVehiculo", "Modificar Vehiculo", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setText(QtGui.QApplication.translate("DialogModificarVehiculo", "Dominio:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setText(QtGui.QApplication.translate("DialogModificarVehiculo", "Marca:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEditDominio = QtGui.QLineEdit(self.groupBox)
        self.lineEditDominio.setObjectName(_fromUtf8("lineEditDominio"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditDominio)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setText(QtGui.QApplication.translate("DialogModificarVehiculo", "Registro Interno:", None, QtGui.QApplication.UnicodeUTF8))
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
        self.label_4.setText(QtGui.QApplication.translate("DialogModificarVehiculo", "Chasis Nro:", None, QtGui.QApplication.UnicodeUTF8))
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
        self.pushButtonAceptar.setText(QtGui.QApplication.translate("DialogModificarVehiculo", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAceptar.setObjectName(_fromUtf8("pushButtonAceptar"))
        self.gridLayout_2.addWidget(self.pushButtonAceptar, 0, 1, 1, 1)
        self.pushButtonCancelar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("DialogModificarVehiculo", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setObjectName(_fromUtf8("pushButtonCancelar"))
        self.gridLayout_2.addWidget(self.pushButtonCancelar, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxButtonBox)

        self.retranslateUi(DialogModificarVehiculo)
        QtCore.QMetaObject.connectSlotsByName(DialogModificarVehiculo)

    def retranslateUi(self, DialogModificarVehiculo):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogModificarVehiculo = QtGui.QDialog()
    ui = Ui_DialogModificarVehiculo()
    ui.setupUi(DialogModificarVehiculo)
    DialogModificarVehiculo.show()
    sys.exit(app.exec_())

