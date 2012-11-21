# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogRegistrarIngresoVehiculo.ui'
#
# Created: Sun Nov 18 20:37:51 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogRegistrarIngresoVehiculo(object):
    def setupUi(self, DialogRegistrarIngresoVehiculo):
        DialogRegistrarIngresoVehiculo.setObjectName(_fromUtf8("DialogRegistrarIngresoVehiculo"))
        DialogRegistrarIngresoVehiculo.resize(815, 530)
        DialogRegistrarIngresoVehiculo.setWindowTitle(QtGui.QApplication.translate("DialogRegistrarIngresoVehiculo", "Registrar Ingreso Vehiculo", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(DialogRegistrarIngresoVehiculo)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = QtGui.QWidget(DialogRegistrarIngresoVehiculo)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout.addWidget(self.widget)
        self.groupBox = QtGui.QGroupBox(DialogRegistrarIngresoVehiculo)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 75))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 75))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(480, 10, 0, 12)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonRegistrarNuevoIngreso = QtGui.QPushButton(self.groupBox)
        self.pushButtonRegistrarNuevoIngreso.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButtonRegistrarNuevoIngreso.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButtonRegistrarNuevoIngreso.setText(QtGui.QApplication.translate("DialogRegistrarIngresoVehiculo", "Registrar Nuevo Ingreso", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonRegistrarNuevoIngreso.setObjectName(_fromUtf8("pushButtonRegistrarNuevoIngreso"))
        self.horizontalLayout.addWidget(self.pushButtonRegistrarNuevoIngreso)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBoxButtonBox = QtGui.QGroupBox(DialogRegistrarIngresoVehiculo)
        self.groupBoxButtonBox.setMinimumSize(QtCore.QSize(271, 41))
        self.groupBoxButtonBox.setMaximumSize(QtCore.QSize(16777215, 41))
        self.groupBoxButtonBox.setTitle(_fromUtf8(""))
        self.groupBoxButtonBox.setObjectName(_fromUtf8("groupBoxButtonBox"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBoxButtonBox)
        self.gridLayout_5.setContentsMargins(9, 9, 9, 8)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.pushButtonAceptar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonAceptar.setText(QtGui.QApplication.translate("DialogRegistrarIngresoVehiculo", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAceptar.setObjectName(_fromUtf8("pushButtonAceptar"))
        self.gridLayout_5.addWidget(self.pushButtonAceptar, 0, 1, 1, 1)
        self.pushButtonCancelar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("DialogRegistrarIngresoVehiculo", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setObjectName(_fromUtf8("pushButtonCancelar"))
        self.gridLayout_5.addWidget(self.pushButtonCancelar, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem1, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxButtonBox)

        self.retranslateUi(DialogRegistrarIngresoVehiculo)
        QtCore.QMetaObject.connectSlotsByName(DialogRegistrarIngresoVehiculo)

    def retranslateUi(self, DialogRegistrarIngresoVehiculo):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogRegistrarIngresoVehiculo = QtGui.QDialog()
    ui = Ui_DialogRegistrarIngresoVehiculo()
    ui.setupUi(DialogRegistrarIngresoVehiculo)
    DialogRegistrarIngresoVehiculo.show()
    sys.exit(app.exec_())

