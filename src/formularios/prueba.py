# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prueba.ui'
#
# Created: Wed Nov 21 16:16:56 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 60, 711, 481))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox_13 = QtGui.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_13.setTitle(QtGui.QApplication.translate("MainWindow", "Verificacion y Reparacion", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_13.setObjectName(_fromUtf8("groupBox_13"))
        self.horizontalLayoutWidget_6 = QtGui.QWidget(self.groupBox_13)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(10, 20, 611, 71))
        self.horizontalLayoutWidget_6.setObjectName(_fromUtf8("horizontalLayoutWidget_6"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.pushButton_16 = QtGui.QPushButton(self.horizontalLayoutWidget_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy)
        self.pushButton_16.setText(QtGui.QApplication.translate("MainWindow", "Alta Vehiculo", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_16.setObjectName(_fromUtf8("pushButton_16"))
        self.horizontalLayout_6.addWidget(self.pushButton_16)
        self.pushButton_17 = QtGui.QPushButton(self.horizontalLayoutWidget_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy)
        self.pushButton_17.setText(QtGui.QApplication.translate("MainWindow", "Modificar Vehiculo", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_17.setObjectName(_fromUtf8("pushButton_17"))
        self.horizontalLayout_6.addWidget(self.pushButton_17)
        self.pushButton_18 = QtGui.QPushButton(self.horizontalLayoutWidget_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_18.sizePolicy().hasHeightForWidth())
        self.pushButton_18.setSizePolicy(sizePolicy)
        self.pushButton_18.setText(QtGui.QApplication.translate("MainWindow", "Planificar Reparacion \n"
"de Vehiculo", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_18.setObjectName(_fromUtf8("pushButton_18"))
        self.horizontalLayout_6.addWidget(self.pushButton_18)
        spacerItem1 = QtGui.QSpacerItem(38, 58, QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.groupBox_11 = QtGui.QGroupBox(self.groupBox_13)
        self.groupBox_11.setGeometry(QtCore.QRect(10, 100, 631, 101))
        self.groupBox_11.setTitle(QtGui.QApplication.translate("MainWindow", "Seccion", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_11.setObjectName(_fromUtf8("groupBox_11"))
        self.groupBox_10 = QtGui.QGroupBox(self.groupBox_13)
        self.groupBox_10.setGeometry(QtCore.QRect(10, 210, 631, 101))
        self.groupBox_10.setTitle(QtGui.QApplication.translate("MainWindow", "Personal", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_10.setObjectName(_fromUtf8("groupBox_10"))
        self.groupBox_14 = QtGui.QGroupBox(self.groupBox_13)
        self.groupBox_14.setGeometry(QtCore.QRect(10, 310, 631, 101))
        self.groupBox_14.setTitle(QtGui.QApplication.translate("MainWindow", "Repuesto", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_14.setObjectName(_fromUtf8("groupBox_14"))
        self.verticalLayout_2.addWidget(self.groupBox_13)
        self.groupBox_12 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_12.setGeometry(QtCore.QRect(300, 580, 631, 101))
        self.groupBox_12.setTitle(QtGui.QApplication.translate("MainWindow", "Repuesto", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_12.setObjectName(_fromUtf8("groupBox_12"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

