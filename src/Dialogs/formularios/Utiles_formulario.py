'''
Created on 28/01/2014

@author: Usuario

QtGui.QTableWidget
|
|_SuperTabla
    |
    |_TablaEmpleadosSeccion
    |
    |_TablaSecciones
    |
    |_TablaVehiculos **new**
'''
from PyQt4 import QtGui, QtCore


class SuperTabla(QtGui.QTableWidget):

    '''
    TODO: Seria bueno implementar TemplateMethod
    '''

    def inicializarTabla(self):
        '''
        - Conecta las senales de seleccion de celda con el metodo que refresca la variable de filaSelecionada
        - Inicializa la filaseleccionada
        - Inicializa el diccionario de elementos.
        TODO: Chequear si es necesario conectarlo con las tres signals...
        '''
        self.connect(self, QtCore.SIGNAL('cellClicked(int,int)'), self.setearFilaSeleccionada)
        self.connect(self, QtCore.SIGNAL('cellEntered(int,int)'), self.setearFilaSeleccionada)
        self.connect(self, QtCore.SIGNAL('cellPressed(int,int)'), self.setearFilaSeleccionada)
        self.filaSeleccionada = None
        #Un diccionario de objetos para llevar una correlacion objeto_listado-Fila_en_la_que_se_encuentra
        self.diccionarioFilaElemento = {}
        
    def setearFilaSeleccionada(self, fila, columna):
        '''
        Setea la fila que esta siendo apuntada actualmente. 
        '''
        self.filaSeleccionada = fila
        #print 'Presionando: %d ; %d \n La fila quedo en: %d' %(fila, columna, self.filaSeleccionada)
        
    def getFilaSeleccionada(self):
        return self.filaSeleccionada
    
    def agregarAlDiccionario(self, posicion, elemento):
        self.diccionarioFilaElemento [posicion] = elemento
        
    def getElementoSeleccionado(self):
        return self.diccionarioFilaElemento.get(self.getFilaSeleccionada())


    #===========================================================================
    # def cargarCon(self, lista):
    #     self.inicializarTabla()
    #     self.clearContents()
    #     self.setRowCount(len(lista))
    #     self.cargar(lista)
    #     
    # def cargar(self):
    #     NotImplemented
    #===========================================================================

class TablaEmpleadosSeccion(SuperTabla):
    '''
        Tabla que lista empleados.
        Puede: 
            - cargar con empleados recibidos
            - cargar con empleados de secciones recibidas
    '''

    def cargarConEmpleados(self, empleados):
        '''
            Recibe una lista de empleados para listar.
            Columnas:
                - nombre
                - apellido
                - tipo de documento
                - nro de documento
                - fecha de nacimiento
                - email
                - seccion

            Ademas, mientras lista los empleados, va armando un diccionario para mantener un correlacion empleado-fila_en_la_que_se_encuentra
        '''
        self.inicializarTabla()
        fila = 0
        self.clearContents()
        self.setRowCount(len(empleados))

        itemSeccionIgualParaTodos = QtGui.QTableWidgetItem()
        itemSeccionIgualParaTodos.setText(unicode('.'))
        empleados.sort()
        for empleado in empleados:
            columna = 0
            itemNombre = QtGui.QTableWidgetItem()
            itemNombre.setText(unicode(empleado.getNombre()))
            self.setItem(fila, columna, itemNombre)
            columna += 1
            itemApellido = QtGui.QTableWidgetItem()
            itemApellido.setText(unicode(empleado.getApellido()))
            self.setItem(fila, columna, itemApellido)
            columna += 1
            itemTipoDoc = QtGui.QTableWidgetItem()
            itemTipoDoc.setText(str(empleado.getTipoDocumento().get_codigo_tipo_documento()))
            self.setItem(fila, columna, itemTipoDoc)
            columna += 1
            itemDocumento = QtGui.QTableWidgetItem()
            itemDocumento.setText(unicode(empleado.getDocumento()))
            self.setItem(fila, columna, itemDocumento)
            columna += 1
            itemFechaNac = QtGui.QTableWidgetItem()
#             itemFechaNac.setText(unicode('empleado.getFechaNacimiento()'))
            itemFechaNac.setText(unicode(empleado.imprimirFechaNacimiento()))
            self.setItem(fila, columna, itemFechaNac)
            columna += 1
            itemEmail = QtGui.QTableWidgetItem()
            itemEmail.setText(unicode(empleado.getEmail()))
            self.setItem(fila, columna, itemEmail)
            columna += 1

#            self.setItem(fila, columna, itemSeccionIgualParaTodos)
#            columna += 1

            self.agregarAlDiccionario(fila, empleado)
            fila += 1

    def cargarConEmpleadosDeSecciones(self, secciones):
        '''
            Recibe una lista de secciones, la cual recorre para listar, por cada seccion, los empleados que posee.
            Columnas:
                - nombre
                - apellido
                - tipo de documento
                - nro de documento
                - fecha de nacimiento
                - email
                - seccion

            Ademas, mientras lista los empleados, va armando un diccionario para mantener un correlacion empleado-fila_en_la_que_se_encuentra
        '''
        #self.diccionario_empleados = {}
        #Inicializacion, conectando los signals:
        self.inicializarTabla()
        fila = 0
        self.clearContents()
        self.setRowCount(self.calcularCantEmpleados(secciones))
        for seccion in secciones:
            #for empleado in seccion.getEmpleados().values():
            for empleado in seccion.getEmpleados():
                columna = 0
                itemNombre = QtGui.QTableWidgetItem()
                itemNombre.setText(unicode(empleado.getNombre()))
                self.setItem(fila, columna, itemNombre)
                columna += 1
                itemApellido = QtGui.QTableWidgetItem()
                itemApellido.setText(unicode(empleado.getApellido()))
                self.setItem(fila, columna, itemApellido)
                columna += 1
                itemTipoDoc = QtGui.QTableWidgetItem()
#                 itemTipoDoc.setText(unicode(empleado.getTipoDocumento()))
                itemTipoDoc.setText(unicode(empleado.getTipoDocumento().get_codigo_tipo_documento()))
                self.setItem(fila, columna, itemTipoDoc)
                columna += 1
                itemDocumento = QtGui.QTableWidgetItem()
                itemDocumento.setText(unicode(empleado.getDocumento()))
                self.setItem(fila, columna, itemDocumento)
                columna += 1
                itemFechaNac = QtGui.QTableWidgetItem()
#                 itemFechaNac.setText(unicode('empleado.getFechaNacimiento()'))
                itemFechaNac.setText(unicode(empleado.imprimirFechaNacimiento()))
                self.setItem(fila, columna, itemFechaNac)
                columna += 1
                itemEmail = QtGui.QTableWidgetItem()
                itemEmail.setText(unicode(empleado.getEmail()))
                self.setItem(fila, columna, itemEmail)
                columna += 1
                itemSeccion = QtGui.QTableWidgetItem()
                itemSeccion.setText(unicode(seccion.getNombre()))
                self.setItem(fila, columna, itemSeccion)
                columna += 1

                #Cargamos el objeto Empleado al diccionario:
                #self.diccionario_empleados[fila] = empleado
                self.agregarAlDiccionario(fila, empleado)
                fila += 1

    def calcularCantEmpleados(self, secciones):
        '''
        Calcula y retorna la cantidad total de empleados de las secciones.
        '''
        cantEmpleados = 0
        for seccion in secciones:
            cantEmpleados += seccion.cantidadEmpleados()
            #print 'Seccion %s tiene %s empleados' %(seccion.getNombre(), seccion.cantidadEmpleados())
        return cantEmpleados

    def getEmpleadoSeleccionado(self):
        #return self.diccionario_empleados.get(self.getFilaSeleccionada())
        return self.getElementoSeleccionado()

    def getPrimerEmpleado(self):
        '''
        Retorna el primer empleado de la lista de empleados
        '''
        return self.diccionarioFilaElemento.get(0)


class TablaSecciones(SuperTabla):

    def cargarConSecciones(self, secciones):
        '''
            Recibe una lista de secciones para listar.
            Columnas:
                - codigo
                - nombre
                - nombre encargado
                - cantidad de empleados

            Ademas, mientras lista las secciones, va armando un diccionario para mantener un correlacion secciones-fila_en_la_que_se_encuentra
        '''
        #self.diccionario_secciones = {}
        self.inicializarTabla()
        fila = 0
        self.clearContents()
        self.setRowCount(len(secciones))
        for seccion in secciones:
            columna = 0
            itemCodigo = QtGui.QTableWidgetItem()
            itemCodigo.setText(unicode(seccion.getCodigo()))
            self.setItem(fila, columna, itemCodigo)
            columna += 1
            itemNombre = QtGui.QTableWidgetItem()
            itemNombre.setText(unicode(seccion.getNombre()))
            self.setItem(fila, columna, itemNombre)
            columna += 1
            itemEncargado = QtGui.QTableWidgetItem()
            itemEncargado.setText(unicode(seccion.getEncargado().nombreCompleto()))
            self.setItem(fila, columna, itemEncargado)
            columna += 1
            itemCantEmpleados = QtGui.QTableWidgetItem()
            itemCantEmpleados.setText(unicode(seccion.cantidadEmpleados()))
            self.setItem(fila, columna, itemCantEmpleados)
            columna += 1
            
            #Cargamos el objeto Empleado al diccionario:
            #self.diccionario_secciones[fila] = seccion
            self.agregarAlDiccionario(fila, seccion)
            
            fila += 1
            
    def getSeccionSeleccionada(self):
        return self.getElementoSeleccionado()

    def getPrimeraSeccion(self):
        '''
        Retorna la primera seccion de la lista de secciones
        '''
        return self.diccionarioFilaElemento.get(0)

class TablaVehiculos(SuperTabla):

    def cargarConVehiculos(self, vehiculos):
        '''
            Recibe una lista de vehiculos para listar.
            Columnas:
                - dominio
                - marca
                - registro interno
                - chasis
                - comisaria

            Ademas, mientras lista los vehiculos, va armando un diccionario para mantener un correlacion vehiculo-fila_en_la_que_se_encuentra
        '''
        self.inicializarTabla()
        fila = 0
        self.clearContents()
        self.setRowCount(len(vehiculos))

        for vehiculo in vehiculos:
            #Crear items y setearlos
            columna = 0
            itemRegistroInterno = QtGui.QTableWidgetItem()
            itemRegistroInterno.setText(vehiculo.registroInterno)
            self.setItem(fila, columna, itemRegistroInterno)
            columna += 1
            itemNumeroChasis = QtGui.QTableWidgetItem()
            itemNumeroChasis.setText(vehiculo.getNumeroChasis())
            self.setItem(fila, columna, itemNumeroChasis)
            columna += 1
            itemMarca = QtGui.QTableWidgetItem()
            itemMarca.setText(vehiculo.marca)
            self.setItem(fila, columna, itemMarca)
            columna += 1
            itemModelo = QtGui.QTableWidgetItem()
            itemModelo.setText(vehiculo.modelo)
            self.setItem(fila, columna, itemModelo)
            columna += 1
            itemDominio = QtGui.QTableWidgetItem()
            itemDominio.setText(vehiculo.dominio)
            self.setItem(fila, columna, itemDominio)

            self.agregarAlDiccionario(fila, vehiculo)
            fila += 1
        
    def getVehiculoEn(self, index):
        return self.diccionarioFilaElemento[index]

    def getVehiculoSeleccionado(self):
        return self.getElementoSeleccionado()
        
class TablaTiposDeRepuestos(SuperTabla):
    '''
        Tabla que lista repuestos.
        Puede: 
            - cargar con tipos de repuestos recibidos
    '''
    
    def cargarConRepuestos(self, repuestos):
        '''
            Recibe una lista de repuestos para listar.
            Columnas:
                - codigo
                - nombre
                - descripcion
                
            Ademas, mientras lista los repuestos, va armando un diccionario para mantener un correlacion repuestos-fila_en_la_que_se_encuentra
        '''
        self.inicializarTabla()
        fila = 0
        self.clearContents()
        repuestos.sort()
        self.setRowCount(len(repuestos))
        
        for repuesto in repuestos:
            columna = 0
            itemCodigo = QtGui.QTableWidgetItem()
            itemCodigo.setText(unicode(repuesto.getCodigo()))
            self.setItem(fila, columna, itemCodigo)
            columna += 1
            itemNombre = QtGui.QTableWidgetItem()
            itemNombre.setText(unicode(repuesto.getNombre()))
            self.setItem(fila, columna, itemNombre)
            columna += 1
            itemDescripcion = QtGui.QTableWidgetItem()
            itemDescripcion.setText(unicode(repuesto.getDescripcion()))
            self.setItem(fila, columna, itemDescripcion)
            
            self.agregarAlDiccionario(fila, repuesto)
            fila += 1


    def getRepuestoSeleccionado(self):
        #return self.diccionario_empleados.get(self.getFilaSeleccionada())
        return self.getElementoSeleccionado()


class TablaReparaciones(SuperTabla):
    '''
        Tabla que lista reparaciones.
        Puede: 
            - cargar con reparaciones recibidas
    '''
    
    def cargarConReparaciones(self, reparaciones):
        '''
            Recibe una lista de reparaciones para listar.
            Columnas:
                - codigo
                - nombre
                - descripcion
                
            Ademas, mientras lista los reparaciones, va armando un diccionario para mantener un correlacion reparaciones-fila_en_la_que_se_encuentra
        '''
        self.inicializarTabla()
        fila = 0
        self.clearContents()
        reparaciones.sort()
        self.setRowCount(len(reparaciones))
        
        for reparacion in reparaciones:
            columna = 0
            itemCodigo = QtGui.QTableWidgetItem()
            itemCodigo.setText(unicode('repuesto.getCodigo()'))
            self.setItem(fila, columna, itemCodigo)
            columna += 1
            itemNombre = QtGui.QTableWidgetItem()
            itemNombre.setText(unicode(reparacion.getNombre()))
            self.setItem(fila, columna, itemNombre)
            columna += 1
            itemDescripcion = QtGui.QTableWidgetItem()
            itemDescripcion.setText(unicode(reparacion.getDescripcion()))
            self.setItem(fila, columna, itemDescripcion)
            
            self.agregarAlDiccionario(fila, reparacion)
            fila += 1


    def getReparacionSeleccionada(self):
        return self.getElementoSeleccionado()


class TablaRepuestosRequeridos(SuperTabla):
    '''
        Tabla que lista repuestos.
        Puede: 
            - cargar con tipos de repuestos recibidos
    '''
    
    def cargarConRepuestos(self, repuestos):
        '''
            Recibe una lista de repuestos para listar.
            Columnas:
                - codigo
                - nombre
                - descripcion
                
            Ademas, mientras lista los repuestos, va armando un diccionario para mantener un correlacion repuestos-fila_en_la_que_se_encuentra
        '''
        self.inicializarTabla()
        fila = 0
        self.clearContents()
        repuestos.sort()
        self.setRowCount(len(repuestos))
        
        for repuesto in repuestos:
            columna = 0
            itemCodigo = QtGui.QTableWidgetItem()
            itemCodigo.setText(unicode(repuesto.getTipoDeRepuesto().getCodigo()))
            self.setItem(fila, columna, itemCodigo)
            columna += 1
            itemNombre = QtGui.QTableWidgetItem()
            itemNombre.setText(unicode(repuesto.getTipoDeRepuesto().getNombre()))
            self.setItem(fila, columna, itemNombre)
            columna += 1
            itemDescripcion = QtGui.QTableWidgetItem()
            itemDescripcion.setText(unicode(repuesto.getTipoDeRepuesto().getDescripcion()))
            self.setItem(fila, columna, itemDescripcion)
            columna += 1
            itemCantidad = QtGui.QTableWidgetItem()
            itemCantidad.setText(unicode(repuesto.getCantidad()))
            self.setItem(fila, columna, itemCantidad)
            
            self.agregarAlDiccionario(fila, repuesto)
            fila += 1


    def getRepuestoSeleccionado(self):
        #return self.diccionario_empleados.get(self.getFilaSeleccionada())
        return self.getElementoSeleccionado()

class TablaSuper(QtGui.QTableWidget):
    
    def cargarGrilla(self, lista_empleados):
        fila = 0
        self.clearContents()
        self.setRowCount(len(lista_empleados))
        for empleado in lista_empleados:
            columna = 0
            itemDocumento = QtGui.QTableWidgetItem()
            itemDocumento.setText(unicode(empleado.documento))
            self.setItem(fila, columna, itemDocumento)
            columna += 1
            itemNombre = QtGui.QTableWidgetItem()
            itemNombre.setText(unicode(empleado.nombre))
            self.setItem(fila, columna, itemNombre)
            fila += 1
            
    def cargarGrillaTwo(self, lista_empleados):
        fila = 0
        self.clearContents()
        self.setRowCount(len(lista_empleados))
        for empleado in lista_empleados:
            print empleado.nombreCompleto()
            columna = 0
            infoEmpleado = empleado.getInfo() 
            for clave in infoEmpleado.keys():
                unItem = QtGui.QTableWidgetItem()
                unItem.setText(unicode(infoEmpleado[clave]))
                print infoEmpleado[clave]
                self.setItem(fila, columna, unItem)
                columna += 1
            fila += 1

class TablaReparacionesNoPlanificadas(SuperTabla):
    '''
        Tabla que lista reparaciones.
        Puede: 
            - cargar con reparaciones recibidas
    '''
    
    def cargarConReparaciones(self, orden):
        '''
            Recibe una lista de reparaciones para listar.
            Columnas:
                - codigo
                - nombre
                - descripcion
                
            Ademas, mientras lista los reparaciones, va armando un diccionario para mantener un correlacion reparaciones-fila_en_la_que_se_encuentra
        '''
        self.inicializarTabla()
        fila = 0
        self.clearContents()
        reparaciones = orden.getReparaciones()
        reparaciones.sort()
        self.setRowCount(len(reparaciones))
        
        for reparacion in reparaciones:
            columna = 0
            itemCodigo = QtGui.QTableWidgetItem()
            itemCodigo.setText(unicode(orden.getCodigoOrdenReparacion()))
            self.setItem(fila, columna, itemCodigo)
            columna += 1
            itemNombre = QtGui.QTableWidgetItem()
            itemNombre.setText(unicode(reparacion.getTipoDeReparacion().getDescipcion()))
            self.setItem(fila, columna, itemNombre)
            columna += 1
            itemCodigo = QtGui.QTableWidgetItem()
            itemCodigo.setText(unicode(reparacion.getCodigo()))
            self.setItem(fila, columna, itemCodigo)
            columna += 1
            itemDescripcion = QtGui.QTableWidgetItem()
            itemDescripcion.setText(unicode(reparacion.getDescripcion()))
            self.setItem(fila, columna, itemDescripcion)
            
            self.agregarAlDiccionario(fila, reparacion)
            fila += 1


    def getReparacionSeleccionada(self):
        return self.getElementoSeleccionado()
    
    
class TablaReparacionesPlanificadas(SuperTabla):
    '''
        Tabla que lista reparaciones.
        Puede: 
            - cargar con reparaciones recibidas
    '''

    def cargarConReparaciones(self, reparaciones):
        '''
            Recibe una lista de reparaciones para listar.
            Columnas:
                - descripcion
                - fecha de inicio
                - fecha de finalizacion
            Ademas, mientras lista los reparaciones, va armando un diccionario para mantener un correlacion reparaciones-fila_en_la_que_se_encuentra
        '''
        self.inicializarTabla()
        fila = 0
        self.clearContents()
        reparaciones.sort()
        self.setRowCount(len(reparaciones))

        for reparacion in reparaciones:
            columna = 0
            itemDescripcion = QtGui.QTableWidgetItem()
            itemDescripcion.setText(unicode(reparacion.getDescripcion()))
            self.setItem(fila, columna, itemDescripcion)
#             columna += 1
#             itemFechaInicio = QtGui.QTableWidgetItem()
#             itemFechaInicio.setText(unicode(reparacion.getFechaInicio()))
#             self.setItem(fila, columna, itemFechaInicio)
#             columna += 1
#             itemFechaFin = QtGui.QTableWidgetItem()
#             itemFechaFin.setText(unicode(reparacion.getFechaFin()))
#             self.setItem(fila, columna, itemFechaFin)

            self.agregarAlDiccionario(fila, reparacion)
            fila += 1

    def getReparacionSeleccionada(self):
        return self.getElementoSeleccionado()