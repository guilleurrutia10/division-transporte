# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WidgetMostrarVehiculosSinPlanificar.ui'
#
# Created: Wed Oct 31 17:55:09 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_WidgetMostrarVehiculosSinPlanificar(object):
    def setupUi(self, WidgetMostrarVehiculosSinPlanificar):
        WidgetMostrarVehiculosSinPlanificar.setObjectName(_fromUtf8("WidgetMostrarVehiculosSinPlanificar"))
        WidgetMostrarVehiculosSinPlanificar.resize(541, 405)
        WidgetMostrarVehiculosSinPlanificar.setMinimumSize(QtCore.QSize(540, 405))
        self.verticalLayout = QtGui.QVBoxLayout(WidgetMostrarVehiculosSinPlanificar)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(WidgetMostrarVehiculosSinPlanificar)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.tableWidgetVehiculosSinPlanificar = QtGui.QTableWidget(self.groupBox)
        self.tableWidgetVehiculosSinPlanificar.setObjectName(_fromUtf8("tableWidgetVehiculosSinPlanificar"))
        self.tableWidgetVehiculosSinPlanificar.setColumnCount(5)
        self.tableWidgetVehiculosSinPlanificar.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetVehiculosSinPlanificar.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetVehiculosSinPlanificar.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetVehiculosSinPlanificar.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetVehiculosSinPlanificar.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetVehiculosSinPlanificar.setHorizontalHeaderItem(4, item)
        self.tableWidgetVehiculosSinPlanificar.horizontalHeader().setDefaultSectionSize(150)
        self.verticalLayout_2.addWidget(self.tableWidgetVehiculosSinPlanificar)
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_3.setEnabled(True)
        self.groupBox_3.setMinimumSize(QtCore.QSize(0, 55))
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 55))
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButtonPlanificarReparaciones = QtGui.QPushButton(self.groupBox_3)
        self.pushButtonPlanificarReparaciones.setObjectName(_fromUtf8("pushButtonPlanificarReparaciones"))
        self.horizontalLayout_2.addWidget(self.pushButtonPlanificarReparaciones)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(WidgetMostrarVehiculosSinPlanificar)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 55))
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.groupBox_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonGuardar = QtGui.QPushButton(self.groupBox_2)
        self.pushButtonGuardar.setObjectName(_fromUtf8("pushButtonGuardar"))
        self.horizontalLayout.addWidget(self.pushButtonGuardar)
        self.pushButtonCancelar = QtGui.QPushButton(self.groupBox_2)
        self.pushButtonCancelar.setObjectName(_fromUtf8("pushButtonCancelar"))
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        self.verticalLayout.addWidget(self.groupBox_2)

        self.retranslateUi(WidgetMostrarVehiculosSinPlanificar)
        QtCore.QMetaObject.connectSlotsByName(WidgetMostrarVehiculosSinPlanificar)

    def retranslateUi(self, WidgetMostrarVehiculosSinPlanificar):
        WidgetMostrarVehiculosSinPlanificar.setWindowTitle(QtGui.QApplication.translate("WidgetMostrarVehiculosSinPlanificar", "Planificar Reparaciones", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("WidgetMostrarVehiculosSinPlanificar", "Planificar Reparaciones", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("WidgetMostrarVehiculosSinPlanificar", "Vehiculos con reparaciones sin planificar:", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidgetVehiculosSinPlanificar.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("WidgetMostrarVehiculosSinPlanificar", "Dominio", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidgetVehiculosSinPlanificar.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("WidgetMostrarVehiculosSinPlanificar", "Marca", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidgetVehiculosSinPlanificar.horizontalHeaderItem(2)
        item.setText(QtGui.QApplication.translate("WidgetMostrarVehiculosSinPlanificar", "Modelo", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidgetVehiculosSinPlanificar.horizontalHeaderItem(3)
        item.setText(QtGui.QApplication.translate("WidgetMostrarVehiculosSinPlanificar", "Nro Registro Interno", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidgetVehiculosSinPlanificar.horizontalHeaderItem(4)
        item.setText(QtGui.QApplication.translate("WidgetMostrarVehiculosSinPlanificar", "Nro Chasis", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonPlanificarReparaciones.setText(QtGui.QApplication.translate("WidgetMostrarVehiculosSinPlanificar", "Planificar Reparaciones \n"
"del Vehiculo", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonGuardar.setText(QtGui.QApplication.translate("WidgetMostrarVehiculosSinPlanificar", "Guardar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("WidgetMostrarVehiculosSinPlanificar", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    WidgetMostrarVehiculosSinPlanificar = QtGui.QWidget()
    ui = Ui_WidgetMostrarVehiculosSinPlanificar()
    ui.setupUi(WidgetMostrarVehiculosSinPlanificar)
    WidgetMostrarVehiculosSinPlanificar.show()
    sys.exit(app.exec_())

