# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/DialogRegistrarReparaciones.ui'
#
# Created: Thu Sep 11 02:44:37 2014
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

class Ui_DialogRegistrarReparaciones(object):
    def setupUi(self, DialogRegistrarReparaciones):
        DialogRegistrarReparaciones.setObjectName(_fromUtf8("DialogRegistrarReparaciones"))
        DialogRegistrarReparaciones.resize(540, 570)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("::/recursos/iconos/logoDivisionTransporte.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogRegistrarReparaciones.setWindowIcon(icon)
        DialogRegistrarReparaciones.setMinimumSize(QtCore.QSize(540, 570))
        self.verticalLayout = QtGui.QVBoxLayout(DialogRegistrarReparaciones)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(DialogRegistrarReparaciones)
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
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.labelIdOrden = QtGui.QLabel(self.groupBox)
        self.labelIdOrden.setObjectName(_fromUtf8("labelIdOrden"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.labelIdOrden)
        self.labelFechaOrden = QtGui.QLabel(self.groupBox)
        self.labelFechaOrden.setObjectName(_fromUtf8("labelFechaOrden"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.labelFechaOrden)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_6)
        self.labelChoferAsignado = QtGui.QLabel(self.groupBox)
        self.labelChoferAsignado.setObjectName(_fromUtf8("labelChoferAsignado"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.labelChoferAsignado)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_8)
        self.labelKilometraje = QtGui.QLabel(self.groupBox)
        self.labelKilometraje.setObjectName(_fromUtf8("labelKilometraje"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.labelKilometraje)
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_10)
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_11)
        self.label_12 = QtGui.QLabel(self.groupBox)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_12)
        self.labelEquipamiento = QtGui.QLabel(self.groupBox)
        self.labelEquipamiento.setObjectName(_fromUtf8("labelEquipamiento"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.labelEquipamiento)
        self.labelCombustible = QtGui.QLabel(self.groupBox)
        self.labelCombustible.setObjectName(_fromUtf8("labelCombustible"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.labelCombustible)
        self.labelComisaria = QtGui.QLabel(self.groupBox)
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
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.tableWidgetReparaciones = QtGui.QTableWidget(self.verticalGroupBox)
        self.tableWidgetReparaciones.setMaximumSize(QtCore.QSize(16777215, 150))
        self.tableWidgetReparaciones.setObjectName(_fromUtf8("tableWidgetReparaciones"))
        self.tableWidgetReparaciones.setColumnCount(2)
        self.tableWidgetReparaciones.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetReparaciones.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetReparaciones.setHorizontalHeaderItem(1, item)
        self.tableWidgetReparaciones.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidgetReparaciones.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidgetReparaciones.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.tableWidgetReparaciones)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButtonAgregarReparacion = QtGui.QPushButton(self.verticalGroupBox)
        self.pushButtonAgregarReparacion.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButtonAgregarReparacion.setMaximumSize(QtCore.QSize(170, 16777215))
        self.pushButtonAgregarReparacion.setLayoutDirection(QtCore.Qt.LeftToRight)
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
        self.pushButtonAceptar.setObjectName(_fromUtf8("pushButtonAceptar"))
        self.gridLayout_7.addWidget(self.pushButtonAceptar, 0, 1, 1, 1)
        self.pushButtonCancelar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonCancelar.setObjectName(_fromUtf8("pushButtonCancelar"))
        self.gridLayout_7.addWidget(self.pushButtonCancelar, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem1, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxButtonBox)

        self.retranslateUi(DialogRegistrarReparaciones)
        QtCore.QMetaObject.connectSlotsByName(DialogRegistrarReparaciones)

    def retranslateUi(self, DialogRegistrarReparaciones):
        DialogRegistrarReparaciones.setWindowTitle(_translate("DialogRegistrarReparaciones", "Registrar Reparaciones de Vehiculo", None))
        self.groupBox.setTitle(_translate("DialogRegistrarReparaciones", "Datos Orden de Reparación  ", None))
        self.label.setText(_translate("DialogRegistrarReparaciones", "ID Orden de Reparación:", None))
        self.label_2.setText(_translate("DialogRegistrarReparaciones", "Fecha Ingreso:", None))
        self.labelIdOrden.setText(_translate("DialogRegistrarReparaciones", "<<Id Orden>>", None))
        self.labelFechaOrden.setText(_translate("DialogRegistrarReparaciones", "<<Fecha Orden>>", None))
        self.label_6.setText(_translate("DialogRegistrarReparaciones", "Chofer Asignado:", None))
        self.labelChoferAsignado.setText(_translate("DialogRegistrarReparaciones", "<<Chofer>>", None))
        self.label_8.setText(_translate("DialogRegistrarReparaciones", "Km Ingreso:", None))
        self.labelKilometraje.setText(_translate("DialogRegistrarReparaciones", "<<Kilometraje>>", None))
        self.label_10.setText(_translate("DialogRegistrarReparaciones", "Equipamiento:", None))
        self.label_11.setText(_translate("DialogRegistrarReparaciones", "Combustible Ingreso:", None))
        self.label_12.setText(_translate("DialogRegistrarReparaciones", "Comisaría:", None))
        self.labelEquipamiento.setText(_translate("DialogRegistrarReparaciones", "<<Equipamiento>>", None))
        self.labelCombustible.setText(_translate("DialogRegistrarReparaciones", "<<Combustible>>", None))
        self.labelComisaria.setText(_translate("DialogRegistrarReparaciones", "<<Comisaria>>", None))
        self.label_3.setText(_translate("DialogRegistrarReparaciones", "Reparaciones:", None))
        item = self.tableWidgetReparaciones.horizontalHeaderItem(0)
        item.setText(_translate("DialogRegistrarReparaciones", "Tipo de Reparación", None))
        item = self.tableWidgetReparaciones.horizontalHeaderItem(1)
        item.setText(_translate("DialogRegistrarReparaciones", "Descripción", None))
        self.pushButtonAgregarReparacion.setText(_translate("DialogRegistrarReparaciones", "Agregar una Reparacion", None))
        self.pushButtonAceptar.setText(_translate("DialogRegistrarReparaciones", "Aceptar", None))
        self.pushButtonCancelar.setText(_translate("DialogRegistrarReparaciones", "Cancelar", None))

import recursos_rc