# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogRemoverEmpleadoDeSeccion.ui'
#
# Created: Wed Nov 14 18:14:42 2012
#      by: PyQt4 UI code generator 4.9.5
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
        Dialog.resize(659, 480)
        Dialog.setMinimumSize(QtCore.QSize(0, 0))
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setMinimumSize(QtCore.QSize(331, 41))
        self.groupBox.setMaximumSize(QtCore.QSize(331, 41))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.listView = QtGui.QListView(self.groupBox)
        self.listView.setGeometry(QtCore.QRect(20, 20, 211, 16))
        self.listView.setMinimumSize(QtCore.QSize(211, 16))
        self.listView.setMaximumSize(QtCore.QSize(211, 16))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.pushButton_FiltroSeccion = QtGui.QPushButton(self.groupBox)
        self.pushButton_FiltroSeccion.setGeometry(QtCore.QRect(240, 20, 75, 16))
        self.pushButton_FiltroSeccion.setObjectName(_fromUtf8("pushButton_FiltroSeccion"))
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setMinimumSize(QtCore.QSize(331, 41))
        self.groupBox_2.setMaximumSize(QtCore.QSize(331, 41))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.listView_3 = QtGui.QListView(self.groupBox_2)
        self.listView_3.setGeometry(QtCore.QRect(20, 20, 211, 16))
        self.listView_3.setMinimumSize(QtCore.QSize(211, 16))
        self.listView_3.setMaximumSize(QtCore.QSize(211, 16))
        self.listView_3.setObjectName(_fromUtf8("listView_3"))
        self.pushButton_FiltroDocumento = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_FiltroDocumento.setGeometry(QtCore.QRect(240, 20, 75, 16))
        self.pushButton_FiltroDocumento.setObjectName(_fromUtf8("pushButton_FiltroDocumento"))
        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 2)
        self.groupBox_4 = QtGui.QGroupBox(Dialog)
        self.groupBox_4.setMinimumSize(QtCore.QSize(331, 41))
        self.groupBox_4.setMaximumSize(QtCore.QSize(331, 41))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.listView_7 = QtGui.QListView(self.groupBox_4)
        self.listView_7.setGeometry(QtCore.QRect(20, 20, 211, 16))
        self.listView_7.setMinimumSize(QtCore.QSize(211, 16))
        self.listView_7.setMaximumSize(QtCore.QSize(211, 16))
        self.listView_7.setObjectName(_fromUtf8("listView_7"))
        self.pushButton_FiltroNombre = QtGui.QPushButton(self.groupBox_4)
        self.pushButton_FiltroNombre.setGeometry(QtCore.QRect(240, 20, 75, 16))
        self.pushButton_FiltroNombre.setObjectName(_fromUtf8("pushButton_FiltroNombre"))
        self.gridLayout.addWidget(self.groupBox_4, 2, 0, 1, 2)
        self.tableWidget = QtGui.QTableWidget(Dialog)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(201, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setMinimumSize(QtCore.QSize(431, 41))
        self.widget.setMaximumSize(QtCore.QSize(431, 41))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(304, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_Remover = QtGui.QPushButton(self.widget)
        self.pushButton_Remover.setObjectName(_fromUtf8("pushButton_Remover"))
        self.horizontalLayout.addWidget(self.pushButton_Remover)
        self.gridLayout.addWidget(self.widget, 4, 1, 1, 1)
        self.groupBoxButtonBox = QtGui.QGroupBox(Dialog)
        self.groupBoxButtonBox.setMinimumSize(QtCore.QSize(271, 41))
        self.groupBoxButtonBox.setMaximumSize(QtCore.QSize(16777215, 41))
        self.groupBoxButtonBox.setTitle(_fromUtf8(""))
        self.groupBoxButtonBox.setObjectName(_fromUtf8("groupBoxButtonBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBoxButtonBox)
        self.gridLayout_2.setContentsMargins(9, 9, 9, 8)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pushButtonAceptar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonAceptar.setObjectName(_fromUtf8("pushButtonAceptar"))
        self.gridLayout_2.addWidget(self.pushButtonAceptar, 0, 1, 1, 1)
        self.pushButtonCancelar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonCancelar.setObjectName(_fromUtf8("pushButtonCancelar"))
        self.gridLayout_2.addWidget(self.pushButtonCancelar, 0, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBoxButtonBox, 5, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Buscar por Sección", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_FiltroSeccion.setText(QtGui.QApplication.translate("Dialog", "Filtrar", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Dialog", "Buscar por Nº Documento", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_FiltroDocumento.setText(QtGui.QApplication.translate("Dialog", "Filtrar", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("Dialog", "Buscar por Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_FiltroNombre.setText(QtGui.QApplication.translate("Dialog", "Filtrar", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("Dialog", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("Dialog", "Tipo de Documento", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(QtGui.QApplication.translate("Dialog", "Nº Documento", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(QtGui.QApplication.translate("Dialog", "Sección", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(QtGui.QApplication.translate("Dialog", "Fecha de Nac", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(QtGui.QApplication.translate("Dialog", "Email", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Remover.setText(QtGui.QApplication.translate("Dialog", "Remover Empleado", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAceptar.setText(QtGui.QApplication.translate("Dialog", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("Dialog", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

