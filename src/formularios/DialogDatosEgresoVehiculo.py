# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogDatosEgresoVehiculo.ui'
#
# Created: Wed Nov 14 00:01:18 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogDatosEgresoVehiculo(object):
    def setupUi(self, DialogDatosEgresoVehiculo):
        DialogDatosEgresoVehiculo.setObjectName(_fromUtf8("DialogDatosEgresoVehiculo"))
        DialogDatosEgresoVehiculo.resize(311, 160)
        DialogDatosEgresoVehiculo.setMinimumSize(QtCore.QSize(310, 160))
        DialogDatosEgresoVehiculo.setWindowTitle(QtGui.QApplication.translate("DialogDatosEgresoVehiculo", "Datos Egreso Vehiculo", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(DialogDatosEgresoVehiculo)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(DialogDatosEgresoVehiculo)
        self.groupBox.setTitle(QtGui.QApplication.translate("DialogDatosEgresoVehiculo", "Registrar Ingreso Vehiculo", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setText(QtGui.QApplication.translate("DialogDatosEgresoVehiculo", "Kilometraje Egreso:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEditKilometraje = QtGui.QLineEdit(self.groupBox)
        self.lineEditKilometraje.setObjectName(_fromUtf8("lineEditKilometraje"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditKilometraje)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setText(QtGui.QApplication.translate("DialogDatosEgresoVehiculo", "Nivel De Combustible Egreso:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEditCombustible = QtGui.QLineEdit(self.groupBox)
        self.lineEditCombustible.setObjectName(_fromUtf8("lineEditCombustible"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEditCombustible)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setText(QtGui.QApplication.translate("DialogDatosEgresoVehiculo", "Fecha Egreso", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEditEquipamiento = QtGui.QLineEdit(self.groupBox)
        self.lineEditEquipamiento.setObjectName(_fromUtf8("lineEditEquipamiento"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEditEquipamiento)
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(DialogDatosEgresoVehiculo)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DialogDatosEgresoVehiculo)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogDatosEgresoVehiculo.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogDatosEgresoVehiculo.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogDatosEgresoVehiculo)

    def retranslateUi(self, DialogDatosEgresoVehiculo):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogDatosEgresoVehiculo = QtGui.QDialog()
    ui = Ui_DialogDatosEgresoVehiculo()
    ui.setupUi(DialogDatosEgresoVehiculo)
    DialogDatosEgresoVehiculo.show()
    sys.exit(app.exec_())

