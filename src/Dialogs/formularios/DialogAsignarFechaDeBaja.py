# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogAsignarFechaDeBaja.ui'
#
# Created: Wed Dec 10 18:32:39 2014
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogAsignarFechaBaja(object):
    def setupUi(self, DialogAsignarFechaBaja):
        DialogAsignarFechaBaja.setObjectName(_fromUtf8("DialogAsignarFechaBaja"))
        DialogAsignarFechaBaja.resize(498, 294)
        DialogAsignarFechaBaja.setMaximumSize(QtCore.QSize(593, 300))
        DialogAsignarFechaBaja.setWindowTitle(QtGui.QApplication.translate("DialogAsignarFechaBaja", "Asignar Fecha de Baja", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/recursos/iconos/car/planificar-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogAsignarFechaBaja.setWindowIcon(icon)
        self.gridLayout_2 = QtGui.QGridLayout(DialogAsignarFechaBaja)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.groupBox = QtGui.QGroupBox(DialogAsignarFechaBaja)
        self.groupBox.setTitle(QtGui.QApplication.translate("DialogAsignarFechaBaja", "Registrar Fecha de Baja", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.calendarWidgetRegistrarBaja = QtGui.QCalendarWidget(self.groupBox)
        self.calendarWidgetRegistrarBaja.setObjectName(_fromUtf8("calendarWidgetRegistrarBaja"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.calendarWidgetRegistrarBaja)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBoxButtonBox = QtGui.QGroupBox(DialogAsignarFechaBaja)
        self.groupBoxButtonBox.setTitle(_fromUtf8(""))
        self.groupBoxButtonBox.setObjectName(_fromUtf8("groupBoxButtonBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBoxButtonBox)
        self.gridLayout.setContentsMargins(9, 9, 9, 8)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButtonAceptar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonAceptar.setText(QtGui.QApplication.translate("DialogAsignarFechaBaja", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAceptar.setObjectName(_fromUtf8("pushButtonAceptar"))
        self.gridLayout.addWidget(self.pushButtonAceptar, 0, 1, 1, 1)
        self.pushButtonCancelar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("DialogAsignarFechaBaja", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setObjectName(_fromUtf8("pushButtonCancelar"))
        self.gridLayout.addWidget(self.pushButtonCancelar, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBoxButtonBox, 1, 0, 1, 1)

        self.retranslateUi(DialogAsignarFechaBaja)
        QtCore.QMetaObject.connectSlotsByName(DialogAsignarFechaBaja)

    def retranslateUi(self, DialogAsignarFechaBaja):
        pass

import recursos_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogAsignarFechaBaja = QtGui.QDialog()
    ui = Ui_DialogAsignarFechaBaja()
    ui.setupUi(DialogAsignarFechaBaja)
    DialogAsignarFechaBaja.show()
    sys.exit(app.exec_())

