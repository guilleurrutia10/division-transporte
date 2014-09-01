# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/WidgetMostrarTiposDeReparaciones.ui'
#
# Created: Thu Aug 28 13:13:27 2014
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

class Ui_WidgetMostrarTiposDeReparaciones(object):
    def setupUi(self, WidgetMostrarTiposDeReparaciones):
        WidgetMostrarTiposDeReparaciones.setObjectName(_fromUtf8("WidgetMostrarTiposDeReparaciones"))
        WidgetMostrarTiposDeReparaciones.resize(800, 600)
        WidgetMostrarTiposDeReparaciones.setMinimumSize(QtCore.QSize(800, 600))
        self.verticalLayout = QtGui.QVBoxLayout(WidgetMostrarTiposDeReparaciones)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox_3 = QtGui.QGroupBox(WidgetMostrarTiposDeReparaciones)
        self.groupBox_3.setMinimumSize(QtCore.QSize(0, 100))
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox_3)
        self.groupBox_4.setMinimumSize(QtCore.QSize(400, 0))
        self.groupBox_4.setMaximumSize(QtCore.QSize(300, 16777215))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.formLayout = QtGui.QFormLayout(self.groupBox_4)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.groupBox_4)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEditNombreTipoReparacion = QtGui.QLineEdit(self.groupBox_4)
        self.lineEditNombreTipoReparacion.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEditNombreTipoReparacion.setObjectName(_fromUtf8("lineEditNombreTipoReparacion"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditNombreTipoReparacion)
        self.horizontalLayout.addWidget(self.groupBox_4)
        self.pushButtonBuscarTipoReparacion = QtGui.QPushButton(self.groupBox_3)
        self.pushButtonBuscarTipoReparacion.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButtonBuscarTipoReparacion.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonBuscarTipoReparacion.setObjectName(_fromUtf8("pushButtonBuscarTipoReparacion"))
        self.horizontalLayout.addWidget(self.pushButtonBuscarTipoReparacion)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_2 = QtGui.QGroupBox(WidgetMostrarTiposDeReparaciones)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.tableWidgetTipoReparacionesDivision = QtGui.QTableWidget(self.groupBox_2)
        self.tableWidgetTipoReparacionesDivision.setMinimumSize(QtCore.QSize(500, 0))
        self.tableWidgetTipoReparacionesDivision.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidgetTipoReparacionesDivision.setObjectName(_fromUtf8("tableWidgetTipoReparacionesDivision"))
        self.tableWidgetTipoReparacionesDivision.setColumnCount(4)
        self.tableWidgetTipoReparacionesDivision.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetTipoReparacionesDivision.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetTipoReparacionesDivision.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetTipoReparacionesDivision.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetTipoReparacionesDivision.setHorizontalHeaderItem(3, item)
        self.tableWidgetTipoReparacionesDivision.horizontalHeader().setDefaultSectionSize(180)
        self.tableWidgetTipoReparacionesDivision.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.tableWidgetTipoReparacionesDivision)
        self.verticalLayout.addWidget(self.groupBox_2)

        self.retranslateUi(WidgetMostrarTiposDeReparaciones)
        QtCore.QMetaObject.connectSlotsByName(WidgetMostrarTiposDeReparaciones)

    def retranslateUi(self, WidgetMostrarTiposDeReparaciones):
        WidgetMostrarTiposDeReparaciones.setWindowTitle(_translate("WidgetMostrarTiposDeReparaciones", "Mostrar Tipos de Reparacion", None))
        self.groupBox_3.setTitle(_translate("WidgetMostrarTiposDeReparaciones", "Mostrar Tipos de Reparaciones de la Division", None))
        self.groupBox_4.setTitle(_translate("WidgetMostrarTiposDeReparaciones", "Filtrar por Nombre", None))
        self.label.setText(_translate("WidgetMostrarTiposDeReparaciones", "Nombre Tipo de Reparación", None))
        self.pushButtonBuscarTipoReparacion.setText(_translate("WidgetMostrarTiposDeReparaciones", "Buscar", None))
        self.label_2.setText(_translate("WidgetMostrarTiposDeReparaciones", "Tipos de Reparaciones de la Division", None))
        item = self.tableWidgetTipoReparacionesDivision.horizontalHeaderItem(0)
        item.setText(_translate("WidgetMostrarTiposDeReparaciones", "Nombre", None))
        item = self.tableWidgetTipoReparacionesDivision.horizontalHeaderItem(1)
        item.setText(_translate("WidgetMostrarTiposDeReparaciones", "Tiempo Estimado", None))
        item = self.tableWidgetTipoReparacionesDivision.horizontalHeaderItem(2)
        item.setText(_translate("WidgetMostrarTiposDeReparaciones", "Realizada en Sección", None))
        item = self.tableWidgetTipoReparacionesDivision.horizontalHeaderItem(3)
        item.setText(_translate("WidgetMostrarTiposDeReparaciones", "Descripción", None))

