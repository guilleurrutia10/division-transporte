# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogCambiarDeSeccionUnEmpleado.ui'
#
# Created: Wed Nov 14 18:14:38 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogCambiarDeSeccionUnEmpleado(object):
    def setupUi(self, DialogCambiarDeSeccionUnEmpleado):
        DialogCambiarDeSeccionUnEmpleado.setObjectName(_fromUtf8("DialogCambiarDeSeccionUnEmpleado"))
        DialogCambiarDeSeccionUnEmpleado.resize(609, 311)
        self.gridLayout = QtGui.QGridLayout(DialogCambiarDeSeccionUnEmpleado)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(DialogCambiarDeSeccionUnEmpleado)
        self.groupBox.setMinimumSize(QtCore.QSize(331, 41))
        self.groupBox.setMaximumSize(QtCore.QSize(331, 41))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.listView = QtGui.QListView(self.groupBox)
        self.listView.setGeometry(QtCore.QRect(20, 20, 211, 16))
        self.listView.setMinimumSize(QtCore.QSize(211, 16))
        self.listView.setMaximumSize(QtCore.QSize(211, 16))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 20, 75, 16))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)
        self.groupBox_2 = QtGui.QGroupBox(DialogCambiarDeSeccionUnEmpleado)
        self.groupBox_2.setMinimumSize(QtCore.QSize(331, 41))
        self.groupBox_2.setMaximumSize(QtCore.QSize(331, 41))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.listView_3 = QtGui.QListView(self.groupBox_2)
        self.listView_3.setGeometry(QtCore.QRect(20, 20, 211, 16))
        self.listView_3.setMinimumSize(QtCore.QSize(211, 16))
        self.listView_3.setMaximumSize(QtCore.QSize(211, 16))
        self.listView_3.setObjectName(_fromUtf8("listView_3"))
        self.pushButton_4 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_4.setGeometry(QtCore.QRect(240, 20, 75, 16))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 2)
        self.tableWidget = QtGui.QTableWidget(DialogCambiarDeSeccionUnEmpleado)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.gridLayout.addWidget(self.tableWidget, 2, 0, 1, 2)
        self.groupBoxButtonBox = QtGui.QGroupBox(DialogCambiarDeSeccionUnEmpleado)
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
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBoxButtonBox, 5, 0, 1, 2)
        self.widget = QtGui.QWidget(DialogCambiarDeSeccionUnEmpleado)
        self.widget.setMinimumSize(QtCore.QSize(431, 41))
        self.widget.setMaximumSize(QtCore.QSize(431, 41))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.widget)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.pushButton_Cambiar = QtGui.QPushButton(self.widget)
        self.pushButton_Cambiar.setObjectName(_fromUtf8("pushButton_Cambiar"))
        self.gridLayout_3.addWidget(self.pushButton_Cambiar, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(163, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.widget, 4, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 4, 0, 1, 1)

        self.retranslateUi(DialogCambiarDeSeccionUnEmpleado)
        QtCore.QMetaObject.connectSlotsByName(DialogCambiarDeSeccionUnEmpleado)

    def retranslateUi(self, DialogCambiarDeSeccionUnEmpleado):
        DialogCambiarDeSeccionUnEmpleado.setWindowTitle(QtGui.QApplication.translate("DialogCambiarDeSeccionUnEmpleado", "Cambiar De Seccion Un Empleado", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("DialogCambiarDeSeccionUnEmpleado", "Buscar por Nº Documento", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("DialogCambiarDeSeccionUnEmpleado", "Filtrar", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("DialogCambiarDeSeccionUnEmpleado", "Buscar por Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("DialogCambiarDeSeccionUnEmpleado", "Filtrar", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("DialogCambiarDeSeccionUnEmpleado", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("DialogCambiarDeSeccionUnEmpleado", "Tipo de Documento", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(QtGui.QApplication.translate("DialogCambiarDeSeccionUnEmpleado", "Nº Documento", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(QtGui.QApplication.translate("DialogCambiarDeSeccionUnEmpleado", "Sección", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(QtGui.QApplication.translate("DialogCambiarDeSeccionUnEmpleado", "Fecha de Nac.", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(QtGui.QApplication.translate("DialogCambiarDeSeccionUnEmpleado", "Email", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAceptar.setText(QtGui.QApplication.translate("DialogCambiarDeSeccionUnEmpleado", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("DialogCambiarDeSeccionUnEmpleado", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Cambiar.setText(QtGui.QApplication.translate("DialogCambiarDeSeccionUnEmpleado", "Cambiar", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogCambiarDeSeccionUnEmpleado = QtGui.QDialog()
    ui = Ui_DialogCambiarDeSeccionUnEmpleado()
    ui.setupUi(DialogCambiarDeSeccionUnEmpleado)
    DialogCambiarDeSeccionUnEmpleado.show()
    sys.exit(app.exec_())

