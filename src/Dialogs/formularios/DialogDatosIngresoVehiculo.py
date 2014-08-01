# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/DialogDatosIngresoVehiculo.ui'
#
# Created: Thu Jul 31 21:33:36 2014
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

class Ui_DialogIngresoVehiculo(object):
    def setupUi(self, DialogIngresoVehiculo):
        DialogIngresoVehiculo.setObjectName(_fromUtf8("DialogIngresoVehiculo"))
        DialogIngresoVehiculo.resize(450, 300)
        DialogIngresoVehiculo.setMinimumSize(QtCore.QSize(450, 300))
        self.verticalLayout = QtGui.QVBoxLayout(DialogIngresoVehiculo)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(DialogIngresoVehiculo)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
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
        self.lineEditCombustible = QtGui.QLineEdit(self.groupBox)
        self.lineEditCombustible.setObjectName(_fromUtf8("lineEditCombustible"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEditCombustible)
        self.lineEditEquipamiento = QtGui.QLineEdit(self.groupBox)
        self.lineEditEquipamiento.setObjectName(_fromUtf8("lineEditEquipamiento"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEditEquipamiento)
        self.lineEditReparacion = QtGui.QLineEdit(self.groupBox)
        self.lineEditReparacion.setObjectName(_fromUtf8("lineEditReparacion"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEditReparacion)
        self.lineEditComisaria = QtGui.QLineEdit(self.groupBox)
        self.lineEditComisaria.setObjectName(_fromUtf8("lineEditComisaria"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEditComisaria)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_6)
        self.lineEditLocalidad = QtGui.QLineEdit(self.groupBox)
        self.lineEditLocalidad.setObjectName(_fromUtf8("lineEditLocalidad"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.lineEditLocalidad)
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

    def retranslateUi(self, DialogIngresoVehiculo):
        DialogIngresoVehiculo.setWindowTitle(_translate("DialogIngresoVehiculo", "Registrar Ingreso Vehiculo", None))
        self.groupBox.setTitle(_translate("DialogIngresoVehiculo", "Registrar Ingreso Vehiculo", None))
        self.label.setText(_translate("DialogIngresoVehiculo", "Kilometraje actual:", None))
        self.label_2.setText(_translate("DialogIngresoVehiculo", "Nivel de combustible actual:", None))
        self.label_3.setText(_translate("DialogIngresoVehiculo", "Equipamiento:", None))
        self.label_4.setText(_translate("DialogIngresoVehiculo", "Reparacion solicitada:", None))
        self.label_5.setText(_translate("DialogIngresoVehiculo", "Comisaria:", None))
        self.label_6.setText(_translate("DialogIngresoVehiculo", "Localidad:", None))
        self.pushButtonAceptar.setText(_translate("DialogIngresoVehiculo", "Aceptar", None))
        self.pushButtonCancelar.setText(_translate("DialogIngresoVehiculo", "Cancelar", None))

