# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogBajaPersonal.ui'
#
# Created: Wed Dec 10 18:08:49 2014
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!
# GUARNING! Este fialogo posee un a tabla de empleados:
from Utiles_formulario import TablaDeEmpleados
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogBajaPersonal(object):
    def setupUi(self, DialogBajaPersonal):
        DialogBajaPersonal.setObjectName(_fromUtf8("DialogBajaPersonal"))
        DialogBajaPersonal.resize(835, 469)
        DialogBajaPersonal.setWindowTitle(QtGui.QApplication.translate("DialogBajaPersonal", "Baja de Personal", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout = QtGui.QGridLayout(DialogBajaPersonal)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox_5 = QtGui.QGroupBox(DialogBajaPersonal)
        self.groupBox_5.setMinimumSize(QtCore.QSize(150, 70))
        self.groupBox_5.setMaximumSize(QtCore.QSize(200, 70))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("DialogBajaPersonal", "Filtro", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEditBuscarDocumento = QtGui.QLineEdit(self.groupBox_5)
        self.lineEditBuscarDocumento.setObjectName(_fromUtf8("lineEditBuscarDocumento"))
        self.horizontalLayout.addWidget(self.lineEditBuscarDocumento)
        self.gridLayout.addWidget(self.groupBox_5, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(449, 57, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(DialogBajaPersonal)
        self.groupBox_3.setMinimumSize(QtCore.QSize(50, 50))
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.pushButtonDarDeBaja = QtGui.QPushButton(self.groupBox_3)
        self.pushButtonDarDeBaja.setText(QtGui.QApplication.translate("DialogBajaPersonal", "Dar de Baja", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonDarDeBaja.setObjectName(_fromUtf8("pushButtonDarDeBaja"))
        self.horizontalLayout_3.addWidget(self.pushButtonDarDeBaja)
        self.pushButtonCancelar = QtGui.QPushButton(self.groupBox_3)
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("DialogBajaPersonal", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setObjectName(_fromUtf8("pushButtonCancelar"))
        self.horizontalLayout_3.addWidget(self.pushButtonCancelar)
        self.gridLayout.addWidget(self.groupBox_3, 2, 0, 1, 2)
#        self.tableWidgetDatosEmpleados = QtGui.QTableWidget(DialogBajaPersonal)
        self.tableWidgetDatosEmpleados = TablaDeEmpleados(DialogBajaPersonal)
        self.tableWidgetDatosEmpleados.setMinimumSize(QtCore.QSize(691, 216))
        self.tableWidgetDatosEmpleados.setObjectName(_fromUtf8("tableWidgetDatosEmpleados"))
        self.tableWidgetDatosEmpleados.setColumnCount(10)
        self.tableWidgetDatosEmpleados.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogBajaPersonal", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDatosEmpleados.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogBajaPersonal", "Apellido", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDatosEmpleados.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogBajaPersonal", "Tipo Documento", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDatosEmpleados.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogBajaPersonal", "Numero Documento", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDatosEmpleados.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogBajaPersonal", "Seccion", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDatosEmpleados.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogBajaPersonal", "Fecha Nacimiento", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDatosEmpleados.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogBajaPersonal", "Domicilio", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDatosEmpleados.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogBajaPersonal", "Email", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDatosEmpleados.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogBajaPersonal", "Telefono", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDatosEmpleados.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogBajaPersonal", "Fecha Alta", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDatosEmpleados.setHorizontalHeaderItem(9, item)
        self.tableWidgetDatosEmpleados.horizontalHeader().setDefaultSectionSize(120)
        self.gridLayout.addWidget(self.tableWidgetDatosEmpleados, 1, 0, 1, 2)

        self.retranslateUi(DialogBajaPersonal)
        QtCore.QMetaObject.connectSlotsByName(DialogBajaPersonal)

    def retranslateUi(self, DialogBajaPersonal):
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


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogBajaPersonal = QtGui.QDialog()
    ui = Ui_DialogBajaPersonal()
    ui.setupUi(DialogBajaPersonal)
    DialogBajaPersonal.show()
    sys.exit(app.exec_())

