# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogCambiarDeSeccionUnEmpleado.ui'
#
# Created: Wed Feb 19 15:09:10 2014
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!
# Se modifico para agregarle el icono
from PyQt4 import QtCore, QtGui
from Utiles_formulario import TablaEmpleadosSeccion

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogCambiarDeSeccionUnEmpleado(object):
    def setupUi(self, DialogCambiarDeSeccionUnEmpleado):
        DialogCambiarDeSeccionUnEmpleado.setObjectName(_fromUtf8("DialogCambiarDeSeccionUnEmpleado"))
        DialogCambiarDeSeccionUnEmpleado.resize(723, 452)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/recursos/iconos/personal/change_person-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogCambiarDeSeccionUnEmpleado.setWindowIcon(icon)
        DialogCambiarDeSeccionUnEmpleado.setMaximumSize(QtCore.QSize(723, 16777215))
        DialogCambiarDeSeccionUnEmpleado.setWindowTitle(QtGui.QApplication.translate("DialogCambiarDeSeccionUnEmpleado", "Cambiar De Seccion Un Empleado", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout = QtGui.QGridLayout(DialogCambiarDeSeccionUnEmpleado)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(DialogCambiarDeSeccionUnEmpleado)
        self.groupBox.setMinimumSize(QtCore.QSize(234, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(234, 56))
        self.groupBox.setTitle(QtGui.QApplication.translate("DialogCambiarDeSeccionUnEmpleado", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lineEditFiltro = QtGui.QLineEdit(self.groupBox)
        self.lineEditFiltro.setMinimumSize(QtCore.QSize(133, 20))
        self.lineEditFiltro.setObjectName(_fromUtf8("lineEditFiltro"))
        self.horizontalLayout_2.addWidget(self.lineEditFiltro)
        self.pushButtonFiltrar = QtGui.QPushButton(self.groupBox)
        self.pushButtonFiltrar.setText(QtGui.QApplication.translate("DialogCambiarDeSeccionUnEmpleado", "Filtrar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonFiltrar.setObjectName(_fromUtf8("pushButtonFiltrar"))
        self.horizontalLayout_2.addWidget(self.pushButtonFiltrar)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)
        self.groupBoxButtonBox = QtGui.QGroupBox(DialogCambiarDeSeccionUnEmpleado)
        self.groupBoxButtonBox.setMinimumSize(QtCore.QSize(271, 41))
        self.groupBoxButtonBox.setMaximumSize(QtCore.QSize(16777215, 41))
        self.groupBoxButtonBox.setTitle(_fromUtf8(""))
        self.groupBoxButtonBox.setObjectName(_fromUtf8("groupBoxButtonBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBoxButtonBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.pushButtonAceptar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonAceptar.setText(QtGui.QApplication.translate("DialogCambiarDeSeccionUnEmpleado", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAceptar.setObjectName(_fromUtf8("pushButtonAceptar"))
        self.gridLayout_2.addWidget(self.pushButtonAceptar, 0, 2, 1, 1)
        self.pushButtonCancelar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("DialogCambiarDeSeccionUnEmpleado", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setObjectName(_fromUtf8("pushButtonCancelar"))
        self.gridLayout_2.addWidget(self.pushButtonCancelar, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.groupBoxButtonBox, 4, 0, 1, 3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(800, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonCambiar = QtGui.QPushButton(DialogCambiarDeSeccionUnEmpleado)
        self.pushButtonCambiar.setText(QtGui.QApplication.translate("DialogCambiarDeSeccionUnEmpleado", "Cambiar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCambiar.setObjectName(_fromUtf8("pushButtonCambiar"))
        self.horizontalLayout.addWidget(self.pushButtonCambiar)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        #self.tableWidgetEmpleados = QtGui.QTableWidget(DialogCambiarDeSeccionUnEmpleado)
        self.tableWidgetEmpleados = TablaEmpleadosSeccion(DialogCambiarDeSeccionUnEmpleado)
        self.tableWidgetEmpleados.setObjectName(_fromUtf8("tableWidgetEmpleados"))
        self.tableWidgetEmpleados.setColumnCount(7)
        self.tableWidgetEmpleados.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogCambiarDeSeccionUnEmpleado", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetEmpleados.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogCambiarDeSeccionUnEmpleado", "Apellido", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetEmpleados.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogCambiarDeSeccionUnEmpleado", "Tipo de Documento", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetEmpleados.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogCambiarDeSeccionUnEmpleado", "Nº Documento", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetEmpleados.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogCambiarDeSeccionUnEmpleado", "Fecha de Nac.", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetEmpleados.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogCambiarDeSeccionUnEmpleado", "Email", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetEmpleados.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogCambiarDeSeccionUnEmpleado", "Sección", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetEmpleados.setHorizontalHeaderItem(6, item)
        self.tableWidgetEmpleados.horizontalHeader().setMinimumSectionSize(25)
        self.tableWidgetEmpleados.verticalHeader().setDefaultSectionSize(30)
        self.gridLayout.addWidget(self.tableWidgetEmpleados, 1, 0, 1, 3)

        self.retranslateUi(DialogCambiarDeSeccionUnEmpleado)
        QtCore.QMetaObject.connectSlotsByName(DialogCambiarDeSeccionUnEmpleado)

    def retranslateUi(self, DialogCambiarDeSeccionUnEmpleado):
        item = self.tableWidgetEmpleados.horizontalHeaderItem(0)
        item = self.tableWidgetEmpleados.horizontalHeaderItem(1)
        item = self.tableWidgetEmpleados.horizontalHeaderItem(2)
        item = self.tableWidgetEmpleados.horizontalHeaderItem(3)
        item = self.tableWidgetEmpleados.horizontalHeaderItem(4)
        item = self.tableWidgetEmpleados.horizontalHeaderItem(5)
        item = self.tableWidgetEmpleados.horizontalHeaderItem(6)

import recursos_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogCambiarDeSeccionUnEmpleado = QtGui.QDialog()
    ui = Ui_DialogCambiarDeSeccionUnEmpleado()
    ui.setupUi(DialogCambiarDeSeccionUnEmpleado)
    DialogCambiarDeSeccionUnEmpleado.show()
    sys.exit(app.exec_())

