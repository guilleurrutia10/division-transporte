# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WidgetListadoSecciones.ui'
#
# Created: Sun Nov 18 20:38:03 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_FormListadoSecciones(object):
    def setupUi(self, FormListadoSecciones):
        FormListadoSecciones.setObjectName(_fromUtf8("FormListadoSecciones"))
        FormListadoSecciones.resize(600, 323)
        FormListadoSecciones.setWindowTitle(QtGui.QApplication.translate("FormListadoSecciones", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(FormListadoSecciones)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(FormListadoSecciones)
        self.groupBox.setTitle(QtGui.QApplication.translate("FormListadoSecciones", "Listado de Secciones", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tableWidgetListadoSecciones = QtGui.QTableWidget(self.groupBox)
        self.tableWidgetListadoSecciones.setObjectName(_fromUtf8("tableWidgetListadoSecciones"))
        self.tableWidgetListadoSecciones.setColumnCount(4)
        self.tableWidgetListadoSecciones.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("FormListadoSecciones", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidgetListadoSecciones.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("FormListadoSecciones", "Cantidad de empleados", None, QtGui.QApplication.UnicodeUTF8))
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidgetListadoSecciones.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("FormListadoSecciones", "Nombre encargado", None, QtGui.QApplication.UnicodeUTF8))
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidgetListadoSecciones.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("FormListadoSecciones", "Código Sección", None, QtGui.QApplication.UnicodeUTF8))
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidgetListadoSecciones.setHorizontalHeaderItem(3, item)
        self.tableWidgetListadoSecciones.horizontalHeader().setDefaultSectionSize(150)
        self.verticalLayout_2.addWidget(self.tableWidgetListadoSecciones)
        self.verticalLayout.addWidget(self.groupBox)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setRowWrapPolicy(QtGui.QFormLayout.WrapLongRows)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.pushButton_2_Cancelar = QtGui.QPushButton(FormListadoSecciones)
        self.pushButton_2_Cancelar.setText(QtGui.QApplication.translate("FormListadoSecciones", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2_Cancelar.setObjectName(_fromUtf8("pushButton_2_Cancelar"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.pushButton_2_Cancelar)
        self.pushButtonSeleccionar = QtGui.QPushButton(FormListadoSecciones)
        self.pushButtonSeleccionar.setText(QtGui.QApplication.translate("FormListadoSecciones", "Seleccionar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonSeleccionar.setObjectName(_fromUtf8("pushButtonSeleccionar"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.pushButtonSeleccionar)
        self.verticalLayout.addLayout(self.formLayout)

        self.retranslateUi(FormListadoSecciones)
        QtCore.QMetaObject.connectSlotsByName(FormListadoSecciones)

    def retranslateUi(self, FormListadoSecciones):
        item = self.tableWidgetListadoSecciones.horizontalHeaderItem(0)
        item = self.tableWidgetListadoSecciones.horizontalHeaderItem(1)
        item = self.tableWidgetListadoSecciones.horizontalHeaderItem(2)
        item = self.tableWidgetListadoSecciones.horizontalHeaderItem(3)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FormListadoSecciones = QtGui.QWidget()
    ui = Ui_FormListadoSecciones()
    ui.setupUi(FormListadoSecciones)
    FormListadoSecciones.show()
    sys.exit(app.exec_())

