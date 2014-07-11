# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormContrasenaEncargado.ui'
#
# Created: Tue Feb 11 17:05:14 2014
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogCrearUsuarioEncargado(object):
    def setupUi(self, DialogCrearUsuarioEncargado):
        DialogCrearUsuarioEncargado.setObjectName(_fromUtf8("DialogCrearUsuarioEncargado"))
        DialogCrearUsuarioEncargado.setWindowModality(QtCore.Qt.NonModal)
        DialogCrearUsuarioEncargado.resize(270, 150)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogCrearUsuarioEncargado.sizePolicy().hasHeightForWidth())
        DialogCrearUsuarioEncargado.setSizePolicy(sizePolicy)
        DialogCrearUsuarioEncargado.setMinimumSize(QtCore.QSize(270, 150))
        DialogCrearUsuarioEncargado.setMaximumSize(QtCore.QSize(280, 152))
        DialogCrearUsuarioEncargado.setWindowTitle(QtGui.QApplication.translate("DialogCrearUsuarioEncargado", "Crear un nuevo Usuario", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../Desarrollo_de_Software/division-transporte/src/imagenes/logoDivisionTransporte.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogCrearUsuarioEncargado.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(DialogCrearUsuarioEncargado)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(DialogCrearUsuarioEncargado)
        self.groupBox.setTitle(QtGui.QApplication.translate("DialogCrearUsuarioEncargado", "Ingresar contraseña del encargado ", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setText(QtGui.QApplication.translate("DialogCrearUsuarioEncargado", "Usuario:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setText(QtGui.QApplication.translate("DialogCrearUsuarioEncargado", "Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.linePassword = QtGui.QLineEdit(self.groupBox)
        self.linePassword.setObjectName(_fromUtf8("linePassword"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.linePassword)
        self.label_nombreUsrEncargado = QtGui.QLabel(self.groupBox)
        self.label_nombreUsrEncargado.setText(_fromUtf8(""))
        self.label_nombreUsrEncargado.setObjectName(_fromUtf8("label_nombreUsrEncargado"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.label_nombreUsrEncargado)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonOk = QtGui.QPushButton(DialogCrearUsuarioEncargado)
        self.pushButtonOk.setText(QtGui.QApplication.translate("DialogCrearUsuarioEncargado", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonOk.setObjectName(_fromUtf8("pushButtonOk"))
        self.horizontalLayout.addWidget(self.pushButtonOk)
        self.pushButtonCancel = QtGui.QPushButton(DialogCrearUsuarioEncargado)
        self.pushButtonCancel.setText(QtGui.QApplication.translate("DialogCrearUsuarioEncargado", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancel.setObjectName(_fromUtf8("pushButtonCancel"))
        self.horizontalLayout.addWidget(self.pushButtonCancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(DialogCrearUsuarioEncargado)
        QtCore.QObject.connect(self.pushButtonCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), DialogCrearUsuarioEncargado.reject)
        QtCore.QObject.connect(self.pushButtonOk, QtCore.SIGNAL(_fromUtf8("clicked()")), DialogCrearUsuarioEncargado.accept)
        QtCore.QMetaObject.connectSlotsByName(DialogCrearUsuarioEncargado)

    def retranslateUi(self, DialogCrearUsuarioEncargado):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogCrearUsuarioEncargado = QtGui.QDialog()
    ui = Ui_DialogCrearUsuarioEncargado()
    ui.setupUi(DialogCrearUsuarioEncargado)
    DialogCrearUsuarioEncargado.show()
    sys.exit(app.exec_())

