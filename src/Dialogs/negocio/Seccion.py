# -*- coding: utf-8 -*-
'''
Created on 28/10/2012

@author: urrutia
'''

from persistent import Persistent
from BTrees.OOBTree import OOBTree
from Turno import Turno

CANTIDAD_MIN_PARA_TRANFERIR = 3
TURNOS_DEL_DIA_VACIA = {8:None, 9:None,10:None, 11:None,12:None, 16:None,17:None, 18:None,19:None, 20:None}

class Seccion(Persistent):
    '''
    classdocs
    @version: 
    @author:
        
        ATTRIBUTES:
        
        - codigoSeccion  (private)
        - nombre  (private)
        - empleados
        - encargado        
        
        - tablaDeTurnos
    '''
    def __init__(self, codigoSeccion, nombre, empleados, encargado):
        '''
        Constructor
        @return: 
        @author: 
        '''
        self.codigoSeccion = codigoSeccion
        self.nombre = nombre
        self.empleados = empleados
        self.encargado = encargado
        
        self.tablaDeTurnos = OOBTree()
    
    def setEncargado(self, encargado):
        '''
        @return: 
        @author: 
        '''
        pass
    
    def setNombre(self):
        '''
        @return: 
        @author: 
        '''
        pass
    
    def agregarEmpleado(self, empleado):
        '''
        @return: 
        @author: 
        '''
        self.empleados[empleado.documento] = empleado
    
    def quitarEmpleado(self):
        '''
        @return: 
        @author: 
        '''
        pass
    
    def getNombre(self):
        return self.nombre
    
    def cantidadEmpleados(self):
        '''
        Devuelve la cantidad de empleados que tiene la Sección.
        (Cantidad de empleados sin contar el encargado)
        '''
        return len(self.empleados)
    
    def cantidadEmpleadosTotales(self):
        '''
        Devuelve la cantidad de empleados que tiene la Sección.
        (Cantidad de empleados mas el encargado)
        '''
        return len(self.empleados) + 1
    
    def puedeTransferir(self):
        '''
        Una Seccion puede tranferir a un empleado si:
            - Ninguno de sus empleados tiene reparaciones pendientes.
            - Posee mas de dos empleados (un empleado y el encargado).
        Util para un listado de solo Secciones que pueden transferir empleados.
        '''
        empleadosConReparacionesPendientes = filter(lambda unEmpleado: unEmpleado.tieneReparacionesPendientes() , self.getEmpleados().values())
        return len(empleadosConReparacionesPendientes) == 0 and self.cantidadEmpleadosTotales() >= CANTIDAD_MIN_PARA_TRANFERIR 
    
    def getEmpleados(self):
        '''
            Retorna un diccionario con:
                - k = dni del empleado 
                - v = Objeto Empleado.
        '''
        return self.empleados
    
    def poseeAEmpleado(self, unEmpleado):
        return unEmpleado in self.getEmpleados().values()
        
    def getEncargado(self):
        return self.encargado
    
    def getCodigo(self):
        return 'codigo'
    
    def removerEmpleado(self, empleadoARemover):
        del self.getEmpleados()[empleadoARemover.getDocumento()]
        
    def asignarNuevoEncargado(self, nuevoEncargado):
        '''
            Asigna un nuevo encargado a la Seccion.
            @return: El encargado anterior.
        '''
        encargadoAnterior = self.getEncargado()
        self.setEncargado(nuevoEncargado)
        return encargadoAnterior
    
    def tieneRegistroParaElDia(self, queDia):
        '''
            OOBTree.has_key(una_clave_que_no_tiene) devuelve 0!
        '''
        return self.tablaDeTurnos.has_key(queDia) != 0

    def crearRegistroParaElDia(self, queDia):
        if not self.tablaDeTurnos.has_key(queDia):
            self.tablaDeTurnos.update({queDia: TURNOS_DEL_DIA_VACIA})
            print "El dia se ha registrado en la tabla de turnos exitosamente!"
            
    def tieneTurnoLibreParaElDia(self, queDia):
        if not self.tieneRegistroParaElDia(queDia):
            self.crearRegistroParaElDia(queDia)
        return None in list(self.tablaDeTurnos.get(queDia).values()) #[Turno, Turno, None, Turno] por ejemplo...

    def tieneTurnoLibreParaFechaHora(self, queDia, queHora):
        if not self.tieneRegistroParaElDia(queDia):
            self.crearRegistroParaElDia(queDia)
        return self.tablaDeTurnos.get(queDia).get(queHora) is None#[Turno, Turno, None, Turno] por ejemplo...
             
    def getPrimerTurnoLibreParaElDia(self, queDia):
        '''
        Devuelve la hora del primer turno libre.
        l = list(self.tablaDeTurnos.get(queDia).keys())
        print 'Horarios2: ', l
        print 'Horarios3: ', l.sort()
        >>'Horarios3: None' 
        '''
        if not self.tieneRegistroParaElDia(queDia):
            self.crearRegistroParaElDia(queDia)
        #Obtengo el diccionario de horarios. Con copy los valores son las mismas referencias, pero a nos no nos importa xq no vamos a modificar nada
        horarios = self.tablaDeTurnos.get(queDia).copy()
        #print 'Horarios: ',list(horarios.keys())

        for hora, turno in horarios.iteritems():
            if turno == None:
                return hora
    
    def crearTurnoParaElDia(self, vehiculo, queDia, hora= None):
        '''
        Crea un turno para el dia indicado.
        El dia debe tener el formato 'dd/mm/YYYY'
        '''
        if not self.tieneRegistroParaElDia(queDia):
            self.crearRegistroParaElDia(queDia)
            
        #si no viene con una hora indicada:
        if hora == None:
            print 'El turno se creara en el primer turno libre disponible'
            hora = self.getPrimerTurnoLibreParaElDia(queDia)
        
        #Creacion y asignacion del Turno:
        self.tablaDeTurnos.get(queDia)[hora] = Turno(self, vehiculo, queDia, hora)

    def registrarTurno(self, turno):
        '''
        Registra el turno en la estructura de la seccion, para busquedas eficientes
        La fecha en el Turno debe tener el formato 'dd/mm/yyyy'
        '''
        if not self.tieneRegistroParaElDia(turno.getFecha()):
            self.crearRegistroParaElDia(turno.getFecha())
            
        #si no viene con una hora indicada:
        if turno.getHora()== None:
            print 'El turno se creara en el primer turno libre disponible'
            turno.setHora(self.getPrimerTurnoLibreParaElDia(turno.getFecha()))
        
        #Creacion y asignacion del Turno:
        self.tablaDeTurnos.get(turno.getFecha())[turno.getHora()] = turno
                    
    def getAgendaDelDia(self, queDia):
        if self.tieneRegistroParaElDia(queDia):
            return self.tablaDeTurnos.get(queDia)
        else:
            self.crearRegistroParaElDia(queDia)
            return self.tablaDeTurnos.get(queDia)
    
    def getTurnoDeFechaHora(self, queDia, queHora):
        return self.tablaDeTurnos.get(queDia).get(queHora)

##############################################################################
########################## TEST SECCION ######################################
##############################################################################
import unittest
from datetime import datetime

class TddSeccion(unittest.TestCase):
    
    def setUp(self):
        codigoSeccion, nombre, empleados, encargado = '1111', 'Seccion1', [],[]
        self.seccion  = Seccion(codigoSeccion, nombre, empleados, encargado)
        self.hoy = datetime.now()
        #self.hoy.strftime("%d/%m/%Y")
        self.hoy = '%s/%s/%s' %(self.hoy.day, self.hoy.month, self.hoy.year)

    def tearDown(self):
        pass
    
    def test_registro_para_el_dia(self):
        tieneRegistro = self.seccion.tieneRegistroParaElDia(self.hoy)
        self.assertEqual(False, tieneRegistro)

    def test_crear_registro_para_el_dia(self):
        self.seccion.crearRegistroParaElDia(self.hoy)
        tieneRegistro = self.seccion.tieneRegistroParaElDia(self.hoy)
        self.assertNotEqual(False, tieneRegistro)


    def test_tiene_turno_libre_para_el_dia(self):
        tieneTurno = self.seccion.tieneTurnoLibreParaElDia(self.hoy)
        self.assertEqual(True, tieneTurno)

    def test_primer_turno_libre_para_el_dia(self):
        horaTurno = self.seccion.getPrimerTurnoLibreParaElDia(self.hoy)
        self.assertEqual(8, horaTurno)
        self.seccion.crearTurnoParaElDia(self.hoy, 8)
        horaTurno = self.seccion.getPrimerTurnoLibreParaElDia(self.hoy)
        self.assertEqual(9, horaTurno)
        
    def test_get_agenda_del_dia(self):
        self.seccion.crearTurnoParaElDia(self.hoy, 16)
        agendaDelDia = self.seccion.getAgendaDelDia(self.hoy)
        print 'Agenda del dia ', self.hoy, ': ', agendaDelDia
        self.assertNotEqual(None, agendaDelDia)
        
