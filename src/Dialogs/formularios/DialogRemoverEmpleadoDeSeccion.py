# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogRemoverEmpleadoDeSeccion.ui'
#
# Created: Tue Mar 18 18:37:48 2014
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Utiles_formulario import TablaEmpleadosSeccion

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogRemoverEmpleadoDeSeccion(object):
    def setupUi(self, DialogRemoverEmpleadoDeSeccion):
        DialogRemoverEmpleadoDeSeccion.setObjectName(_fromUtf8("DialogRemoverEmpleadoDeSeccion"))
        DialogRemoverEmpleadoDeSeccion.resize(720, 411)
        DialogRemoverEmpleadoDeSeccion.setMinimumSize(QtCore.QSize(720, 0))
        DialogRemoverEmpleadoDeSeccion.setWindowTitle(QtGui.QApplication.translate("DialogRemoverEmpleadoDeSeccion", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout = QtGui.QGridLayout(DialogRemoverEmpleadoDeSeccion)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(DialogRemoverEmpleadoDeSeccion)
        self.groupBox.setMinimumSize(QtCore.QSize(331, 41))
        self.groupBox.setMaximumSize(QtCore.QSize(331, 41))
        self.groupBox.setTitle(QtGui.QApplication.translate("DialogRemoverEmpleadoDeSeccion", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.pushButton_filtroSeccion = QtGui.QPushButton(self.groupBox)
        self.pushButton_filtroSeccion.setGeometry(QtCore.QRect(240, 20, 75, 16))
        self.pushButton_filtroSeccion.setText(QtGui.QApplication.translate("DialogRemoverEmpleadoDeSeccion", "Filtrar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_filtroSeccion.setObjectName(_fromUtf8("pushButton_filtroSeccion"))
        self.lineEdit_condicionDeFiltro = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_condicionDeFiltro.setGeometry(QtCore.QRect(10, 20, 221, 16))
        self.lineEdit_condicionDeFiltro.setObjectName(_fromUtf8("lineEdit_condicionDeFiltro"))
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)
        #self.tableWidget_empleados = QtGui.QTableWidget(DialogRemoverEmpleadoDeSeccion)
        self.tableWidget_empleados = TablaEmpleadosSeccion(DialogRemoverEmpleadoDeSeccion)
        self.tableWidget_empleados.setMinimumSize(QtCore.QSize(603, 181))
        self.tableWidget_empleados.setObjectName(_fromUtf8("tableWidget_empleados"))
        self.tableWidget_empleados.setColumnCount(7)
        self.tableWidget_empleados.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogRemoverEmpleadoDeSeccion", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_empleados.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogRemoverEmpleadoDeSeccion", "Apellido", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_empleados.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogRemoverEmpleadoDeSeccion", "Tipo de Documento", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_empleados.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogRemoverEmpleadoDeSeccion", "Nº Documento", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_empleados.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogRemoverEmpleadoDeSeccion", "Fecha de nacimiento", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_empleados.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogRemoverEmpleadoDeSeccion", "Email", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_empleados.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogRemoverEmpleadoDeSeccion", "Sección", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_empleados.setHorizontalHeaderItem(6, item)
        self.gridLayout.addWidget(self.tableWidget_empleados, 1, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(201, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.widget = QtGui.QWidget(DialogRemoverEmpleadoDeSeccion)
        self.widget.setMinimumSize(QtCore.QSize(431, 41))
        self.widget.setMaximumSize(QtCore.QSize(431, 41))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(304, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_removerEmpleados = QtGui.QPushButton(self.widget)
        self.pushButton_removerEmpleados.setText(QtGui.QApplication.translate("DialogRemoverEmpleadoDeSeccion", "Remover Empleado", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_removerEmpleados.setObjectName(_fromUtf8("pushButton_removerEmpleados"))
        self.horizontalLayout.addWidget(self.pushButton_removerEmpleados)
        self.gridLayout.addWidget(self.widget, 2, 1, 1, 1)
        self.groupBoxButtonBox = QtGui.QGroupBox(DialogRemoverEmpleadoDeSeccion)
        self.groupBoxButtonBox.setMinimumSize(QtCore.QSize(271, 41))
        self.groupBoxButtonBox.setMaximumSize(QtCore.QSize(16777215, 41))
        self.groupBoxButtonBox.setTitle(_fromUtf8(""))
        self.groupBoxButtonBox.setObjectName(_fromUtf8("groupBoxButtonBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBoxButtonBox)
        self.gridLayout_2.setContentsMargins(9, 9, 9, 8)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pushButtonAceptar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonAceptar.setText(QtGui.QApplication.translate("DialogRemoverEmpleadoDeSeccion", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAceptar.setObjectName(_fromUtf8("pushButtonAceptar"))
        self.gridLayout_2.addWidget(self.pushButtonAceptar, 0, 1, 1, 1)
        self.pushButtonCancelar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("DialogRemoverEmpleadoDeSeccion", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setObjectName(_fromUtf8("pushButtonCancelar"))
        self.gridLayout_2.addWidget(self.pushButtonCancelar, 0, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBoxButtonBox, 3, 0, 1, 2)

        self.retranslateUi(DialogRemoverEmpleadoDeSeccion)
        QtCore.QObject.connect(self.pushButtonAceptar, QtCore.SIGNAL(_fromUtf8("clicked()")), DialogRemoverEmpleadoDeSeccion.accept)
        QtCore.QObject.connect(self.pushButtonCancelar, QtCore.SIGNAL(_fromUtf8("clicked()")), DialogRemoverEmpleadoDeSeccion.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogRemoverEmpleadoDeSeccion)

    def retranslateUi(self, DialogRemoverEmpleadoDeSeccion):
        item = self.tableWidget_empleados.horizontalHeaderItem(0)
        item = self.tableWidget_empleados.horizontalHeaderItem(1)
        item = self.tableWidget_empleados.horizontalHeaderItem(2)
        item = self.tableWidget_empleados.horizontalHeaderItem(3)
        item = self.tableWidget_empleados.horizontalHeaderItem(4)
        item = self.tableWidget_empleados.horizontalHeaderItem(5)
        item = self.tableWidget_empleados.horizontalHeaderItem(6)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogRemoverEmpleadoDeSeccion = QtGui.QDialog()
    ui = Ui_DialogRemoverEmpleadoDeSeccion()
    ui.setupUi(DialogRemoverEmpleadoDeSeccion)
    DialogRemoverEmpleadoDeSeccion.show()
    sys.exit(app.exec_())

