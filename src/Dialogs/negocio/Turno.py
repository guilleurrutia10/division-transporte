'''
Created on 11/07/2014

@author: LeoMorales
'''
from persistent import Persistent
from persistent.list import PersistentList

class Turno(Persistent):
    '''
    Un turno posee toda la informacion pertinente al turno que tiene un
    vehiculo para ser atendido en una seccion.
    
    Ademas, el turno tiene una lista con las reparaciones que se realizaran en dicho turno.
    '''


    def __init__(self, seccion, vehiculo, fecha, hora = None):
        '''
        Constructor
        '''
        self._seccion = seccion
        self._vehiculo = vehiculo
        self._fecha = fecha
        self._hora = hora
        
        self._detallesPlan = PersistentList()
        self._finalizado = False
        self._empleadosAsignados = PersistentList()
        
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
                                                                                               [str(detalle) for detalle in self._detallesPlan]
                                                                                               )
    
    def addDetalle(self, nuevoDetallePlan):
        self._detallesPlan.append(nuevoDetallePlan)
    
    def getDetalles(self):
        return self._detallesPlan
    
    def finalizar(self):
        self._finalizado = True
        
    def estaFinalizado(self):
        return self._finalizado
    
    def finalizarTodasLasReparaciones(self):
        '''
        Recupera las reparaciones de los detalles del plan
        y las marca como finalizadas
        '''
        for reparacion in [detalle.getReparacion() for detalle in self._detallesPlan]:
            reparacion.finalizar()
        
    def asignarEmpleados(self, empleados):
        '''
        Recibe una lista de empleados y los asigna al turno
        '''
        self._empleadosAsignados.extend(empleados)
            