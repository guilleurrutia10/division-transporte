# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogRegistrarCambioDeSeccion.ui'
#
# Created: Sun Nov 18 20:37:49 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogRegistrarCambioDeSeccion(object):
    def setupUi(self, DialogRegistrarCambioDeSeccion):
        DialogRegistrarCambioDeSeccion.setObjectName(_fromUtf8("DialogRegistrarCambioDeSeccion"))
        DialogRegistrarCambioDeSeccion.resize(928, 513)
        DialogRegistrarCambioDeSeccion.setWindowTitle(QtGui.QApplication.translate("DialogRegistrarCambioDeSeccion", "Cambiar de Seccion a un Empleado", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(DialogRegistrarCambioDeSeccion)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = QtGui.QWidget(DialogRegistrarCambioDeSeccion)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout.addWidget(self.widget)
        self.groupBox = QtGui.QGroupBox(DialogRegistrarCambioDeSeccion)
        self.groupBox.setMaximumSize(QtCore.QSize(901, 61))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(770, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonCambiarDeSeccion = QtGui.QPushButton(self.groupBox)
        self.pushButtonCambiarDeSeccion.setText(QtGui.QApplication.translate("DialogRegistrarCambioDeSeccion", "Cambiar De Seccion", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCambiarDeSeccion.setObjectName(_fromUtf8("pushButtonCambiarDeSeccion"))
        self.horizontalLayout.addWidget(self.pushButtonCambiarDeSeccion)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBoxButtonBox = QtGui.QGroupBox(DialogRegistrarCambioDeSeccion)
        self.groupBoxButtonBox.setMinimumSize(QtCore.QSize(271, 41))
        self.groupBoxButtonBox.setMaximumSize(QtCore.QSize(16777215, 41))
        self.groupBoxButtonBox.setTitle(_fromUtf8(""))
        self.groupBoxButtonBox.setObjectName(_fromUtf8("groupBoxButtonBox"))
        self.gridLayout_7 = QtGui.QGridLayout(self.groupBoxButtonBox)
        self.gridLayout_7.setContentsMargins(9, 9, 9, 8)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.pushButtonAceptar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonAceptar.setText(QtGui.QApplication.translate("DialogRegistrarCambioDeSeccion", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAceptar.setObjectName(_fromUtf8("pushButtonAceptar"))
        self.gridLayout_7.addWidget(self.pushButtonAceptar, 0, 1, 1, 1)
        self.pushButtonCancelar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("DialogRegistrarCambioDeSeccion", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setObjectName(_fromUtf8("pushButtonCancelar"))
        self.gridLayout_7.addWidget(self.pushButtonCancelar, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem1, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxButtonBox)

        self.retranslateUi(DialogRegistrarCambioDeSeccion)
        QtCore.QMetaObject.connectSlotsByName(DialogRegistrarCambioDeSeccion)

    def retranslateUi(self, DialogRegistrarCambioDeSeccion):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogRegistrarCambioDeSeccion = QtGui.QDialog()
    ui = Ui_DialogRegistrarCambioDeSeccion()
    ui.setupUi(DialogRegistrarCambioDeSeccion)
    DialogRegistrarCambioDeSeccion.show()
    sys.exit(app.exec_())

