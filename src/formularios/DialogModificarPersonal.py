# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogModificarPersonal.ui'
#
# Created: Wed Nov 14 00:01:19 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogModificarPersonal(object):
    def setupUi(self, DialogModificarPersonal):
        DialogModificarPersonal.setObjectName(_fromUtf8("DialogModificarPersonal"))
        DialogModificarPersonal.resize(300, 300)
        DialogModificarPersonal.setMinimumSize(QtCore.QSize(300, 300))
        DialogModificarPersonal.setMaximumSize(QtCore.QSize(300, 300))
        DialogModificarPersonal.setWindowTitle(QtGui.QApplication.translate("DialogModificarPersonal", "Modificar Personal", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(DialogModificarPersonal)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(DialogModificarPersonal)
        self.groupBox.setTitle(QtGui.QApplication.translate("DialogModificarPersonal", "Modificar Empleado", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setText(QtGui.QApplication.translate("DialogModificarPersonal", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setText(QtGui.QApplication.translate("DialogModificarPersonal", "Apellido:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEditNombre = QtGui.QLineEdit(self.groupBox)
        self.lineEditNombre.setObjectName(_fromUtf8("lineEditNombre"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditNombre)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setText(QtGui.QApplication.translate("DialogModificarPersonal", "Nro Documento:", None, QtGui.QApplication.UnicodeUTF8))
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
        self.label_4.setText(QtGui.QApplication.translate("DialogModificarPersonal", "Domicilio:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setText(QtGui.QApplication.translate("DialogModificarPersonal", "Tipo de Documento:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_5)
        self.comboBoxTipoDocumento = QtGui.QComboBox(self.groupBox)
        self.comboBoxTipoDocumento.setObjectName(_fromUtf8("comboBoxTipoDocumento"))
        self.comboBoxTipoDocumento.addItem(_fromUtf8(""))
        self.comboBoxTipoDocumento.setItemText(0, QtGui.QApplication.translate("DialogModificarPersonal", "L.C.", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTipoDocumento.addItem(_fromUtf8(""))
        self.comboBoxTipoDocumento.setItemText(1, QtGui.QApplication.translate("DialogModificarPersonal", "D.N.I.", None, QtGui.QApplication.UnicodeUTF8))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.comboBoxTipoDocumento)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setText(QtGui.QApplication.translate("DialogModificarPersonal", "Fecha de Nacimiento:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_6)
        self.dateEditFechaNacimiento = QtGui.QDateEdit(self.groupBox)
        self.dateEditFechaNacimiento.setObjectName(_fromUtf8("dateEditFechaNacimiento"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.dateEditFechaNacimiento)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setText(QtGui.QApplication.translate("DialogModificarPersonal", "Telefono:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setText(QtGui.QApplication.translate("DialogModificarPersonal", "Email:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_8)
        self.lineEditTelefono = QtGui.QLineEdit(self.groupBox)
        self.lineEditTelefono.setObjectName(_fromUtf8("lineEditTelefono"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.lineEditTelefono)
        self.lineEditEmail = QtGui.QLineEdit(self.groupBox)
        self.lineEditEmail.setObjectName(_fromUtf8("lineEditEmail"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.lineEditEmail)
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(DialogModificarPersonal)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DialogModificarPersonal)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogModificarPersonal.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogModificarPersonal.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogModificarPersonal)

    def retranslateUi(self, DialogModificarPersonal):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogModificarPersonal = QtGui.QDialog()
    ui = Ui_DialogModificarPersonal()
    ui.setupUi(DialogModificarPersonal)
    DialogModificarPersonal.show()
    sys.exit(app.exec_())

