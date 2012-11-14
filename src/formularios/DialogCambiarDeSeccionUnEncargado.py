# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogCambiarDeSeccionUnEncargado.ui'
#
# Created: Wed Nov 14 00:01:17 2012
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
        Dialog.resize(622, 386)
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setMinimumSize(QtCore.QSize(331, 41))
        self.groupBox.setMaximumSize(QtCore.QSize(331, 41))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Buscar por Sección", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.listView = QtGui.QListView(self.groupBox)
        self.listView.setGeometry(QtCore.QRect(20, 20, 211, 16))
        self.listView.setMinimumSize(QtCore.QSize(211, 16))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 20, 75, 16))
        self.pushButton_3.setText(QtGui.QApplication.translate("Dialog", "Filtrar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setMinimumSize(QtCore.QSize(331, 41))
        self.groupBox_2.setMaximumSize(QtCore.QSize(331, 41))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Dialog", "Buscar por Nº Documento", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.listView_3 = QtGui.QListView(self.groupBox_2)
        self.listView_3.setGeometry(QtCore.QRect(20, 20, 211, 16))
        self.listView_3.setMinimumSize(QtCore.QSize(211, 16))
        self.listView_3.setMaximumSize(QtCore.QSize(211, 16))
        self.listView_3.setObjectName(_fromUtf8("listView_3"))
        self.pushButton_4 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_4.setGeometry(QtCore.QRect(240, 20, 75, 16))
        self.pushButton_4.setText(QtGui.QApplication.translate("Dialog", "Filtrar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 2)
        self.groupBox_4 = QtGui.QGroupBox(Dialog)
        self.groupBox_4.setMinimumSize(QtCore.QSize(331, 41))
        self.groupBox_4.setMaximumSize(QtCore.QSize(331, 41))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("Dialog", "Buscar por Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.listView_7 = QtGui.QListView(self.groupBox_4)
        self.listView_7.setGeometry(QtCore.QRect(20, 20, 211, 16))
        self.listView_7.setMinimumSize(QtCore.QSize(211, 16))
        self.listView_7.setMaximumSize(QtCore.QSize(211, 16))
        self.listView_7.setObjectName(_fromUtf8("listView_7"))
        self.pushButton_5 = QtGui.QPushButton(self.groupBox_4)
        self.pushButton_5.setGeometry(QtCore.QRect(240, 20, 75, 16))
        self.pushButton_5.setText(QtGui.QApplication.translate("Dialog", "Filtrar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout.addWidget(self.groupBox_4, 2, 0, 1, 2)
        self.tableWidget = QtGui.QTableWidget(Dialog)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Dialog", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Dialog", "Tipo de Documento", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Dialog", "Nº Documento", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Dialog", "Sección", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Dialog", "Fecha de Nac.", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("Dialog", "Email", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(164, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setMinimumSize(QtCore.QSize(431, 41))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.pushButton_Cancelar = QtGui.QPushButton(self.widget)
        self.pushButton_Cancelar.setGeometry(QtCore.QRect(350, 10, 75, 23))
        self.pushButton_Cancelar.setText(QtGui.QApplication.translate("Dialog", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Cancelar.setObjectName(_fromUtf8("pushButton_Cancelar"))
        self.pushButton_Asignar = QtGui.QPushButton(self.widget)
        self.pushButton_Asignar.setGeometry(QtCore.QRect(234, 10, 111, 23))
        self.pushButton_Asignar.setText(QtGui.QApplication.translate("Dialog", "Asignar nuevo Jefe", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Asignar.setObjectName(_fromUtf8("pushButton_Asignar"))
        self.gridLayout.addWidget(self.widget, 4, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        item = self.tableWidget.horizontalHeaderItem(0)
        item = self.tableWidget.horizontalHeaderItem(1)
        item = self.tableWidget.horizontalHeaderItem(2)
        item = self.tableWidget.horizontalHeaderItem(3)
        item = self.tableWidget.horizontalHeaderItem(4)
        item = self.tableWidget.horizontalHeaderItem(5)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

