# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogAsignarReparacion.ui'
#
# Created: Wed Nov 14 00:01:16 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(706, 504)
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Reparación", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.tableWidgetReparacion = QtGui.QTableWidget(self.groupBox)
        self.tableWidgetReparacion.setObjectName(_fromUtf8("tableWidgetReparacion"))
        self.tableWidgetReparacion.setColumnCount(3)
        self.tableWidgetReparacion.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Dialog", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetReparacion.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Dialog", "Descripcion", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetReparacion.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Dialog", "Tiempo Estimado", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetReparacion.setHorizontalHeaderItem(2, item)
        self.horizontalLayout_2.addWidget(self.tableWidgetReparacion)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Dialog", "Empleados", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButtonNombre = QtGui.QPushButton(self.groupBox_3)
        self.pushButtonNombre.setText(QtGui.QApplication.translate("Dialog", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
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
        item.setText(QtGui.QApplication.translate("Dialog", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetEmpleados.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Dialog", "Numero de Documento", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetEmpleados.setHorizontalHeaderItem(1, item)
        self.tableWidgetEmpleados.horizontalHeader().setDefaultSectionSize(120)
        self.gridLayout.addWidget(self.tableWidgetEmpleados, 2, 0, 1, 4)
        self.pushButtonAsignarResponsable = QtGui.QPushButton(self.groupBox_2)
        self.pushButtonAsignarResponsable.setText(QtGui.QApplication.translate("Dialog", "Asignar Responsable", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAsignarResponsable.setObjectName(_fromUtf8("pushButtonAsignarResponsable"))
        self.gridLayout.addWidget(self.pushButtonAsignarResponsable, 3, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(149, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 1, 1, 2)
        spacerItem3 = QtGui.QSpacerItem(20, 71, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 3, 3, 1, 1)
        self.pushButton_Cancelar = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_Cancelar.setText(QtGui.QApplication.translate("Dialog", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Cancelar.setObjectName(_fromUtf8("pushButton_Cancelar"))
        self.gridLayout.addWidget(self.pushButton_Cancelar, 3, 4, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        item = self.tableWidgetReparacion.horizontalHeaderItem(0)
        item = self.tableWidgetReparacion.horizontalHeaderItem(1)
        item = self.tableWidgetReparacion.horizontalHeaderItem(2)
        item = self.tableWidgetEmpleados.horizontalHeaderItem(0)
        item = self.tableWidgetEmpleados.horizontalHeaderItem(1)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

