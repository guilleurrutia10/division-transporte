# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WidgetListadoEmpleados.ui'
#
# Created: Wed Dec 05 21:19:28 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(948, 412)
        Form.setMinimumSize(QtCore.QSize(705, 0))
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 99))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox_5 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_5.setMaximumSize(QtCore.QSize(153, 16777215))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("Form", "Buscar Documento", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lineEditBuscarDocumento = QtGui.QLineEdit(self.groupBox_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditBuscarDocumento.sizePolicy().hasHeightForWidth())
        self.lineEditBuscarDocumento.setSizePolicy(sizePolicy)
        self.lineEditBuscarDocumento.setMaximumSize(QtCore.QSize(133, 20))
        self.lineEditBuscarDocumento.setObjectName(_fromUtf8("lineEditBuscarDocumento"))
        self.horizontalLayout_4.addWidget(self.lineEditBuscarDocumento)
        self.horizontalLayout.addWidget(self.groupBox_5)
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Form", "Filtrar Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lineEditFiltroNombre = QtGui.QLineEdit(self.groupBox_2)
        self.lineEditFiltroNombre.setObjectName(_fromUtf8("lineEditFiltroNombre"))
        self.horizontalLayout_2.addWidget(self.lineEditFiltroNombre)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_4.setTitle(QtGui.QApplication.translate("Form", "Filtrar por Fecha", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.dateEditFechaInicio = QtGui.QDateEdit(self.groupBox_4)
        self.dateEditFechaInicio.setObjectName(_fromUtf8("dateEditFechaInicio"))
        self.verticalLayout_2.addWidget(self.dateEditFechaInicio)
        self.dateEditFechaFin = QtGui.QDateEdit(self.groupBox_4)
        self.dateEditFechaFin.setObjectName(_fromUtf8("dateEditFechaFin"))
        self.verticalLayout_2.addWidget(self.dateEditFechaFin)
        self.horizontalLayout.addWidget(self.groupBox_4)
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Form", "Filtro Seccion", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lineEditFiltroSeccion = QtGui.QLineEdit(self.groupBox_3)
        self.lineEditFiltroSeccion.setObjectName(_fromUtf8("lineEditFiltroSeccion"))
        self.horizontalLayout_3.addWidget(self.lineEditFiltroSeccion)
        self.horizontalLayout.addWidget(self.groupBox_3)
        self.pushButtonBuscar = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonBuscar.sizePolicy().hasHeightForWidth())
        self.pushButtonBuscar.setSizePolicy(sizePolicy)
        self.pushButtonBuscar.setWhatsThis(QtGui.QApplication.translate("Form", "Buscar segun el criterio elegido", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonBuscar.setText(QtGui.QApplication.translate("Form", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonBuscar.setObjectName(_fromUtf8("pushButtonBuscar"))
        self.horizontalLayout.addWidget(self.pushButtonBuscar)
        self.verticalLayout.addWidget(self.groupBox)
        self.tableWidgetDatosEmpleados = QtGui.QTableWidget(Form)
        self.tableWidgetDatosEmpleados.setObjectName(_fromUtf8("tableWidgetDatosEmpleados"))
        self.tableWidgetDatosEmpleados.setColumnCount(11)
        self.tableWidgetDatosEmpleados.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Form", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDatosEmpleados.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Form", "Apellido", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDatosEmpleados.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Form", "Tipo Documento", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDatosEmpleados.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Form", "Numero Documento", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDatosEmpleados.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Form", "Seccion", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDatosEmpleados.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Form", "Fecha Nacimiento", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDatosEmpleados.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Form", "Domicilio", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDatosEmpleados.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Form", "Email", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDatosEmpleados.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Form", "Telefono", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDatosEmpleados.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Form", "Fecha Alta", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDatosEmpleados.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Form", "Fecha Baja", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetDatosEmpleados.setHorizontalHeaderItem(10, item)
        self.tableWidgetDatosEmpleados.horizontalHeader().setDefaultSectionSize(150)
        self.verticalLayout.addWidget(self.tableWidgetDatosEmpleados)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
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
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

