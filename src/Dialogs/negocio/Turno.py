'''
Created on 11/07/2014

@author: LeoMorales
'''
from persistent import Persistent
from persistent.list import PersistentList
import transaction
import copy

class Turno(Persistent):
    '''
    Un turno posee toda la informacion pertinente al turno que tiene un
    vehiculo para ser atendido en una seccion.
    
    Ademas, el turno tiene una lista con las reparaciones que se realizaran en dicho turno.
    '''


    def __init__(self, codigo, seccion, vehiculo, fecha, hora = None, reparaciones = []):
        '''
        Constructor
        '''
        self._codigo = codigo
        self._seccion = seccion
        self._vehiculo = vehiculo
        self._fecha = fecha
        self._hora = hora
        
        self._detallesPlan = PersistentList()#Detalle --> Reparaciones, hacer un objeto detalle no agrega nada a la logica...
        for reparacion in reparaciones:
            reparacion.planificada()
        self._detallesPlan.extend(reparaciones)
        #transaction.commit()#Para guardar reparaciones en estado planificada
        self._finalizado = False
        self._empleadosAsignados = PersistentList()
        self._observaciones = ''
        #transaction.commit()#Para guardar reparaciones en estado planificada
        
    def getHora(self):
        return self._hora
    
    def getFecha(self):
        return self._fecha
    
    def setHora(self, hora):
        self._hora = hora
        
    def __str__(self):
        return 'Turno: Vehiculo: %s | Seccion: %s | fecha: %s | hora: %s | reparaciones: %s' %(self._vehiculo.getDominio(), 
                                                                                               self._seccion.getNombre(), 
                                                                                               self._fecha, 
                                                                                               self._hora,
                                                                                               [unicode(detalle) for detalle in self._detallesPlan]
                                                                                               )
    
    def addDetalle(self, nuevoDetallePlan):
        self._detallesPlan.append(nuevoDetallePlan)
    
    def getDetalles(self):
        return self._detallesPlan
    
    def finalizar(self, observaciones= ''):
        self._observaciones = observaciones
        self._finalizado = True
        self.finalizarTodasLasReparaciones()
        #yo era el ultimo turno que faltaba?
        if self._vehiculo.tieneTodosLosTurnosFinalizados():
            #SI
            self._vehiculo.finalizarVerificacionReparacion()
            
    def estaFinalizado(self):
        return self._finalizado
    
    def finalizarTodasLasReparaciones(self):
        '''
        Recupera las reparaciones de los detalles del plan
        y las marca como finalizadas
        '''
        #for reparacion in [detalle.getReparacion() for detalle in self._detallesPlan]:
        for reparacion in self._detallesPlan:
            reparacion.finalizar(self._fecha)
            #De paso aprovechamos para decrementar las reparaciones pendientes de cada empleado
            for cada_empleado in self._empleadosAsignados:
                cada_empleado.decrementarReparacionesPendientes()
                print "%s: %d reparaciones pendientes"%(cada_empleado.nombreCompleto(), cada_empleado.reparaciones_pendientes())
        
    def asignarEmpleados(self, empleados):
        '''
        Recibe una lista de empleados y los asigna al turno
        '''
        #Por cada empleado, incrementar las reparaciones que tienen asignadas...
        cantidad_de_reparaciones = len(self._detallesPlan)
        for cada_empleado in empleados:
            cada_empleado.incrementarReparacionesAsignadas(cantidad_de_reparaciones)
            print "%s: %d reparaciones pendientes"%(cada_empleado.nombreCompleto(), cada_empleado.reparaciones_pendientes())
        #Y los asignamos a la lista de empleados del turno
        #self._empleadosAsignados.extend(empleados)
        #Sigue sacando los empleados de la seccion al asignar...prueba 1:
        self._empleadosAsignados.extend(copy.copy(empleados))
        transaction.commit()

    def getReparaciones(self):
        return self._detallesPlan
    
    def getVehiculo(self):
        return self._vehiculo
    
    def noEstaAsignado(self):
        return self._empleadosAsignados == []
    
    def estaAsignado(self):
        return self._empleadosAsignados != []
    
    def getEmpleadosAsignados(self):
        return self._empleadosAsignados
    
    def empleadosAsignados(self):
        '''
        @return: una cadena con los nombres de los encargados separados por coma
        '''
        if not self.getEmpleadosAsignados():
            return '-'
        return ', '.join([empleado.nombreCompleto() for empleado in self.getEmpleadosAsignados()])

    def getSeccion(self):
        return self._seccion

    def getCodigo(self):
        return self._codigo

    def setCodigo(self, value):
        self._codigo = value
   
    