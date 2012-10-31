# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogAltaPersonal.ui'
#
# Created: Wed Oct 31 17:55:02 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogAltaPersonal(object):
    def setupUi(self, DialogAltaPersonal):
        DialogAltaPersonal.setObjectName(_fromUtf8("DialogAltaPersonal"))
        DialogAltaPersonal.resize(300, 300)
        DialogAltaPersonal.setMinimumSize(QtCore.QSize(300, 300))
        DialogAltaPersonal.setMaximumSize(QtCore.QSize(300, 300))
        self.verticalLayout = QtGui.QVBoxLayout(DialogAltaPersonal)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(DialogAltaPersonal)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEditNombre = QtGui.QLineEdit(self.groupBox)
        self.lineEditNombre.setObjectName(_fromUtf8("lineEditNombre"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditNombre)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEditApellido = QtGui.QLineEdit(self.groupBox)
        self.lineEditApellido.setObjectName(_fromUtf8("lineEditApellido"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEditApellido)
        self.lineEditNroDocumento = QtGui.QLineEdit(self.groupBox)
        self.lineEditNroDocumento.setObjectName(_fromUtf8("lineEditNroDocumento"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEditNroDocumento)
        self.lineEditDomicilio = QtGui.QLineEdit(self.groupBox)
        self.lineEditDomicilio.setObjectName(_fromUtf8("lineEditDomicilio"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.lineEditDomicilio)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_5)
        self.comboBoxTipoDocumento = QtGui.QComboBox(self.groupBox)
        self.comboBoxTipoDocumento.setObjectName(_fromUtf8("comboBoxTipoDocumento"))
        self.comboBoxTipoDocumento.addItem(_fromUtf8(""))
        self.comboBoxTipoDocumento.addItem(_fromUtf8(""))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.comboBoxTipoDocumento)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_6)
        self.dateEditFechaNacimiento = QtGui.QDateEdit(self.groupBox)
        self.dateEditFechaNacimiento.setObjectName(_fromUtf8("dateEditFechaNacimiento"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.dateEditFechaNacimiento)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_8)
        self.lineEditTelefono = QtGui.QLineEdit(self.groupBox)
        self.lineEditTelefono.setObjectName(_fromUtf8("lineEditTelefono"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.lineEditTelefono)
        self.lineEditEmail = QtGui.QLineEdit(self.groupBox)
        self.lineEditEmail.setObjectName(_fromUtf8("lineEditEmail"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.lineEditEmail)
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(DialogAltaPersonal)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DialogAltaPersonal)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogAltaPersonal.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogAltaPersonal.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogAltaPersonal)

    def retranslateUi(self, DialogAltaPersonal):
        DialogAltaPersonal.setWindowTitle(QtGui.QApplication.translate("DialogAltaPersonal", "Alta Personal", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("DialogAltaPersonal", "Nuevo Empleado", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DialogAltaPersonal", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DialogAltaPersonal", "Apellido:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("DialogAltaPersonal", "Nro Documento:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("DialogAltaPersonal", "Domicilio:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("DialogAltaPersonal", "Tipo de Documento:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTipoDocumento.setItemText(0, QtGui.QApplication.translate("DialogAltaPersonal", "L.C.", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTipoDocumento.setItemText(1, QtGui.QApplication.translate("DialogAltaPersonal", "D.N.I.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("DialogAltaPersonal", "Fecha de Nacimiento:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("DialogAltaPersonal", "Telefono:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("DialogAltaPersonal", "Email:", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogAltaPersonal = QtGui.QDialog()
    ui = Ui_DialogAltaPersonal()
    ui.setupUi(DialogAltaPersonal)
    DialogAltaPersonal.show()
    sys.exit(app.exec_())

