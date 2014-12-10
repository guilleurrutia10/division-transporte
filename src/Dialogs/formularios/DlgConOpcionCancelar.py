# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DlgConOpcionCancelar.ui'
#
# Created: Wed Dec 10 16:25:00 2014
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DlgConOpcionCancelar(object):
    def setupUi(self, DlgConOpcionCancelar):
        DlgConOpcionCancelar.setObjectName(_fromUtf8("DlgConOpcionCancelar"))
        DlgConOpcionCancelar.resize(366, 151)
        DlgConOpcionCancelar.setMinimumSize(QtCore.QSize(366, 150))
        DlgConOpcionCancelar.setWindowTitle(QtGui.QApplication.translate("DlgConOpcionCancelar", "Confirmar", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/recursos/iconos/logoDivisionTransporte.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DlgConOpcionCancelar.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(DlgConOpcionCancelar)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(DlgConOpcionCancelar)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.labelMensaje = QtGui.QLabel(self.groupBox)
        self.labelMensaje.setText(QtGui.QApplication.translate("DlgConOpcionCancelar", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.labelMensaje.setObjectName(_fromUtf8("labelMensaje"))
        self.verticalLayout_2.addWidget(self.labelMensaje)
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(DlgConOpcionCancelar)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DlgConOpcionCancelar)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DlgConOpcionCancelar.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DlgConOpcionCancelar.reject)
        QtCore.QMetaObject.connectSlotsByName(DlgConOpcionCancelar)

    def retranslateUi(self, DlgConOpcionCancelar):
        pass

import recursos_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DlgConOpcionCancelar = QtGui.QDialog()
    ui = Ui_DlgConOpcionCancelar()
    ui.setupUi(DlgConOpcionCancelar)
    DlgConOpcionCancelar.show()
    sys.exit(app.exec_())

