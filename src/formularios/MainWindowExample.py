# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowExample.ui'
#
# Created: Wed Nov 14 18:14:43 2012
#      by: PyQt4 UI code generator 4.9.5
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
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        MainWindow.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks|QtGui.QMainWindow.AnimatedDocks)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuArchivo = QtGui.QMenu(self.menubar)
        self.menuArchivo.setObjectName(_fromUtf8("menuArchivo"))
        self.menuVerificacion_y_Reparacion = QtGui.QMenu(self.menubar)
        self.menuVerificacion_y_Reparacion.setObjectName(_fromUtf8("menuVerificacion_y_Reparacion"))
        self.menuListados_de_Vehiculos = QtGui.QMenu(self.menuVerificacion_y_Reparacion)
        self.menuListados_de_Vehiculos.setObjectName(_fromUtf8("menuListados_de_Vehiculos"))
        self.menuPersonal = QtGui.QMenu(self.menubar)
        self.menuPersonal.setObjectName(_fromUtf8("menuPersonal"))
        self.menuListados_Personal = QtGui.QMenu(self.menuPersonal)
        self.menuListados_Personal.setObjectName(_fromUtf8("menuListados_Personal"))
        self.menuRepuestos = QtGui.QMenu(self.menubar)
        self.menuRepuestos.setObjectName(_fromUtf8("menuRepuestos"))
        self.menuListados_de_Repuestos = QtGui.QMenu(self.menuRepuestos)
        self.menuListados_de_Repuestos.setObjectName(_fromUtf8("menuListados_de_Repuestos"))
        self.menuSecciones = QtGui.QMenu(self.menubar)
        self.menuSecciones.setObjectName(_fromUtf8("menuSecciones"))
        self.menuConfiguracion = QtGui.QMenu(self.menubar)
        self.menuConfiguracion.setObjectName(_fromUtf8("menuConfiguracion"))
        self.menuAyuda = QtGui.QMenu(self.menubar)
        self.menuAyuda.setObjectName(_fromUtf8("menuAyuda"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionSalir = QtGui.QAction(MainWindow)
        self.actionSalir.setObjectName(_fromUtf8("actionSalir"))
        self.actionListado = QtGui.QAction(MainWindow)
        self.actionListado.setObjectName(_fromUtf8("actionListado"))
        self.actionSobre = QtGui.QAction(MainWindow)
        self.actionSobre.setObjectName(_fromUtf8("actionSobre"))
        self.actionAyuda = QtGui.QAction(MainWindow)
        self.actionAyuda.setCheckable(True)
        self.actionAyuda.setObjectName(_fromUtf8("actionAyuda"))
        self.actionAlta_de_Vehiculo = QtGui.QAction(MainWindow)
        self.actionAlta_de_Vehiculo.setObjectName(_fromUtf8("actionAlta_de_Vehiculo"))
        self.actionModificacion_de_Vehiculo = QtGui.QAction(MainWindow)
        self.actionModificacion_de_Vehiculo.setObjectName(_fromUtf8("actionModificacion_de_Vehiculo"))
        self.actionRegistrar_Ingreso_de_Vehiculo = QtGui.QAction(MainWindow)
        self.actionRegistrar_Ingreso_de_Vehiculo.setObjectName(_fromUtf8("actionRegistrar_Ingreso_de_Vehiculo"))
        self.actionVerificar_Reparaciones_Necesarias_del_Vehiculo = QtGui.QAction(MainWindow)
        self.actionVerificar_Reparaciones_Necesarias_del_Vehiculo.setObjectName(_fromUtf8("actionVerificar_Reparaciones_Necesarias_del_Vehiculo"))
        self.actionRegistrar_Egreso = QtGui.QAction(MainWindow)
        self.actionRegistrar_Egreso.setObjectName(_fromUtf8("actionRegistrar_Egreso"))
        self.actionPlanificar_Reparaciones_de_Vehiculo = QtGui.QAction(MainWindow)
        self.actionPlanificar_Reparaciones_de_Vehiculo.setObjectName(_fromUtf8("actionPlanificar_Reparaciones_de_Vehiculo"))
        self.actionListado_Vehiculos_en_reparacion_por_Seccion = QtGui.QAction(MainWindow)
        self.actionListado_Vehiculos_en_reparacion_por_Seccion.setObjectName(_fromUtf8("actionListado_Vehiculos_en_reparacion_por_Seccion"))
        self.actionListado_Vehiculos_con_Reparaciones_Planificadas = QtGui.QAction(MainWindow)
        self.actionListado_Vehiculos_con_Reparaciones_Planificadas.setObjectName(_fromUtf8("actionListado_Vehiculos_con_Reparaciones_Planificadas"))
        self.actionListado_Vehiculos_Reparados_por_Seccion = QtGui.QAction(MainWindow)
        self.actionListado_Vehiculos_Reparados_por_Seccion.setObjectName(_fromUtf8("actionListado_Vehiculos_Reparados_por_Seccion"))
        self.actionListado_de_Reparaciones_Realizadas_a_un_Vehiculos = QtGui.QAction(MainWindow)
        self.actionListado_de_Reparaciones_Realizadas_a_un_Vehiculos.setObjectName(_fromUtf8("actionListado_de_Reparaciones_Realizadas_a_un_Vehiculos"))
        self.actionListado_Vehiculos_con_Reparaciones_no_Planificadas = QtGui.QAction(MainWindow)
        self.actionListado_Vehiculos_con_Reparaciones_no_Planificadas.setObjectName(_fromUtf8("actionListado_Vehiculos_con_Reparaciones_no_Planificadas"))
        self.actionListado_Vehiculos_de_la_Division_2 = QtGui.QAction(MainWindow)
        self.actionListado_Vehiculos_de_la_Division_2.setObjectName(_fromUtf8("actionListado_Vehiculos_de_la_Division_2"))
        self.actionListado_Vehiculos_con_Reparaciones_Planificadas_2 = QtGui.QAction(MainWindow)
        self.actionListado_Vehiculos_con_Reparaciones_Planificadas_2.setObjectName(_fromUtf8("actionListado_Vehiculos_con_Reparaciones_Planificadas_2"))
        self.actionListado_Vehiculos_en_Reparacion_por_Seccion = QtGui.QAction(MainWindow)
        self.actionListado_Vehiculos_en_Reparacion_por_Seccion.setObjectName(_fromUtf8("actionListado_Vehiculos_en_Reparacion_por_Seccion"))
        self.actionListado_Vehiculos_Reparados_por_Seccion_2 = QtGui.QAction(MainWindow)
        self.actionListado_Vehiculos_Reparados_por_Seccion_2.setObjectName(_fromUtf8("actionListado_Vehiculos_Reparados_por_Seccion_2"))
        self.actionListado_de_Reparaciones_Realizadas_a_un_Vehiculos_2 = QtGui.QAction(MainWindow)
        self.actionListado_de_Reparaciones_Realizadas_a_un_Vehiculos_2.setObjectName(_fromUtf8("actionListado_de_Reparaciones_Realizadas_a_un_Vehiculos_2"))
        self.actionListado_Vehiculos_con_Reparaciones_no_Planificadas_2 = QtGui.QAction(MainWindow)
        self.actionListado_Vehiculos_con_Reparaciones_no_Planificadas_2.setObjectName(_fromUtf8("actionListado_Vehiculos_con_Reparaciones_no_Planificadas_2"))
        self.actionAlta_de_Personal = QtGui.QAction(MainWindow)
        self.actionAlta_de_Personal.setObjectName(_fromUtf8("actionAlta_de_Personal"))
        self.actionBaja_de_Personal = QtGui.QAction(MainWindow)
        self.actionBaja_de_Personal.setObjectName(_fromUtf8("actionBaja_de_Personal"))
        self.actionModificacion_de_Personal = QtGui.QAction(MainWindow)
        self.actionModificacion_de_Personal.setObjectName(_fromUtf8("actionModificacion_de_Personal"))
        self.actionCambiar_de_Seccion_a_un_Empleado = QtGui.QAction(MainWindow)
        self.actionCambiar_de_Seccion_a_un_Empleado.setObjectName(_fromUtf8("actionCambiar_de_Seccion_a_un_Empleado"))
        self.actionCambiar_el_Encargado_de_una_Seccion = QtGui.QAction(MainWindow)
        self.actionCambiar_el_Encargado_de_una_Seccion.setObjectName(_fromUtf8("actionCambiar_el_Encargado_de_una_Seccion"))
        self.actionRemover_Empleado_de_Seccion = QtGui.QAction(MainWindow)
        self.actionRemover_Empleado_de_Seccion.setObjectName(_fromUtf8("actionRemover_Empleado_de_Seccion"))
        self.actionListado_de_Personal_de_la_Division = QtGui.QAction(MainWindow)
        self.actionListado_de_Personal_de_la_Division.setObjectName(_fromUtf8("actionListado_de_Personal_de_la_Division"))
        self.actionListado_de_Personal_sin_Asignar_a_Secciones = QtGui.QAction(MainWindow)
        self.actionListado_de_Personal_sin_Asignar_a_Secciones.setObjectName(_fromUtf8("actionListado_de_Personal_sin_Asignar_a_Secciones"))
        self.actionAlta_de_Repuesto = QtGui.QAction(MainWindow)
        self.actionAlta_de_Repuesto.setObjectName(_fromUtf8("actionAlta_de_Repuesto"))
        self.actionModificacion_de_Repuesto = QtGui.QAction(MainWindow)
        self.actionModificacion_de_Repuesto.setObjectName(_fromUtf8("actionModificacion_de_Repuesto"))
        self.actionRegistrar_Recepcion_de_Pedido_de_Actuacion = QtGui.QAction(MainWindow)
        self.actionRegistrar_Recepcion_de_Pedido_de_Actuacion.setObjectName(_fromUtf8("actionRegistrar_Recepcion_de_Pedido_de_Actuacion"))
        self.actionListado_de_Repuestos_de_la_Division = QtGui.QAction(MainWindow)
        self.actionListado_de_Repuestos_de_la_Division.setObjectName(_fromUtf8("actionListado_de_Repuestos_de_la_Division"))
        self.actionAlta_de_Seccion = QtGui.QAction(MainWindow)
        self.actionAlta_de_Seccion.setObjectName(_fromUtf8("actionAlta_de_Seccion"))
        self.actionAsignar_Reparacion = QtGui.QAction(MainWindow)
        self.actionAsignar_Reparacion.setObjectName(_fromUtf8("actionAsignar_Reparacion"))
        self.actionRegistrar_Finalizacion_de_Reparacion = QtGui.QAction(MainWindow)
        self.actionRegistrar_Finalizacion_de_Reparacion.setObjectName(_fromUtf8("actionRegistrar_Finalizacion_de_Reparacion"))
        self.actionListados_de_Seccion = QtGui.QAction(MainWindow)
        self.actionListados_de_Seccion.setObjectName(_fromUtf8("actionListados_de_Seccion"))
        self.actionListado_de_Tipos_de_Reparaciones_de_la_Division = QtGui.QAction(MainWindow)
        self.actionListado_de_Tipos_de_Reparaciones_de_la_Division.setObjectName(_fromUtf8("actionListado_de_Tipos_de_Reparaciones_de_la_Division"))
        self.actionListado_de_Tipos_de_Reparaciones_de_la_Division_2 = QtGui.QAction(MainWindow)
        self.actionListado_de_Tipos_de_Reparaciones_de_la_Division_2.setObjectName(_fromUtf8("actionListado_de_Tipos_de_Reparaciones_de_la_Division_2"))
        self.actionAcerca_de_Division_de_Transporte = QtGui.QAction(MainWindow)
        self.actionAcerca_de_Division_de_Transporte.setObjectName(_fromUtf8("actionAcerca_de_Division_de_Transporte"))
        self.actionPreferencias = QtGui.QAction(MainWindow)
        self.actionPreferencias.setObjectName(_fromUtf8("actionPreferencias"))
        self.menuArchivo.addAction(self.actionSobre)
        self.menuArchivo.addAction(self.actionListado)
        self.menuArchivo.addAction(self.actionAyuda)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionSalir)
        self.menuListados_de_Vehiculos.addAction(self.actionListado_Vehiculos_de_la_Division_2)
        self.menuListados_de_Vehiculos.addAction(self.actionListado_de_Reparaciones_Realizadas_a_un_Vehiculos_2)
        self.menuListados_de_Vehiculos.addSeparator()
        self.menuListados_de_Vehiculos.addAction(self.actionListado_Vehiculos_con_Reparaciones_Planificadas_2)
        self.menuListados_de_Vehiculos.addAction(self.actionListado_Vehiculos_con_Reparaciones_no_Planificadas_2)
        self.menuListados_de_Vehiculos.addSeparator()
        self.menuListados_de_Vehiculos.addAction(self.actionListado_Vehiculos_en_Reparacion_por_Seccion)
        self.menuListados_de_Vehiculos.addAction(self.actionListado_Vehiculos_Reparados_por_Seccion_2)
        self.menuVerificacion_y_Reparacion.addAction(self.actionAlta_de_Vehiculo)
        self.menuVerificacion_y_Reparacion.addAction(self.actionRegistrar_Ingreso_de_Vehiculo)
        self.menuVerificacion_y_Reparacion.addAction(self.actionRegistrar_Egreso)
        self.menuVerificacion_y_Reparacion.addAction(self.actionModificacion_de_Vehiculo)
        self.menuVerificacion_y_Reparacion.addSeparator()
        self.menuVerificacion_y_Reparacion.addAction(self.actionVerificar_Reparaciones_Necesarias_del_Vehiculo)
        self.menuVerificacion_y_Reparacion.addAction(self.actionPlanificar_Reparaciones_de_Vehiculo)
        self.menuVerificacion_y_Reparacion.addSeparator()
        self.menuVerificacion_y_Reparacion.addAction(self.menuListados_de_Vehiculos.menuAction())
        self.menuVerificacion_y_Reparacion.addAction(self.actionListado_de_Tipos_de_Reparaciones_de_la_Division_2)
        self.menuListados_Personal.addAction(self.actionListado_de_Personal_de_la_Division)
        self.menuPersonal.addAction(self.actionAlta_de_Personal)
        self.menuPersonal.addAction(self.actionBaja_de_Personal)
        self.menuPersonal.addAction(self.actionModificacion_de_Personal)
        self.menuPersonal.addSeparator()
        self.menuPersonal.addAction(self.actionCambiar_de_Seccion_a_un_Empleado)
        self.menuPersonal.addAction(self.actionCambiar_el_Encargado_de_una_Seccion)
        self.menuPersonal.addAction(self.actionRemover_Empleado_de_Seccion)
        self.menuPersonal.addSeparator()
        self.menuPersonal.addAction(self.menuListados_Personal.menuAction())
        self.menuListados_de_Repuestos.addAction(self.actionListado_de_Repuestos_de_la_Division)
        self.menuRepuestos.addAction(self.actionAlta_de_Repuesto)
        self.menuRepuestos.addAction(self.actionModificacion_de_Repuesto)
        self.menuRepuestos.addSeparator()
        self.menuRepuestos.addAction(self.actionRegistrar_Recepcion_de_Pedido_de_Actuacion)
        self.menuRepuestos.addSeparator()
        self.menuRepuestos.addAction(self.menuListados_de_Repuestos.menuAction())
        self.menuSecciones.addAction(self.actionAlta_de_Seccion)
        self.menuSecciones.addSeparator()
        self.menuSecciones.addAction(self.actionAsignar_Reparacion)
        self.menuSecciones.addAction(self.actionRegistrar_Finalizacion_de_Reparacion)
        self.menuSecciones.addSeparator()
        self.menuSecciones.addAction(self.actionListados_de_Seccion)
        self.menuConfiguracion.addAction(self.actionPreferencias)
        self.menuAyuda.addAction(self.actionAcerca_de_Division_de_Transporte)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuVerificacion_y_Reparacion.menuAction())
        self.menubar.addAction(self.menuPersonal.menuAction())
        self.menubar.addAction(self.menuRepuestos.menuAction())
        self.menubar.addAction(self.menuSecciones.menuAction())
        self.menubar.addAction(self.menuConfiguracion.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionSalir, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Division Transporte", None, QtGui.QApplication.UnicodeUTF8))
        self.menuArchivo.setTitle(QtGui.QApplication.translate("MainWindow", "Archivo", None, QtGui.QApplication.UnicodeUTF8))
        self.menuVerificacion_y_Reparacion.setTitle(QtGui.QApplication.translate("MainWindow", "Verificacion y Reparacion", None, QtGui.QApplication.UnicodeUTF8))
        self.menuListados_de_Vehiculos.setTitle(QtGui.QApplication.translate("MainWindow", "Listados de Vehiculos", None, QtGui.QApplication.UnicodeUTF8))
        self.menuPersonal.setTitle(QtGui.QApplication.translate("MainWindow", "Personal", None, QtGui.QApplication.UnicodeUTF8))
        self.menuListados_Personal.setTitle(QtGui.QApplication.translate("MainWindow", "Listados Personal", None, QtGui.QApplication.UnicodeUTF8))
        self.menuRepuestos.setTitle(QtGui.QApplication.translate("MainWindow", "Repuestos", None, QtGui.QApplication.UnicodeUTF8))
        self.menuListados_de_Repuestos.setTitle(QtGui.QApplication.translate("MainWindow", "Listados de Repuestos", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSecciones.setTitle(QtGui.QApplication.translate("MainWindow", "Secciones", None, QtGui.QApplication.UnicodeUTF8))
        self.menuConfiguracion.setTitle(QtGui.QApplication.translate("MainWindow", "Configuracion", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAyuda.setTitle(QtGui.QApplication.translate("MainWindow", "Ayuda", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalir.setText(QtGui.QApplication.translate("MainWindow", "Salir", None, QtGui.QApplication.UnicodeUTF8))
        self.actionListado.setText(QtGui.QApplication.translate("MainWindow", "Listado", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSobre.setText(QtGui.QApplication.translate("MainWindow", "Sobre", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAyuda.setText(QtGui.QApplication.translate("MainWindow", "Ayuda", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAlta_de_Vehiculo.setText(QtGui.QApplication.translate("MainWindow", "Alta de Vehiculo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionModificacion_de_Vehiculo.setText(QtGui.QApplication.translate("MainWindow", "Modificacion de Vehiculo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRegistrar_Ingreso_de_Vehiculo.setText(QtGui.QApplication.translate("MainWindow", "Registrar Ingreso de Vehiculo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionVerificar_Reparaciones_Necesarias_del_Vehiculo.setText(QtGui.QApplication.translate("MainWindow", "Registrar Reparaciones necesarias del Vehiculo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRegistrar_Egreso.setText(QtGui.QApplication.translate("MainWindow", "Registrar Egreso Vehiculo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPlanificar_Reparaciones_de_Vehiculo.setText(QtGui.QApplication.translate("MainWindow", "Planificar Reparaciones de Vehiculo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionListado_Vehiculos_en_reparacion_por_Seccion.setText(QtGui.QApplication.translate("MainWindow", "Listado Vehiculos en Reparacion por Seccion", None, QtGui.QApplication.UnicodeUTF8))
        self.actionListado_Vehiculos_con_Reparaciones_Planificadas.setText(QtGui.QApplication.translate("MainWindow", "Listado Vehiculos con Reparaciones Planificadas", None, QtGui.QApplication.UnicodeUTF8))
        self.actionListado_Vehiculos_Reparados_por_Seccion.setText(QtGui.QApplication.translate("MainWindow", "Listado Vehiculos Reparados por Seccion", None, QtGui.QApplication.UnicodeUTF8))
        self.actionListado_de_Reparaciones_Realizadas_a_un_Vehiculos.setText(QtGui.QApplication.translate("MainWindow", "Listado de Reparaciones Realizadas a un Vehiculos", None, QtGui.QApplication.UnicodeUTF8))
        self.actionListado_Vehiculos_con_Reparaciones_no_Planificadas.setText(QtGui.QApplication.translate("MainWindow", "Listado Vehiculos con Reparaciones no Planificadas", None, QtGui.QApplication.UnicodeUTF8))
        self.actionListado_Vehiculos_de_la_Division_2.setText(QtGui.QApplication.translate("MainWindow", "Listado Vehiculos de la Division", None, QtGui.QApplication.UnicodeUTF8))
        self.actionListado_Vehiculos_con_Reparaciones_Planificadas_2.setText(QtGui.QApplication.translate("MainWindow", "Listado Vehiculos con Reparaciones Planificadas", None, QtGui.QApplication.UnicodeUTF8))
        self.actionListado_Vehiculos_en_Reparacion_por_Seccion.setText(QtGui.QApplication.translate("MainWindow", "Listado Vehiculos en Reparacion por Seccion", None, QtGui.QApplication.UnicodeUTF8))
        self.actionListado_Vehiculos_Reparados_por_Seccion_2.setText(QtGui.QApplication.translate("MainWindow", "Listado Vehiculos Reparados por Seccion", None, QtGui.QApplication.UnicodeUTF8))
        self.actionListado_de_Reparaciones_Realizadas_a_un_Vehiculos_2.setText(QtGui.QApplication.translate("MainWindow", "Listado de Reparaciones Realizadas a un Vehiculos", None, QtGui.QApplication.UnicodeUTF8))
        self.actionListado_Vehiculos_con_Reparaciones_no_Planificadas_2.setText(QtGui.QApplication.translate("MainWindow", "Listado Vehiculos con Reparaciones no Planificadas", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAlta_de_Personal.setText(QtGui.QApplication.translate("MainWindow", "Alta de Personal", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBaja_de_Personal.setText(QtGui.QApplication.translate("MainWindow", "Baja de Personal", None, QtGui.QApplication.UnicodeUTF8))
        self.actionModificacion_de_Personal.setText(QtGui.QApplication.translate("MainWindow", "Modificacion de Personal", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCambiar_de_Seccion_a_un_Empleado.setText(QtGui.QApplication.translate("MainWindow", "Cambiar de Seccion a un Empleado", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCambiar_el_Encargado_de_una_Seccion.setText(QtGui.QApplication.translate("MainWindow", "Cambiar el Encargado de una Seccion", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemover_Empleado_de_Seccion.setText(QtGui.QApplication.translate("MainWindow", "Remover Empleado de Seccion", None, QtGui.QApplication.UnicodeUTF8))
        self.actionListado_de_Personal_de_la_Division.setText(QtGui.QApplication.translate("MainWindow", "Listado de Personal de la Division", None, QtGui.QApplication.UnicodeUTF8))
        self.actionListado_de_Personal_sin_Asignar_a_Secciones.setText(QtGui.QApplication.translate("MainWindow", "Listado de Empleados por Seccion", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAlta_de_Repuesto.setText(QtGui.QApplication.translate("MainWindow", "Alta de Repuesto", None, QtGui.QApplication.UnicodeUTF8))
        self.actionModificacion_de_Repuesto.setText(QtGui.QApplication.translate("MainWindow", "Modificacion de Repuesto", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRegistrar_Recepcion_de_Pedido_de_Actuacion.setText(QtGui.QApplication.translate("MainWindow", "Registrar Recepcion de Pedido de Actuacion", None, QtGui.QApplication.UnicodeUTF8))
        self.actionListado_de_Repuestos_de_la_Division.setText(QtGui.QApplication.translate("MainWindow", "Listado de Repuestos Solicitados", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAlta_de_Seccion.setText(QtGui.QApplication.translate("MainWindow", "Alta de Seccion", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAsignar_Reparacion.setText(QtGui.QApplication.translate("MainWindow", "Asignar Reparacion", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRegistrar_Finalizacion_de_Reparacion.setText(QtGui.QApplication.translate("MainWindow", "Registrar Finalizacion de Reparacion", None, QtGui.QApplication.UnicodeUTF8))
        self.actionListados_de_Seccion.setText(QtGui.QApplication.translate("MainWindow", "Listados de Seccion", None, QtGui.QApplication.UnicodeUTF8))
        self.actionListado_de_Tipos_de_Reparaciones_de_la_Division.setText(QtGui.QApplication.translate("MainWindow", "Listado de Tipos de Reparaciones de la Division", None, QtGui.QApplication.UnicodeUTF8))
        self.actionListado_de_Tipos_de_Reparaciones_de_la_Division_2.setText(QtGui.QApplication.translate("MainWindow", "Listado de Tipos de Reparaciones de la Division", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAcerca_de_Division_de_Transporte.setText(QtGui.QApplication.translate("MainWindow", "Acerca de \"Division de Transporte\"", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferencias.setText(QtGui.QApplication.translate("MainWindow", "Preferencias", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

