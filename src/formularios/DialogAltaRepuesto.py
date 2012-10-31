# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogAltaRepuesto.ui'
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

class Ui_DialogAltaRepuesto(object):
    def setupUi(self, DialogAltaRepuesto):
        DialogAltaRepuesto.setObjectName(_fromUtf8("DialogAltaRepuesto"))
        DialogAltaRepuesto.resize(300, 140)
        DialogAltaRepuesto.setMinimumSize(QtCore.QSize(300, 140))
        DialogAltaRepuesto.setMaximumSize(QtCore.QSize(300, 140))
        self.verticalLayout = QtGui.QVBoxLayout(DialogAltaRepuesto)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(DialogAltaRepuesto)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEditNombreRepuesto = QtGui.QLineEdit(self.groupBox)
        self.lineEditNombreRepuesto.setObjectName(_fromUtf8("lineEditNombreRepuesto"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditNombreRepuesto)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEditDescRepuesto = QtGui.QLineEdit(self.groupBox)
        self.lineEditDescRepuesto.setObjectName(_fromUtf8("lineEditDescRepuesto"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEditDescRepuesto)
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(DialogAltaRepuesto)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DialogAltaRepuesto)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogAltaRepuesto.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogAltaRepuesto.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogAltaRepuesto)

    def retranslateUi(self, DialogAltaRepuesto):
        DialogAltaRepuesto.setWindowTitle(QtGui.QApplication.translate("DialogAltaRepuesto", "Alta Repuesto", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("DialogAltaRepuesto", "Nuevo Repuesto", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DialogAltaRepuesto", "Nombre Repuesto:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DialogAltaRepuesto", "Descripcion Repuesto:", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogAltaRepuesto = QtGui.QDialog()
    ui = Ui_DialogAltaRepuesto()
    ui.setupUi(DialogAltaRepuesto)
    DialogAltaRepuesto.show()
    sys.exit(app.exec_())

