# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogCrearReparacion.ui'
#
# Created: Wed Dec 05 21:18:58 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogCrearReparacion(object):
    def setupUi(self, DialogCrearReparacion):
        DialogCrearReparacion.setObjectName(_fromUtf8("DialogCrearReparacion"))
        DialogCrearReparacion.resize(653, 506)
        DialogCrearReparacion.setWindowTitle(QtGui.QApplication.translate("DialogCrearReparacion", "Crear Reparacion", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(DialogCrearReparacion)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(DialogCrearReparacion)
        self.groupBox.setTitle(QtGui.QApplication.translate("DialogCrearReparacion", "Crear Reparacion", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(300, 90))
        self.groupBox_2.setMaximumSize(QtCore.QSize(300, 150))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("DialogCrearReparacion", "Datos Reparacion", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.formLayout = QtGui.QFormLayout(self.groupBox_2)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setText(QtGui.QApplication.translate("DialogCrearReparacion", "Tipo de Reparacion:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_5)
        self.comboBoxTipoDeReparacion = QtGui.QComboBox(self.groupBox_2)
        self.comboBoxTipoDeReparacion.setObjectName(_fromUtf8("comboBoxTipoDeReparacion"))
        self.comboBoxTipoDeReparacion.addItem(_fromUtf8(""))
        self.comboBoxTipoDeReparacion.setItemText(0, QtGui.QApplication.translate("DialogCrearReparacion", "Reparacion Caja de Cambio", None, QtGui.QApplication.UnicodeUTF8))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBoxTipoDeReparacion)
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setText(QtGui.QApplication.translate("DialogCrearReparacion", "Descripcion:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEditDescripcion = QtGui.QLineEdit(self.groupBox_2)
        self.lineEditDescripcion.setObjectName(_fromUtf8("lineEditDescripcion"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEditDescripcion)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QtCore.QSize(615, 260))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("DialogCrearReparacion", "Asignar Repuestos", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tableWidgetRepuestosDisponibles = QtGui.QTableWidget(self.groupBox_3)
        self.tableWidgetRepuestosDisponibles.setObjectName(_fromUtf8("tableWidgetRepuestosDisponibles"))
        self.tableWidgetRepuestosDisponibles.setColumnCount(2)
        self.tableWidgetRepuestosDisponibles.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogCrearReparacion", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetRepuestosDisponibles.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogCrearReparacion", "Descripcion", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetRepuestosDisponibles.setHorizontalHeaderItem(1, item)
        self.horizontalLayout.addWidget(self.tableWidgetRepuestosDisponibles)
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox_3)
        self.groupBox_4.setMinimumSize(QtCore.QSize(130, 100))
        self.groupBox_4.setMaximumSize(QtCore.QSize(130, 100))
        self.groupBox_4.setTitle(_fromUtf8(""))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_6 = QtGui.QLabel(self.groupBox_4)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_6.setText(QtGui.QApplication.translate("DialogCrearReparacion", "Cantidad Repuesto:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_2.addWidget(self.label_6)
        self.lineEditCantidadRepuesto = QtGui.QLineEdit(self.groupBox_4)
        self.lineEditCantidadRepuesto.setObjectName(_fromUtf8("lineEditCantidadRepuesto"))
        self.verticalLayout_2.addWidget(self.lineEditCantidadRepuesto)
        self.pushButtonAgregarRepuesto = QtGui.QPushButton(self.groupBox_4)
        self.pushButtonAgregarRepuesto.setText(QtGui.QApplication.translate("DialogCrearReparacion", "Agregar \n"
"Repuesto", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAgregarRepuesto.setObjectName(_fromUtf8("pushButtonAgregarRepuesto"))
        self.verticalLayout_2.addWidget(self.pushButtonAgregarRepuesto)
        self.horizontalLayout.addWidget(self.groupBox_4)
        self.tableWidgetRepuestosAsignados = QtGui.QTableWidget(self.groupBox_3)
        self.tableWidgetRepuestosAsignados.setObjectName(_fromUtf8("tableWidgetRepuestosAsignados"))
        self.tableWidgetRepuestosAsignados.setColumnCount(3)
        self.tableWidgetRepuestosAsignados.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogCrearReparacion", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetRepuestosAsignados.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogCrearReparacion", "Descripcion", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetRepuestosAsignados.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogCrearReparacion", "Cantidad", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetRepuestosAsignados.setHorizontalHeaderItem(2, item)
        self.horizontalLayout.addWidget(self.tableWidgetRepuestosAsignados)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBoxButtonBox = QtGui.QGroupBox(DialogCrearReparacion)
        self.groupBoxButtonBox.setMinimumSize(QtCore.QSize(271, 41))
        self.groupBoxButtonBox.setMaximumSize(QtCore.QSize(16777215, 41))
        self.groupBoxButtonBox.setTitle(_fromUtf8(""))
        self.groupBoxButtonBox.setObjectName(_fromUtf8("groupBoxButtonBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBoxButtonBox)
        self.gridLayout_2.setContentsMargins(9, 9, 9, 8)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pushButtonAceptar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonAceptar.setText(QtGui.QApplication.translate("DialogCrearReparacion", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAceptar.setObjectName(_fromUtf8("pushButtonAceptar"))
        self.gridLayout_2.addWidget(self.pushButtonAceptar, 0, 1, 1, 1)
        self.pushButtonCancelar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("DialogCrearReparacion", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setObjectName(_fromUtf8("pushButtonCancelar"))
        self.gridLayout_2.addWidget(self.pushButtonCancelar, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxButtonBox)

        self.retranslateUi(DialogCrearReparacion)
        QtCore.QMetaObject.connectSlotsByName(DialogCrearReparacion)

    def retranslateUi(self, DialogCrearReparacion):
        item = self.tableWidgetRepuestosDisponibles.horizontalHeaderItem(0)
        item = self.tableWidgetRepuestosDisponibles.horizontalHeaderItem(1)
        item = self.tableWidgetRepuestosAsignados.horizontalHeaderItem(0)
        item = self.tableWidgetRepuestosAsignados.horizontalHeaderItem(1)
        item = self.tableWidgetRepuestosAsignados.horizontalHeaderItem(2)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogCrearReparacion = QtGui.QDialog()
    ui = Ui_DialogCrearReparacion()
    ui.setupUi(DialogCrearReparacion)
    DialogCrearReparacion.show()
    sys.exit(app.exec_())

