# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WidgetBajaPersonal.ui'
#
# Created: Thu Nov 22 02:15:26 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_FormBajaPersonal(object):
    def setupUi(self, FormBajaPersonal):
        FormBajaPersonal.setObjectName(_fromUtf8("FormBajaPersonal"))
        FormBajaPersonal.resize(915, 491)
        FormBajaPersonal.setWindowTitle(QtGui.QApplication.translate("FormBajaPersonal", "BajaPersonal", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(FormBajaPersonal)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(FormBajaPersonal)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox_5 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_5.setMinimumSize(QtCore.QSize(150, 70))
        self.groupBox_5.setMaximumSize(QtCore.QSize(200, 70))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("FormBajaPersonal", "Buscar Documento", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEditBuscarDocumento = QtGui.QLineEdit(self.groupBox_5)
        self.lineEditBuscarDocumento.setObjectName(_fromUtf8("lineEditBuscarDocumento"))
        self.horizontalLayout.addWidget(self.lineEditBuscarDocumento)
        self.verticalLayout_2.addWidget(self.groupBox_5)
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(150, 70))
        self.groupBox_2.setMaximumSize(QtCore.QSize(200, 70))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("FormBajaPersonal", "Buscar Nombre", None, QtGui.QApplication.UnicodeUTF8))
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
        self.pushButtonBuscar.setWhatsThis(QtGui.QApplication.translate("FormBajaPersonal", "Buscar segun el criterio elegido", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonBuscar.setText(QtGui.QApplication.translate("FormBajaPersonal", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonBuscar.setObjectName(_fromUtf8("pushButtonBuscar"))
        self.verticalLayout_2.addWidget(self.pushButtonBuscar)
        self.verticalLayout.addWidget(self.groupBox)
        self.tableWidgetDatosEmpleados = QtGui.QTableWidget(FormBajaPersonal)
        self.tableWidgetDatosEmpleados.setObjectName(_fromUtf8("tableWidgetDatosEmpleados"))
        self.tableWidgetDatosEmpleados.setColumnCount(11)
        self.tableWidgetDatosEmpleados.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("FormBajaPersonal", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDatosEmpleados.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("FormBajaPersonal", "Apellido", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDatosEmpleados.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("FormBajaPersonal", "Tipo Documento", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDatosEmpleados.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("FormBajaPersonal", "Numero Documento", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDatosEmpleados.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("FormBajaPersonal", "Seccion", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDatosEmpleados.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("FormBajaPersonal", "Fecha Nacimiento", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDatosEmpleados.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("FormBajaPersonal", "Domicilio", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDatosEmpleados.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("FormBajaPersonal", "Email", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDatosEmpleados.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("FormBajaPersonal", "Telefono", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDatosEmpleados.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("FormBajaPersonal", "Fecha Alta", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDatosEmpleados.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("FormBajaPersonal", "Fecha Baja", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDatosEmpleados.setHorizontalHeaderItem(10, item)
        self.tableWidgetDatosEmpleados.horizontalHeader().setDefaultSectionSize(120)
        self.verticalLayout.addWidget(self.tableWidgetDatosEmpleados)
        self.groupBox_3 = QtGui.QGroupBox(FormBajaPersonal)
        self.groupBox_3.setMinimumSize(QtCore.QSize(50, 50))
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.pushButtonModificar = QtGui.QPushButton(self.groupBox_3)
        self.pushButtonModificar.setText(QtGui.QApplication.translate("FormBajaPersonal", "Modificar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonModificar.setObjectName(_fromUtf8("pushButtonModificar"))
        self.horizontalLayout_3.addWidget(self.pushButtonModificar)
        self.pushButtonDarDeBaja = QtGui.QPushButton(self.groupBox_3)
        self.pushButtonDarDeBaja.setText(QtGui.QApplication.translate("FormBajaPersonal", "Dar de Baja", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonDarDeBaja.setObjectName(_fromUtf8("pushButtonDarDeBaja"))
        self.horizontalLayout_3.addWidget(self.pushButtonDarDeBaja)
        self.verticalLayout.addWidget(self.groupBox_3)

        self.retranslateUi(FormBajaPersonal)
        QtCore.QMetaObject.connectSlotsByName(FormBajaPersonal)

    def retranslateUi(self, FormBajaPersonal):
        item = self.tableWidgetDatosEmpleados.horizontalHeaderItem(0)
        item = self.tableWidgetDatosEmpleados.horizontalHeaderItem(1)
        item = self.tableWidgetDatosEmpleados.horizontalHeaderItem(2)
        item = self.tableWidgetDatosEmpleados.horizontalHeaderItem(3)
        item = self.tableWidgetDatosEmpleados.horizontalHeaderItem(4)
        item = self.tableWidgetDatosEmpleados.horizontalHeaderItem(5)
        item = self.tableWidgetDatosEmpleados.horizontalHeaderItem(6)
        item = self.tableWidgetDatosEmpleados.horizontalHeaderItem(7)
        item = self.tableWidgetDatosEmpleados.horizontalHeaderItem(8)
        item = self.tableWidgetDatosEmpleados.horizontalHeaderItem(9)
        item = self.tableWidgetDatosEmpleados.horizontalHeaderItem(10)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FormBajaPersonal = QtGui.QWidget()
    ui = Ui_FormBajaPersonal()
    ui.setupUi(FormBajaPersonal)
    FormBajaPersonal.show()
    sys.exit(app.exec_())

