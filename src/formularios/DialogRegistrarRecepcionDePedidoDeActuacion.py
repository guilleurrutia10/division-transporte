# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogRegistrarRecepcionDePedidoDeActuacion.ui'
#
# Created: Sun Nov 25 16:33:41 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogRegistrarRecepcionDePedidoDeActuacion(object):
    def setupUi(self, DialogRegistrarRecepcionDePedidoDeActuacion):
        DialogRegistrarRecepcionDePedidoDeActuacion.setObjectName(_fromUtf8("DialogRegistrarRecepcionDePedidoDeActuacion"))
        DialogRegistrarRecepcionDePedidoDeActuacion.resize(572, 416)
        DialogRegistrarRecepcionDePedidoDeActuacion.setWindowTitle(QtGui.QApplication.translate("DialogRegistrarRecepcionDePedidoDeActuacion", "Registrar Recepcion de Pedido de Actuacion", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(DialogRegistrarRecepcionDePedidoDeActuacion)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(DialogRegistrarRecepcionDePedidoDeActuacion)
        self.groupBox.setTitle(QtGui.QApplication.translate("DialogRegistrarRecepcionDePedidoDeActuacion", "Pedidos deActuacion", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tableWidget = QtGui.QTableWidget(self.groupBox)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_2.setTitle(QtGui.QApplication.translate("DialogRegistrarRecepcionDePedidoDeActuacion", "Nro Pedido de Actuacion:  ", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout_2.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.pushButton_FiltroNroPedido = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_FiltroNroPedido.setText(QtGui.QApplication.translate("DialogRegistrarRecepcionDePedidoDeActuacion", "Filtrar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_FiltroNroPedido.setObjectName(_fromUtf8("pushButton_FiltroNroPedido"))
        self.gridLayout_2.addWidget(self.pushButton_FiltroNroPedido, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.pushButton_Registrar = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_Registrar.setText(QtGui.QApplication.translate("DialogRegistrarRecepcionDePedidoDeActuacion", "Registrar Recepcion", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Registrar.setObjectName(_fromUtf8("pushButton_Registrar"))
        self.gridLayout_3.addWidget(self.pushButton_Registrar, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_3, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBoxButtonBox = QtGui.QGroupBox(DialogRegistrarRecepcionDePedidoDeActuacion)
        self.groupBoxButtonBox.setMinimumSize(QtCore.QSize(271, 41))
        self.groupBoxButtonBox.setMaximumSize(QtCore.QSize(16777215, 41))
        self.groupBoxButtonBox.setTitle(_fromUtf8(""))
        self.groupBoxButtonBox.setObjectName(_fromUtf8("groupBoxButtonBox"))
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBoxButtonBox)
        self.gridLayout_6.setContentsMargins(9, 9, 9, 8)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.pushButtonAceptar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonAceptar.setText(QtGui.QApplication.translate("DialogRegistrarRecepcionDePedidoDeActuacion", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAceptar.setObjectName(_fromUtf8("pushButtonAceptar"))
        self.gridLayout_6.addWidget(self.pushButtonAceptar, 0, 1, 1, 1)
        self.pushButtonCancelar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("DialogRegistrarRecepcionDePedidoDeActuacion", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setObjectName(_fromUtf8("pushButtonCancelar"))
        self.gridLayout_6.addWidget(self.pushButtonCancelar, 0, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem2, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxButtonBox)

        self.retranslateUi(DialogRegistrarRecepcionDePedidoDeActuacion)
        QtCore.QMetaObject.connectSlotsByName(DialogRegistrarRecepcionDePedidoDeActuacion)

    def retranslateUi(self, DialogRegistrarRecepcionDePedidoDeActuacion):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogRegistrarRecepcionDePedidoDeActuacion = QtGui.QDialog()
    ui = Ui_DialogRegistrarRecepcionDePedidoDeActuacion()
    ui.setupUi(DialogRegistrarRecepcionDePedidoDeActuacion)
    DialogRegistrarRecepcionDePedidoDeActuacion.show()
    sys.exit(app.exec_())

