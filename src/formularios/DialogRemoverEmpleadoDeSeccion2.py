# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogRemoverEmpleadoDeSeccion2.ui'
#
# Created: Sun Nov 18 20:37:54 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogRemoverEmpleadoDeSeccion(object):
    def setupUi(self, DialogRemoverEmpleadoDeSeccion):
        DialogRemoverEmpleadoDeSeccion.setObjectName(_fromUtf8("DialogRemoverEmpleadoDeSeccion"))
        DialogRemoverEmpleadoDeSeccion.resize(400, 300)
        DialogRemoverEmpleadoDeSeccion.setWindowTitle(QtGui.QApplication.translate("DialogRemoverEmpleadoDeSeccion", "Remover Empleado de Seccion", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(DialogRemoverEmpleadoDeSeccion)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = QtGui.QWidget(DialogRemoverEmpleadoDeSeccion)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout.addWidget(self.widget)
        self.groupBox = QtGui.QGroupBox(DialogRemoverEmpleadoDeSeccion)
        self.groupBox.setMaximumSize(QtCore.QSize(901, 61))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(770, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonRemoverDeSeccion = QtGui.QPushButton(self.groupBox)
        self.pushButtonRemoverDeSeccion.setText(QtGui.QApplication.translate("DialogRemoverEmpleadoDeSeccion", "Remover De Seccion", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonRemoverDeSeccion.setObjectName(_fromUtf8("pushButtonRemoverDeSeccion"))
        self.horizontalLayout.addWidget(self.pushButtonRemoverDeSeccion)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBoxButtonBox = QtGui.QGroupBox(DialogRemoverEmpleadoDeSeccion)
        self.groupBoxButtonBox.setMinimumSize(QtCore.QSize(271, 41))
        self.groupBoxButtonBox.setMaximumSize(QtCore.QSize(16777215, 41))
        self.groupBoxButtonBox.setTitle(_fromUtf8(""))
        self.groupBoxButtonBox.setObjectName(_fromUtf8("groupBoxButtonBox"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBoxButtonBox)
        self.gridLayout_3.setContentsMargins(9, 9, 9, 8)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.pushButtonAceptar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonAceptar.setText(QtGui.QApplication.translate("DialogRemoverEmpleadoDeSeccion", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAceptar.setObjectName(_fromUtf8("pushButtonAceptar"))
        self.gridLayout_3.addWidget(self.pushButtonAceptar, 0, 1, 1, 1)
        self.pushButtonCancelar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("DialogRemoverEmpleadoDeSeccion", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setObjectName(_fromUtf8("pushButtonCancelar"))
        self.gridLayout_3.addWidget(self.pushButtonCancelar, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxButtonBox)

        self.retranslateUi(DialogRemoverEmpleadoDeSeccion)
        QtCore.QMetaObject.connectSlotsByName(DialogRemoverEmpleadoDeSeccion)

    def retranslateUi(self, DialogRemoverEmpleadoDeSeccion):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogRemoverEmpleadoDeSeccion = QtGui.QDialog()
    ui = Ui_DialogRemoverEmpleadoDeSeccion()
    ui.setupUi(DialogRemoverEmpleadoDeSeccion)
    DialogRemoverEmpleadoDeSeccion.show()
    sys.exit(app.exec_())

