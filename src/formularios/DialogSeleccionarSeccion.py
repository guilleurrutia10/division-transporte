# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogSeleccionarSeccion.ui'
#
# Created: Wed Nov 14 00:01:23 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog_SeleccionarSeccion(object):
    def setupUi(self, Dialog_SeleccionarSeccion):
        Dialog_SeleccionarSeccion.setObjectName(_fromUtf8("Dialog_SeleccionarSeccion"))
        Dialog_SeleccionarSeccion.resize(645, 425)
        Dialog_SeleccionarSeccion.setWindowTitle(QtGui.QApplication.translate("Dialog_SeleccionarSeccion", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout = QtGui.QGridLayout(Dialog_SeleccionarSeccion)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.widget_SeleccionarSeccion = QtGui.QWidget(Dialog_SeleccionarSeccion)
        self.widget_SeleccionarSeccion.setObjectName(_fromUtf8("widget_SeleccionarSeccion"))
        self.gridLayout.addWidget(self.widget_SeleccionarSeccion, 0, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(627, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 2)
        self.pushButton_Seleccionar = QtGui.QPushButton(Dialog_SeleccionarSeccion)
        self.pushButton_Seleccionar.setText(QtGui.QApplication.translate("Dialog_SeleccionarSeccion", "Seleccionar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Seleccionar.setObjectName(_fromUtf8("pushButton_Seleccionar"))
        self.gridLayout.addWidget(self.pushButton_Seleccionar, 2, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        self.pushButton_Cancelar = QtGui.QPushButton(Dialog_SeleccionarSeccion)
        self.pushButton_Cancelar.setText(QtGui.QApplication.translate("Dialog_SeleccionarSeccion", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Cancelar.setObjectName(_fromUtf8("pushButton_Cancelar"))
        self.gridLayout.addWidget(self.pushButton_Cancelar, 3, 1, 1, 1)

        self.retranslateUi(Dialog_SeleccionarSeccion)
        QtCore.QMetaObject.connectSlotsByName(Dialog_SeleccionarSeccion)

    def retranslateUi(self, Dialog_SeleccionarSeccion):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog_SeleccionarSeccion = QtGui.QDialog()
    ui = Ui_Dialog_SeleccionarSeccion()
    ui.setupUi(Dialog_SeleccionarSeccion)
    Dialog_SeleccionarSeccion.show()
    sys.exit(app.exec_())

