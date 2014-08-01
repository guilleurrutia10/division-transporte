# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/DialogMostrarPedidoDeActuacion.ui'
#
# Created: Thu Jul 31 21:36:47 2014
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

class Ui_DialogMostrarPedidoDeActuacion(object):
    def setupUi(self, DialogMostrarPedidoDeActuacion):
        DialogMostrarPedidoDeActuacion.setObjectName(_fromUtf8("DialogMostrarPedidoDeActuacion"))
        DialogMostrarPedidoDeActuacion.resize(800, 400)
        DialogMostrarPedidoDeActuacion.setMinimumSize(QtCore.QSize(800, 400))
        self.verticalLayout = QtGui.QVBoxLayout(DialogMostrarPedidoDeActuacion)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(DialogMostrarPedidoDeActuacion)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(60, -1, -1, -1)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.labelFechaPedido = QtGui.QLabel(self.groupBox)
        self.labelFechaPedido.setObjectName(_fromUtf8("labelFechaPedido"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.labelFechaPedido)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.tableWidgetRepuestos = QtGui.QTableWidget(self.groupBox)
        self.tableWidgetRepuestos.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidgetRepuestos.setObjectName(_fromUtf8("tableWidgetRepuestos"))
        self.tableWidgetRepuestos.setColumnCount(3)
        self.tableWidgetRepuestos.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetRepuestos.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetRepuestos.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetRepuestos.setHorizontalHeaderItem(2, item)
        self.tableWidgetRepuestos.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidgetRepuestos.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidgetRepuestos.horizontalHeader().setStretchLastSection(True)
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.tableWidgetRepuestos)
        self.horizontalLayout.addLayout(self.formLayout)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBoxButtonBox = QtGui.QGroupBox(DialogMostrarPedidoDeActuacion)
        self.groupBoxButtonBox.setMinimumSize(QtCore.QSize(271, 41))
        self.groupBoxButtonBox.setMaximumSize(QtCore.QSize(16777215, 41))
        self.groupBoxButtonBox.setTitle(_fromUtf8(""))
        self.groupBoxButtonBox.setObjectName(_fromUtf8("groupBoxButtonBox"))
        self.gridLayout_7 = QtGui.QGridLayout(self.groupBoxButtonBox)
        self.gridLayout_7.setContentsMargins(9, 9, 9, 8)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.pushButtonAceptar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonAceptar.setObjectName(_fromUtf8("pushButtonAceptar"))
        self.gridLayout_7.addWidget(self.pushButtonAceptar, 0, 1, 1, 1)
        self.pushButtonCancelar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonCancelar.setObjectName(_fromUtf8("pushButtonCancelar"))
        self.gridLayout_7.addWidget(self.pushButtonCancelar, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxButtonBox)

        self.retranslateUi(DialogMostrarPedidoDeActuacion)
        QtCore.QMetaObject.connectSlotsByName(DialogMostrarPedidoDeActuacion)

    def retranslateUi(self, DialogMostrarPedidoDeActuacion):
        DialogMostrarPedidoDeActuacion.setWindowTitle(_translate("DialogMostrarPedidoDeActuacion", "Pedido de Actuacion Generado", None))
        self.groupBox.setTitle(_translate("DialogMostrarPedidoDeActuacion", "Datos Pedido de Actuacion  ", None))
        self.label_2.setText(_translate("DialogMostrarPedidoDeActuacion", "Fecha Ingreso:", None))
        self.labelFechaPedido.setText(_translate("DialogMostrarPedidoDeActuacion", "<<Fecha Pedido>>", None))
        self.label.setText(_translate("DialogMostrarPedidoDeActuacion", "Repuestos:", None))
        item = self.tableWidgetRepuestos.horizontalHeaderItem(0)
        item.setText(_translate("DialogMostrarPedidoDeActuacion", "Nombre", None))
        item = self.tableWidgetRepuestos.horizontalHeaderItem(1)
        item.setText(_translate("DialogMostrarPedidoDeActuacion", "Descripcion", None))
        item = self.tableWidgetRepuestos.horizontalHeaderItem(2)
        item.setText(_translate("DialogMostrarPedidoDeActuacion", "Cantidad", None))
        self.pushButtonAceptar.setText(_translate("DialogMostrarPedidoDeActuacion", "Aceptar", None))
        self.pushButtonCancelar.setText(_translate("DialogMostrarPedidoDeActuacion", "Cancelar", None))

