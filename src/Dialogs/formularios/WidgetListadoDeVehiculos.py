# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WidgetListadoDeVehiculos.ui'
#
# Created: Sun Jul 20 21:56:06 2014
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

from Utiles_formulario import TablaVehiculos

class Ui_FormListadoVehiculos(object):
    def setupUi(self, FormListadoVehiculos):
        FormListadoVehiculos.setObjectName(_fromUtf8("FormListadoVehiculos"))
        FormListadoVehiculos.resize(771, 476)
        FormListadoVehiculos.setMinimumSize(QtCore.QSize(771, 476))
        FormListadoVehiculos.setWindowTitle(QtGui.QApplication.translate("FormListadoVehiculos", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(FormListadoVehiculos)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(FormListadoVehiculos)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labelDominio = QtGui.QLabel(self.groupBox)
        self.labelDominio.setText(QtGui.QApplication.translate("FormListadoVehiculos", "Filtrar:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelDominio.setObjectName(_fromUtf8("labelDominio"))
        self.horizontalLayout.addWidget(self.labelDominio)
        self.lineEditBuscar = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditBuscar.sizePolicy().hasHeightForWidth())
        self.lineEditBuscar.setSizePolicy(sizePolicy)
        self.lineEditBuscar.setMinimumSize(QtCore.QSize(133, 20))
        self.lineEditBuscar.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEditBuscar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEditBuscar.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEditBuscar.setObjectName(_fromUtf8("lineEditBuscar"))
        self.horizontalLayout.addWidget(self.lineEditBuscar)
        spacerItem = QtGui.QSpacerItem(513, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.groupBox)
        self.labelListadoVehiculos = QtGui.QLabel(FormListadoVehiculos)
        self.labelListadoVehiculos.setText(QtGui.QApplication.translate("FormListadoVehiculos", "Listado de Vehículos", None, QtGui.QApplication.UnicodeUTF8))
        self.labelListadoVehiculos.setObjectName(_fromUtf8("labelListadoVehiculos"))
        self.verticalLayout.addWidget(self.labelListadoVehiculos)
#        self.tableWidgetListadoDeVehiculos = QtGui.QTableWidget(FormListadoVehiculos)
        self.tableWidgetListadoDeVehiculos = TablaVehiculos(FormListadoVehiculos)
        self.tableWidgetListadoDeVehiculos.setObjectName(_fromUtf8("tableWidgetListadoDeVehiculos"))
        self.tableWidgetListadoDeVehiculos.setColumnCount(5)
        self.tableWidgetListadoDeVehiculos.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("FormListadoVehiculos", "Dominio", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetListadoDeVehiculos.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("FormListadoVehiculos", "Marca", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetListadoDeVehiculos.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("FormListadoVehiculos", "Registro Interno", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetListadoDeVehiculos.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("FormListadoVehiculos", "Numero de Chasis", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetListadoDeVehiculos.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("FormListadoVehiculos", "Comisaría", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetListadoDeVehiculos.setHorizontalHeaderItem(4, item)
        self.tableWidgetListadoDeVehiculos.horizontalHeader().setDefaultSectionSize(150)
        self.verticalLayout.addWidget(self.tableWidgetListadoDeVehiculos)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButtonSeleccionar = QtGui.QPushButton(FormListadoVehiculos)
        self.pushButtonSeleccionar.setText(QtGui.QApplication.translate("FormListadoVehiculos", "Seleccionar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonSeleccionar.setObjectName(_fromUtf8("pushButtonSeleccionar"))
        self.horizontalLayout_2.addWidget(self.pushButtonSeleccionar)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(FormListadoVehiculos)
        QtCore.QMetaObject.connectSlotsByName(FormListadoVehiculos)

    def retranslateUi(self, FormListadoVehiculos):
        item = self.tableWidgetListadoDeVehiculos.horizontalHeaderItem(0)
        item = self.tableWidgetListadoDeVehiculos.horizontalHeaderItem(1)
        item = self.tableWidgetListadoDeVehiculos.horizontalHeaderItem(2)
        item = self.tableWidgetListadoDeVehiculos.horizontalHeaderItem(3)
        item = self.tableWidgetListadoDeVehiculos.horizontalHeaderItem(4)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FormListadoVehiculos = QtGui.QWidget()
    ui = Ui_FormListadoVehiculos()
    ui.setupUi(FormListadoVehiculos)
    FormListadoVehiculos.show()
    sys.exit(app.exec_())

