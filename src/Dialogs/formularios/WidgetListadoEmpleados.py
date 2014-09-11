# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/WidgetListadoEmpleados.ui'
#
# Created: Wed Sep 10 22:25:43 2014
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(899, 454)
        Form.setMinimumSize(QtCore.QSize(705, 0))
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 130))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 99))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox_5 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_5.setMaximumSize(QtCore.QSize(200, 16777215))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lineEditBuscarDocumento = QtGui.QLineEdit(self.groupBox_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditBuscarDocumento.sizePolicy().hasHeightForWidth())
        self.lineEditBuscarDocumento.setSizePolicy(sizePolicy)
        self.lineEditBuscarDocumento.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEditBuscarDocumento.setMaximumSize(QtCore.QSize(133, 20))
        self.lineEditBuscarDocumento.setObjectName(_fromUtf8("lineEditBuscarDocumento"))
        self.horizontalLayout_4.addWidget(self.lineEditBuscarDocumento)
        self.horizontalLayout.addWidget(self.groupBox_5)
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.dateEditFechaInicio = QtGui.QDateEdit(self.groupBox_4)
        self.dateEditFechaInicio.setCalendarPopup(True)
        self.dateEditFechaInicio.setObjectName(_fromUtf8("dateEditFechaInicio"))
        self.verticalLayout_2.addWidget(self.dateEditFechaInicio)
        self.dateEditFechaFin = QtGui.QDateEdit(self.groupBox_4)
        self.dateEditFechaFin.setCalendarPopup(True)
        self.dateEditFechaFin.setObjectName(_fromUtf8("dateEditFechaFin"))
        self.verticalLayout_2.addWidget(self.dateEditFechaFin)
        self.horizontalLayout.addWidget(self.groupBox_4)
        self.pushButtonToPDF = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonToPDF.sizePolicy().hasHeightForWidth())
        self.pushButtonToPDF.setSizePolicy(sizePolicy)
        self.pushButtonToPDF.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/recursos/iconos/pdf.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonToPDF.setIcon(icon)
        self.pushButtonToPDF.setObjectName(_fromUtf8("pushButtonToPDF"))
        self.horizontalLayout.addWidget(self.pushButtonToPDF)
        self.verticalLayout.addWidget(self.groupBox)
        self.tableWidgetDatosEmpleados = QtGui.QTableWidget(Form)
        self.tableWidgetDatosEmpleados.setObjectName(_fromUtf8("tableWidgetDatosEmpleados"))
        self.tableWidgetDatosEmpleados.setColumnCount(11)
        self.tableWidgetDatosEmpleados.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetDatosEmpleados.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetDatosEmpleados.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetDatosEmpleados.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetDatosEmpleados.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetDatosEmpleados.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetDatosEmpleados.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetDatosEmpleados.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetDatosEmpleados.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetDatosEmpleados.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetDatosEmpleados.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetDatosEmpleados.setHorizontalHeaderItem(10, item)
        self.tableWidgetDatosEmpleados.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidgetDatosEmpleados.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableWidgetDatosEmpleados)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox_5.setTitle(_translate("Form", "Buscar Documento", None))
        self.groupBox_4.setTitle(_translate("Form", "Filtrar por Fecha", None))
        self.pushButtonToPDF.setToolTip(_translate("Form", "Haga click para exportar el listado como pdf", None))
        self.pushButtonToPDF.setWhatsThis(_translate("Form", "Buscar segun el criterio elegido", None))
        item = self.tableWidgetDatosEmpleados.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Nombre", None))
        item = self.tableWidgetDatosEmpleados.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Apellido", None))
        item = self.tableWidgetDatosEmpleados.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Tipo Documento", None))
        item = self.tableWidgetDatosEmpleados.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Número Documento", None))
        item = self.tableWidgetDatosEmpleados.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Sección", None))
        item = self.tableWidgetDatosEmpleados.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Fecha Nacimiento", None))
        item = self.tableWidgetDatosEmpleados.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Domicilio", None))
        item = self.tableWidgetDatosEmpleados.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Email", None))
        item = self.tableWidgetDatosEmpleados.horizontalHeaderItem(8)
        item.setText(_translate("Form", "Teléfono", None))
        item = self.tableWidgetDatosEmpleados.horizontalHeaderItem(9)
        item.setText(_translate("Form", "Fecha Alta", None))
        item = self.tableWidgetDatosEmpleados.horizontalHeaderItem(10)
        item.setText(_translate("Form", "Fecha Baja", None))

import recursos_rc
