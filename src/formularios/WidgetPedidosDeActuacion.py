# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WidgetPedidosDeActuacion.ui'
#
# Created: Sun Nov 18 20:38:09 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_FormPedidoDeActuacion(object):
    def setupUi(self, FormPedidoDeActuacion):
        FormPedidoDeActuacion.setObjectName(_fromUtf8("FormPedidoDeActuacion"))
        FormPedidoDeActuacion.resize(752, 593)
        FormPedidoDeActuacion.setWindowTitle(QtGui.QApplication.translate("FormPedidoDeActuacion", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(FormPedidoDeActuacion)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tableWidget = QtGui.QTableWidget(FormPedidoDeActuacion)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("FormPedidoDeActuacion", "Número Pedido de Actuación", None, QtGui.QApplication.UnicodeUTF8))
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("FormPedidoDeActuacion", "Fecha de Realización", None, QtGui.QApplication.UnicodeUTF8))
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.verticalLayout.addWidget(self.tableWidget)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setRowWrapPolicy(QtGui.QFormLayout.WrapLongRows)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.pushButton_Registrar = QtGui.QPushButton(FormPedidoDeActuacion)
        self.pushButton_Registrar.setText(QtGui.QApplication.translate("FormPedidoDeActuacion", "Registrar Fecha de Recepción", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Registrar.setObjectName(_fromUtf8("pushButton_Registrar"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.pushButton_Registrar)
        self.pushButton_2_Cancelar = QtGui.QPushButton(FormPedidoDeActuacion)
        self.pushButton_2_Cancelar.setEnabled(True)
        self.pushButton_2_Cancelar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_2_Cancelar.setAutoFillBackground(False)
        self.pushButton_2_Cancelar.setText(QtGui.QApplication.translate("FormPedidoDeActuacion", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2_Cancelar.setObjectName(_fromUtf8("pushButton_2_Cancelar"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.pushButton_2_Cancelar)
        self.verticalLayout.addLayout(self.formLayout)

        self.retranslateUi(FormPedidoDeActuacion)
        QtCore.QObject.connect(self.pushButton_Registrar, QtCore.SIGNAL(_fromUtf8("pressed()")), FormPedidoDeActuacion.update)
        QtCore.QObject.connect(self.pushButton_2_Cancelar, QtCore.SIGNAL(_fromUtf8("pressed()")), FormPedidoDeActuacion.close)
        QtCore.QMetaObject.connectSlotsByName(FormPedidoDeActuacion)

    def retranslateUi(self, FormPedidoDeActuacion):
        item = self.tableWidget.horizontalHeaderItem(0)
        item = self.tableWidget.horizontalHeaderItem(1)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FormPedidoDeActuacion = QtGui.QWidget()
    ui = Ui_FormPedidoDeActuacion()
    ui.setupUi(FormPedidoDeActuacion)
    FormPedidoDeActuacion.show()
    sys.exit(app.exec_())

