# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/WidgetListadoSecciones2.ui'
#
# Created: Thu Aug 28 12:21:56 2014
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

class Ui_FormListadoSecciones(object):
    def setupUi(self, FormListadoSecciones):
        FormListadoSecciones.setObjectName(_fromUtf8("FormListadoSecciones"))
        FormListadoSecciones.resize(600, 323)
        self.verticalLayout = QtGui.QVBoxLayout(FormListadoSecciones)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(FormListadoSecciones)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tableWidgetListadoSecciones = QtGui.QTableWidget(self.groupBox)
        self.tableWidgetListadoSecciones.setObjectName(_fromUtf8("tableWidgetListadoSecciones"))
        self.tableWidgetListadoSecciones.setColumnCount(4)
        self.tableWidgetListadoSecciones.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidgetListadoSecciones.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidgetListadoSecciones.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidgetListadoSecciones.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidgetListadoSecciones.setHorizontalHeaderItem(3, item)
        self.tableWidgetListadoSecciones.horizontalHeader().setDefaultSectionSize(180)
        self.tableWidgetListadoSecciones.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.tableWidgetListadoSecciones)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(FormListadoSecciones)
        QtCore.QMetaObject.connectSlotsByName(FormListadoSecciones)

    def retranslateUi(self, FormListadoSecciones):
        FormListadoSecciones.setWindowTitle(_translate("FormListadoSecciones", "Form", None))
        self.groupBox.setTitle(_translate("FormListadoSecciones", "Listado de Secciones", None))
        item = self.tableWidgetListadoSecciones.horizontalHeaderItem(0)
        item.setText(_translate("FormListadoSecciones", "Nombre", None))
        item = self.tableWidgetListadoSecciones.horizontalHeaderItem(1)
        item.setText(_translate("FormListadoSecciones", "Cantidad de empleados", None))
        item = self.tableWidgetListadoSecciones.horizontalHeaderItem(2)
        item.setText(_translate("FormListadoSecciones", "Nombre encargado", None))
        item = self.tableWidgetListadoSecciones.horizontalHeaderItem(3)
        item.setText(_translate("FormListadoSecciones", "Código Sección", None))

