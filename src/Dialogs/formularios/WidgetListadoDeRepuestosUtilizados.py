# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/WidgetListadoDeRepuestosUtilizados.ui'
#
# Created: Thu Aug 28 13:29:14 2014
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
        self.tableWidget = QtGui.QTableWidget(self.groupBox)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(210)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(FormRepuestosUtilizados)
        QtCore.QMetaObject.connectSlotsByName(FormRepuestosUtilizados)

    def retranslateUi(self, FormRepuestosUtilizados):
        FormRepuestosUtilizados.setWindowTitle(_translate("FormRepuestosUtilizados", "Form", None))
        self.groupBox.setTitle(_translate("FormRepuestosUtilizados", "Listado de Repuestos Utilizados", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("FormRepuestosUtilizados", "Código", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("FormRepuestosUtilizados", "Nombre", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("FormRepuestosUtilizados", "Descripción", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("FormRepuestosUtilizados", "Número Pedido de Actuación", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("FormRepuestosUtilizados", "Número Orden de Reparación", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("FormRepuestosUtilizados", "Dominio del Vehículo", None))

