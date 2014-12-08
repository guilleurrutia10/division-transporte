# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogoSeleccionarDiaAgenda.ui'
#
# Created: Sun Dec 07 20:03:43 2014
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogAgendaDeSeccion(object):
    def setupUi(self, DialogAgendaDeSeccion):
        DialogAgendaDeSeccion.setObjectName(_fromUtf8("DialogAgendaDeSeccion"))
        DialogAgendaDeSeccion.resize(211, 131)
        DialogAgendaDeSeccion.setMinimumSize(QtCore.QSize(211, 131))
        DialogAgendaDeSeccion.setWindowTitle(QtGui.QApplication.translate("DialogAgendaDeSeccion", "Agenda de Sección", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/recursos/iconos/car/planificar-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogAgendaDeSeccion.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(DialogAgendaDeSeccion)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_Desde = QtGui.QLabel(DialogAgendaDeSeccion)
        self.label_Desde.setText(QtGui.QApplication.translate("DialogAgendaDeSeccion", "Día:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Desde.setObjectName(_fromUtf8("label_Desde"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_Desde)
        self.label_Hasta = QtGui.QLabel(DialogAgendaDeSeccion)
        self.label_Hasta.setEnabled(True)
        self.label_Hasta.setText(_fromUtf8(""))
        self.label_Hasta.setObjectName(_fromUtf8("label_Hasta"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_Hasta)
        self.label_3 = QtGui.QLabel(DialogAgendaDeSeccion)
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.dateEdit_Desde = QtGui.QDateEdit(DialogAgendaDeSeccion)
        self.dateEdit_Desde.setCalendarPopup(True)
        self.dateEdit_Desde.setObjectName(_fromUtf8("dateEdit_Desde"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.dateEdit_Desde)
        self.dateEdit_Hasta = QtGui.QDateEdit(DialogAgendaDeSeccion)
        self.dateEdit_Hasta.setEnabled(False)
        self.dateEdit_Hasta.setCalendarPopup(True)
        self.dateEdit_Hasta.setObjectName(_fromUtf8("dateEdit_Hasta"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.dateEdit_Hasta)
        self.checkBox_porRango = QtGui.QCheckBox(DialogAgendaDeSeccion)
        self.checkBox_porRango.setText(QtGui.QApplication.translate("DialogAgendaDeSeccion", "Por rango", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_porRango.setObjectName(_fromUtf8("checkBox_porRango"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.checkBox_porRango)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtGui.QDialogButtonBox(DialogAgendaDeSeccion)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DialogAgendaDeSeccion)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogAgendaDeSeccion.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogAgendaDeSeccion.reject)
        QtCore.QObject.connect(self.checkBox_porRango, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.dateEdit_Hasta.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(DialogAgendaDeSeccion)

    def retranslateUi(self, DialogAgendaDeSeccion):
        pass

import recursos_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogAgendaDeSeccion = QtGui.QDialog()
    ui = Ui_DialogAgendaDeSeccion()
    ui.setupUi(DialogAgendaDeSeccion)
    DialogAgendaDeSeccion.show()
    sys.exit(app.exec_())

