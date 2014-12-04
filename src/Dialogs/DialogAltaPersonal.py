# -*- coding: utf-8 -*-
'''
Created on 03/10/2012

@author: Usuario
'''
from PyQt4 import QtCore, QtGui
from re import match

from formularios.DialogAltaPersonal import Ui_DialogAltaPersonal
from AyudaManejador import AyudaManejador
from negocio.Division_Transporte import Division_Transporte

from negocio.excepciones.ExcepcionObjetoExiste import ExcepcionObjetoExiste


class DialogAltaPersonal(QtGui.QDialog, Ui_DialogAltaPersonal, AyudaManejador):
    '''
    Atributos:
        - self.lineEditNombre
        - self.lineEditApellido
        - self.lineEditNroDocumento
        - self.comboBoxTipoDocumento
        - self.dateEditFechaNacimiento
        - self.lineEditDomicilio
        - self.lineEditTelefono
        - self.lineEditEmail
    '''
    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super(DialogAltaPersonal, self).__init__(parent)
        self.setupUi(self)
        self.validacionesLineEdit()
        self.llenarComboBoxTipoDocumentos()

        # seteo de nombres de los Labels para el estilo
        self.label.setObjectName("label")
        self.label_2.setObjectName("label")
        self.label_3.setObjectName("label")
        self.label_4.setObjectName("label")
        self.label_5.setObjectName("label")
        self.label_6.setObjectName("label")
        self.label_7.setObjectName("label")
        self.label_8.setObjectName("label")

        print self.parent().usuario.name

    def validacionesLineEdit(self):
        '''
        Se establecen las validaciones que se realizarán a medida que
        se llenan los campos.
        '''
        # TODO: Establecer modulo con las expresiones regulares a utilizar.
        # Validación a medida que se escribe en el lineEdit
        nombreRegExp = QtCore.QRegExp('[A-Za-z|\s]+')
        validadorRegExp = QtGui.QRegExpValidator(nombreRegExp, self)
        self.lineEditNombre.setValidator(validadorRegExp)
        numDocumentoRegExp = QtCore.QRegExp('[0-9]+')
        validadorRegExp = QtGui.QRegExpValidator(numDocumentoRegExp, self)
        self.lineEditNroDocumento.setValidator(validadorRegExp)
        domicilioRegExp = QtCore.QRegExp('[A-Za-z\s]+[0-9]+')
        validadorRegExp = QtGui.QRegExpValidator(domicilioRegExp, self)
        self.lineEditDomicilio.setValidator(validadorRegExp)
        telefonoRegExp = QtCore.QRegExp('[0-9]+')
        validadorRegExp = QtGui.QRegExpValidator(telefonoRegExp, self)
        self.lineEditTelefono.setValidator(validadorRegExp)
        mailRegExp = QtCore.QRegExp('^[_a-z0-9-]+(.[_a-z0-9-]+)*@[a-z0-9-]+(.[a-z0-9-]+)*(.[a-z]{2,3})$')
        validadorRegExp = QtGui.QRegExpValidator(mailRegExp, self)
        self.lineEditEmail.setValidator(validadorRegExp)

    def llenarComboBoxTipoDocumentos(self):
        '''
        Obtiene los tipos de documentos de la base de datos
        y llena un comboBox para listarlos.
        '''
        dvTrans = Division_Transporte()
        for i in dvTrans.getTipoDeDocumentos():
            item = QtCore.QStringList(i)
            self.comboBoxTipoDocumento.addItems(item)

    @QtCore.pyqtSlot()
    def on_pushButtonCancelar_clicked(self):
        '''
        '''
        self.reject()

    @QtCore.pyqtSlot()
    def on_pushButtonAceptar_clicked(self):
        '''
        '''
        if not self.testearDialogo():
            return
        self.cargarPersonal()
        if self.mostrarMensaje('El Empleado se ha cargado exitosamente!! :)', 'Cargando Empleado'):
            self.accept()

    '''
    TODO: Se ha repetido este mismo método en varias de las clsase Dialogos.
    '''
    def mostrarMensaje(self, mensaje, titulo):
        '''
        Función que muestra un pequeña ventana con información relevante.
        '''
        msgBox = QtGui.QMessageBox(self)
        msgBox.setText(QtCore.QString.fromUtf8(mensaje))
        msgBox.setWindowTitle(QtCore.QString.fromUtf8(titulo))
        return msgBox.exec_()

    def testearDialogo(self):
        '''
        Función que se encarga de comprobar que los campos obligatorios se
        completaron correctamente.
        '''
        if not match('[A-Za-z|\s]', self.lineEditNombre.text()):
            self.mostrarMensaje('Debe ingresar el nombre.', 'Ingreso')
            self.lineEditNombre.clear()
            self.lineEditNombre.setFocus()
            return
        if not match('[a-z|A-Z]+', self.lineEditApellido.text()):
            self.mostrarMensaje('Debe ingresar el apellido', 'Ingreso')
            self.lineEditApellido.clear()
            self.lineEditApellido.setFocus()
            return
        if not match('[0-9]+', self.lineEditNroDocumento.text()):
            self.mostrarMensaje('Debe ingresar el número de Documento.', 'Ingreso')
            self.lineEditNroDocumento.clear()
            self.lineEditNroDocumento.setFocus()
            return
        # Si ingresó un mail, lo validamos, sino no nos ocupamos de validar...
        if self.lineEditEmail.text() and not match('^[_a-z0-9-]+(.[_a-z0-9-]+)*@[a-z0-9-]+(.[a-z0-9-]+)*(.[a-z]{2,3})$', self.lineEditEmail.text()):
            self.mostrarMensaje('Debe ingresar un mail válido. Ejemplo: "pepe@pepe.com"', 'Ingreso')
            self.lineEditEmail.clear()
            self.lineEditEmail.setFocus()
            return
        return True

    def cargarPersonal(self):
        nombre = unicode(self.lineEditNombre.text())
        apellido = unicode(self.lineEditApellido.text())
        nroDocumento = unicode(self.lineEditNroDocumento.text())
        tipoDocumento = unicode(self.comboBoxTipoDocumento.currentText())

        fechaNac = self.dateEditFechaNacimiento.date().toPyDate()
        domicilio = unicode(self.lineEditDomicilio.text())
        telefono = unicode(self.lineEditTelefono.text())
        email = unicode(self.lineEditEmail.text())
        division = Division_Transporte()
        try:
            # Se carga el empleado en el sistema.
            division.agregarEmpleado(nombre, apellido, nroDocumento, tipoDocumento,
                                     fechaNac, domicilio, telefono, email)
        except ExcepcionObjetoExiste:
            mensaje = u'El Empleado con Tipo de Documento %s y número %s ya se encuentra cargado.' % (tipoDocumento, nroDocumento)
            self.mostrarMensaje(mensaje, 'Alta Personal')
