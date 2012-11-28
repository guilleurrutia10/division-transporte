# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WidgetListadoDeRepuestosUtilizados.ui'
#
# Created: Sun Nov 25 16:33:51 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_FormRepuestosUtilizados(object):
    def setupUi(self, FormRepuestosUtilizados):
        FormRepuestosUtilizados.setObjectName(_fromUtf8("FormRepuestosUtilizados"))
        FormRepuestosUtilizados.resize(941, 612)
        FormRepuestosUtilizados.setWindowTitle(QtGui.QApplication.translate("FormRepuestosUtilizados", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(FormRepuestosUtilizados)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(FormRepuestosUtilizados)
        self.groupBox.setTitle(QtGui.QApplication.translate("FormRepuestosUtilizados", "Listado de Repuestos Utilizados", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tableWidget = QtGui.QTableWidget(self.groupBox)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("FormRepuestosUtilizados", "Codigo", None, QtGui.QApplication.UnicodeUTF8))
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("FormRepuestosUtilizados", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("FormRepuestosUtilizados", "Descripción", None, QtGui.QApplication.UnicodeUTF8))
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("FormRepuestosUtilizados", "Número Pedido de Actuacion", None, QtGui.QApplication.UnicodeUTF8))
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("FormRepuestosUtilizados", "Número Orden de Reparación", None, QtGui.QApplication.UnicodeUTF8))
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("FormRepuestosUtilizados", "Dominio del Vehículo", None, QtGui.QApplication.UnicodeUTF8))
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(FormRepuestosUtilizados)
        QtCore.QMetaObject.connectSlotsByName(FormRepuestosUtilizados)

    def retranslateUi(self, FormRepuestosUtilizados):
        item = self.tableWidget.horizontalHeaderItem(0)
        item = self.tableWidget.horizontalHeaderItem(1)
        item = self.tableWidget.horizontalHeaderItem(2)
        item = self.tableWidget.horizontalHeaderItem(3)
        item = self.tableWidget.horizontalHeaderItem(4)
        item = self.tableWidget.horizontalHeaderItem(5)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FormRepuestosUtilizados = QtGui.QWidget()
    ui = Ui_FormRepuestosUtilizados()
    ui.setupUi(FormRepuestosUtilizados)
    FormRepuestosUtilizados.show()
    sys.exit(app.exec_())

