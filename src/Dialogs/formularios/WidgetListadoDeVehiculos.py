# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/WidgetListadoDeVehiculos.ui'
#
# Created: Wed Sep 10 21:47:42 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

from Utiles_formulario import TablaVehiculos

class Ui_FormListadoVehiculos(object):
    def setupUi(self, FormListadoVehiculos):
        FormListadoVehiculos.setObjectName(_fromUtf8("FormListadoVehiculos"))
        FormListadoVehiculos.resize(771, 476)
        FormListadoVehiculos.setMinimumSize(QtCore.QSize(771, 476))
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
        self.labelDominio.setObjectName(_fromUtf8("labelDominio"))
        self.horizontalLayout.addWidget(self.labelDominio)
        self.lineEditBuscar = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditBuscar.sizePolicy().hasHeightForWidth())
        self.lineEditBuscar.setSizePolicy(sizePolicy)
        self.lineEditBuscar.setMinimumSize(QtCore.QSize(133, 10))
        self.lineEditBuscar.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEditBuscar.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEditBuscar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEditBuscar.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEditBuscar.setObjectName(_fromUtf8("lineEditBuscar"))
        self.horizontalLayout.addWidget(self.lineEditBuscar)
        spacerItem = QtGui.QSpacerItem(513, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonToPdf = QtGui.QPushButton(self.groupBox)
        self.pushButtonToPdf.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/recursos/iconos/pdf.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonToPdf.setIcon(icon)
        self.pushButtonToPdf.setIconSize(QtCore.QSize(32, 32))
        self.pushButtonToPdf.setObjectName(_fromUtf8("pushButtonToPdf"))
        self.horizontalLayout.addWidget(self.pushButtonToPdf)
        self.verticalLayout.addWidget(self.groupBox)
        self.labelListadoVehiculos = QtGui.QLabel(FormListadoVehiculos)
        self.labelListadoVehiculos.setObjectName(_fromUtf8("labelListadoVehiculos"))
        self.verticalLayout.addWidget(self.labelListadoVehiculos)
        self.tableWidgetListadoDeVehiculos = TablaVehiculos(FormListadoVehiculos)
        self.tableWidgetListadoDeVehiculos.setObjectName(_fromUtf8("tableWidgetListadoDeVehiculos"))
        self.tableWidgetListadoDeVehiculos.setColumnCount(5)
        self.tableWidgetListadoDeVehiculos.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetListadoDeVehiculos.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetListadoDeVehiculos.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetListadoDeVehiculos.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetListadoDeVehiculos.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetListadoDeVehiculos.setHorizontalHeaderItem(4, item)
        self.tableWidgetListadoDeVehiculos.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidgetListadoDeVehiculos.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableWidgetListadoDeVehiculos)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButtonSeleccionar = QtGui.QPushButton(FormListadoVehiculos)
        self.pushButtonSeleccionar.setObjectName(_fromUtf8("pushButtonSeleccionar"))
        self.horizontalLayout_2.addWidget(self.pushButtonSeleccionar)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(FormListadoVehiculos)
        QtCore.QMetaObject.connectSlotsByName(FormListadoVehiculos)

    def retranslateUi(self, FormListadoVehiculos):
        FormListadoVehiculos.setWindowTitle(_translate("FormListadoVehiculos", "Form", None))
        self.labelDominio.setText(_translate("FormListadoVehiculos", "Filtrar:", None))
        self.pushButtonToPdf.setToolTip(_translate("FormListadoVehiculos", "Haga click para exportar el listado como pdf", None))
        self.labelListadoVehiculos.setText(_translate("FormListadoVehiculos", "Listado de Vehículos", None))
        item = self.tableWidgetListadoDeVehiculos.horizontalHeaderItem(0)
        item.setText(_translate("FormListadoVehiculos", "Dominio", None))
        item = self.tableWidgetListadoDeVehiculos.horizontalHeaderItem(1)
        item.setText(_translate("FormListadoVehiculos", "Marca", None))
        item = self.tableWidgetListadoDeVehiculos.horizontalHeaderItem(2)
        item.setText(_translate("FormListadoVehiculos", "Registro Interno", None))
        item = self.tableWidgetListadoDeVehiculos.horizontalHeaderItem(3)
        item.setText(_translate("FormListadoVehiculos", "Numero de Chasis", None))
        item = self.tableWidgetListadoDeVehiculos.horizontalHeaderItem(4)
        item.setText(_translate("FormListadoVehiculos", "Comisaría", None))
        self.pushButtonSeleccionar.setText(_translate("FormListadoVehiculos", "Seleccionar", None))

import recursos_rc
