# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogAltaSeccion.ui'
#
# Created: Wed Nov 21 16:18:49 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogAltaSeccion(object):
    def setupUi(self, DialogAltaSeccion):
        DialogAltaSeccion.setObjectName(_fromUtf8("DialogAltaSeccion"))
        DialogAltaSeccion.resize(1242, 541)
        DialogAltaSeccion.setWindowTitle(QtGui.QApplication.translate("DialogAltaSeccion", "Alta Seccion", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(DialogAltaSeccion)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(DialogAltaSeccion)
        self.groupBox.setTitle(QtGui.QApplication.translate("DialogAltaSeccion", "Nueva Seccion", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 60))
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.groupBox_3)
        self.label.setText(QtGui.QApplication.translate("DialogAltaSeccion", "Nombre Seccion:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEditNombreSeccion = QtGui.QLineEdit(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditNombreSeccion.sizePolicy().hasHeightForWidth())
        self.lineEditNombreSeccion.setSizePolicy(sizePolicy)
        self.lineEditNombreSeccion.setObjectName(_fromUtf8("lineEditNombreSeccion"))
        self.horizontalLayout.addWidget(self.lineEditNombreSeccion)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_2.setTitle(QtGui.QApplication.translate("DialogAltaSeccion", "Asignar Empleados", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_4.setTitle(_fromUtf8(""))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.pushButtonAsignarEmpleado = QtGui.QPushButton(self.groupBox_4)
        self.pushButtonAsignarEmpleado.setText(QtGui.QApplication.translate("DialogAltaSeccion", ">", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAsignarEmpleado.setObjectName(_fromUtf8("pushButtonAsignarEmpleado"))
        self.verticalLayout_3.addWidget(self.pushButtonAsignarEmpleado)
        self.pushButtonDesasignarEmpleado = QtGui.QPushButton(self.groupBox_4)
        self.pushButtonDesasignarEmpleado.setText(QtGui.QApplication.translate("DialogAltaSeccion", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonDesasignarEmpleado.setObjectName(_fromUtf8("pushButtonDesasignarEmpleado"))
        self.verticalLayout_3.addWidget(self.pushButtonDesasignarEmpleado)
        self.gridLayout.addWidget(self.groupBox_4, 1, 1, 1, 1)
        self.pushButtonAsignarComoEncargado = QtGui.QPushButton(self.groupBox_2)
        self.pushButtonAsignarComoEncargado.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButtonAsignarComoEncargado.setText(QtGui.QApplication.translate("DialogAltaSeccion", "Asignar como Encargado", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAsignarComoEncargado.setObjectName(_fromUtf8("pushButtonAsignarComoEncargado"))
        self.gridLayout.addWidget(self.pushButtonAsignarComoEncargado, 2, 3, 1, 1)
        self.tableWidgetEmpleadosAsignados = QtGui.QTableWidget(self.groupBox_2)
        self.tableWidgetEmpleadosAsignados.setObjectName(_fromUtf8("tableWidgetEmpleadosAsignados"))
        self.tableWidgetEmpleadosAsignados.setColumnCount(2)
        self.tableWidgetEmpleadosAsignados.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogAltaSeccion", "Número de Documento", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetEmpleadosAsignados.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogAltaSeccion", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetEmpleadosAsignados.setHorizontalHeaderItem(1, item)
        self.tableWidgetEmpleadosAsignados.horizontalHeader().setDefaultSectionSize(150)
        self.gridLayout.addWidget(self.tableWidgetEmpleadosAsignados, 1, 3, 1, 1)
        self.tableWidgetEmpleadosSinAsignar = QtGui.QTableWidget(self.groupBox_2)
        self.tableWidgetEmpleadosSinAsignar.setObjectName(_fromUtf8("tableWidgetEmpleadosSinAsignar"))
        self.tableWidgetEmpleadosSinAsignar.setColumnCount(2)
        self.tableWidgetEmpleadosSinAsignar.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogAltaSeccion", "Número de Documento", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetEmpleadosSinAsignar.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogAltaSeccion", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetEmpleadosSinAsignar.setHorizontalHeaderItem(1, item)
        self.tableWidgetEmpleadosSinAsignar.horizontalHeader().setDefaultSectionSize(150)
        self.gridLayout.addWidget(self.tableWidgetEmpleadosSinAsignar, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBoxButtonBox = QtGui.QGroupBox(DialogAltaSeccion)
        self.groupBoxButtonBox.setMinimumSize(QtCore.QSize(271, 41))
        self.groupBoxButtonBox.setMaximumSize(QtCore.QSize(16777215, 41))
        self.groupBoxButtonBox.setTitle(_fromUtf8(""))
        self.groupBoxButtonBox.setObjectName(_fromUtf8("groupBoxButtonBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBoxButtonBox)
        self.gridLayout_2.setContentsMargins(9, 9, 9, 8)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pushButtonAceptar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonAceptar.setText(QtGui.QApplication.translate("DialogAltaSeccion", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAceptar.setObjectName(_fromUtf8("pushButtonAceptar"))
        self.gridLayout_2.addWidget(self.pushButtonAceptar, 0, 1, 1, 1)
        self.pushButtonCancelar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("DialogAltaSeccion", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setObjectName(_fromUtf8("pushButtonCancelar"))
        self.gridLayout_2.addWidget(self.pushButtonCancelar, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxButtonBox)

        self.retranslateUi(DialogAltaSeccion)
        QtCore.QMetaObject.connectSlotsByName(DialogAltaSeccion)

    def retranslateUi(self, DialogAltaSeccion):
        item = self.tableWidgetEmpleadosAsignados.horizontalHeaderItem(0)
        item = self.tableWidgetEmpleadosAsignados.horizontalHeaderItem(1)
        item = self.tableWidgetEmpleadosSinAsignar.horizontalHeaderItem(0)
        item = self.tableWidgetEmpleadosSinAsignar.horizontalHeaderItem(1)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogAltaSeccion = QtGui.QDialog()
    ui = Ui_DialogAltaSeccion()
    ui.setupUi(DialogAltaSeccion)
    DialogAltaSeccion.show()
    sys.exit(app.exec_())

