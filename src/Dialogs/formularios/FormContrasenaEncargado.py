# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/FormContrasenaEncargado.ui'
#
# Created: Thu Sep 11 02:46:52 2014
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

class Ui_DialogCrearUsuarioEncargado(object):
    def setupUi(self, DialogCrearUsuarioEncargado):
        DialogCrearUsuarioEncargado.setObjectName(_fromUtf8("DialogCrearUsuarioEncargado"))
        DialogCrearUsuarioEncargado.setWindowModality(QtCore.Qt.NonModal)
        DialogCrearUsuarioEncargado.resize(280, 186)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogCrearUsuarioEncargado.sizePolicy().hasHeightForWidth())
        DialogCrearUsuarioEncargado.setSizePolicy(sizePolicy)
        DialogCrearUsuarioEncargado.setMinimumSize(QtCore.QSize(270, 166))
        DialogCrearUsuarioEncargado.setMaximumSize(QtCore.QSize(280, 186))
        DialogCrearUsuarioEncargado.setWindowTitle(QtGui.QApplication.translate("DialogCrearUsuarioEncargado", "Crear un nuevo Usuario", None, QtGui.QApplication.UnicodeUTF8))
        #DialogCrearUsuarioEncargado.setMinimumSize(QtCore.QSize(270, 150))
        #DialogCrearUsuarioEncargado.setMaximumSize(QtCore.QSize(280, 152))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../Desarrollo_de_Software/division-transporte/src/imagenes/logoDivisionTransporte.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogCrearUsuarioEncargado.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(DialogCrearUsuarioEncargado)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(DialogCrearUsuarioEncargado)
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.linePassword = QtGui.QLineEdit(self.groupBox)
        self.linePassword.setEchoMode(QtGui.QLineEdit.Password)
        self.linePassword.setObjectName(_fromUtf8("linePassword"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.linePassword)
        self.label_nombreUsrEncargado = QtGui.QLabel(self.groupBox)
        self.label_nombreUsrEncargado.setText(_fromUtf8(""))
        self.label_nombreUsrEncargado.setObjectName(_fromUtf8("label_nombreUsrEncargado"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.label_nombreUsrEncargado)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setText(QtGui.QApplication.translate("DialogCrearUsuarioEncargado", "Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEditPassword = QtGui.QLineEdit(self.groupBox)
        self.lineEditPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEditPassword.setObjectName(_fromUtf8("lineEditPassword"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEditPassword)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setText(QtGui.QApplication.translate("DialogCrearUsuarioEncargado", "Confirmar password:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEditPassword2 = QtGui.QLineEdit(self.groupBox)
        self.lineEditPassword2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEditPassword2.setObjectName(_fromUtf8("lineEditPassword2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEditPassword2)
        self.labelMsgError = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.labelMsgError.setFont(font)
        self.labelMsgError.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelMsgError.setText(_fromUtf8(""))
        self.labelMsgError.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelMsgError.setObjectName(_fromUtf8("labelMsgError"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.SpanningRole, self.labelMsgError)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonOk = QtGui.QPushButton(DialogCrearUsuarioEncargado)
        self.pushButtonOk.setObjectName(_fromUtf8("pushButtonOk"))
        self.horizontalLayout.addWidget(self.pushButtonOk)
        self.pushButtonCancel = QtGui.QPushButton(DialogCrearUsuarioEncargado)
        self.pushButtonCancel.setObjectName(_fromUtf8("pushButtonCancel"))
        self.horizontalLayout.addWidget(self.pushButtonCancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(DialogCrearUsuarioEncargado)
        QtCore.QObject.connect(self.pushButtonCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), DialogCrearUsuarioEncargado.reject)
        QtCore.QObject.connect(self.pushButtonOk, QtCore.SIGNAL(_fromUtf8("clicked()")), DialogCrearUsuarioEncargado.accept)
        QtCore.QMetaObject.connectSlotsByName(DialogCrearUsuarioEncargado)

    def retranslateUi(self, DialogCrearUsuarioEncargado):
        DialogCrearUsuarioEncargado.setWindowTitle(_translate("DialogCrearUsuarioEncargado", "Crear un nuevo Usuario", None))
        self.groupBox.setTitle(_translate("DialogCrearUsuarioEncargado", "Ingresar contraseña del encargado ", None))
        self.label.setText(_translate("DialogCrearUsuarioEncargado", "Usuario:", None))
        self.label_3.setText(_translate("DialogCrearUsuarioEncargado", "Password:", None))
        self.pushButtonOk.setText(_translate("DialogCrearUsuarioEncargado", "Ok", None))
        self.pushButtonCancel.setText(_translate("DialogCrearUsuarioEncargado", "Cancel", None))

