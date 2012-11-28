# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogAsignarFechaRecepcionPedidoActuacion.ui'
#
# Created: Sun Nov 25 16:33:22 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogAsignarFechaRecepcionPedidoActuacion(object):
    def setupUi(self, DialogAsignarFechaRecepcionPedidoActuacion):
        DialogAsignarFechaRecepcionPedidoActuacion.setObjectName(_fromUtf8("DialogAsignarFechaRecepcionPedidoActuacion"))
        DialogAsignarFechaRecepcionPedidoActuacion.resize(348, 314)
        DialogAsignarFechaRecepcionPedidoActuacion.setWindowTitle(QtGui.QApplication.translate("DialogAsignarFechaRecepcionPedidoActuacion", "Asignar Fecha de Recepcion a Pedido de Actuacion", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(DialogAsignarFechaRecepcionPedidoActuacion)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(DialogAsignarFechaRecepcionPedidoActuacion)
        self.groupBox.setTitle(QtGui.QApplication.translate("DialogAsignarFechaRecepcionPedidoActuacion", "Informacion de Pedido de Actuacion:   ", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setText(QtGui.QApplication.translate("DialogAsignarFechaRecepcionPedidoActuacion", "Nro Pedido Actuacion:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.labelNroPedido = QtGui.QLabel(self.groupBox)
        self.labelNroPedido.setText(QtGui.QApplication.translate("DialogAsignarFechaRecepcionPedidoActuacion", "<nro pedido de actuacion>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelNroPedido.setObjectName(_fromUtf8("labelNroPedido"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.labelNroPedido)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setText(QtGui.QApplication.translate("DialogAsignarFechaRecepcionPedidoActuacion", "Fecha de Realizacion:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.labelFechaRealizacionPedido = QtGui.QLabel(self.groupBox)
        self.labelFechaRealizacionPedido.setText(QtGui.QApplication.translate("DialogAsignarFechaRecepcionPedidoActuacion", "<fecha de realizacion>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelFechaRealizacionPedido.setObjectName(_fromUtf8("labelFechaRealizacionPedido"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.labelFechaRealizacionPedido)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setText(QtGui.QApplication.translate("DialogAsignarFechaRecepcionPedidoActuacion", "Repuestos Solicitados:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_5)
        self.listWidgetRepuestosDelPedido = QtGui.QListWidget(self.groupBox)
        self.listWidgetRepuestosDelPedido.setObjectName(_fromUtf8("listWidgetRepuestosDelPedido"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.listWidgetRepuestosDelPedido)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(DialogAsignarFechaRecepcionPedidoActuacion)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setText(QtGui.QApplication.translate("DialogAsignarFechaRecepcionPedidoActuacion", "Fecha de Recepcion:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.dateEditFechaRecepcioPedido = QtGui.QDateEdit(self.groupBox_2)
        self.dateEditFechaRecepcioPedido.setObjectName(_fromUtf8("dateEditFechaRecepcioPedido"))
        self.gridLayout.addWidget(self.dateEditFechaRecepcioPedido, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBoxButtonBox = QtGui.QGroupBox(DialogAsignarFechaRecepcionPedidoActuacion)
        self.groupBoxButtonBox.setMinimumSize(QtCore.QSize(271, 41))
        self.groupBoxButtonBox.setMaximumSize(QtCore.QSize(16777215, 41))
        self.groupBoxButtonBox.setTitle(_fromUtf8(""))
        self.groupBoxButtonBox.setObjectName(_fromUtf8("groupBoxButtonBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBoxButtonBox)
        self.gridLayout_2.setContentsMargins(9, 9, 9, 8)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pushButtonAceptar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonAceptar.setText(QtGui.QApplication.translate("DialogAsignarFechaRecepcionPedidoActuacion", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAceptar.setObjectName(_fromUtf8("pushButtonAceptar"))
        self.gridLayout_2.addWidget(self.pushButtonAceptar, 0, 1, 1, 1)
        self.pushButtonCancelar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("DialogAsignarFechaRecepcionPedidoActuacion", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setObjectName(_fromUtf8("pushButtonCancelar"))
        self.gridLayout_2.addWidget(self.pushButtonCancelar, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxButtonBox)

        self.retranslateUi(DialogAsignarFechaRecepcionPedidoActuacion)
        QtCore.QMetaObject.connectSlotsByName(DialogAsignarFechaRecepcionPedidoActuacion)

    def retranslateUi(self, DialogAsignarFechaRecepcionPedidoActuacion):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogAsignarFechaRecepcionPedidoActuacion = QtGui.QDialog()
    ui = Ui_DialogAsignarFechaRecepcionPedidoActuacion()
    ui.setupUi(DialogAsignarFechaRecepcionPedidoActuacion)
    DialogAsignarFechaRecepcionPedidoActuacion.show()
    sys.exit(app.exec_())

