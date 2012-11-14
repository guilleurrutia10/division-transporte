# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogRegistrarEgresoVehiculo.ui'
#
# Created: Wed Nov 14 00:01:21 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogRegistraEgresoVehiculo(object):
    def setupUi(self, DialogRegistraEgresoVehiculo):
        DialogRegistraEgresoVehiculo.setObjectName(_fromUtf8("DialogRegistraEgresoVehiculo"))
        DialogRegistraEgresoVehiculo.resize(793, 474)
        DialogRegistraEgresoVehiculo.setWindowTitle(QtGui.QApplication.translate("DialogRegistraEgresoVehiculo", "Registra Egreso Vehiculo", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(DialogRegistraEgresoVehiculo)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = QtGui.QWidget(DialogRegistraEgresoVehiculo)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout.addWidget(self.widget)
        self.groupBox = QtGui.QGroupBox(DialogRegistraEgresoVehiculo)
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
        self.pushButtonRegistrarEgreso = QtGui.QPushButton(self.groupBox)
        self.pushButtonRegistrarEgreso.setMinimumSize(QtCore.QSize(134, 0))
        self.pushButtonRegistrarEgreso.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButtonRegistrarEgreso.setText(QtGui.QApplication.translate("DialogRegistraEgresoVehiculo", "Registrar Egreso", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonRegistrarEgreso.setObjectName(_fromUtf8("pushButtonRegistrarEgreso"))
        self.horizontalLayout.addWidget(self.pushButtonRegistrarEgreso)
        self.pushButtonCancelar = QtGui.QPushButton(self.groupBox)
        self.pushButtonCancelar.setMinimumSize(QtCore.QSize(134, 0))
        self.pushButtonCancelar.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("DialogRegistraEgresoVehiculo", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setObjectName(_fromUtf8("pushButtonCancelar"))
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(DialogRegistraEgresoVehiculo)
        QtCore.QMetaObject.connectSlotsByName(DialogRegistraEgresoVehiculo)

    def retranslateUi(self, DialogRegistraEgresoVehiculo):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogRegistraEgresoVehiculo = QtGui.QDialog()
    ui = Ui_DialogRegistraEgresoVehiculo()
    ui.setupUi(DialogRegistraEgresoVehiculo)
    DialogRegistraEgresoVehiculo.show()
    sys.exit(app.exec_())

