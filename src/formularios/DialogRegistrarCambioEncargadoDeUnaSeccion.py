# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogRegistrarCambioEncargadoDeUnaSeccion.ui'
#
# Created: Thu Nov 22 02:15:15 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogRegistrarCambioEncargadoDeUnaSeccion(object):
    def setupUi(self, DialogRegistrarCambioEncargadoDeUnaSeccion):
        DialogRegistrarCambioEncargadoDeUnaSeccion.setObjectName(_fromUtf8("DialogRegistrarCambioEncargadoDeUnaSeccion"))
        DialogRegistrarCambioEncargadoDeUnaSeccion.resize(657, 399)
        DialogRegistrarCambioEncargadoDeUnaSeccion.setWindowTitle(QtGui.QApplication.translate("DialogRegistrarCambioEncargadoDeUnaSeccion", "Cambiar Encargado de una Seccion", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(DialogRegistrarCambioEncargadoDeUnaSeccion)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = QtGui.QWidget(DialogRegistrarCambioEncargadoDeUnaSeccion)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout.addWidget(self.widget)
        self.groupBox = QtGui.QGroupBox(DialogRegistrarCambioEncargadoDeUnaSeccion)
        self.groupBox.setMaximumSize(QtCore.QSize(901, 61))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(770, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonCambiarDeSeccion = QtGui.QPushButton(self.groupBox)
        self.pushButtonCambiarDeSeccion.setText(QtGui.QApplication.translate("DialogRegistrarCambioEncargadoDeUnaSeccion", "Asignar Como Encargado", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCambiarDeSeccion.setObjectName(_fromUtf8("pushButtonCambiarDeSeccion"))
        self.horizontalLayout.addWidget(self.pushButtonCambiarDeSeccion)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBoxButtonBox = QtGui.QGroupBox(DialogRegistrarCambioEncargadoDeUnaSeccion)
        self.groupBoxButtonBox.setMinimumSize(QtCore.QSize(271, 41))
        self.groupBoxButtonBox.setMaximumSize(QtCore.QSize(16777215, 41))
        self.groupBoxButtonBox.setTitle(_fromUtf8(""))
        self.groupBoxButtonBox.setObjectName(_fromUtf8("groupBoxButtonBox"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBoxButtonBox)
        self.gridLayout_3.setContentsMargins(9, 9, 9, 8)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.pushButtonAceptar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonAceptar.setText(QtGui.QApplication.translate("DialogRegistrarCambioEncargadoDeUnaSeccion", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAceptar.setObjectName(_fromUtf8("pushButtonAceptar"))
        self.gridLayout_3.addWidget(self.pushButtonAceptar, 0, 1, 1, 1)
        self.pushButtonCancelar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("DialogRegistrarCambioEncargadoDeUnaSeccion", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setObjectName(_fromUtf8("pushButtonCancelar"))
        self.gridLayout_3.addWidget(self.pushButtonCancelar, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxButtonBox)

        self.retranslateUi(DialogRegistrarCambioEncargadoDeUnaSeccion)
        QtCore.QMetaObject.connectSlotsByName(DialogRegistrarCambioEncargadoDeUnaSeccion)

    def retranslateUi(self, DialogRegistrarCambioEncargadoDeUnaSeccion):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogRegistrarCambioEncargadoDeUnaSeccion = QtGui.QDialog()
    ui = Ui_DialogRegistrarCambioEncargadoDeUnaSeccion()
    ui.setupUi(DialogRegistrarCambioEncargadoDeUnaSeccion)
    DialogRegistrarCambioEncargadoDeUnaSeccion.show()
    sys.exit(app.exec_())

