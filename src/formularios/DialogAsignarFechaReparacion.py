# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogAsignarFechaReparacion.ui'
#
# Created: Sun Oct 28 02:29:28 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AsignarFechaReparacion(object):
    def setupUi(self, AsignarFechaReparacion):
        AsignarFechaReparacion.setObjectName(_fromUtf8("AsignarFechaReparacion"))
        AsignarFechaReparacion.resize(293, 139)
        AsignarFechaReparacion.setMinimumSize(QtCore.QSize(293, 139))
        AsignarFechaReparacion.setWindowTitle(QtGui.QApplication.translate("AsignarFechaReparacion", "Asignar Fecha", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(AsignarFechaReparacion)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(AsignarFechaReparacion)
        self.groupBox.setTitle(QtGui.QApplication.translate("AsignarFechaReparacion", "Planificar Reparacion", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setText(QtGui.QApplication.translate("AsignarFechaReparacion", "Fecha Estimada Inicio:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setText(QtGui.QApplication.translate("AsignarFechaReparacion", "Nro de Secuencia:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.lineEditNroSecuencia = QtGui.QLineEdit(self.groupBox)
        self.lineEditNroSecuencia.setObjectName(_fromUtf8("lineEditNroSecuencia"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEditNroSecuencia)
        self.dateEditFechaReparacion = QtGui.QDateEdit(self.groupBox)
        self.dateEditFechaReparacion.setObjectName(_fromUtf8("dateEditFechaReparacion"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.dateEditFechaReparacion)
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(AsignarFechaReparacion)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(AsignarFechaReparacion)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AsignarFechaReparacion.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AsignarFechaReparacion.reject)
        QtCore.QMetaObject.connectSlotsByName(AsignarFechaReparacion)

    def retranslateUi(self, AsignarFechaReparacion):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    AsignarFechaReparacion = QtGui.QDialog()
    ui = Ui_AsignarFechaReparacion()
    ui.setupUi(AsignarFechaReparacion)
    AsignarFechaReparacion.show()
    sys.exit(app.exec_())

