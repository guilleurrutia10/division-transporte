# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/DialogRegistrarRecepcionDePedidoDeActuacion.ui'
#
# Created: Fri Aug  8 20:01:04 2014
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

class Ui_DialogRegistrarRecepcionDePedidoDeActuacion(object):
    def setupUi(self, DialogRegistrarRecepcionDePedidoDeActuacion):
        DialogRegistrarRecepcionDePedidoDeActuacion.setObjectName(_fromUtf8("DialogRegistrarRecepcionDePedidoDeActuacion"))
        DialogRegistrarRecepcionDePedidoDeActuacion.resize(600, 400)
        DialogRegistrarRecepcionDePedidoDeActuacion.setMinimumSize(QtCore.QSize(600, 400))
        self.verticalLayout = QtGui.QVBoxLayout(DialogRegistrarRecepcionDePedidoDeActuacion)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(DialogRegistrarRecepcionDePedidoDeActuacion)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tableWidget = QtGui.QTableWidget(self.groupBox)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout_2.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.pushButton_FiltroNroPedido = QtGui.QPushButton(self.groupBox_2)
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
        self.pushButtonHecho = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonHecho.setObjectName(_fromUtf8("pushButtonHecho"))
        self.gridLayout_6.addWidget(self.pushButtonHecho, 0, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem2, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxButtonBox)

        self.retranslateUi(DialogRegistrarRecepcionDePedidoDeActuacion)
        QtCore.QObject.connect(self.pushButtonHecho, QtCore.SIGNAL(_fromUtf8("clicked()")), DialogRegistrarRecepcionDePedidoDeActuacion.accept)
        QtCore.QObject.connect(self.pushButtonHecho, QtCore.SIGNAL(_fromUtf8("pressed()")), DialogRegistrarRecepcionDePedidoDeActuacion.accept)
        QtCore.QMetaObject.connectSlotsByName(DialogRegistrarRecepcionDePedidoDeActuacion)

    def retranslateUi(self, DialogRegistrarRecepcionDePedidoDeActuacion):
        DialogRegistrarRecepcionDePedidoDeActuacion.setWindowTitle(_translate("DialogRegistrarRecepcionDePedidoDeActuacion", "Registrar Recepcion de Pedido de Actuacion", None))
        self.groupBox.setTitle(_translate("DialogRegistrarRecepcionDePedidoDeActuacion", "Pedidos deActuación", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("DialogRegistrarRecepcionDePedidoDeActuacion", "Número Pedido", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("DialogRegistrarRecepcionDePedidoDeActuacion", "Fecha de Realización", None))
        self.groupBox_2.setTitle(_translate("DialogRegistrarRecepcionDePedidoDeActuacion", "Nro Pedido de Actuación:  ", None))
        self.pushButton_FiltroNroPedido.setText(_translate("DialogRegistrarRecepcionDePedidoDeActuacion", "Filtrar", None))
        self.pushButton_Registrar.setText(_translate("DialogRegistrarRecepcionDePedidoDeActuacion", "Registrar Recepción", None))
        self.pushButtonHecho.setText(_translate("DialogRegistrarRecepcionDePedidoDeActuacion", "Hecho", None))

