# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WidgetMostrarReparacionesVehiculo.ui'
#
# Created: Tue Jul 22 20:20:03 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

from Utiles_formulario import TablaReparacionesNoPlanificadas, TablaVehiculos

class Ui_WidgetMostrarReparacionesPorVehiculo(object):
    def setupUi(self, WidgetMostrarReparacionesPorVehiculo):
        WidgetMostrarReparacionesPorVehiculo.setObjectName(_fromUtf8("WidgetMostrarReparacionesPorVehiculo"))
        WidgetMostrarReparacionesPorVehiculo.setWindowModality(QtCore.Qt.WindowModal)
        WidgetMostrarReparacionesPorVehiculo.resize(1289, 620)
        WidgetMostrarReparacionesPorVehiculo.setMinimumSize(QtCore.QSize(988, 460))
        self.verticalLayout = QtGui.QVBoxLayout(WidgetMostrarReparacionesPorVehiculo)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox_3 = QtGui.QGroupBox(WidgetMostrarReparacionesPorVehiculo)
        self.groupBox_3.setMinimumSize(QtCore.QSize(0, 100))
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox_3)
        self.groupBox_4.setMinimumSize(QtCore.QSize(300, 0))
        self.groupBox_4.setMaximumSize(QtCore.QSize(300, 16777215))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.formLayout = QtGui.QFormLayout(self.groupBox_4)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.groupBox_4)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.horizontalLayout.addWidget(self.groupBox_4)
        self.pushButton = QtGui.QPushButton(self.groupBox_3)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_2 = QtGui.QGroupBox(WidgetMostrarReparacionesPorVehiculo)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
#         self.tableWidgetReparaciones = QtGui.QTableWidget(self.groupBox_2)
        self.tableWidgetReparaciones = TablaReparacionesNoPlanificadas(self.groupBox_2)
        self.tableWidgetReparaciones.setObjectName(_fromUtf8("tableWidgetReparaciones"))
        self.tableWidgetReparaciones.setColumnCount(4)
        self.tableWidgetReparaciones.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetReparaciones.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetReparaciones.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetReparaciones.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetReparaciones.setHorizontalHeaderItem(3, item)
        self.tableWidgetReparaciones.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidgetReparaciones.horizontalHeader().setDefaultSectionSize(160)
        self.tableWidgetReparaciones.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidgetReparaciones.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidgetReparaciones, 1, 2, 1, 1)
#         self.tableWidgetVehiculos = QtGui.QTableWidget(self.groupBox_2)
        self.tableWidgetVehiculos = TablaVehiculos(self.groupBox_2)
        self.tableWidgetVehiculos.setMinimumSize(QtCore.QSize(600, 0))
        self.tableWidgetVehiculos.setMaximumSize(QtCore.QSize(600, 16777215))
        self.tableWidgetVehiculos.setObjectName(_fromUtf8("tableWidgetVehiculos"))
        self.tableWidgetVehiculos.setColumnCount(5)
        self.tableWidgetVehiculos.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetVehiculos.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetVehiculos.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetVehiculos.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetVehiculos.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetVehiculos.setHorizontalHeaderItem(4, item)
        self.tableWidgetVehiculos.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidgetVehiculos.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidgetVehiculos.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidgetVehiculos, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)

        self.retranslateUi(WidgetMostrarReparacionesPorVehiculo)
        QtCore.QMetaObject.connectSlotsByName(WidgetMostrarReparacionesPorVehiculo)

    def retranslateUi(self, WidgetMostrarReparacionesPorVehiculo):
        WidgetMostrarReparacionesPorVehiculo.setWindowTitle(_translate("WidgetMostrarReparacionesPorVehiculo", "Mostrar Reparaciones Por Vehiculo", None))
        self.groupBox_3.setTitle(_translate("WidgetMostrarReparacionesPorVehiculo", "Mostrar Vehiculos con reparaciones sin planificar", None))
        self.groupBox_4.setTitle(_translate("WidgetMostrarReparacionesPorVehiculo", "Filtrar por Dominio", None))
        self.label.setText(_translate("WidgetMostrarReparacionesPorVehiculo", "Dominio:", None))
        self.pushButton.setText(_translate("WidgetMostrarReparacionesPorVehiculo", "Buscar", None))
        item = self.tableWidgetReparaciones.horizontalHeaderItem(0)
        item.setText(_translate("WidgetMostrarReparacionesPorVehiculo", "Orden", None))
        item = self.tableWidgetReparaciones.horizontalHeaderItem(1)
        item.setText(_translate("WidgetMostrarReparacionesPorVehiculo", "Tipo", None))
        item = self.tableWidgetReparaciones.horizontalHeaderItem(2)
        item.setText(_translate("WidgetMostrarReparacionesPorVehiculo", "Codigo", None))
        item = self.tableWidgetReparaciones.horizontalHeaderItem(3)
        item.setText(_translate("WidgetMostrarReparacionesPorVehiculo", "Descripción", None))
        item = self.tableWidgetVehiculos.horizontalHeaderItem(0)
        item.setText(_translate("WidgetMostrarReparacionesPorVehiculo", "Dominio", None))
        item = self.tableWidgetVehiculos.horizontalHeaderItem(1)
        item.setText(_translate("WidgetMostrarReparacionesPorVehiculo", "Marca", None))
        item = self.tableWidgetVehiculos.horizontalHeaderItem(2)
        item.setText(_translate("WidgetMostrarReparacionesPorVehiculo", "Modelo", None))
        item = self.tableWidgetVehiculos.horizontalHeaderItem(3)
        item.setText(_translate("WidgetMostrarReparacionesPorVehiculo", "Registro Interno", None))
        item = self.tableWidgetVehiculos.horizontalHeaderItem(4)
        item.setText(_translate("WidgetMostrarReparacionesPorVehiculo", "Chasis Nro", None))
        self.label_2.setText(_translate("WidgetMostrarReparacionesPorVehiculo", "Vehiculos:", None))
        self.label_3.setText(_translate("WidgetMostrarReparacionesPorVehiculo", "Reparaciones :", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    WidgetMostrarReparacionesPorVehiculo = QtGui.QWidget()
    ui = Ui_WidgetMostrarReparacionesPorVehiculo()
    ui.setupUi(WidgetMostrarReparacionesPorVehiculo)
    WidgetMostrarReparacionesPorVehiculo.show()
    sys.exit(app.exec_())

