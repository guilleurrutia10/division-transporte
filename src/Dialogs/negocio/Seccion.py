# -*- coding: utf-8 -*-
'''
Created on 28/10/2012

@author: urrutia
'''

from persistent import Persistent
from persistent.list import PersistentList
from BTrees.OOBTree import OOBTree
from Turno import Turno
import transaction
from persistent.mapping import PersistentMapping

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
        - tiposDeReparaciones
    '''
    def __init__(self, codigoSeccion, nombre, empleados, encargado):
        '''
        Constructor
        @return: 
        @author: 
        '''
        self.codigoSeccion = codigoSeccion
        self.nombre = nombre
#        self.empleados = PersistentMapping(empleados)
        self.empleados = PersistentList(empleados)
        self.empleados.extend(empleados)
        self.encargado = encargado
        self.tablaDeTurnos = OOBTree()
        self.tiposDeReparaciones = PersistentList()
    
    def setEncargado(self, encargado):
        '''
        @return: 
        @author: 
        '''
        self.encargado = encargado
    
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
#        self.empleados[empleado.getDocumento()] = empleado
        self.empleados.append(empleado)
        transaction.commit()
    
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
#        empleadosConReparacionesPendientes = filter(lambda unEmpleado: unEmpleado.tieneReparacionesPendientes() , self.getEmpleados().values())
        empleadosConReparacionesPendientes = filter(lambda unEmpleado: unEmpleado.tieneReparacionesPendientes() , self.getEmpleados())
        return len(empleadosConReparacionesPendientes) == 0 and self.cantidadEmpleadosTotales() >= CANTIDAD_MIN_PARA_TRANFERIR 
    
    def getEmpleados(self):
        '''
            Retorna una lista de empleados.Si
            Antes: Retorna un diccionario de empelados.
        '''
        return self.empleados
    
    def poseeAEmpleado(self, unEmpleado):
#        return unEmpleado in self.getEmpleados().values()
        return unEmpleado in self.getEmpleados()
        
    def getEncargado(self):
        return self.encargado
    
    def getCodigo(self):
        return 'codigo'
    
    def removerEmpleado(self, empleadoARemover):
#        del self.getEmpleados()[empleadoARemover.getDocumento()]
        self.empleados.remove(empleadoARemover)
        transaction.commit()
        
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

    def crearRegistroParaElDia_deprecated(self, queDia):
        if not self.tablaDeTurnos.has_key(queDia):
            self.tablaDeTurnos.update({queDia: TURNOS_DEL_DIA_VACIA})
            transaction.commit()
            print "El dia se ha registrado en la tabla de turnos exitosamente!"

    def crearRegistroParaElDia(self, queDia):
        if not self.tablaDeTurnos.has_key(queDia):
            horas_turno = OOBTree()
            horas_turno.update(TURNOS_DEL_DIA_VACIA)
            self.tablaDeTurnos.update({queDia: horas_turno})
            transaction.commit()
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
#        transaction.commit()
                    
    def getAgendaDelDia(self, queDia):
        if self.tieneRegistroParaElDia(queDia):
            return self.tablaDeTurnos.get(queDia)
        else:
            self.crearRegistroParaElDia(queDia)
            return self.tablaDeTurnos.get(queDia)
        
    def getHorasSinTurnoParaElDia(self, dia):
        '''
        Retorna una lista con todas las horas en las que la seccion
        no tiene registrado un turno
        '''
        list_retorno = []
        for hora, turno in self.getAgendaDelDia(dia).iteritems():
            if not turno:
                list_retorno.append(hora)
        return list_retorno
    
    def getTurnoDeFechaHora(self, queDia, queHora):
        '''
        queDia: string <<10/10/2014>>
        queHora: int in [8,9,10,11,12,16,17,18,19,20]'''
        return self.tablaDeTurnos.get(queDia).get(queHora)

    def __str__(self):
        return '%s | %s' %(self.codigoSeccion, self.nombre)
    
    def agregarTipoDeReparacion(self, reparacion):
        '''
        Agrega la reaparacion ingresada como una nueva reparacion que la seccion es capaz de realizar
        '''
        self.tiposDeReparaciones.append(reparacion)

    def getTiposDeReparaciones(self):
        return self.tiposDeReparaciones
    
    def realiza(self, unaReparacion):
        return unaReparacion.getTipoDeReparacion() in self.tiposDeReparaciones
    
    def getDiasEnLosQueHayTurnoSinAsignar(self):
        '''
        Retorna una lista con todos los dias en los cuales se ha asignado un turno
        pero no dse han asignado empleados encargados de dichos turnos.
        '''
        dias = []
        for dia in self.tablaDeTurnos.keys():
            if self.getHorasEnLosQueHayTurnoSinAsignar(dia):
                dias.append(dia)
        return dias
    
    def getDiasEnLosQueHayTurno_deprecated(self):
        '''
        Retorna una lista con todos los dias en los cuales se ha asignado un turno
        '''
        return self.tablaDeTurnos.keys()

    def getHorasEnLosQueHayTurnoSinAsignar(self, dia):
        '''
        Retorna una lista con todas las horas en las que la seccion
        tiene registrado un turno que no tenga empleados asignados.
        '''
        list_retorno = []
        for hora, turno in self.getAgendaDelDia(dia).iteritems():
            if turno:
                if turno.noEstaAsignado():
                    list_retorno.append(hora)
        return list_retorno
        
    def getDiasEnLosQueHayTurnoAsignado(self):
        '''
        Retorna una lista con todos los dias en los cuales se ha asignado un turno
        y al que ya se le han asignado empleados encargados de dichos turnos.
        '''
        dias = []
        for dia in self.tablaDeTurnos.keys():
            if self.getHorasEnLosQueHayTurnoAsignados(dia):
                dias.append(dia)
        return dias

    def getHorasEnLosQueHayTurnoAsignados(self, dia):
        '''
        Retorna una lista con todas las horas en las que la seccion
        tiene registrado un turno que tenga empleados asignados.
        '''
        list_retorno = []
        for hora, turno in self.getAgendaDelDia(dia).iteritems():
            if turno:
                if turno.estaAsignado() and not turno.estaFinalizado():
                    list_retorno.append(hora)
        return list_retorno
        
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
    
    
