# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DlgPlanificar_1.ui'
#
# Created: Thu Jul 17 21:39:49 2014
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DlgPlanificar_1(object):
    def setupUi(self, DlgPlanificar_1):
        DlgPlanificar_1.setObjectName(_fromUtf8("DlgPlanificar_1"))
        DlgPlanificar_1.resize(521, 490)
        DlgPlanificar_1.setWindowTitle(QtGui.QApplication.translate("DlgPlanificar_1", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout_2 = QtGui.QVBoxLayout(DlgPlanificar_1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(DlgPlanificar_1)
        self.groupBox.setTitle(QtGui.QApplication.translate("DlgPlanificar_1", "Planificar Reparaciones", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButtonMecanica = QtGui.QPushButton(self.groupBox)
        self.pushButtonMecanica.setEnabled(False)
        self.pushButtonMecanica.setMinimumSize(QtCore.QSize(130, 130))
        self.pushButtonMecanica.setMaximumSize(QtCore.QSize(200, 200))
        self.pushButtonMecanica.setToolTip(_fromUtf8(""))
        self.pushButtonMecanica.setWhatsThis(_fromUtf8(""))
        self.pushButtonMecanica.setText(QtGui.QApplication.translate("DlgPlanificar_1", "Mecánica", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonMecanica.setObjectName(_fromUtf8("pushButtonMecanica"))
        self.gridLayout.addWidget(self.pushButtonMecanica, 0, 0, 1, 1)
        self.pushButtonChapaSoldadura = QtGui.QPushButton(self.groupBox)
        self.pushButtonChapaSoldadura.setEnabled(False)
        self.pushButtonChapaSoldadura.setMinimumSize(QtCore.QSize(130, 130))
        self.pushButtonChapaSoldadura.setMaximumSize(QtCore.QSize(200, 200))
        self.pushButtonChapaSoldadura.setText(QtGui.QApplication.translate("DlgPlanificar_1", "Chapa\n"
"Soldadura", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonChapaSoldadura.setObjectName(_fromUtf8("pushButtonChapaSoldadura"))
        self.gridLayout.addWidget(self.pushButtonChapaSoldadura, 1, 0, 1, 1)
        self.pushButtonGomeria = QtGui.QPushButton(self.groupBox)
        self.pushButtonGomeria.setEnabled(False)
        self.pushButtonGomeria.setMinimumSize(QtCore.QSize(130, 130))
        self.pushButtonGomeria.setMaximumSize(QtCore.QSize(200, 200))
        self.pushButtonGomeria.setText(QtGui.QApplication.translate("DlgPlanificar_1", "Gomería", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonGomeria.setObjectName(_fromUtf8("pushButtonGomeria"))
        self.gridLayout.addWidget(self.pushButtonGomeria, 1, 1, 1, 1)
        self.pushButtonElectricidad = QtGui.QPushButton(self.groupBox)
        self.pushButtonElectricidad.setEnabled(False)
        self.pushButtonElectricidad.setMinimumSize(QtCore.QSize(130, 130))
        self.pushButtonElectricidad.setMaximumSize(QtCore.QSize(200, 200))
        self.pushButtonElectricidad.setText(QtGui.QApplication.translate("DlgPlanificar_1", "Electricidad\n"
"Electrónica", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonElectricidad.setObjectName(_fromUtf8("pushButtonElectricidad"))
        self.gridLayout.addWidget(self.pushButtonElectricidad, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(DlgPlanificar_1)
        self.groupBox_2.setTitle(QtGui.QApplication.translate("DlgPlanificar_1", "Descripción", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.labelDescripcion = QtGui.QLabel(self.groupBox_2)
        self.labelDescripcion.setMinimumSize(QtCore.QSize(0, 0))
        self.labelDescripcion.setMaximumSize(QtCore.QSize(16777215, 70))
        self.labelDescripcion.setText(QtGui.QApplication.translate("DlgPlanificar_1", "Seleccione una Seccion para planificar sus reparaciones.", None, QtGui.QApplication.UnicodeUTF8))
        self.labelDescripcion.setObjectName(_fromUtf8("labelDescripcion"))
        self.verticalLayout.addWidget(self.labelDescripcion)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.buttonBox = QtGui.QDialogButtonBox(DlgPlanificar_1)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(DlgPlanificar_1)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DlgPlanificar_1.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DlgPlanificar_1.reject)
        QtCore.QMetaObject.connectSlotsByName(DlgPlanificar_1)
        DlgPlanificar_1.setTabOrder(self.pushButtonMecanica, self.pushButtonElectricidad)
        DlgPlanificar_1.setTabOrder(self.pushButtonElectricidad, self.pushButtonChapaSoldadura)
        DlgPlanificar_1.setTabOrder(self.pushButtonChapaSoldadura, self.pushButtonGomeria)
        DlgPlanificar_1.setTabOrder(self.pushButtonGomeria, self.buttonBox)

    def retranslateUi(self, DlgPlanificar_1):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DlgPlanificar_1 = QtGui.QDialog()
    ui = Ui_DlgPlanificar_1()
    ui.setupUi(DlgPlanificar_1)
    DlgPlanificar_1.show()
    sys.exit(app.exec_())

