# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogPlanificarReparaciones.ui'
#
# Created: Sun Nov 25 16:33:37 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogPlanificarReparaciones(object):
    def setupUi(self, DialogPlanificarReparaciones):
        DialogPlanificarReparaciones.setObjectName(_fromUtf8("DialogPlanificarReparaciones"))
        DialogPlanificarReparaciones.resize(435, 350)
        DialogPlanificarReparaciones.setMinimumSize(QtCore.QSize(435, 350))
        DialogPlanificarReparaciones.setWindowTitle(QtGui.QApplication.translate("DialogPlanificarReparaciones", "Planificar Reparaciones", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(DialogPlanificarReparaciones)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(DialogPlanificarReparaciones)
        self.groupBox.setTitle(QtGui.QApplication.translate("DialogPlanificarReparaciones", "Reparaciones", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tableWidgetReparaciones = QtGui.QTableWidget(self.groupBox)
        self.tableWidgetReparaciones.setObjectName(_fromUtf8("tableWidgetReparaciones"))
        self.tableWidgetReparaciones.setColumnCount(3)
        self.tableWidgetReparaciones.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogPlanificarReparaciones", "Tipo de Reparacion", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetReparaciones.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogPlanificarReparaciones", "Id Reparacion", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetReparaciones.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogPlanificarReparaciones", "Descripcion", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetReparaciones.setHorizontalHeaderItem(2, item)
        self.verticalLayout_2.addWidget(self.tableWidgetReparaciones)
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonPlanificarReparacion = QtGui.QPushButton(self.groupBox_2)
        self.pushButtonPlanificarReparacion.setText(QtGui.QApplication.translate("DialogPlanificarReparaciones", "Planificar Reparacion", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonPlanificarReparacion.setObjectName(_fromUtf8("pushButtonPlanificarReparacion"))
        self.horizontalLayout.addWidget(self.pushButtonPlanificarReparacion)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBoxButtonBox = QtGui.QGroupBox(DialogPlanificarReparaciones)
        self.groupBoxButtonBox.setMinimumSize(QtCore.QSize(271, 41))
        self.groupBoxButtonBox.setMaximumSize(QtCore.QSize(16777215, 41))
        self.groupBoxButtonBox.setTitle(_fromUtf8(""))
        self.groupBoxButtonBox.setObjectName(_fromUtf8("groupBoxButtonBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBoxButtonBox)
        self.gridLayout_2.setContentsMargins(9, 9, 9, 8)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pushButtonAceptar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonAceptar.setText(QtGui.QApplication.translate("DialogPlanificarReparaciones", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAceptar.setObjectName(_fromUtf8("pushButtonAceptar"))
        self.gridLayout_2.addWidget(self.pushButtonAceptar, 0, 1, 1, 1)
        self.pushButtonCancelar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("DialogPlanificarReparaciones", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setObjectName(_fromUtf8("pushButtonCancelar"))
        self.gridLayout_2.addWidget(self.pushButtonCancelar, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxButtonBox)

        self.retranslateUi(DialogPlanificarReparaciones)
        QtCore.QMetaObject.connectSlotsByName(DialogPlanificarReparaciones)

    def retranslateUi(self, DialogPlanificarReparaciones):
        item = self.tableWidgetReparaciones.horizontalHeaderItem(0)
        item = self.tableWidgetReparaciones.horizontalHeaderItem(1)
        item = self.tableWidgetReparaciones.horizontalHeaderItem(2)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogPlanificarReparaciones = QtGui.QDialog()
    ui = Ui_DialogPlanificarReparaciones()
    ui.setupUi(DialogPlanificarReparaciones)
    DialogPlanificarReparaciones.show()
    sys.exit(app.exec_())

