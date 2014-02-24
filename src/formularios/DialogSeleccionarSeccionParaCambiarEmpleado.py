# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogSeleccionarSeccionParaCambiarEmpleado.ui'
#
# Created: Thu Feb 20 15:08:38 2014
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Utiles_formulario import TablaSecciones

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogSeleccionarUnaSeccion(object):
    def setupUi(self, DialogSeleccionarUnaSeccion):
        DialogSeleccionarUnaSeccion.setObjectName(_fromUtf8("DialogSeleccionarUnaSeccion"))
        DialogSeleccionarUnaSeccion.resize(723, 452)
        DialogSeleccionarUnaSeccion.setMaximumSize(QtCore.QSize(723, 16777215))
        DialogSeleccionarUnaSeccion.setWindowTitle(QtGui.QApplication.translate("DialogSeleccionarUnaSeccion", "Seleccionar una Seccion", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout = QtGui.QGridLayout(DialogSeleccionarUnaSeccion)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(DialogSeleccionarUnaSeccion)
        self.groupBox.setMinimumSize(QtCore.QSize(234, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(234, 56))
        self.groupBox.setTitle(QtGui.QApplication.translate("DialogSeleccionarUnaSeccion", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lineEditFiltro = QtGui.QLineEdit(self.groupBox)
        self.lineEditFiltro.setMinimumSize(QtCore.QSize(133, 20))
        self.lineEditFiltro.setObjectName(_fromUtf8("lineEditFiltro"))
        self.horizontalLayout_2.addWidget(self.lineEditFiltro)
        self.pushButtonFiltrar = QtGui.QPushButton(self.groupBox)
        self.pushButtonFiltrar.setText(QtGui.QApplication.translate("DialogSeleccionarUnaSeccion", "Filtrar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonFiltrar.setObjectName(_fromUtf8("pushButtonFiltrar"))
        self.horizontalLayout_2.addWidget(self.pushButtonFiltrar)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)
        self.groupBoxButtonBox = QtGui.QGroupBox(DialogSeleccionarUnaSeccion)
        self.groupBoxButtonBox.setMinimumSize(QtCore.QSize(271, 41))
        self.groupBoxButtonBox.setMaximumSize(QtCore.QSize(16777215, 41))
        self.groupBoxButtonBox.setTitle(_fromUtf8(""))
        self.groupBoxButtonBox.setObjectName(_fromUtf8("groupBoxButtonBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBoxButtonBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.pushButtonSeleccionar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonSeleccionar.setText(QtGui.QApplication.translate("DialogSeleccionarUnaSeccion", "Seleccionar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonSeleccionar.setObjectName(_fromUtf8("pushButtonSeleccionar"))
        self.gridLayout_2.addWidget(self.pushButtonSeleccionar, 0, 2, 1, 1)
        self.pushButtonCancelar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("DialogSeleccionarUnaSeccion", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setObjectName(_fromUtf8("pushButtonCancelar"))
        self.gridLayout_2.addWidget(self.pushButtonCancelar, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.groupBoxButtonBox, 3, 0, 1, 3)
        #self.tableWidgetSecciones = QtGui.QTableWidget(DialogSeleccionarUnaSeccion)
        self.tableWidgetSecciones = TablaSecciones(DialogSeleccionarUnaSeccion)
        self.tableWidgetSecciones.setObjectName(_fromUtf8("tableWidgetSecciones"))
        self.tableWidgetSecciones.setColumnCount(4)
        self.tableWidgetSecciones.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogSeleccionarUnaSeccion", "Codigo", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetSecciones.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogSeleccionarUnaSeccion", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetSecciones.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogSeleccionarUnaSeccion", "Encargado", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetSecciones.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogSeleccionarUnaSeccion", "Cantidad de empleados", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetSecciones.setHorizontalHeaderItem(3, item)
        self.tableWidgetSecciones.horizontalHeader().setMinimumSectionSize(25)
        self.tableWidgetSecciones.verticalHeader().setDefaultSectionSize(30)
        self.gridLayout.addWidget(self.tableWidgetSecciones, 1, 0, 1, 3)

        self.retranslateUi(DialogSeleccionarUnaSeccion)
        QtCore.QObject.connect(self.pushButtonSeleccionar, QtCore.SIGNAL(_fromUtf8("clicked()")), DialogSeleccionarUnaSeccion.accept)
        QtCore.QObject.connect(self.pushButtonCancelar, QtCore.SIGNAL(_fromUtf8("clicked()")), DialogSeleccionarUnaSeccion.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogSeleccionarUnaSeccion)

    def retranslateUi(self, DialogSeleccionarUnaSeccion):
        item = self.tableWidgetSecciones.horizontalHeaderItem(0)
        item = self.tableWidgetSecciones.horizontalHeaderItem(1)
        item = self.tableWidgetSecciones.horizontalHeaderItem(2)
        item = self.tableWidgetSecciones.horizontalHeaderItem(3)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogSeleccionarUnaSeccion = QtGui.QDialog()
    ui = Ui_DialogSeleccionarUnaSeccion()
    ui.setupUi(DialogSeleccionarUnaSeccion)
    DialogSeleccionarUnaSeccion.show()
    sys.exit(app.exec_())

