# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogRegistrarReparaciones.ui'
#
# Created: Fri Dec 07 02:13:56 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogRegistrarReparaciones(object):
    def setupUi(self, DialogRegistrarReparaciones):
        DialogRegistrarReparaciones.setObjectName(_fromUtf8("DialogRegistrarReparaciones"))
        DialogRegistrarReparaciones.resize(540, 570)
        DialogRegistrarReparaciones.setMinimumSize(QtCore.QSize(540, 570))
        DialogRegistrarReparaciones.setWindowTitle(QtGui.QApplication.translate("DialogRegistrarReparaciones", "Registrar Reparaciones de Vehiculo", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(DialogRegistrarReparaciones)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(DialogRegistrarReparaciones)
        self.groupBox.setTitle(QtGui.QApplication.translate("DialogRegistrarReparaciones", "Datos Orden de Reparacion  ", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(60, -1, -1, -1)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setText(QtGui.QApplication.translate("DialogRegistrarReparaciones", "ID Orden de Reparacion:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setText(QtGui.QApplication.translate("DialogRegistrarReparaciones", "Fecha Ingreso:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.labelIdOrden = QtGui.QLabel(self.groupBox)
        self.labelIdOrden.setText(QtGui.QApplication.translate("DialogRegistrarReparaciones", "<<Id Orden>>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelIdOrden.setObjectName(_fromUtf8("labelIdOrden"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.labelIdOrden)
        self.labelFechaOrden = QtGui.QLabel(self.groupBox)
        self.labelFechaOrden.setText(QtGui.QApplication.translate("DialogRegistrarReparaciones", "<<Fecha Orden>>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelFechaOrden.setObjectName(_fromUtf8("labelFechaOrden"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.labelFechaOrden)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setText(QtGui.QApplication.translate("DialogRegistrarReparaciones", "Chofer Asignado:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_6)
        self.labelChoferAsignado = QtGui.QLabel(self.groupBox)
        self.labelChoferAsignado.setText(QtGui.QApplication.translate("DialogRegistrarReparaciones", "<<Chofer>>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelChoferAsignado.setObjectName(_fromUtf8("labelChoferAsignado"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.labelChoferAsignado)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setText(QtGui.QApplication.translate("DialogRegistrarReparaciones", "Km Ingreso:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_8)
        self.labelKilometraje = QtGui.QLabel(self.groupBox)
        self.labelKilometraje.setText(QtGui.QApplication.translate("DialogRegistrarReparaciones", "<<Kilometraje>>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelKilometraje.setObjectName(_fromUtf8("labelKilometraje"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.labelKilometraje)
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setText(QtGui.QApplication.translate("DialogRegistrarReparaciones", "Equipamiento:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_10)
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setText(QtGui.QApplication.translate("DialogRegistrarReparaciones", "Combustible Ingreso:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_11)
        self.label_12 = QtGui.QLabel(self.groupBox)
        self.label_12.setText(QtGui.QApplication.translate("DialogRegistrarReparaciones", "Comisaria:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_12)
        self.labelEquipamiento = QtGui.QLabel(self.groupBox)
        self.labelEquipamiento.setText(QtGui.QApplication.translate("DialogRegistrarReparaciones", "<<Equipamiento>>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelEquipamiento.setObjectName(_fromUtf8("labelEquipamiento"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.labelEquipamiento)
        self.labelCombustible = QtGui.QLabel(self.groupBox)
        self.labelCombustible.setText(QtGui.QApplication.translate("DialogRegistrarReparaciones", "<<Combustible>>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelCombustible.setObjectName(_fromUtf8("labelCombustible"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.labelCombustible)
        self.labelComisaria = QtGui.QLabel(self.groupBox)
        self.labelComisaria.setText(QtGui.QApplication.translate("DialogRegistrarReparaciones", "<<Comisaria>>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelComisaria.setObjectName(_fromUtf8("labelComisaria"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.labelComisaria)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.verticalGroupBox = QtGui.QGroupBox(self.groupBox)
        self.verticalGroupBox.setObjectName(_fromUtf8("verticalGroupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.verticalLayout_2.setContentsMargins(4, 9, 1, 1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_3 = QtGui.QLabel(self.verticalGroupBox)
        self.label_3.setText(QtGui.QApplication.translate("DialogRegistrarReparaciones", "Reparaciones:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.tableWidgetReparaciones = QtGui.QTableWidget(self.verticalGroupBox)
        self.tableWidgetReparaciones.setMaximumSize(QtCore.QSize(16777215, 150))
        self.tableWidgetReparaciones.setObjectName(_fromUtf8("tableWidgetReparaciones"))
        self.tableWidgetReparaciones.setColumnCount(2)
        self.tableWidgetReparaciones.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogRegistrarReparaciones", "Tipo de Reparacion", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetReparaciones.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogRegistrarReparaciones", "Descripcion", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetReparaciones.setHorizontalHeaderItem(1, item)
        self.tableWidgetReparaciones.horizontalHeader().setDefaultSectionSize(140)
        self.verticalLayout_2.addWidget(self.tableWidgetReparaciones)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButtonAgregarReparacion = QtGui.QPushButton(self.verticalGroupBox)
        self.pushButtonAgregarReparacion.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButtonAgregarReparacion.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButtonAgregarReparacion.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButtonAgregarReparacion.setText(QtGui.QApplication.translate("DialogRegistrarReparaciones", "Agregar una Reparacion", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAgregarReparacion.setObjectName(_fromUtf8("pushButtonAgregarReparacion"))
        self.horizontalLayout_2.addWidget(self.pushButtonAgregarReparacion)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addWidget(self.verticalGroupBox)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBoxButtonBox = QtGui.QGroupBox(DialogRegistrarReparaciones)
        self.groupBoxButtonBox.setMinimumSize(QtCore.QSize(271, 41))
        self.groupBoxButtonBox.setMaximumSize(QtCore.QSize(16777215, 41))
        self.groupBoxButtonBox.setTitle(_fromUtf8(""))
        self.groupBoxButtonBox.setObjectName(_fromUtf8("groupBoxButtonBox"))
        self.gridLayout_7 = QtGui.QGridLayout(self.groupBoxButtonBox)
        self.gridLayout_7.setContentsMargins(9, 9, 9, 8)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.pushButtonAceptar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonAceptar.setText(QtGui.QApplication.translate("DialogRegistrarReparaciones", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAceptar.setObjectName(_fromUtf8("pushButtonAceptar"))
        self.gridLayout_7.addWidget(self.pushButtonAceptar, 0, 1, 1, 1)
        self.pushButtonCancelar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("DialogRegistrarReparaciones", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setObjectName(_fromUtf8("pushButtonCancelar"))
        self.gridLayout_7.addWidget(self.pushButtonCancelar, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem1, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxButtonBox)

        self.retranslateUi(DialogRegistrarReparaciones)
        QtCore.QMetaObject.connectSlotsByName(DialogRegistrarReparaciones)

    def retranslateUi(self, DialogRegistrarReparaciones):
        item = self.tableWidgetReparaciones.horizontalHeaderItem(0)
        item = self.tableWidgetReparaciones.horizontalHeaderItem(1)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogRegistrarReparaciones = QtGui.QDialog()
    ui = Ui_DialogRegistrarReparaciones()
    ui.setupUi(DialogRegistrarReparaciones)
    DialogRegistrarReparaciones.show()
    sys.exit(app.exec_())
