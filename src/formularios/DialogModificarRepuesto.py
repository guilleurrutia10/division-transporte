# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogModificarRepuesto.ui'
#
# Created: Sun Nov 25 16:33:34 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogMoficarRepuesto(object):
    def setupUi(self, DialogMoficarRepuesto):
        DialogMoficarRepuesto.setObjectName(_fromUtf8("DialogMoficarRepuesto"))
        DialogMoficarRepuesto.resize(300, 140)
        DialogMoficarRepuesto.setMinimumSize(QtCore.QSize(300, 140))
        DialogMoficarRepuesto.setMaximumSize(QtCore.QSize(300, 140))
        DialogMoficarRepuesto.setWindowTitle(QtGui.QApplication.translate("DialogMoficarRepuesto", "Modificar Repuesto", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(DialogMoficarRepuesto)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(DialogMoficarRepuesto)
        self.groupBox.setTitle(QtGui.QApplication.translate("DialogMoficarRepuesto", "Modificar Repuesto", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setText(QtGui.QApplication.translate("DialogMoficarRepuesto", "Nombre Repuesto:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEditNombreRepuesto = QtGui.QLineEdit(self.groupBox)
        self.lineEditNombreRepuesto.setObjectName(_fromUtf8("lineEditNombreRepuesto"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditNombreRepuesto)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setText(QtGui.QApplication.translate("DialogMoficarRepuesto", "Descripcion Repuesto:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEditDescRepuesto = QtGui.QLineEdit(self.groupBox)
        self.lineEditDescRepuesto.setObjectName(_fromUtf8("lineEditDescRepuesto"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEditDescRepuesto)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBoxButtonBox = QtGui.QGroupBox(DialogMoficarRepuesto)
        self.groupBoxButtonBox.setMinimumSize(QtCore.QSize(271, 41))
        self.groupBoxButtonBox.setMaximumSize(QtCore.QSize(16777215, 41))
        self.groupBoxButtonBox.setTitle(_fromUtf8(""))
        self.groupBoxButtonBox.setObjectName(_fromUtf8("groupBoxButtonBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBoxButtonBox)
        self.gridLayout_2.setContentsMargins(9, 9, 9, 8)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pushButtonAceptar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonAceptar.setText(QtGui.QApplication.translate("DialogMoficarRepuesto", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAceptar.setObjectName(_fromUtf8("pushButtonAceptar"))
        self.gridLayout_2.addWidget(self.pushButtonAceptar, 0, 1, 1, 1)
        self.pushButtonCancelar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("DialogMoficarRepuesto", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setObjectName(_fromUtf8("pushButtonCancelar"))
        self.gridLayout_2.addWidget(self.pushButtonCancelar, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxButtonBox)

        self.retranslateUi(DialogMoficarRepuesto)
        QtCore.QMetaObject.connectSlotsByName(DialogMoficarRepuesto)

    def retranslateUi(self, DialogMoficarRepuesto):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogMoficarRepuesto = QtGui.QDialog()
    ui = Ui_DialogMoficarRepuesto()
    ui.setupUi(DialogMoficarRepuesto)
    DialogMoficarRepuesto.show()
    sys.exit(app.exec_())

