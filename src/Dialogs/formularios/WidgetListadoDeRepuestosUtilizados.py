# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/WidgetListadoDeRepuestosUtilizados.ui'
#
# Created: Wed Oct 22 18:45:20 2014
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

class Ui_FormRepuestosUtilizados(object):
    def setupUi(self, FormRepuestosUtilizados):
        FormRepuestosUtilizados.setObjectName(_fromUtf8("FormRepuestosUtilizados"))
        FormRepuestosUtilizados.resize(941, 612)
        self.verticalLayout = QtGui.QVBoxLayout(FormRepuestosUtilizados)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(FormRepuestosUtilizados)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tableWidgetRepuestos = QtGui.QTableWidget(self.groupBox)
        self.tableWidgetRepuestos.setObjectName(_fromUtf8("tableWidgetRepuestos"))
        self.tableWidgetRepuestos.setColumnCount(6)
        self.tableWidgetRepuestos.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidgetRepuestos.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidgetRepuestos.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidgetRepuestos.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidgetRepuestos.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidgetRepuestos.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidgetRepuestos.setHorizontalHeaderItem(5, item)
        self.tableWidgetRepuestos.horizontalHeader().setDefaultSectionSize(210)
        self.tableWidgetRepuestos.horizontalHeader().setHighlightSections(True)
        self.tableWidgetRepuestos.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.tableWidgetRepuestos)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(FormRepuestosUtilizados)
        QtCore.QMetaObject.connectSlotsByName(FormRepuestosUtilizados)

    def retranslateUi(self, FormRepuestosUtilizados):
        FormRepuestosUtilizados.setWindowTitle(_translate("FormRepuestosUtilizados", "Form", None))
        self.groupBox.setTitle(_translate("FormRepuestosUtilizados", "Listado de Repuestos Utilizados", None))
        item = self.tableWidgetRepuestos.horizontalHeaderItem(0)
        item.setText(_translate("FormRepuestosUtilizados", "Código", None))
        item = self.tableWidgetRepuestos.horizontalHeaderItem(1)
        item.setText(_translate("FormRepuestosUtilizados", "Nombre", None))
        item = self.tableWidgetRepuestos.horizontalHeaderItem(2)
        item.setText(_translate("FormRepuestosUtilizados", "Descripción", None))
        item = self.tableWidgetRepuestos.horizontalHeaderItem(3)
        item.setText(_translate("FormRepuestosUtilizados", "Número Pedido de Actuación", None))
        item = self.tableWidgetRepuestos.horizontalHeaderItem(4)
        item.setText(_translate("FormRepuestosUtilizados", "Número Orden de Reparación", None))
        item = self.tableWidgetRepuestos.horizontalHeaderItem(5)
        item.setText(_translate("FormRepuestosUtilizados", "Dominio del Vehículo", None))

