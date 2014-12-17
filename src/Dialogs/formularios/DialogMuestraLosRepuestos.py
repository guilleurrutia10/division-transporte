# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/DialogMuestraLosRepuestos.ui'
#
# Created: Mon Jul 28 21:08:55 2014
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("DialogMuestraLosRepuestos"))
        Dialog.resize(800, 600)
        Dialog.setMinimumSize(QtCore.QSize(800, 600))
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(150, 70))
        self.groupBox_2.setMaximumSize(QtCore.QSize(200, 70))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lineEditBuscarNombre = QtGui.QLineEdit(self.groupBox_2)
        self.lineEditBuscarNombre.setObjectName(_fromUtf8("lineEditBuscarNombre"))
        self.horizontalLayout_2.addWidget(self.lineEditBuscarNombre)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.pushButtonBuscar = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonBuscar.sizePolicy().hasHeightForWidth())
        self.pushButtonBuscar.setSizePolicy(sizePolicy)
        self.pushButtonBuscar.setObjectName(_fromUtf8("pushButtonBuscar"))
        self.verticalLayout_2.addWidget(self.pushButtonBuscar)
        self.verticalLayout.addWidget(self.groupBox)
        self.tableWidgetDatosRepuestos = QtGui.QTableWidget(Dialog)
        self.tableWidgetDatosRepuestos.setObjectName(_fromUtf8("tableWidgetDatosRepuestos"))
        self.tableWidgetDatosRepuestos.setColumnCount(3)
        self.tableWidgetDatosRepuestos.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetDatosRepuestos.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetDatosRepuestos.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetDatosRepuestos.setHorizontalHeaderItem(2, item)
        self.tableWidgetDatosRepuestos.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidgetDatosRepuestos.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidgetDatosRepuestos.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidgetDatosRepuestos.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableWidgetDatosRepuestos)
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setMinimumSize(QtCore.QSize(50, 50))
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonModificarRepuesto = QtGui.QPushButton(self.groupBox_3)
        self.pushButtonModificarRepuesto.setObjectName(_fromUtf8("pushButtonModificarRepuesto"))
        self.horizontalLayout.addWidget(self.pushButtonModificarRepuesto)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBoxButtonBox = QtGui.QGroupBox(Dialog)
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
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxButtonBox)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Repuestos de la Division", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Buscar Nombre", None))
        self.pushButtonBuscar.setWhatsThis(_translate("Dialog", "Buscar segun el criterio elegido", None))
        self.pushButtonBuscar.setText(_translate("Dialog", "Buscar", None))
        item = self.tableWidgetDatosRepuestos.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Código", None))
        item = self.tableWidgetDatosRepuestos.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Nombre", None))
        item = self.tableWidgetDatosRepuestos.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Descripción", None))
        self.pushButtonModificarRepuesto.setText(_translate("Dialog", "Modificar Repuesto", None))
        self.pushButtonAceptar.setText(_translate("Dialog", "Aceptar", None))
        self.pushButtonCancelar.setText(_translate("Dialog", "Cancelar", None))

