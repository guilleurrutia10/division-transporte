# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogMuestraLosRepuestos.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(933, 605)
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Repuestos de la Division", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(150, 70))
        self.groupBox_2.setMaximumSize(QtCore.QSize(200, 70))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Dialog", "Buscar Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lineEditBuscarNombre = QtGui.QLineEdit(self.groupBox_2)
        self.lineEditBuscarNombre.setObjectName(_fromUtf8("lineEditBuscarNombre"))
        self.horizontalLayout_2.addWidget(self.lineEditBuscarNombre)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.pushButtonBuscar = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonBuscar.sizePolicy().hasHeightForWidth())
        self.pushButtonBuscar.setSizePolicy(sizePolicy)
        self.pushButtonBuscar.setWhatsThis(QtGui.QApplication.translate("Dialog", "Buscar segun el criterio elegido", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonBuscar.setText(QtGui.QApplication.translate("Dialog", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonBuscar.setObjectName(_fromUtf8("pushButtonBuscar"))
        self.verticalLayout_2.addWidget(self.pushButtonBuscar)
        self.verticalLayout.addWidget(self.groupBox)
        self.tableWidgetDatosRepuestos = QtGui.QTableWidget(Dialog)
        self.tableWidgetDatosRepuestos.setObjectName(_fromUtf8("tableWidgetDatosRepuestos"))
        self.tableWidgetDatosRepuestos.setColumnCount(2)
        self.tableWidgetDatosRepuestos.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Dialog", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDatosRepuestos.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Dialog", "Descripcion", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDatosRepuestos.setHorizontalHeaderItem(1, item)
        self.verticalLayout.addWidget(self.tableWidgetDatosRepuestos)
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setMinimumSize(QtCore.QSize(50, 50))
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonModificarRepuesto = QtGui.QPushButton(self.groupBox_3)
        self.pushButtonModificarRepuesto.setText(QtGui.QApplication.translate("Dialog", "Modificar Repuesto", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonModificarRepuesto.setObjectName(_fromUtf8("pushButtonModificarRepuesto"))
        self.horizontalLayout.addWidget(self.pushButtonModificarRepuesto)
        self.verticalLayout.addWidget(self.groupBox_3)
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
        item = self.tableWidgetDatosRepuestos.horizontalHeaderItem(0)
        item = self.tableWidgetDatosRepuestos.horizontalHeaderItem(1)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

