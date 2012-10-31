# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogModificarRepuesto.ui'
#
# Created: Sun Oct 28 02:29:29 2012
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
        self.buttonBox = QtGui.QDialogButtonBox(DialogMoficarRepuesto)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DialogMoficarRepuesto)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogMoficarRepuesto.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogMoficarRepuesto.reject)
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

