# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormLogin.ui'
#
# Created: Sun Oct 28 02:29:31 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(280, 152)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(280, 150))
        Dialog.setMaximumSize(QtCore.QSize(280, 152))
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.comboBoxUsuario = QtGui.QComboBox(self.groupBox)
        self.comboBoxUsuario.setObjectName(_fromUtf8("comboBoxUsuario"))
        self.comboBoxUsuario.addItem(_fromUtf8(""))
        self.comboBoxUsuario.setItemText(0, QtGui.QApplication.translate("Dialog", "Jefe de Division", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxUsuario.addItem(_fromUtf8(""))
        self.comboBoxUsuario.setItemText(1, QtGui.QApplication.translate("Dialog", "Jefe de Seccion", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxUsuario.addItem(_fromUtf8(""))
        self.comboBoxUsuario.setItemText(2, QtGui.QApplication.translate("Dialog", "Inspector", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxUsuario.addItem(_fromUtf8(""))
        self.comboBoxUsuario.setItemText(3, QtGui.QApplication.translate("Dialog", "Empleado Administrativo", None, QtGui.QApplication.UnicodeUTF8))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBoxUsuario)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setText(QtGui.QApplication.translate("Dialog", "Usuario", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.comboBoxTipoDocumento = QtGui.QComboBox(self.groupBox)
        self.comboBoxTipoDocumento.setObjectName(_fromUtf8("comboBoxTipoDocumento"))
        self.comboBoxTipoDocumento.addItem(_fromUtf8(""))
        self.comboBoxTipoDocumento.setItemText(0, QtGui.QApplication.translate("Dialog", "L.C.", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTipoDocumento.addItem(_fromUtf8(""))
        self.comboBoxTipoDocumento.setItemText(1, QtGui.QApplication.translate("Dialog", "D.N.I.", None, QtGui.QApplication.UnicodeUTF8))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.comboBoxTipoDocumento)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Tipo Documento", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEditNumeroDocumento = QtGui.QLineEdit(self.groupBox)
        self.lineEditNumeroDocumento.setObjectName(_fromUtf8("lineEditNumeroDocumento"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEditNumeroDocumento)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Numero Documento", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

