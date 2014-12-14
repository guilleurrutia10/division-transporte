# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WidgetModificarPersonal.ui'
#
# Created: Sat Dec 13 23:30:33 2014
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
#Se modifico para agregar una tabla de empleados
from Utiles_formulario import TablaDeEmpleados
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_WidgetModificarPersonal(object):
    def setupUi(self, WidgetModificarPersonal):
        WidgetModificarPersonal.setObjectName(_fromUtf8("WidgetModificarPersonal"))
        WidgetModificarPersonal.resize(915, 491)
        WidgetModificarPersonal.setWindowTitle(QtGui.QApplication.translate("WidgetModificarPersonal", "Modificar Personal", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(WidgetModificarPersonal)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(WidgetModificarPersonal)
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
        self.groupBox_2.setTitle(QtGui.QApplication.translate("WidgetModificarPersonal", "Filtrar", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lineEditBuscarNombre = QtGui.QLineEdit(self.groupBox_2)
        self.lineEditBuscarNombre.setObjectName(_fromUtf8("lineEditBuscarNombre"))
        self.horizontalLayout_2.addWidget(self.lineEditBuscarNombre)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.verticalLayout.addWidget(self.groupBox)
#        self.tableWidgetEmpleados = QtGui.QTableWidget(WidgetModificarPersonal)
        self.tableWidgetEmpleados = TablaDeEmpleados(WidgetModificarPersonal)
        self.tableWidgetEmpleados.setObjectName(_fromUtf8("tableWidgetEmpleados"))
        self.tableWidgetEmpleados.setColumnCount(8)
        self.tableWidgetEmpleados.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("WidgetModificarPersonal", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetEmpleados.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("WidgetModificarPersonal", "Apellido", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetEmpleados.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("WidgetModificarPersonal", "Tipo Documento", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetEmpleados.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("WidgetModificarPersonal", "Numero Documento", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetEmpleados.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("WidgetModificarPersonal", "Fecha Nacimiento", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetEmpleados.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("WidgetModificarPersonal", "Domicilio", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetEmpleados.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("WidgetModificarPersonal", "Email", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetEmpleados.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("WidgetModificarPersonal", "Telefono", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetEmpleados.setHorizontalHeaderItem(7, item)
        self.tableWidgetEmpleados.horizontalHeader().setDefaultSectionSize(120)
        self.verticalLayout.addWidget(self.tableWidgetEmpleados)
        self.groupBox_3 = QtGui.QGroupBox(WidgetModificarPersonal)
        self.groupBox_3.setMinimumSize(QtCore.QSize(50, 50))
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.pushButtonModificar = QtGui.QPushButton(self.groupBox_3)
        self.pushButtonModificar.setText(QtGui.QApplication.translate("WidgetModificarPersonal", "Modificar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonModificar.setObjectName(_fromUtf8("pushButtonModificar"))
        self.horizontalLayout_3.addWidget(self.pushButtonModificar)
        self.verticalLayout.addWidget(self.groupBox_3)

        self.retranslateUi(WidgetModificarPersonal)
        QtCore.QMetaObject.connectSlotsByName(WidgetModificarPersonal)

    def retranslateUi(self, WidgetModificarPersonal):
        item = self.tableWidgetEmpleados.horizontalHeaderItem(0)
        item = self.tableWidgetEmpleados.horizontalHeaderItem(1)
        item = self.tableWidgetEmpleados.horizontalHeaderItem(2)
        item = self.tableWidgetEmpleados.horizontalHeaderItem(3)
        item = self.tableWidgetEmpleados.horizontalHeaderItem(4)
        item = self.tableWidgetEmpleados.horizontalHeaderItem(5)
        item = self.tableWidgetEmpleados.horizontalHeaderItem(6)
        item = self.tableWidgetEmpleados.horizontalHeaderItem(7)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    WidgetModificarPersonal = QtGui.QWidget()
    ui = Ui_WidgetModificarPersonal()
    ui.setupUi(WidgetModificarPersonal)
    WidgetModificarPersonal.show()
    sys.exit(app.exec_())

