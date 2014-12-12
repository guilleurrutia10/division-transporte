# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DlgSeleccionarReporteSeccion.ui'
#
# Created: Fri Dec 12 15:54:39 2014
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
        Dialog.resize(291, 127)
        Dialog.setMinimumSize(QtCore.QSize(291, 127))
        Dialog.setMaximumSize(QtCore.QSize(291, 127))
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Reparaciones por Sección", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/recursos/iconos/add_seccion.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 85))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Generar", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.checkBoxTorta = QtGui.QCheckBox(self.groupBox)
        self.checkBoxTorta.setText(QtGui.QApplication.translate("Dialog", "Gráfico de Torta", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxTorta.setObjectName(_fromUtf8("checkBoxTorta"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.checkBoxTorta)
        self.checkBoxCsv = QtGui.QCheckBox(self.groupBox)
        self.checkBoxCsv.setText(QtGui.QApplication.translate("Dialog", "Archivo csv", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxCsv.setObjectName(_fromUtf8("checkBoxCsv"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.checkBoxCsv)
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

import recursos_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

