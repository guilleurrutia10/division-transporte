# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogCambiarDeSeccionUnEmpleado.ui'
#
# Created: Wed Dec 05 21:18:56 2012
#      by: PyQt4 UI code generator 4.8.6
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
        DialogCambiarDeSeccionUnEmpleado.resize(623, 476)
        DialogCambiarDeSeccionUnEmpleado.setWindowTitle(QtGui.QApplication.translate("DialogCambiarDeSeccionUnEmpleado", "Cambiar De Seccion Un Empleado", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout = QtGui.QGridLayout(DialogCambiarDeSeccionUnEmpleado)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(DialogCambiarDeSeccionUnEmpleado)
        self.groupBox.setMinimumSize(QtCore.QSize(234, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(234, 56))
        self.groupBox.setTitle(QtGui.QApplication.translate("DialogCambiarDeSeccionUnEmpleado", "Buscar por Nº Documento", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lineEditFiltrarDocumento = QtGui.QLineEdit(self.groupBox)
        self.lineEditFiltrarDocumento.setMinimumSize(QtCore.QSize(133, 20))
        self.lineEditFiltrarDocumento.setObjectName(_fromUtf8("lineEditFiltrarDocumento"))
        self.horizontalLayout_2.addWidget(self.lineEditFiltrarDocumento)
        self.pushButtonFiltrarDocumento = QtGui.QPushButton(self.groupBox)
        self.pushButtonFiltrarDocumento.setText(QtGui.QApplication.translate("DialogCambiarDeSeccionUnEmpleado", "Filtrar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonFiltrarDocumento.setObjectName(_fromUtf8("pushButtonFiltrarDocumento"))
        self.horizontalLayout_2.addWidget(self.pushButtonFiltrarDocumento)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)
        self.groupBox_2 = QtGui.QGroupBox(DialogCambiarDeSeccionUnEmpleado)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_2.setMaximumSize(QtCore.QSize(234, 56))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("DialogCambiarDeSeccionUnEmpleado", "Buscar por Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEditFiltrarNombre = QtGui.QLineEdit(self.groupBox_2)
        self.lineEditFiltrarNombre.setMinimumSize(QtCore.QSize(133, 20))
        self.lineEditFiltrarNombre.setObjectName(_fromUtf8("lineEditFiltrarNombre"))
        self.horizontalLayout.addWidget(self.lineEditFiltrarNombre)
        self.pushButtonFiltrarNombre = QtGui.QPushButton(self.groupBox_2)
        self.pushButtonFiltrarNombre.setText(QtGui.QApplication.translate("DialogCambiarDeSeccionUnEmpleado", "Filtrar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonFiltrarNombre.setObjectName(_fromUtf8("pushButtonFiltrarNombre"))
        self.horizontalLayout.addWidget(self.pushButtonFiltrarNombre)
        self.gridLayout.addWidget(self.groupBox_2, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(185, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        self.tableWidget = QtGui.QTableWidget(DialogCambiarDeSeccionUnEmpleado)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogCambiarDeSeccionUnEmpleado", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogCambiarDeSeccionUnEmpleado", "Tipo de Documento", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogCambiarDeSeccionUnEmpleado", "Nº Documento", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogCambiarDeSeccionUnEmpleado", "Sección", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogCambiarDeSeccionUnEmpleado", "Fecha de Nac.", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogCambiarDeSeccionUnEmpleado", "Email", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 4)
        self.groupBoxButtonBox = QtGui.QGroupBox(DialogCambiarDeSeccionUnEmpleado)
        self.groupBoxButtonBox.setMinimumSize(QtCore.QSize(271, 41))
        self.groupBoxButtonBox.setMaximumSize(QtCore.QSize(16777215, 41))
        self.groupBoxButtonBox.setTitle(_fromUtf8(""))
        self.groupBoxButtonBox.setObjectName(_fromUtf8("groupBoxButtonBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBoxButtonBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        self.pushButton_Cambiar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButton_Cambiar.setText(QtGui.QApplication.translate("DialogCambiarDeSeccionUnEmpleado", "Cambiar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Cambiar.setObjectName(_fromUtf8("pushButton_Cambiar"))
        self.gridLayout_2.addWidget(self.pushButton_Cambiar, 0, 1, 1, 1)
        self.pushButtonAceptar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonAceptar.setText(QtGui.QApplication.translate("DialogCambiarDeSeccionUnEmpleado", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAceptar.setObjectName(_fromUtf8("pushButtonAceptar"))
        self.gridLayout_2.addWidget(self.pushButtonAceptar, 0, 2, 1, 1)
        self.pushButtonCancelar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("DialogCambiarDeSeccionUnEmpleado", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setObjectName(_fromUtf8("pushButtonCancelar"))
        self.gridLayout_2.addWidget(self.pushButtonCancelar, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.groupBoxButtonBox, 2, 0, 1, 4)

        self.retranslateUi(DialogCambiarDeSeccionUnEmpleado)
        QtCore.QMetaObject.connectSlotsByName(DialogCambiarDeSeccionUnEmpleado)

    def retranslateUi(self, DialogCambiarDeSeccionUnEmpleado):
        item = self.tableWidget.horizontalHeaderItem(0)
        item = self.tableWidget.horizontalHeaderItem(1)
        item = self.tableWidget.horizontalHeaderItem(2)
        item = self.tableWidget.horizontalHeaderItem(3)
        item = self.tableWidget.horizontalHeaderItem(4)
        item = self.tableWidget.horizontalHeaderItem(5)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogCambiarDeSeccionUnEmpleado = QtGui.QDialog()
    ui = Ui_DialogCambiarDeSeccionUnEmpleado()
    ui.setupUi(DialogCambiarDeSeccionUnEmpleado)
    DialogCambiarDeSeccionUnEmpleado.show()
    sys.exit(app.exec_())

