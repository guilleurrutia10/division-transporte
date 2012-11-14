# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogPlanificarReparaciones.ui'
#
# Created: Wed Nov 14 00:01:20 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogPlanificarReparaciones(object):
    def setupUi(self, DialogPlanificarReparaciones):
        DialogPlanificarReparaciones.setObjectName(_fromUtf8("DialogPlanificarReparaciones"))
        DialogPlanificarReparaciones.resize(435, 350)
        DialogPlanificarReparaciones.setMinimumSize(QtCore.QSize(435, 350))
        DialogPlanificarReparaciones.setWindowTitle(QtGui.QApplication.translate("DialogPlanificarReparaciones", "Planificar Reparaciones", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(DialogPlanificarReparaciones)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(DialogPlanificarReparaciones)
        self.groupBox.setTitle(QtGui.QApplication.translate("DialogPlanificarReparaciones", "Reparaciones", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tableWidgetReparaciones = QtGui.QTableWidget(self.groupBox)
        self.tableWidgetReparaciones.setObjectName(_fromUtf8("tableWidgetReparaciones"))
        self.tableWidgetReparaciones.setColumnCount(3)
        self.tableWidgetReparaciones.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogPlanificarReparaciones", "Tipo de Reparacion", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetReparaciones.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogPlanificarReparaciones", "Id Reparacion", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetReparaciones.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogPlanificarReparaciones", "Descripcion", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetReparaciones.setHorizontalHeaderItem(2, item)
        self.verticalLayout_2.addWidget(self.tableWidgetReparaciones)
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonPlanificarReparacion = QtGui.QPushButton(self.groupBox_2)
        self.pushButtonPlanificarReparacion.setText(QtGui.QApplication.translate("DialogPlanificarReparaciones", "Planificar Reparacion", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonPlanificarReparacion.setObjectName(_fromUtf8("pushButtonPlanificarReparacion"))
        self.horizontalLayout.addWidget(self.pushButtonPlanificarReparacion)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(DialogPlanificarReparaciones)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DialogPlanificarReparaciones)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogPlanificarReparaciones.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogPlanificarReparaciones.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogPlanificarReparaciones)

    def retranslateUi(self, DialogPlanificarReparaciones):
        item = self.tableWidgetReparaciones.horizontalHeaderItem(0)
        item = self.tableWidgetReparaciones.horizontalHeaderItem(1)
        item = self.tableWidgetReparaciones.horizontalHeaderItem(2)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogPlanificarReparaciones = QtGui.QDialog()
    ui = Ui_DialogPlanificarReparaciones()
    ui.setupUi(DialogPlanificarReparaciones)
    DialogPlanificarReparaciones.show()
    sys.exit(app.exec_())

