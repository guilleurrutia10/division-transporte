# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogAsignarReparacion.ui'
#
# Created: Wed Nov 14 18:14:37 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogAsignarReparacion(object):
    def setupUi(self, DialogAsignarReparacion):
        DialogAsignarReparacion.setObjectName(_fromUtf8("DialogAsignarReparacion"))
        DialogAsignarReparacion.resize(706, 504)
        self.verticalLayout = QtGui.QVBoxLayout(DialogAsignarReparacion)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(DialogAsignarReparacion)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.tableWidgetReparacion = QtGui.QTableWidget(self.groupBox)
        self.tableWidgetReparacion.setObjectName(_fromUtf8("tableWidgetReparacion"))
        self.tableWidgetReparacion.setColumnCount(3)
        self.tableWidgetReparacion.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetReparacion.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetReparacion.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetReparacion.setHorizontalHeaderItem(2, item)
        self.horizontalLayout_2.addWidget(self.tableWidgetReparacion)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(DialogAsignarReparacion)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButtonNombre = QtGui.QPushButton(self.groupBox_3)
        self.pushButtonNombre.setObjectName(_fromUtf8("pushButtonNombre"))
        self.horizontalLayout.addWidget(self.pushButtonNombre)
        self.lineEditNombre = QtGui.QLineEdit(self.groupBox_3)
        self.lineEditNombre.setObjectName(_fromUtf8("lineEditNombre"))
        self.horizontalLayout.addWidget(self.lineEditNombre)
        self.gridLayout.addWidget(self.groupBox_3, 0, 0, 2, 2)
        spacerItem = QtGui.QSpacerItem(148, 28, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 3)
        spacerItem1 = QtGui.QSpacerItem(48, 238, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 4, 2, 1)
        self.tableWidgetEmpleados = QtGui.QTableWidget(self.groupBox_2)
        self.tableWidgetEmpleados.setObjectName(_fromUtf8("tableWidgetEmpleados"))
        self.tableWidgetEmpleados.setColumnCount(2)
        self.tableWidgetEmpleados.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetEmpleados.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetEmpleados.setHorizontalHeaderItem(1, item)
        self.tableWidgetEmpleados.horizontalHeader().setDefaultSectionSize(120)
        self.gridLayout.addWidget(self.tableWidgetEmpleados, 2, 0, 1, 4)
        self.pushButtonAsignarResponsable = QtGui.QPushButton(self.groupBox_2)
        self.pushButtonAsignarResponsable.setObjectName(_fromUtf8("pushButtonAsignarResponsable"))
        self.gridLayout.addWidget(self.pushButtonAsignarResponsable, 3, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(149, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 1, 1, 2)
        spacerItem3 = QtGui.QSpacerItem(20, 71, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 3, 3, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBoxButtonBox = QtGui.QGroupBox(DialogAsignarReparacion)
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
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxButtonBox)

        self.retranslateUi(DialogAsignarReparacion)
        QtCore.QMetaObject.connectSlotsByName(DialogAsignarReparacion)

    def retranslateUi(self, DialogAsignarReparacion):
        DialogAsignarReparacion.setWindowTitle(QtGui.QApplication.translate("DialogAsignarReparacion", "Asignar Encargados de Reparacion", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("DialogAsignarReparacion", "Reparación", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidgetReparacion.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("DialogAsignarReparacion", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidgetReparacion.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("DialogAsignarReparacion", "Descripcion", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidgetReparacion.horizontalHeaderItem(2)
        item.setText(QtGui.QApplication.translate("DialogAsignarReparacion", "Tiempo Estimado", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("DialogAsignarReparacion", "Empleados", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonNombre.setText(QtGui.QApplication.translate("DialogAsignarReparacion", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidgetEmpleados.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("DialogAsignarReparacion", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidgetEmpleados.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("DialogAsignarReparacion", "Numero de Documento", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAsignarResponsable.setText(QtGui.QApplication.translate("DialogAsignarReparacion", "Asignar Responsable", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAceptar.setText(QtGui.QApplication.translate("DialogAsignarReparacion", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("DialogAsignarReparacion", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogAsignarReparacion = QtGui.QDialog()
    ui = Ui_DialogAsignarReparacion()
    ui.setupUi(DialogAsignarReparacion)
    DialogAsignarReparacion.show()
    sys.exit(app.exec_())

