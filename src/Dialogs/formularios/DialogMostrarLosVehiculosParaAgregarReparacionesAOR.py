# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/DialogMostrarLosVehiculosParaAgregarReparacionesAOR.ui'
#
# Created: Fri Sep 12 01:20:05 2014
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

class Ui_DialogMostrarLosVehiculosParaAgregarReparacionesAOR(object):
    def setupUi(self, DialogMostrarLosVehiculosParaAgregarReparacionesAOR):
        DialogMostrarLosVehiculosParaAgregarReparacionesAOR.setObjectName(_fromUtf8("DialogMostrarLosVehiculosParaAgregarReparacionesAOR"))
        DialogMostrarLosVehiculosParaAgregarReparacionesAOR.resize(800, 600)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogMostrarLosVehiculosParaAgregarReparacionesAOR.sizePolicy().hasHeightForWidth())
        DialogMostrarLosVehiculosParaAgregarReparacionesAOR.setSizePolicy(sizePolicy)
        DialogMostrarLosVehiculosParaAgregarReparacionesAOR.setMinimumSize(QtCore.QSize(800, 600))
        self.verticalLayout = QtGui.QVBoxLayout(DialogMostrarLosVehiculosParaAgregarReparacionesAOR)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.widget = QtGui.QWidget(DialogMostrarLosVehiculosParaAgregarReparacionesAOR)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2.addWidget(self.widget)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.groupBox = QtGui.QGroupBox(DialogMostrarLosVehiculosParaAgregarReparacionesAOR)
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
        self.pushButtonAgregarReparacionesAOrden = QtGui.QPushButton(self.groupBox)
        self.pushButtonAgregarReparacionesAOrden.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButtonAgregarReparacionesAOrden.setMaximumSize(QtCore.QSize(150, 16777215))
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
        self.pushButtonAceptar.setObjectName(_fromUtf8("pushButtonAceptar"))
        self.gridLayout_5.addWidget(self.pushButtonAceptar, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem1, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxButtonBox)

        self.retranslateUi(DialogMostrarLosVehiculosParaAgregarReparacionesAOR)
        QtCore.QObject.connect(self.pushButtonAceptar, QtCore.SIGNAL(_fromUtf8("clicked()")), DialogMostrarLosVehiculosParaAgregarReparacionesAOR.accept)
        QtCore.QObject.connect(self.pushButtonAceptar, QtCore.SIGNAL(_fromUtf8("pressed()")), DialogMostrarLosVehiculosParaAgregarReparacionesAOR.accept)
        QtCore.QMetaObject.connectSlotsByName(DialogMostrarLosVehiculosParaAgregarReparacionesAOR)

    def retranslateUi(self, DialogMostrarLosVehiculosParaAgregarReparacionesAOR):
        DialogMostrarLosVehiculosParaAgregarReparacionesAOR.setWindowTitle(_translate("DialogMostrarLosVehiculosParaAgregarReparacionesAOR", "Agregar Reparaciones a Orden de Reparación de Vehículo", None))
        self.pushButtonAgregarReparacionesAOrden.setText(_translate("DialogMostrarLosVehiculosParaAgregarReparacionesAOR", "Agregar Reparaciones a Orden", None))
        self.pushButtonAceptar.setText(_translate("DialogMostrarLosVehiculosParaAgregarReparacionesAOR", "Hecho", None))

