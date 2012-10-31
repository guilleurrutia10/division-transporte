# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WidgetListadoDeVehiculos.ui'
#
# Created: Wed Oct 31 17:55:07 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_FormListadoVehiculos(object):
    def setupUi(self, FormListadoVehiculos):
        FormListadoVehiculos.setObjectName(_fromUtf8("FormListadoVehiculos"))
        FormListadoVehiculos.resize(817, 510)
        self.verticalLayout = QtGui.QVBoxLayout(FormListadoVehiculos)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.labelListadoVehiculos = QtGui.QLabel(FormListadoVehiculos)
        self.labelListadoVehiculos.setObjectName(_fromUtf8("labelListadoVehiculos"))
        self.verticalLayout.addWidget(self.labelListadoVehiculos)
        self.tableWidgetListadoDeVehiculos = QtGui.QTableWidget(FormListadoVehiculos)
        self.tableWidgetListadoDeVehiculos.setObjectName(_fromUtf8("tableWidgetListadoDeVehiculos"))
        self.tableWidgetListadoDeVehiculos.setColumnCount(5)
        self.tableWidgetListadoDeVehiculos.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetListadoDeVehiculos.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetListadoDeVehiculos.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetListadoDeVehiculos.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetListadoDeVehiculos.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetListadoDeVehiculos.setHorizontalHeaderItem(4, item)
        self.verticalLayout.addWidget(self.tableWidgetListadoDeVehiculos)

        self.retranslateUi(FormListadoVehiculos)
        QtCore.QMetaObject.connectSlotsByName(FormListadoVehiculos)

    def retranslateUi(self, FormListadoVehiculos):
        FormListadoVehiculos.setWindowTitle(QtGui.QApplication.translate("FormListadoVehiculos", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.labelListadoVehiculos.setText(QtGui.QApplication.translate("FormListadoVehiculos", "Listado de Vehículos", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidgetListadoDeVehiculos.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("FormListadoVehiculos", "Dominio", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidgetListadoDeVehiculos.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("FormListadoVehiculos", "Marca", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidgetListadoDeVehiculos.horizontalHeaderItem(2)
        item.setText(QtGui.QApplication.translate("FormListadoVehiculos", "Registro Interno", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidgetListadoDeVehiculos.horizontalHeaderItem(3)
        item.setText(QtGui.QApplication.translate("FormListadoVehiculos", "Numero de Chasis", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidgetListadoDeVehiculos.horizontalHeaderItem(4)
        item.setText(QtGui.QApplication.translate("FormListadoVehiculos", "Comisaría", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FormListadoVehiculos = QtGui.QWidget()
    ui = Ui_FormListadoVehiculos()
    ui.setupUi(FormListadoVehiculos)
    FormListadoVehiculos.show()
    sys.exit(app.exec_())

