# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogAsignarEncargadoDeSeccion.ui'
#
# Created: Sun Nov 18 20:37:36 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogAsignarEncargadoDeSeccion(object):
    def setupUi(self, DialogAsignarEncargadoDeSeccion):
        DialogAsignarEncargadoDeSeccion.setObjectName(_fromUtf8("DialogAsignarEncargadoDeSeccion"))
        DialogAsignarEncargadoDeSeccion.resize(392, 238)
        DialogAsignarEncargadoDeSeccion.setWindowTitle(QtGui.QApplication.translate("DialogAsignarEncargadoDeSeccion", "Asignar Encargado De Seccion", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(DialogAsignarEncargadoDeSeccion)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(DialogAsignarEncargadoDeSeccion)
        self.groupBox.setTitle(QtGui.QApplication.translate("DialogAsignarEncargadoDeSeccion", "Seleccionar Seccion:  ", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(-1, -1, -1, 10)
        self.formLayout.setHorizontalSpacing(7)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setText(QtGui.QApplication.translate("DialogAsignarEncargadoDeSeccion", "Empleado: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.labelNombreEmpleado = QtGui.QLabel(self.groupBox)
        self.labelNombreEmpleado.setText(QtGui.QApplication.translate("DialogAsignarEncargadoDeSeccion", "<nombre y apellido del empleado>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelNombreEmpleado.setObjectName(_fromUtf8("labelNombreEmpleado"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.labelNombreEmpleado)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setText(QtGui.QApplication.translate("DialogAsignarEncargadoDeSeccion", "Seleccione la Nueva Seccion:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.tableWidgetSecciones = QtGui.QTableWidget(self.groupBox)
        self.tableWidgetSecciones.setObjectName(_fromUtf8("tableWidgetSecciones"))
        self.tableWidgetSecciones.setColumnCount(0)
        self.tableWidgetSecciones.setRowCount(0)
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.tableWidgetSecciones)
        spacerItem = QtGui.QSpacerItem(10, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.formLayout.setItem(0, QtGui.QFormLayout.LabelRole, spacerItem)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBoxButtonBox = QtGui.QGroupBox(DialogAsignarEncargadoDeSeccion)
        self.groupBoxButtonBox.setMinimumSize(QtCore.QSize(271, 41))
        self.groupBoxButtonBox.setMaximumSize(QtCore.QSize(16777215, 41))
        self.groupBoxButtonBox.setTitle(_fromUtf8(""))
        self.groupBoxButtonBox.setObjectName(_fromUtf8("groupBoxButtonBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBoxButtonBox)
        self.gridLayout_2.setContentsMargins(9, 9, 9, 8)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pushButtonAceptar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonAceptar.setText(QtGui.QApplication.translate("DialogAsignarEncargadoDeSeccion", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAceptar.setObjectName(_fromUtf8("pushButtonAceptar"))
        self.gridLayout_2.addWidget(self.pushButtonAceptar, 0, 1, 1, 1)
        self.pushButtonCancelar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("DialogAsignarEncargadoDeSeccion", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setObjectName(_fromUtf8("pushButtonCancelar"))
        self.gridLayout_2.addWidget(self.pushButtonCancelar, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxButtonBox)

        self.retranslateUi(DialogAsignarEncargadoDeSeccion)
        QtCore.QMetaObject.connectSlotsByName(DialogAsignarEncargadoDeSeccion)

    def retranslateUi(self, DialogAsignarEncargadoDeSeccion):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogAsignarEncargadoDeSeccion = QtGui.QDialog()
    ui = Ui_DialogAsignarEncargadoDeSeccion()
    ui.setupUi(DialogAsignarEncargadoDeSeccion)
    DialogAsignarEncargadoDeSeccion.show()
    sys.exit(app.exec_())

