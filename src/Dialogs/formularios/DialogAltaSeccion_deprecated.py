# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/DialogAltaSeccion.ui'
#
# Created: Wed Sep 10 22:04:14 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

# GUARNING! Se modifico este archivo para utilizar los siguientes paquetes:

from PyQt4 import QtCore, QtGui
from Utiles_formulario import TablaEmpleadosSeccion

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

class Ui_DialogAltaSeccion(object):
    def setupUi(self, DialogAltaSeccion):
        DialogAltaSeccion.setObjectName(_fromUtf8("DialogAltaSeccion"))
        DialogAltaSeccion.resize(1024, 599)
        self.verticalLayout = QtGui.QVBoxLayout(DialogAltaSeccion)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(DialogAltaSeccion)
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
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_4.setTitle(_fromUtf8(""))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        spacerItem1 = QtGui.QSpacerItem(20, 3, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem1)
        self.pushButtonAsignarComoEncargado = QtGui.QPushButton(self.groupBox_4)
        self.pushButtonAsignarComoEncargado.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButtonAsignarComoEncargado.setObjectName(_fromUtf8("pushButtonAsignarComoEncargado"))
        self.verticalLayout_5.addWidget(self.pushButtonAsignarComoEncargado)
        self.pushButtonDesasignarEncargado = QtGui.QPushButton(self.groupBox_4)
        self.pushButtonDesasignarEncargado.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButtonDesasignarEncargado.setObjectName(_fromUtf8("pushButtonDesasignarEncargado"))
        self.verticalLayout_5.addWidget(self.pushButtonDesasignarEncargado)
        spacerItem2 = QtGui.QSpacerItem(20, 45, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem2)
        self.pushButtonAsignarEmpleado = QtGui.QPushButton(self.groupBox_4)
        self.pushButtonAsignarEmpleado.setObjectName(_fromUtf8("pushButtonAsignarEmpleado"))
        self.verticalLayout_5.addWidget(self.pushButtonAsignarEmpleado)
        self.pushButtonDesasignarEmpleado = QtGui.QPushButton(self.groupBox_4)
        self.pushButtonDesasignarEmpleado.setObjectName(_fromUtf8("pushButtonDesasignarEmpleado"))
        self.verticalLayout_5.addWidget(self.pushButtonDesasignarEmpleado)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.verticalLayout_5)
        self.gridLayout.addWidget(self.groupBox_4, 1, 1, 1, 1)
        self.tableWidgetEmpleadosSinAsignar = TablaEmpleadosSeccion(self.groupBox_2)
        self.tableWidgetEmpleadosSinAsignar.setObjectName(_fromUtf8("tableWidgetEmpleadosSinAsignar"))
        self.tableWidgetEmpleadosSinAsignar.setColumnCount(2)
        self.tableWidgetEmpleadosSinAsignar.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetEmpleadosSinAsignar.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetEmpleadosSinAsignar.setHorizontalHeaderItem(1, item)
        self.tableWidgetEmpleadosSinAsignar.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidgetEmpleadosSinAsignar.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidgetEmpleadosSinAsignar, 1, 0, 1, 1)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_4.addWidget(self.label_2)
        self.tableWidgetEncargadoAsignado = TablaEmpleadosSeccion(self.groupBox_2)
        self.tableWidgetEncargadoAsignado.setMaximumSize(QtCore.QSize(16777215, 52))
        self.tableWidgetEncargadoAsignado.setObjectName(_fromUtf8("tableWidgetEncargadoAsignado"))
        self.tableWidgetEncargadoAsignado.setColumnCount(2)
        self.tableWidgetEncargadoAsignado.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.tableWidgetEncargadoAsignado.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetEncargadoAsignado.setHorizontalHeaderItem(1, item)
        self.tableWidgetEncargadoAsignado.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidgetEncargadoAsignado.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_4.addWidget(self.tableWidgetEncargadoAsignado)
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_4.addWidget(self.label_3)
        self.tableWidgetEmpleadosAsignados = TablaEmpleadosSeccion(self.groupBox_2)
        self.tableWidgetEmpleadosAsignados.setObjectName(_fromUtf8("tableWidgetEmpleadosAsignados"))
        self.tableWidgetEmpleadosAsignados.setColumnCount(2)
        self.tableWidgetEmpleadosAsignados.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetEmpleadosAsignados.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetEmpleadosAsignados.setHorizontalHeaderItem(1, item)
        self.tableWidgetEmpleadosAsignados.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidgetEmpleadosAsignados.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_4.addWidget(self.tableWidgetEmpleadosAsignados)
        self.gridLayout.addLayout(self.verticalLayout_4, 1, 3, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
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
        self.pushButtonAceptar.setObjectName(_fromUtf8("pushButtonAceptar"))
        self.gridLayout_2.addWidget(self.pushButtonAceptar, 0, 1, 1, 1)
        self.pushButtonCancelar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonCancelar.setObjectName(_fromUtf8("pushButtonCancelar"))
        self.gridLayout_2.addWidget(self.pushButtonCancelar, 0, 2, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxButtonBox)

        self.retranslateUi(DialogAltaSeccion)
        QtCore.QMetaObject.connectSlotsByName(DialogAltaSeccion)

    def retranslateUi(self, DialogAltaSeccion):
        DialogAltaSeccion.setWindowTitle(_translate("DialogAltaSeccion", "Alta Seccion", None))
        self.groupBox.setTitle(_translate("DialogAltaSeccion", "Nueva Sección", None))
        self.label.setText(_translate("DialogAltaSeccion", "Nombre Sección:", None))
        self.lineEditNombreSeccion.setToolTip(_translate("DialogAltaSeccion", "Ingrese aquí el nombre de la nueva sección", None))
        self.groupBox_2.setTitle(_translate("DialogAltaSeccion", "Asignar Empleados", None))
        self.pushButtonAsignarComoEncargado.setToolTip(_translate("DialogAltaSeccion", "Haga click aquí para asignar al empleado seleccionado como encargado de la sección", None))
        self.pushButtonAsignarComoEncargado.setText(_translate("DialogAltaSeccion", "Asignar como Encargado", None))
        self.pushButtonDesasignarEncargado.setToolTip(_translate("DialogAltaSeccion", "Haga click aquí para quitar al empleado seleccionado como encargado de la sección", None))
        self.pushButtonDesasignarEncargado.setText(_translate("DialogAltaSeccion", "Desasignar Encargado", None))
        self.pushButtonAsignarEmpleado.setToolTip(_translate("DialogAltaSeccion", "Haga click aquí para agregar el empleado seleccionado a la sección", None))
        self.pushButtonAsignarEmpleado.setWhatsThis(_translate("DialogAltaSeccion", "Agrega el empleado seleccionado a la sección", None))
        self.pushButtonAsignarEmpleado.setText(_translate("DialogAltaSeccion", ">", None))
        self.pushButtonDesasignarEmpleado.setToolTip(_translate("DialogAltaSeccion", "Haga click aquí para quitar el empleado seleccionado de la sección", None))
        self.pushButtonDesasignarEmpleado.setText(_translate("DialogAltaSeccion", "<", None))
        item = self.tableWidgetEmpleadosSinAsignar.horizontalHeaderItem(0)
        item.setText(_translate("DialogAltaSeccion", "Número de Documento", None))
        item = self.tableWidgetEmpleadosSinAsignar.horizontalHeaderItem(1)
        item.setText(_translate("DialogAltaSeccion", "Nombre", None))
        self.label_2.setText(_translate("DialogAltaSeccion", "Encargado:", None))
        item = self.tableWidgetEncargadoAsignado.horizontalHeaderItem(0)
        item.setText(_translate("DialogAltaSeccion", "Número de Documento", None))
        item = self.tableWidgetEncargadoAsignado.horizontalHeaderItem(1)
        item.setText(_translate("DialogAltaSeccion", "Nombre Encargado", None))
        self.label_3.setText(_translate("DialogAltaSeccion", "Empleados:", None))
        item = self.tableWidgetEmpleadosAsignados.horizontalHeaderItem(0)
        item.setText(_translate("DialogAltaSeccion", "Número de Documento", None))
        item = self.tableWidgetEmpleadosAsignados.horizontalHeaderItem(1)
        item.setText(_translate("DialogAltaSeccion", "Nombre", None))
        self.label_4.setText(_translate("DialogAltaSeccion", "Empleados sin asignar:", None))
        self.pushButtonAceptar.setText(_translate("DialogAltaSeccion", "Aceptar", None))
        self.pushButtonCancelar.setText(_translate("DialogAltaSeccion", "Cancelar", None))

