# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormOpcJefeDivision.ui'
#
# Created: Sun Nov 25 16:33:46 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogOpcionesJefeDivision(object):
    def setupUi(self, DialogOpcionesJefeDivision):
        DialogOpcionesJefeDivision.setObjectName(_fromUtf8("DialogOpcionesJefeDivision"))
        DialogOpcionesJefeDivision.resize(337, 387)
        DialogOpcionesJefeDivision.setWindowTitle(QtGui.QApplication.translate("DialogOpcionesJefeDivision", "Opciones Jefe de Division", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalLayoutWidget = QtGui.QWidget(DialogOpcionesJefeDivision)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 141, 31))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lbl_perfil = QtGui.QLabel(self.horizontalLayoutWidget)
        self.lbl_perfil.setText(QtGui.QApplication.translate("DialogOpcionesJefeDivision", "Perfil:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_perfil.setObjectName(_fromUtf8("lbl_perfil"))
        self.horizontalLayout.addWidget(self.lbl_perfil)
        self.lblPerfil = QtGui.QLabel(self.horizontalLayoutWidget)
        self.lblPerfil.setText(QtGui.QApplication.translate("DialogOpcionesJefeDivision", "Jefe de Division", None, QtGui.QApplication.UnicodeUTF8))
        self.lblPerfil.setObjectName(_fromUtf8("lblPerfil"))
        self.horizontalLayout.addWidget(self.lblPerfil)
        self.groupBoxOpcJD = QtGui.QGroupBox(DialogOpcionesJefeDivision)
        self.groupBoxOpcJD.setGeometry(QtCore.QRect(20, 50, 301, 291))
        self.groupBoxOpcJD.setTitle(QtGui.QApplication.translate("DialogOpcionesJefeDivision", "Opciones", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxOpcJD.setObjectName(_fromUtf8("groupBoxOpcJD"))
        self.gridLayoutWidget = QtGui.QWidget(self.groupBoxOpcJD)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 261, 251))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(58, 38, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Ignored)
        self.gridLayout.addItem(spacerItem, 4, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(38, 58, QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 3, 1, 1)
        self.button_opcPersonal = QtGui.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_opcPersonal.sizePolicy().hasHeightForWidth())
        self.button_opcPersonal.setSizePolicy(sizePolicy)
        self.button_opcPersonal.setText(QtGui.QApplication.translate("DialogOpcionesJefeDivision", "Opciones\n"
"de Personal", None, QtGui.QApplication.UnicodeUTF8))
        self.button_opcPersonal.setObjectName(_fromUtf8("button_opcPersonal"))
        self.gridLayout.addWidget(self.button_opcPersonal, 1, 2, 1, 1)
        self.button_opcRepuestos = QtGui.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_opcRepuestos.sizePolicy().hasHeightForWidth())
        self.button_opcRepuestos.setSizePolicy(sizePolicy)
        self.button_opcRepuestos.setText(QtGui.QApplication.translate("DialogOpcionesJefeDivision", "Opciones \n"
"de Repuestos", None, QtGui.QApplication.UnicodeUTF8))
        self.button_opcRepuestos.setObjectName(_fromUtf8("button_opcRepuestos"))
        self.gridLayout.addWidget(self.button_opcRepuestos, 3, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(58, 38, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem2, 2, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(38, 58, QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(58, 38, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Ignored)
        self.gridLayout.addItem(spacerItem4, 0, 1, 1, 1)
        self.button_opcVehiculo = QtGui.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_opcVehiculo.sizePolicy().hasHeightForWidth())
        self.button_opcVehiculo.setSizePolicy(sizePolicy)
        self.button_opcVehiculo.setText(QtGui.QApplication.translate("DialogOpcionesJefeDivision", "Opciones \n"
" Vehiculos", None, QtGui.QApplication.UnicodeUTF8))
        self.button_opcVehiculo.setObjectName(_fromUtf8("button_opcVehiculo"))
        self.gridLayout.addWidget(self.button_opcVehiculo, 1, 1, 1, 1)
        self.button_AltaSeccion = QtGui.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_AltaSeccion.sizePolicy().hasHeightForWidth())
        self.button_AltaSeccion.setSizePolicy(sizePolicy)
        self.button_AltaSeccion.setText(QtGui.QApplication.translate("DialogOpcionesJefeDivision", "Alta Seccion", None, QtGui.QApplication.UnicodeUTF8))
        self.button_AltaSeccion.setObjectName(_fromUtf8("button_AltaSeccion"))
        self.gridLayout.addWidget(self.button_AltaSeccion, 3, 1, 1, 1)
        self.pushButton_Cerrar = QtGui.QPushButton(DialogOpcionesJefeDivision)
        self.pushButton_Cerrar.setGeometry(QtCore.QRect(250, 350, 75, 23))
        self.pushButton_Cerrar.setText(QtGui.QApplication.translate("DialogOpcionesJefeDivision", "Cerrar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Cerrar.setObjectName(_fromUtf8("pushButton_Cerrar"))

        self.retranslateUi(DialogOpcionesJefeDivision)
        QtCore.QObject.connect(self.pushButton_Cerrar, QtCore.SIGNAL(_fromUtf8("clicked()")), DialogOpcionesJefeDivision.close)
        QtCore.QMetaObject.connectSlotsByName(DialogOpcionesJefeDivision)

    def retranslateUi(self, DialogOpcionesJefeDivision):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogOpcionesJefeDivision = QtGui.QDialog()
    ui = Ui_DialogOpcionesJefeDivision()
    ui.setupUi(DialogOpcionesJefeDivision)
    DialogOpcionesJefeDivision.show()
    sys.exit(app.exec_())

