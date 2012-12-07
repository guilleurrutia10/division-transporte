# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogMostrarPedidoDeActuacion.ui'
#
# Created: Thu Dec 06 14:49:20 2012
# Created: Wed Dec 05 21:19:07 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogMostrarPedidoDeActuacion(object):
    def setupUi(self, DialogMostrarPedidoDeActuacion):
        DialogMostrarPedidoDeActuacion.setObjectName(_fromUtf8("DialogMostrarPedidoDeActuacion"))
        DialogMostrarPedidoDeActuacion.resize(589, 356)
        DialogMostrarPedidoDeActuacion.setMinimumSize(QtCore.QSize(0, 0))
        DialogMostrarPedidoDeActuacion.setWindowTitle(QtGui.QApplication.translate("DialogMostrarPedidoDeActuacion", "Pedido de Actuacion Generado", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(DialogMostrarPedidoDeActuacion)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(DialogMostrarPedidoDeActuacion)
        self.groupBox.setTitle(QtGui.QApplication.translate("DialogMostrarPedidoDeActuacion", "Datos Pedido de Actuacion  ", None, QtGui.QApplication.UnicodeUTF8))
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
        self.label_2.setText(QtGui.QApplication.translate("DialogMostrarPedidoDeActuacion", "Fecha Ingreso:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.labelFechaPedido = QtGui.QLabel(self.groupBox)
        self.labelFechaPedido.setText(QtGui.QApplication.translate("DialogMostrarPedidoDeActuacion", "<<Fecha Pedido>>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelFechaPedido.setObjectName(_fromUtf8("labelFechaPedido"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.labelFechaPedido)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setText(QtGui.QApplication.translate("DialogMostrarPedidoDeActuacion", "Repuestos:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.tableWidgetRepuestos = QtGui.QTableWidget(self.groupBox)
        self.tableWidgetRepuestos.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidgetRepuestos.setObjectName(_fromUtf8("tableWidgetRepuestos"))
        self.tableWidgetRepuestos.setColumnCount(3)
        self.tableWidgetRepuestos.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogMostrarPedidoDeActuacion", "Nombre Tipo de Repuesto", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetRepuestos.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogMostrarPedidoDeActuacion", "Descripcion Tipo de Repuesto", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetRepuestos.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogMostrarPedidoDeActuacion", "Cantidad", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetRepuestos.setHorizontalHeaderItem(2, item)
        self.tableWidgetRepuestos.horizontalHeader().setDefaultSectionSize(165)
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
        self.pushButtonAceptar.setText(QtGui.QApplication.translate("DialogMostrarPedidoDeActuacion", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAceptar.setObjectName(_fromUtf8("pushButtonAceptar"))
        self.gridLayout_7.addWidget(self.pushButtonAceptar, 0, 1, 1, 1)
        self.pushButtonCancelar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("DialogMostrarPedidoDeActuacion", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setObjectName(_fromUtf8("pushButtonCancelar"))
        self.gridLayout_7.addWidget(self.pushButtonCancelar, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxButtonBox)

        self.retranslateUi(DialogMostrarPedidoDeActuacion)
        QtCore.QMetaObject.connectSlotsByName(DialogMostrarPedidoDeActuacion)

    def retranslateUi(self, DialogMostrarPedidoDeActuacion):
        item = self.tableWidgetRepuestos.horizontalHeaderItem(0)
        item = self.tableWidgetRepuestos.horizontalHeaderItem(1)
        item = self.tableWidgetRepuestos.horizontalHeaderItem(2)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogMostrarPedidoDeActuacion = QtGui.QDialog()
    ui = Ui_DialogMostrarPedidoDeActuacion()
    ui.setupUi(DialogMostrarPedidoDeActuacion)
    DialogMostrarPedidoDeActuacion.show()
    sys.exit(app.exec_())

