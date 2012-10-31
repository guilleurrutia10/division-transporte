# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogAltaSeccion.ui'
#
# Created: Sun Oct 28 02:29:28 2012
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
        DialogAltaSeccion.resize(817, 515)
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
        self.tableWidgetEmpleadosSinAsignar = QtGui.QTableWidget(self.groupBox_2)
        self.tableWidgetEmpleadosSinAsignar.setObjectName(_fromUtf8("tableWidgetEmpleadosSinAsignar"))
        self.tableWidgetEmpleadosSinAsignar.setColumnCount(0)
        self.tableWidgetEmpleadosSinAsignar.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidgetEmpleadosSinAsignar, 1, 0, 1, 1)
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
        self.tableWidgetEmpleadosAsignados.setColumnCount(0)
        self.tableWidgetEmpleadosAsignados.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidgetEmpleadosAsignados, 1, 3, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(DialogAltaSeccion)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DialogAltaSeccion)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogAltaSeccion.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogAltaSeccion.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogAltaSeccion)

    def retranslateUi(self, DialogAltaSeccion):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogAltaSeccion = QtGui.QDialog()
    ui = Ui_DialogAltaSeccion()
    ui.setupUi(DialogAltaSeccion)
    DialogAltaSeccion.show()
    sys.exit(app.exec_())

