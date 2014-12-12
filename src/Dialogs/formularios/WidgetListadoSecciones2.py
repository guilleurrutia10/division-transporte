# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WidgetListadoSecciones2.ui'
#
# Created: Fri Dec 12 15:29:01 2014
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
#Guarning se agrego la tabla de secciones
from Utiles_formulario import TablaSecciones
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_FormListadoSecciones(object):
    def setupUi(self, FormListadoSecciones):
        FormListadoSecciones.setObjectName(_fromUtf8("FormListadoSecciones"))
        FormListadoSecciones.resize(467, 305)
        FormListadoSecciones.setWindowTitle(QtGui.QApplication.translate("FormListadoSecciones", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(FormListadoSecciones)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.pushButtonReparacionesPorSeccion = QtGui.QPushButton(FormListadoSecciones)
        self.pushButtonReparacionesPorSeccion.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/recursos/iconos/add_seccion.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonReparacionesPorSeccion.setIcon(icon)
        self.pushButtonReparacionesPorSeccion.setIconSize(QtCore.QSize(30, 30))
        self.pushButtonReparacionesPorSeccion.setObjectName(_fromUtf8("pushButtonReparacionesPorSeccion"))
        self.verticalLayout_3.addWidget(self.pushButtonReparacionesPorSeccion)
        self.label = QtGui.QLabel(FormListadoSecciones)
        self.label.setText(QtGui.QApplication.translate("FormListadoSecciones", "Raparaciones por Sección", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.groupBox = QtGui.QGroupBox(FormListadoSecciones)
        self.groupBox.setTitle(QtGui.QApplication.translate("FormListadoSecciones", "Listado de Secciones", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
#        self.tableWidgetListadoSecciones = QtGui.QTableWidget(self.groupBox)
        self.tableWidgetListadoSecciones = TablaSecciones(self.groupBox)
        self.tableWidgetListadoSecciones.setObjectName(_fromUtf8("tableWidgetListadoSecciones"))
        self.tableWidgetListadoSecciones.setColumnCount(4)
        self.tableWidgetListadoSecciones.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("FormListadoSecciones", "Código Sección", None, QtGui.QApplication.UnicodeUTF8))
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidgetListadoSecciones.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("FormListadoSecciones", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidgetListadoSecciones.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("FormListadoSecciones", "Nombre encargado", None, QtGui.QApplication.UnicodeUTF8))
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidgetListadoSecciones.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("FormListadoSecciones", "Cantidad de empleados", None, QtGui.QApplication.UnicodeUTF8))
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidgetListadoSecciones.setHorizontalHeaderItem(3, item)
        self.tableWidgetListadoSecciones.horizontalHeader().setDefaultSectionSize(180)
        self.tableWidgetListadoSecciones.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.tableWidgetListadoSecciones)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(FormListadoSecciones)
        QtCore.QMetaObject.connectSlotsByName(FormListadoSecciones)

    def retranslateUi(self, FormListadoSecciones):
        item = self.tableWidgetListadoSecciones.horizontalHeaderItem(0)
        item = self.tableWidgetListadoSecciones.horizontalHeaderItem(1)
        item = self.tableWidgetListadoSecciones.horizontalHeaderItem(2)
        item = self.tableWidgetListadoSecciones.horizontalHeaderItem(3)

import recursos_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FormListadoSecciones = QtGui.QWidget()
    ui = Ui_FormListadoSecciones()
    ui.setupUi(FormListadoSecciones)
    FormListadoSecciones.show()
    sys.exit(app.exec_())

