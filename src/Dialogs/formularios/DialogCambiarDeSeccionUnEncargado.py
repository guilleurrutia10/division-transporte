# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogCambiarDeSeccionUnEncargado.ui'
#
# Created: Tue Mar 11 22:56:35 2014
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

#Importante: Si se recompila este formulario, se perderan los retoques hechos "manualmente"
#Se modifico para agregar el icono
from PyQt4 import QtCore, QtGui
from Utiles_formulario import TablaEmpleadosSeccion, TablaSecciones

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogCambiaDeSeccionUnEncargado(object):
    def setupUi(self, DialogCambiaDeSeccionUnEncargado):
        DialogCambiaDeSeccionUnEncargado.setObjectName(_fromUtf8("DialogCambiaDeSeccionUnEncargado"))
        DialogCambiaDeSeccionUnEncargado.resize(979, 625)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/recursos/iconos/personal/cambiar_encargado-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogCambiaDeSeccionUnEncargado.setWindowIcon(icon)
        DialogCambiaDeSeccionUnEncargado.setMinimumSize(QtCore.QSize(979, 625))
        DialogCambiaDeSeccionUnEncargado.setWindowTitle(QtGui.QApplication.translate("DialogCambiaDeSeccionUnEncargado", "Cambia de Seccion un Encargado", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(DialogCambiaDeSeccionUnEncargado)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox_9 = QtGui.QGroupBox(DialogCambiaDeSeccionUnEncargado)
        self.groupBox_9.setTitle(QtGui.QApplication.translate("DialogCambiaDeSeccionUnEncargado", "Empleados", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_9.setObjectName(_fromUtf8("groupBox_9"))
        self.verticalLayoutWidget_5 = QtGui.QWidget(self.groupBox_9)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 20, 461, 511))
        self.verticalLayoutWidget_5.setObjectName(_fromUtf8("verticalLayoutWidget_5"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.groupBox_10 = QtGui.QGroupBox(self.verticalLayoutWidget_5)
        self.groupBox_10.setMinimumSize(QtCore.QSize(331, 41))
        self.groupBox_10.setMaximumSize(QtCore.QSize(331, 41))
        self.groupBox_10.setTitle(QtGui.QApplication.translate("DialogCambiaDeSeccionUnEncargado", "Buscar empleado", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_10.setObjectName(_fromUtf8("groupBox_10"))
        self.pushButton_filtroEmpleado = QtGui.QPushButton(self.groupBox_10)
        self.pushButton_filtroEmpleado.setGeometry(QtCore.QRect(250, 20, 75, 16))
        self.pushButton_filtroEmpleado.setText(QtGui.QApplication.translate("DialogCambiaDeSeccionUnEncargado", "Filtrar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_filtroEmpleado.setObjectName(_fromUtf8("pushButton_filtroEmpleado"))
        self.lineEdit_filtroEmpleado = QtGui.QLineEdit(self.groupBox_10)
        self.lineEdit_filtroEmpleado.setGeometry(QtCore.QRect(10, 20, 231, 16))
        self.lineEdit_filtroEmpleado.setObjectName(_fromUtf8("lineEdit_filtroEmpleado"))
        self.verticalLayout_6.addWidget(self.groupBox_10)
        #self.tableWidget_empleados = QtGui.QTableWidget(self.verticalLayoutWidget_5)
        self.tableWidget_empleados = TablaEmpleadosSeccion(self.verticalLayoutWidget_5)
        self.tableWidget_empleados.setObjectName(_fromUtf8("tableWidget_empleados"))
        self.tableWidget_empleados.setColumnCount(7)
        self.tableWidget_empleados.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogCambiaDeSeccionUnEncargado", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_empleados.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogCambiaDeSeccionUnEncargado", "Apellido", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_empleados.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogCambiaDeSeccionUnEncargado", "Tipo de Documento", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_empleados.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogCambiaDeSeccionUnEncargado", "Nº Documento", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_empleados.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogCambiaDeSeccionUnEncargado", "Fecha de Nac.", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_empleados.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogCambiaDeSeccionUnEncargado", "Email", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_empleados.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogCambiaDeSeccionUnEncargado", "Sección", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_empleados.setHorizontalHeaderItem(6, item)
        self.verticalLayout_6.addWidget(self.tableWidget_empleados)
        self.horizontalLayout_botonera = QtGui.QHBoxLayout()
        self.horizontalLayout_botonera.setObjectName(_fromUtf8("horizontalLayout_botonera"))
        self.pushButton_elegirEmpleado = QtGui.QPushButton(self.verticalLayoutWidget_5)
        self.pushButton_elegirEmpleado.setText(QtGui.QApplication.translate("DialogCambiaDeSeccionUnEncargado", "Elegir empleado", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_elegirEmpleado.setObjectName(_fromUtf8("pushButton_elegirEmpleado"))
        self.horizontalLayout_botonera.addWidget(self.pushButton_elegirEmpleado)
        self.pushButton_removerEmpleado = QtGui.QPushButton(self.verticalLayoutWidget_5)
        self.pushButton_removerEmpleado.setEnabled(False)
        self.pushButton_removerEmpleado.setText(QtGui.QApplication.translate("DialogCambiaDeSeccionUnEncargado", "Remover empleado", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_removerEmpleado.setObjectName(_fromUtf8("pushButton_removerEmpleado"))
        self.horizontalLayout_botonera.addWidget(self.pushButton_removerEmpleado)
        self.verticalLayout_6.addLayout(self.horizontalLayout_botonera)
        self.label = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label.setText(QtGui.QApplication.translate("DialogCambiaDeSeccionUnEncargado", "Empleado seleccionado:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_6.addWidget(self.label)
        #self.tableWidget_empleadoSeleccionado = QtGui.QTableWidget(self.verticalLayoutWidget_5)
        self.tableWidget_empleadoSeleccionado = TablaEmpleadosSeccion(self.verticalLayoutWidget_5)
        self.tableWidget_empleadoSeleccionado.setMaximumSize(QtCore.QSize(16777215, 72))
        self.tableWidget_empleadoSeleccionado.setObjectName(_fromUtf8("tableWidget_empleadoSeleccionado"))
        self.tableWidget_empleadoSeleccionado.setColumnCount(7)
        self.tableWidget_empleadoSeleccionado.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogCambiaDeSeccionUnEncargado", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_empleadoSeleccionado.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogCambiaDeSeccionUnEncargado", "Apellido", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_empleadoSeleccionado.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogCambiaDeSeccionUnEncargado", "Tipo de Documento", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_empleadoSeleccionado.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogCambiaDeSeccionUnEncargado", "Nº Documento", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_empleadoSeleccionado.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogCambiaDeSeccionUnEncargado", "Fecha de Nac.", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_empleadoSeleccionado.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogCambiaDeSeccionUnEncargado", "Email", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_empleadoSeleccionado.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogCambiaDeSeccionUnEncargado", "Sección", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_empleadoSeleccionado.setHorizontalHeaderItem(6, item)
        self.verticalLayout_6.addWidget(self.tableWidget_empleadoSeleccionado)
        self.horizontalLayout.addWidget(self.groupBox_9)
        self.groupBox_11 = QtGui.QGroupBox(DialogCambiaDeSeccionUnEncargado)
        self.groupBox_11.setTitle(QtGui.QApplication.translate("DialogCambiaDeSeccionUnEncargado", "Secciones", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_11.setObjectName(_fromUtf8("groupBox_11"))
        self.verticalLayoutWidget_6 = QtGui.QWidget(self.groupBox_11)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(20, 20, 451, 511))
        self.verticalLayoutWidget_6.setObjectName(_fromUtf8("verticalLayoutWidget_6"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_7.setMargin(0)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.groupBox_12 = QtGui.QGroupBox(self.verticalLayoutWidget_6)
        self.groupBox_12.setMinimumSize(QtCore.QSize(331, 41))
        self.groupBox_12.setMaximumSize(QtCore.QSize(331, 41))
        self.groupBox_12.setTitle(QtGui.QApplication.translate("DialogCambiaDeSeccionUnEncargado", "Buscar seccion", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_12.setObjectName(_fromUtf8("groupBox_12"))
        self.pushButton_filtroSeccion = QtGui.QPushButton(self.groupBox_12)
        self.pushButton_filtroSeccion.setGeometry(QtCore.QRect(250, 20, 75, 16))
        self.pushButton_filtroSeccion.setText(QtGui.QApplication.translate("DialogCambiaDeSeccionUnEncargado", "Filtrar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_filtroSeccion.setObjectName(_fromUtf8("pushButton_filtroSeccion"))
        self.lineEdit_filtroSeccion = QtGui.QLineEdit(self.groupBox_12)
        self.lineEdit_filtroSeccion.setGeometry(QtCore.QRect(10, 20, 231, 16))
        self.lineEdit_filtroSeccion.setObjectName(_fromUtf8("lineEdit_filtroSeccion"))
        self.verticalLayout_7.addWidget(self.groupBox_12)
        self.tableWidget_secciones = TablaSecciones(self.verticalLayoutWidget_6)
        self.tableWidget_secciones.setObjectName(_fromUtf8("tableWidget_secciones"))
        self.tableWidget_secciones.setColumnCount(4)
        self.tableWidget_secciones.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogCambiaDeSeccionUnEncargado", "Codigo", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_secciones.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogCambiaDeSeccionUnEncargado", "Nombre de Seccion", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_secciones.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogCambiaDeSeccionUnEncargado", "Nombre de Encargado", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_secciones.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogCambiaDeSeccionUnEncargado", "Cantidad de empleados", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_secciones.setHorizontalHeaderItem(3, item)
        self.verticalLayout_7.addWidget(self.tableWidget_secciones)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.pushButton_elegirSeccion = QtGui.QPushButton(self.verticalLayoutWidget_6)
        self.pushButton_elegirSeccion.setText(QtGui.QApplication.translate("DialogCambiaDeSeccionUnEncargado", "Elegir seccion", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_elegirSeccion.setObjectName(_fromUtf8("pushButton_elegirSeccion"))
        self.horizontalLayout_9.addWidget(self.pushButton_elegirSeccion)
        self.pushButton_removerSeccion = QtGui.QPushButton(self.verticalLayoutWidget_6)
        self.pushButton_removerSeccion.setEnabled(False)
        self.pushButton_removerSeccion.setText(QtGui.QApplication.translate("DialogCambiaDeSeccionUnEncargado", "Remover seccion", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_removerSeccion.setObjectName(_fromUtf8("pushButton_removerSeccion"))
        self.horizontalLayout_9.addWidget(self.pushButton_removerSeccion)
        self.verticalLayout_7.addLayout(self.horizontalLayout_9)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget_6)
        self.label_2.setText(QtGui.QApplication.translate("DialogCambiaDeSeccionUnEncargado", "Seccion seleccionada:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_7.addWidget(self.label_2)
        self.tableWidget_seccionSeleccionada = TablaSecciones(self.verticalLayoutWidget_6)
        self.tableWidget_seccionSeleccionada.setMaximumSize(QtCore.QSize(16777215, 72))
        self.tableWidget_seccionSeleccionada.setObjectName(_fromUtf8("tableWidget_seccionSeleccionada"))
        self.tableWidget_seccionSeleccionada.setColumnCount(4)
        self.tableWidget_seccionSeleccionada.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogCambiaDeSeccionUnEncargado", "Codigo", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_seccionSeleccionada.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogCambiaDeSeccionUnEncargado", "Nombre de Seccion", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_seccionSeleccionada.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogCambiaDeSeccionUnEncargado", "Nombre del Encargado", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_seccionSeleccionada.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("DialogCambiaDeSeccionUnEncargado", "Cantidad de empleados", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget_seccionSeleccionada.setHorizontalHeaderItem(3, item)
        self.verticalLayout_7.addWidget(self.tableWidget_seccionSeleccionada)
        self.horizontalLayout.addWidget(self.groupBox_11)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.groupBoxButtonBox = QtGui.QGroupBox(DialogCambiaDeSeccionUnEncargado)
        self.groupBoxButtonBox.setMinimumSize(QtCore.QSize(271, 41))
        self.groupBoxButtonBox.setMaximumSize(QtCore.QSize(16777215, 41))
        self.groupBoxButtonBox.setTitle(_fromUtf8(""))
        self.groupBoxButtonBox.setObjectName(_fromUtf8("groupBoxButtonBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBoxButtonBox)
        self.gridLayout_2.setContentsMargins(9, 9, 9, 8)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pushButtonAceptar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonAceptar.setText(QtGui.QApplication.translate("DialogCambiaDeSeccionUnEncargado", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAceptar.setObjectName(_fromUtf8("pushButtonAceptar"))
        self.gridLayout_2.addWidget(self.pushButtonAceptar, 0, 1, 1, 1)
        self.pushButtonCancelar = QtGui.QPushButton(self.groupBoxButtonBox)
        self.pushButtonCancelar.setText(QtGui.QApplication.translate("DialogCambiaDeSeccionUnEncargado", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancelar.setObjectName(_fromUtf8("pushButtonCancelar"))
        self.gridLayout_2.addWidget(self.pushButtonCancelar, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxButtonBox)

        self.retranslateUi(DialogCambiaDeSeccionUnEncargado)
        QtCore.QObject.connect(self.pushButtonAceptar, QtCore.SIGNAL(_fromUtf8("clicked()")), DialogCambiaDeSeccionUnEncargado.accept)
        QtCore.QObject.connect(self.pushButtonCancelar, QtCore.SIGNAL(_fromUtf8("clicked()")), DialogCambiaDeSeccionUnEncargado.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogCambiaDeSeccionUnEncargado)

    def retranslateUi(self, DialogCambiaDeSeccionUnEncargado):
        item = self.tableWidget_empleados.horizontalHeaderItem(0)
        item = self.tableWidget_empleados.horizontalHeaderItem(1)
        item = self.tableWidget_empleados.horizontalHeaderItem(2)
        item = self.tableWidget_empleados.horizontalHeaderItem(3)
        item = self.tableWidget_empleados.horizontalHeaderItem(4)
        item = self.tableWidget_empleados.horizontalHeaderItem(5)
        item = self.tableWidget_empleados.horizontalHeaderItem(6)
        item = self.tableWidget_empleadoSeleccionado.horizontalHeaderItem(0)
        item = self.tableWidget_empleadoSeleccionado.horizontalHeaderItem(1)
        item = self.tableWidget_empleadoSeleccionado.horizontalHeaderItem(2)
        item = self.tableWidget_empleadoSeleccionado.horizontalHeaderItem(3)
        item = self.tableWidget_empleadoSeleccionado.horizontalHeaderItem(4)
        item = self.tableWidget_empleadoSeleccionado.horizontalHeaderItem(5)
        item = self.tableWidget_empleadoSeleccionado.horizontalHeaderItem(6)
        item = self.tableWidget_secciones.horizontalHeaderItem(0)
        item = self.tableWidget_secciones.horizontalHeaderItem(1)
        item = self.tableWidget_secciones.horizontalHeaderItem(2)
        item = self.tableWidget_secciones.horizontalHeaderItem(3)
        item = self.tableWidget_seccionSeleccionada.horizontalHeaderItem(0)
        item = self.tableWidget_seccionSeleccionada.horizontalHeaderItem(1)
        item = self.tableWidget_seccionSeleccionada.horizontalHeaderItem(2)
        item = self.tableWidget_seccionSeleccionada.horizontalHeaderItem(3)

import recursos_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogCambiaDeSeccionUnEncargado = QtGui.QDialog()
    ui = Ui_DialogCambiaDeSeccionUnEncargado()
    ui.setupUi(DialogCambiaDeSeccionUnEncargado)
    DialogCambiaDeSeccionUnEncargado.show()
    sys.exit(app.exec_())

