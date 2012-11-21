# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogAltaVehiculoPrueba.ui'
#
# Created: Wed Nov 21 16:16:43 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogAltaVehiculo(object):
    def setupUi(self, DialogAltaVehiculo):
        DialogAltaVehiculo.setObjectName(_fromUtf8("DialogAltaVehiculo"))
        DialogAltaVehiculo.resize(300, 200)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogAltaVehiculo.sizePolicy().hasHeightForWidth())
        DialogAltaVehiculo.setSizePolicy(sizePolicy)
        DialogAltaVehiculo.setMinimumSize(QtCore.QSize(300, 180))
        DialogAltaVehiculo.setMaximumSize(QtCore.QSize(300, 200))
        DialogAltaVehiculo.setWindowTitle(QtGui.QApplication.translate("DialogAltaVehiculo", "Alta Vehiculo", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(DialogAltaVehiculo)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(DialogAltaVehiculo)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setTitle(QtGui.QApplication.translate("DialogAltaVehiculo", "Nuevo Vehiculo", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setText(QtGui.QApplication.translate("DialogAltaVehiculo", "Dominio:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEditDominio = QtGui.QLineEdit(self.groupBox)
        self.lineEditDominio.setObjectName(_fromUtf8("lineEditDominio"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditDominio)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setText(QtGui.QApplication.translate("DialogAltaVehiculo", "Marca:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEditMarca = QtGui.QLineEdit(self.groupBox)
        self.lineEditMarca.setObjectName(_fromUtf8("lineEditMarca"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEditMarca)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setText(QtGui.QApplication.translate("DialogAltaVehiculo", "Registro Interno:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEditRegistroInterno = QtGui.QLineEdit(self.groupBox)
        self.lineEditRegistroInterno.setObjectName(_fromUtf8("lineEditRegistroInterno"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEditRegistroInterno)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setText(QtGui.QApplication.translate("DialogAltaVehiculo", "Chasis Nro:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.lineEditChasisNro = QtGui.QLineEdit(self.groupBox)
        self.lineEditChasisNro.setObjectName(_fromUtf8("lineEditChasisNro"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEditChasisNro)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(DialogAltaVehiculo)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout.setContentsMargins(100, -1, -1, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_2Aceptar = QtGui.QPushButton(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2Aceptar.sizePolicy().hasHeightForWidth())
        self.pushButton_2Aceptar.setSizePolicy(sizePolicy)
        self.pushButton_2Aceptar.setText(QtGui.QApplication.translate("DialogAltaVehiculo", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2Aceptar.setObjectName(_fromUtf8("pushButton_2Aceptar"))
        self.horizontalLayout.addWidget(self.pushButton_2Aceptar)
        self.pushButton_Cancelar = QtGui.QPushButton(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Cancelar.sizePolicy().hasHeightForWidth())
        self.pushButton_Cancelar.setSizePolicy(sizePolicy)
        self.pushButton_Cancelar.setText(QtGui.QApplication.translate("DialogAltaVehiculo", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Cancelar.setObjectName(_fromUtf8("pushButton_Cancelar"))
        self.horizontalLayout.addWidget(self.pushButton_Cancelar)
        self.verticalLayout.addWidget(self.groupBox_2)

        self.retranslateUi(DialogAltaVehiculo)
        QtCore.QMetaObject.connectSlotsByName(DialogAltaVehiculo)

    def retranslateUi(self, DialogAltaVehiculo):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogAltaVehiculo = QtGui.QDialog()
    ui = Ui_DialogAltaVehiculo()
    ui.setupUi(DialogAltaVehiculo)
    DialogAltaVehiculo.show()
    sys.exit(app.exec_())

