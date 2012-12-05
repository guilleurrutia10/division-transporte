# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogMostrarLosVehiculosParaAgregarReparacionesAOR.ui'
#
# Created: Thu Nov 29 17:00:36 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogMostrarLosVehiculosParaAgregarReparacionesAOR(object):
    def setupUi(self, DialogMostrarLosVehiculosParaAgregarReparacionesAOR):
        DialogMostrarLosVehiculosParaAgregarReparacionesAOR.setObjectName(_fromUtf8("DialogMostrarLosVehiculosParaAgregarReparacionesAOR"))
        DialogMostrarLosVehiculosParaAgregarReparacionesAOR.resize(702, 444)
        DialogMostrarLosVehiculosParaAgregarReparacionesAOR.setWindowTitle(QtGui.QApplication.translate("DialogMostrarLosVehiculosParaAgregarReparacionesAOR", "Agregar Reparaciones a Orden de Reparacion de Vehiculo", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../recursos/Imagenes/logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogMostrarLosVehiculosParaAgregarReparacionesAOR.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(DialogMostrarLosVehiculosParaAgregarReparacionesAOR)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = QtGui.QWidget(DialogMostrarLosVehiculosParaAgregarReparacionesAOR)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout.addWidget(self.widget)
        self.groupBox = QtGui.QGroupBox(DialogMostrarLosVehiculosParaAgregarReparacionesAOR)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(40, 50))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 50))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(9, 10, 0, 12)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonAgregarReparacionesAOrden = QtGui.QPushButton(self.groupBox)
        self.pushButtonAgregarReparacionesAOrden.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButtonAgregarReparacionesAOrden.setMaximumSize(QtCore.QSize(163, 16777215))
        self.pushButtonAgregarReparacionesAOrden.setText(QtGui.QApplication.translate("DialogMostrarLosVehiculosParaAgregarReparacionesAOR", "Agregar Reparaciones a Orden", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAgregarReparacionesAOrden.setObjectName(_fromUtf8("pushButtonAgregarReparacionesAOrden"))
        self.horizontalLayout.addWidget(self.pushButtonAgregarReparacionesAOrden)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBoxButtonBox = QtGui.QGroupBox(DialogMostrarLosVehiculosParaAgregarReparacionesAOR)
        self.groupBoxButtonBox.setMinimumSize(QtCore.QSize(271, 41))
        self.groupBoxButtonBox.setMaximumSize(QtCore.QSize(16777215, 41))
        self.groupBoxButtonBox.setTitle(_fromUtf8(""))
        self.groupBoxButtonBox.setObjectName(_fromUtf8("groupBoxButtonBox"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBoxButtonBox)
        self.gridLayout_5.setContentsMargins(9, 9, 9, 8)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.pushButtonAceptar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonAceptar.setText(QtGui.QApplication.translate("DialogMostrarLosVehiculosParaAgregarReparacionesAOR", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAceptar.setObjectName(_fromUtf8("pushButtonAceptar"))
        self.gridLayout_5.addWidget(self.pushButtonAceptar, 0, 1, 1, 1)
        self.pushButtonCancelar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("DialogMostrarLosVehiculosParaAgregarReparacionesAOR", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setObjectName(_fromUtf8("pushButtonCancelar"))
        self.gridLayout_5.addWidget(self.pushButtonCancelar, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem1, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxButtonBox)

        self.retranslateUi(DialogMostrarLosVehiculosParaAgregarReparacionesAOR)
        QtCore.QMetaObject.connectSlotsByName(DialogMostrarLosVehiculosParaAgregarReparacionesAOR)

    def retranslateUi(self, DialogMostrarLosVehiculosParaAgregarReparacionesAOR):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogMostrarLosVehiculosParaAgregarReparacionesAOR = QtGui.QDialog()
    ui = Ui_DialogMostrarLosVehiculosParaAgregarReparacionesAOR()
    ui.setupUi(DialogMostrarLosVehiculosParaAgregarReparacionesAOR)
    DialogMostrarLosVehiculosParaAgregarReparacionesAOR.show()
    sys.exit(app.exec_())

