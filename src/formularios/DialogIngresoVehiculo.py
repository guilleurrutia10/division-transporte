# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogIngresoVehiculo.ui'
#
# Created: Sun Nov 18 20:37:44 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogIngresoVehiculo(object):
    def setupUi(self, DialogIngresoVehiculo):
        DialogIngresoVehiculo.setObjectName(_fromUtf8("DialogIngresoVehiculo"))
        DialogIngresoVehiculo.resize(334, 244)
        DialogIngresoVehiculo.setWindowTitle(QtGui.QApplication.translate("DialogIngresoVehiculo", "Registrar Ingreso Vehiculo", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(DialogIngresoVehiculo)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(DialogIngresoVehiculo)
        self.groupBox.setTitle(QtGui.QApplication.translate("DialogIngresoVehiculo", "Registrar Ingreso Vehiculo", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setText(QtGui.QApplication.translate("DialogIngresoVehiculo", "Kilometraje actual:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEditKilometraje = QtGui.QLineEdit(self.groupBox)
        self.lineEditKilometraje.setObjectName(_fromUtf8("lineEditKilometraje"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditKilometraje)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setText(QtGui.QApplication.translate("DialogIngresoVehiculo", "Nivel de combustible actual:", None, QtGui.QApplication.UnicodeUTF8))
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
        self.label_3.setText(QtGui.QApplication.translate("DialogIngresoVehiculo", "Equipamiento:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setText(QtGui.QApplication.translate("DialogIngresoVehiculo", "Reparacion solicitada:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setText(QtGui.QApplication.translate("DialogIngresoVehiculo", "Comisaria:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setText(QtGui.QApplication.translate("DialogIngresoVehiculo", "Localidad:", None, QtGui.QApplication.UnicodeUTF8))
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
        self.pushButtonAceptar.setText(QtGui.QApplication.translate("DialogIngresoVehiculo", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAceptar.setObjectName(_fromUtf8("pushButtonAceptar"))
        self.gridLayout_2.addWidget(self.pushButtonAceptar, 0, 1, 1, 1)
        self.pushButtonCancelar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("DialogIngresoVehiculo", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setObjectName(_fromUtf8("pushButtonCancelar"))
        self.gridLayout_2.addWidget(self.pushButtonCancelar, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxButtonBox)

        self.retranslateUi(DialogIngresoVehiculo)
        QtCore.QMetaObject.connectSlotsByName(DialogIngresoVehiculo)

    def retranslateUi(self, DialogIngresoVehiculo):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogIngresoVehiculo = QtGui.QDialog()
    ui = Ui_DialogIngresoVehiculo()
    ui.setupUi(DialogIngresoVehiculo)
    DialogIngresoVehiculo.show()
    sys.exit(app.exec_())

