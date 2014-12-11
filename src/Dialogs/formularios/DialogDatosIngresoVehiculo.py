# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/DialogDatosIngresoVehiculo.ui'
#
# Created: Sun Aug 31 22:01:43 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

# GUARNING, este archivo se modifico para reflejar los datos obligatorios y no recompilar...
# Tambien se agrego el icono a manopla 
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

class Ui_DialogIngresoVehiculo(object):
    def setupUi(self, DialogIngresoVehiculo):
        DialogIngresoVehiculo.setObjectName(_fromUtf8("DialogIngresoVehiculo"))
        DialogIngresoVehiculo.resize(584, 464)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/recursos/iconos/car/ingreso_car-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogIngresoVehiculo.setWindowIcon(icon)
        DialogIngresoVehiculo.setMinimumSize(QtCore.QSize(450, 300))
        self.verticalLayout = QtGui.QVBoxLayout(DialogIngresoVehiculo)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(DialogIngresoVehiculo)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEditKilometraje = QtGui.QLineEdit(self.groupBox)
        self.lineEditKilometraje.setObjectName(_fromUtf8("lineEditKilometraje"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditKilometraje)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.lineEditComisaria = QtGui.QLineEdit(self.groupBox)
        self.lineEditComisaria.setObjectName(_fromUtf8("lineEditComisaria"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEditComisaria)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_6)
        self.lineEditLocalidad = QtGui.QLineEdit(self.groupBox)
        self.lineEditLocalidad.setObjectName(_fromUtf8("lineEditLocalidad"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.lineEditLocalidad)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_7)
        self.lineEditChoferAsignado = QtGui.QLineEdit(self.groupBox)
        self.lineEditChoferAsignado.setObjectName(_fromUtf8("lineEditChoferAsignado"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.lineEditChoferAsignado)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_4)
        self.plainTextEditReparacion = QtGui.QPlainTextEdit(self.groupBox)
        self.plainTextEditReparacion.setObjectName(_fromUtf8("plainTextEditReparacion"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.plainTextEditReparacion)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_3)
        self.plainTextEditEquipamiento = QtGui.QPlainTextEdit(self.groupBox)
        self.plainTextEditEquipamiento.setObjectName(_fromUtf8("plainTextEditEquipamiento"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.plainTextEditEquipamiento)
        self.comboBoxCombustible = QtGui.QComboBox(self.groupBox)
        self.comboBoxCombustible.setObjectName(_fromUtf8("comboBoxCombustible"))
        self.comboBoxCombustible.addItem(_fromUtf8(""))
        self.comboBoxCombustible.addItem(_fromUtf8(""))
        self.comboBoxCombustible.addItem(_fromUtf8(""))
        self.comboBoxCombustible.addItem(_fromUtf8(""))
        self.comboBoxCombustible.addItem(_fromUtf8(""))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.comboBoxCombustible)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBoxButtonBox = QtGui.QGroupBox(DialogIngresoVehiculo)
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
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxButtonBox)

        self.retranslateUi(DialogIngresoVehiculo)
        QtCore.QMetaObject.connectSlotsByName(DialogIngresoVehiculo)
        DialogIngresoVehiculo.setTabOrder(self.lineEditKilometraje, self.lineEditComisaria)
        DialogIngresoVehiculo.setTabOrder(self.lineEditComisaria, self.lineEditLocalidad)
        DialogIngresoVehiculo.setTabOrder(self.lineEditLocalidad, self.lineEditChoferAsignado)
        DialogIngresoVehiculo.setTabOrder(self.lineEditChoferAsignado, self.plainTextEditEquipamiento)
        DialogIngresoVehiculo.setTabOrder(self.plainTextEditEquipamiento, self.plainTextEditReparacion)
        DialogIngresoVehiculo.setTabOrder(self.plainTextEditReparacion, self.pushButtonAceptar)
        DialogIngresoVehiculo.setTabOrder(self.pushButtonAceptar, self.pushButtonCancelar)

    def retranslateUi(self, DialogIngresoVehiculo):
        DialogIngresoVehiculo.setWindowTitle(_translate("DialogIngresoVehiculo", "Registrar Ingreso Vehiculo", None))
        self.groupBox.setTitle(_translate("DialogIngresoVehiculo", "Registrar Ingreso Vehiculo", None))
        self.label.setText(_translate("DialogIngresoVehiculo", "Kilometraje actual(*):", None))
        self.label_2.setText(_translate("DialogIngresoVehiculo", "Nivel de combustible actual(*):", None))
        self.label_5.setText(_translate("DialogIngresoVehiculo", "Comisaría(*):", None))
        self.label_6.setText(_translate("DialogIngresoVehiculo", "Localidad(*):", None))
        self.label_7.setText(_translate("DialogIngresoVehiculo", "Chofer asignado(*):", None))
        self.label_4.setText(_translate("DialogIngresoVehiculo", "Reparación solicitada:", None))
        self.label_3.setText(_translate("DialogIngresoVehiculo", "Equipamiento:", None))
        self.comboBoxCombustible.setToolTip(_translate("DialogIngresoVehiculo", "<html><head/><body><p>Indica la cantidad de combustible en el vehículo.</p></body></html>", None))
        self.comboBoxCombustible.setItemText(0, _translate("DialogIngresoVehiculo", "V", None))
        self.comboBoxCombustible.setItemText(1, _translate("DialogIngresoVehiculo", "1/4", None))
        self.comboBoxCombustible.setItemText(2, _translate("DialogIngresoVehiculo", "1/2", None))
        self.comboBoxCombustible.setItemText(3, _translate("DialogIngresoVehiculo", "3/4", None))
        self.comboBoxCombustible.setItemText(4, _translate("DialogIngresoVehiculo", "LL", None))
        self.pushButtonAceptar.setText(_translate("DialogIngresoVehiculo", "Aceptar", None))
        self.pushButtonCancelar.setText(_translate("DialogIngresoVehiculo", "Cancelar", None))

import recursos_rc