# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WidgetMostrarSecciones.ui'
#
# Created: Sun Nov 25 16:33:59 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_WidgetMostrarSecciones(object):
    def setupUi(self, WidgetMostrarSecciones):
        WidgetMostrarSecciones.setObjectName(_fromUtf8("WidgetMostrarSecciones"))
        WidgetMostrarSecciones.resize(829, 449)
        WidgetMostrarSecciones.setWindowTitle(QtGui.QApplication.translate("WidgetMostrarSecciones", "Mostrar Secciones", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(WidgetMostrarSecciones)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(WidgetMostrarSecciones)
        self.groupBox.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(300, 65))
        self.groupBox.setTitle(QtGui.QApplication.translate("WidgetMostrarSecciones", "Seleccione Seccion", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setText(QtGui.QApplication.translate("WidgetMostrarSecciones", "Seccion:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.comboBoxSecciones = QtGui.QComboBox(self.groupBox)
        self.comboBoxSecciones.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBoxSecciones.setObjectName(_fromUtf8("comboBoxSecciones"))
        self.comboBoxSecciones.addItem(_fromUtf8(""))
        self.comboBoxSecciones.setItemText(0, QtGui.QApplication.translate("WidgetMostrarSecciones", "Gomeria", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxSecciones.addItem(_fromUtf8(""))
        self.comboBoxSecciones.setItemText(1, QtGui.QApplication.translate("WidgetMostrarSecciones", "Electricidad", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxSecciones.addItem(_fromUtf8(""))
        self.comboBoxSecciones.setItemText(2, QtGui.QApplication.translate("WidgetMostrarSecciones", "Chapa y Pintura", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxSecciones.addItem(_fromUtf8(""))
        self.comboBoxSecciones.setItemText(3, QtGui.QApplication.translate("WidgetMostrarSecciones", "Mecanica", None, QtGui.QApplication.UnicodeUTF8))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBoxSecciones)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(WidgetMostrarSecciones)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tableWidgetEmpleadosSecciones = QtGui.QTableWidget(self.groupBox_2)
        self.tableWidgetEmpleadosSecciones.setObjectName(_fromUtf8("tableWidgetEmpleadosSecciones"))
        self.tableWidgetEmpleadosSecciones.setColumnCount(5)
        self.tableWidgetEmpleadosSecciones.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("WidgetMostrarSecciones", "Apellido", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetEmpleadosSecciones.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("WidgetMostrarSecciones", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetEmpleadosSecciones.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("WidgetMostrarSecciones", "Tipo Documento", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetEmpleadosSecciones.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("WidgetMostrarSecciones", "Numero Documento", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetEmpleadosSecciones.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("WidgetMostrarSecciones", "Fecha Nacimiento", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetEmpleadosSecciones.setHorizontalHeaderItem(4, item)
        self.tableWidgetEmpleadosSecciones.horizontalHeader().setDefaultSectionSize(120)
        self.gridLayout.addWidget(self.tableWidgetEmpleadosSecciones, 1, 2, 1, 1)
        self.tableWidgetTipoReparacionesSecciones = QtGui.QTableWidget(self.groupBox_2)
        self.tableWidgetTipoReparacionesSecciones.setMinimumSize(QtCore.QSize(303, 0))
        self.tableWidgetTipoReparacionesSecciones.setMaximumSize(QtCore.QSize(344, 16777215))
        self.tableWidgetTipoReparacionesSecciones.setObjectName(_fromUtf8("tableWidgetTipoReparacionesSecciones"))
        self.tableWidgetTipoReparacionesSecciones.setColumnCount(3)
        self.tableWidgetTipoReparacionesSecciones.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("WidgetMostrarSecciones", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetTipoReparacionesSecciones.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("WidgetMostrarSecciones", "Descripcion", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetTipoReparacionesSecciones.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("WidgetMostrarSecciones", "Tiempo Estimado", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetTipoReparacionesSecciones.setHorizontalHeaderItem(2, item)
        self.gridLayout.addWidget(self.tableWidgetTipoReparacionesSecciones, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setText(QtGui.QApplication.translate("WidgetMostrarSecciones", "Tipos de Reparaciones Realizadas:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setText(QtGui.QApplication.translate("WidgetMostrarSecciones", "Empleados Asignados:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)

        self.retranslateUi(WidgetMostrarSecciones)
        QtCore.QMetaObject.connectSlotsByName(WidgetMostrarSecciones)

    def retranslateUi(self, WidgetMostrarSecciones):
        item = self.tableWidgetEmpleadosSecciones.horizontalHeaderItem(0)
        item = self.tableWidgetEmpleadosSecciones.horizontalHeaderItem(1)
        item = self.tableWidgetEmpleadosSecciones.horizontalHeaderItem(2)
        item = self.tableWidgetEmpleadosSecciones.horizontalHeaderItem(3)
        item = self.tableWidgetEmpleadosSecciones.horizontalHeaderItem(4)
        item = self.tableWidgetTipoReparacionesSecciones.horizontalHeaderItem(0)
        item = self.tableWidgetTipoReparacionesSecciones.horizontalHeaderItem(1)
        item = self.tableWidgetTipoReparacionesSecciones.horizontalHeaderItem(2)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    WidgetMostrarSecciones = QtGui.QWidget()
    ui = Ui_WidgetMostrarSecciones()
    ui.setupUi(WidgetMostrarSecciones)
    WidgetMostrarSecciones.show()
    sys.exit(app.exec_())

