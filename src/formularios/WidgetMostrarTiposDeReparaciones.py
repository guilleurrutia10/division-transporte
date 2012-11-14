# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WidgetMostrarTiposDeReparaciones.ui'
#
# Created: Wed Nov 14 00:01:29 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_WidgetMostrarTiposDeReparaciones(object):
    def setupUi(self, WidgetMostrarTiposDeReparaciones):
        WidgetMostrarTiposDeReparaciones.setObjectName(_fromUtf8("WidgetMostrarTiposDeReparaciones"))
        WidgetMostrarTiposDeReparaciones.resize(816, 449)
        WidgetMostrarTiposDeReparaciones.setWindowTitle(QtGui.QApplication.translate("WidgetMostrarTiposDeReparaciones", "Mostrar Tipos de Reparacion", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(WidgetMostrarTiposDeReparaciones)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox_3 = QtGui.QGroupBox(WidgetMostrarTiposDeReparaciones)
        self.groupBox_3.setMinimumSize(QtCore.QSize(0, 100))
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("WidgetMostrarTiposDeReparaciones", "Mostrar Tipos de Reparaciones de la Division", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox_3)
        self.groupBox_4.setMinimumSize(QtCore.QSize(300, 0))
        self.groupBox_4.setMaximumSize(QtCore.QSize(300, 16777215))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("WidgetMostrarTiposDeReparaciones", "Filtrar por Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.formLayout = QtGui.QFormLayout(self.groupBox_4)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.groupBox_4)
        self.label.setText(QtGui.QApplication.translate("WidgetMostrarTiposDeReparaciones", "Nombre Tipo de Reparacion", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEditNombreTipoReparacion = QtGui.QLineEdit(self.groupBox_4)
        self.lineEditNombreTipoReparacion.setObjectName(_fromUtf8("lineEditNombreTipoReparacion"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditNombreTipoReparacion)
        self.horizontalLayout.addWidget(self.groupBox_4)
        self.pushButtonBuscarTipoReparacion = QtGui.QPushButton(self.groupBox_3)
        self.pushButtonBuscarTipoReparacion.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButtonBuscarTipoReparacion.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonBuscarTipoReparacion.setText(QtGui.QApplication.translate("WidgetMostrarTiposDeReparaciones", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonBuscarTipoReparacion.setObjectName(_fromUtf8("pushButtonBuscarTipoReparacion"))
        self.horizontalLayout.addWidget(self.pushButtonBuscarTipoReparacion)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_2 = QtGui.QGroupBox(WidgetMostrarTiposDeReparaciones)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setText(QtGui.QApplication.translate("WidgetMostrarTiposDeReparaciones", "Tipos de Reparaciones de la Division", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.tableWidgetTipoReparacionesDivision = QtGui.QTableWidget(self.groupBox_2)
        self.tableWidgetTipoReparacionesDivision.setMinimumSize(QtCore.QSize(500, 0))
        self.tableWidgetTipoReparacionesDivision.setMaximumSize(QtCore.QSize(816, 16777215))
        self.tableWidgetTipoReparacionesDivision.setObjectName(_fromUtf8("tableWidgetTipoReparacionesDivision"))
        self.tableWidgetTipoReparacionesDivision.setColumnCount(4)
        self.tableWidgetTipoReparacionesDivision.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("WidgetMostrarTiposDeReparaciones", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetTipoReparacionesDivision.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("WidgetMostrarTiposDeReparaciones", "Descripcion", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetTipoReparacionesDivision.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("WidgetMostrarTiposDeReparaciones", "Tiempo Estimado", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetTipoReparacionesDivision.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("WidgetMostrarTiposDeReparaciones", "Realizada en Seccion", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetTipoReparacionesDivision.setHorizontalHeaderItem(3, item)
        self.tableWidgetTipoReparacionesDivision.horizontalHeader().setDefaultSectionSize(150)
        self.verticalLayout_2.addWidget(self.tableWidgetTipoReparacionesDivision)
        self.verticalLayout.addWidget(self.groupBox_2)

        self.retranslateUi(WidgetMostrarTiposDeReparaciones)
        QtCore.QMetaObject.connectSlotsByName(WidgetMostrarTiposDeReparaciones)

    def retranslateUi(self, WidgetMostrarTiposDeReparaciones):
        item = self.tableWidgetTipoReparacionesDivision.horizontalHeaderItem(0)
        item = self.tableWidgetTipoReparacionesDivision.horizontalHeaderItem(1)
        item = self.tableWidgetTipoReparacionesDivision.horizontalHeaderItem(2)
        item = self.tableWidgetTipoReparacionesDivision.horizontalHeaderItem(3)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    WidgetMostrarTiposDeReparaciones = QtGui.QWidget()
    ui = Ui_WidgetMostrarTiposDeReparaciones()
    ui.setupUi(WidgetMostrarTiposDeReparaciones)
    WidgetMostrarTiposDeReparaciones.show()
    sys.exit(app.exec_())

