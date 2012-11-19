# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogAltaPersonal.ui'
#
# Created: Sun Nov 18 20:37:33 2012
#      by: PyQt4 UI code generator 4.8.6
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
        DialogAltaPersonal.setWindowTitle(QtGui.QApplication.translate("DialogAltaPersonal", "Alta Personal", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(DialogAltaPersonal)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(DialogAltaPersonal)
        self.groupBox.setTitle(QtGui.QApplication.translate("DialogAltaPersonal", "Nuevo Empleado", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setText(QtGui.QApplication.translate("DialogAltaPersonal", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setText(QtGui.QApplication.translate("DialogAltaPersonal", "Apellido:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEditNombre = QtGui.QLineEdit(self.groupBox)
        self.lineEditNombre.setObjectName(_fromUtf8("lineEditNombre"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditNombre)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setText(QtGui.QApplication.translate("DialogAltaPersonal", "Nro Documento:", None, QtGui.QApplication.UnicodeUTF8))
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
        self.label_4.setText(QtGui.QApplication.translate("DialogAltaPersonal", "Domicilio:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setText(QtGui.QApplication.translate("DialogAltaPersonal", "Tipo de Documento:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_5)
        self.comboBoxTipoDocumento = QtGui.QComboBox(self.groupBox)
        self.comboBoxTipoDocumento.setObjectName(_fromUtf8("comboBoxTipoDocumento"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.comboBoxTipoDocumento)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setText(QtGui.QApplication.translate("DialogAltaPersonal", "Fecha de Nacimiento:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_6)
        self.dateEditFechaNacimiento = QtGui.QDateEdit(self.groupBox)
        self.dateEditFechaNacimiento.setObjectName(_fromUtf8("dateEditFechaNacimiento"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.dateEditFechaNacimiento)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setText(QtGui.QApplication.translate("DialogAltaPersonal", "Telefono:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setText(QtGui.QApplication.translate("DialogAltaPersonal", "Email:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_8)
        self.lineEditTelefono = QtGui.QLineEdit(self.groupBox)
        self.lineEditTelefono.setObjectName(_fromUtf8("lineEditTelefono"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.lineEditTelefono)
        self.lineEditEmail = QtGui.QLineEdit(self.groupBox)
        self.lineEditEmail.setObjectName(_fromUtf8("lineEditEmail"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.lineEditEmail)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBoxButtonBox = QtGui.QGroupBox(DialogAltaPersonal)
        self.groupBoxButtonBox.setMinimumSize(QtCore.QSize(271, 41))
        self.groupBoxButtonBox.setMaximumSize(QtCore.QSize(16777215, 41))
        self.groupBoxButtonBox.setTitle(_fromUtf8(""))
        self.groupBoxButtonBox.setObjectName(_fromUtf8("groupBoxButtonBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBoxButtonBox)
        self.gridLayout_2.setContentsMargins(9, 9, 9, 8)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pushButtonAceptar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonAceptar.setText(QtGui.QApplication.translate("DialogAltaPersonal", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAceptar.setObjectName(_fromUtf8("pushButtonAceptar"))
        self.gridLayout_2.addWidget(self.pushButtonAceptar, 0, 1, 1, 1)
        self.pushButtonCancelar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("DialogAltaPersonal", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setObjectName(_fromUtf8("pushButtonCancelar"))
        self.gridLayout_2.addWidget(self.pushButtonCancelar, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxButtonBox)

        self.retranslateUi(DialogAltaPersonal)
        QtCore.QMetaObject.connectSlotsByName(DialogAltaPersonal)
        DialogAltaPersonal.setTabOrder(self.lineEditNombre, self.lineEditApellido)
        DialogAltaPersonal.setTabOrder(self.lineEditApellido, self.comboBoxTipoDocumento)
        DialogAltaPersonal.setTabOrder(self.comboBoxTipoDocumento, self.lineEditNroDocumento)
        DialogAltaPersonal.setTabOrder(self.lineEditNroDocumento, self.dateEditFechaNacimiento)
        DialogAltaPersonal.setTabOrder(self.dateEditFechaNacimiento, self.lineEditDomicilio)
        DialogAltaPersonal.setTabOrder(self.lineEditDomicilio, self.lineEditTelefono)
        DialogAltaPersonal.setTabOrder(self.lineEditTelefono, self.lineEditEmail)
        DialogAltaPersonal.setTabOrder(self.lineEditEmail, self.pushButtonAceptar)
        DialogAltaPersonal.setTabOrder(self.pushButtonAceptar, self.pushButtonCancelar)

    def retranslateUi(self, DialogAltaPersonal):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogAltaPersonal = QtGui.QDialog()
    ui = Ui_DialogAltaPersonal()
    ui.setupUi(DialogAltaPersonal)
    DialogAltaPersonal.show()
    sys.exit(app.exec_())

