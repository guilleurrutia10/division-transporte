# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogRegistrarCambioEncargadoDeUnaSeccion.ui'
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
        self.buttonBox = QtGui.QDialogButtonBox(DialogRegistrarCambioEncargadoDeUnaSeccion)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

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

