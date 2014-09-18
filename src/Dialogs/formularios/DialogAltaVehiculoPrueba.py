# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/DialogAltaVehiculoPrueba.ui'
#
# Created: Thu Sep 11 03:04:27 2014
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

class Ui_DialogAltaVehiculo(object):
    def setupUi(self, DialogAltaVehiculo):
        DialogAltaVehiculo.setObjectName(_fromUtf8("DialogAltaVehiculo"))
        DialogAltaVehiculo.resize(416, 300)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogAltaVehiculo.sizePolicy().hasHeightForWidth())
        DialogAltaVehiculo.setSizePolicy(sizePolicy)
        DialogAltaVehiculo.setMinimumSize(QtCore.QSize(300, 219))
        DialogAltaVehiculo.setMaximumSize(QtCore.QSize(500, 300))
        self.verticalLayout = QtGui.QVBoxLayout(DialogAltaVehiculo)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(DialogAltaVehiculo)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(-1, -1, 9, -1)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEditDominio = QtGui.QLineEdit(self.groupBox)
        self.lineEditDominio.setObjectName(_fromUtf8("lineEditDominio"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditDominio)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEditMarca = QtGui.QLineEdit(self.groupBox)
        self.lineEditMarca.setObjectName(_fromUtf8("lineEditMarca"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEditMarca)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEditRegistroInterno = QtGui.QLineEdit(self.groupBox)
        self.lineEditRegistroInterno.setObjectName(_fromUtf8("lineEditRegistroInterno"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEditRegistroInterno)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_4)
        self.lineEditChasisNro = QtGui.QLineEdit(self.groupBox)
        self.lineEditChasisNro.setObjectName(_fromUtf8("lineEditChasisNro"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEditChasisNro)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_5)
        self.lineEditModelo = QtGui.QLineEdit(self.groupBox)
        self.lineEditModelo.setObjectName(_fromUtf8("lineEditModelo"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEditModelo)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(DialogAltaVehiculo)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(9, -1, 9, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_2Aceptar = QtGui.QPushButton(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2Aceptar.sizePolicy().hasHeightForWidth())
        self.pushButton_2Aceptar.setSizePolicy(sizePolicy)
        self.pushButton_2Aceptar.setObjectName(_fromUtf8("pushButton_2Aceptar"))
        self.horizontalLayout.addWidget(self.pushButton_2Aceptar)
        self.pushButton_Cancelar = QtGui.QPushButton(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Cancelar.sizePolicy().hasHeightForWidth())
        self.pushButton_Cancelar.setSizePolicy(sizePolicy)
        self.pushButton_Cancelar.setObjectName(_fromUtf8("pushButton_Cancelar"))
        self.horizontalLayout.addWidget(self.pushButton_Cancelar)
        self.verticalLayout.addWidget(self.groupBox_2)

        self.retranslateUi(DialogAltaVehiculo)
        QtCore.QMetaObject.connectSlotsByName(DialogAltaVehiculo)
        DialogAltaVehiculo.setTabOrder(self.lineEditDominio, self.lineEditMarca)
        DialogAltaVehiculo.setTabOrder(self.lineEditMarca, self.lineEditModelo)
        DialogAltaVehiculo.setTabOrder(self.lineEditModelo, self.lineEditRegistroInterno)
        DialogAltaVehiculo.setTabOrder(self.lineEditRegistroInterno, self.lineEditChasisNro)
        DialogAltaVehiculo.setTabOrder(self.lineEditChasisNro, self.pushButton_2Aceptar)
        DialogAltaVehiculo.setTabOrder(self.pushButton_2Aceptar, self.pushButton_Cancelar)

    def retranslateUi(self, DialogAltaVehiculo):
        DialogAltaVehiculo.setWindowTitle(_translate("DialogAltaVehiculo", "Alta Vehiculo", None))
        self.groupBox.setTitle(_translate("DialogAltaVehiculo", "Nuevo Vehículo", None))
        self.label.setText(_translate("DialogAltaVehiculo", "Dominio:", None))
        self.label_2.setText(_translate("DialogAltaVehiculo", "Marca:", None))
        self.label_3.setText(_translate("DialogAltaVehiculo", "Registro Interno:", None))
        self.label_4.setText(_translate("DialogAltaVehiculo", "Número de Chasis:", None))
        self.label_5.setText(_translate("DialogAltaVehiculo", "Modelo:", None))
        self.pushButton_2Aceptar.setText(_translate("DialogAltaVehiculo", "Aceptar", None))
        self.pushButton_Cancelar.setText(_translate("DialogAltaVehiculo", "Cancelar", None))

