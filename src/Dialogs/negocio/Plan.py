'''
Created on 13/11/2012

@author: Usuario
'''
from persistent import Persistent
from persistent.list import PersistentList
import DetallePlan

class Plan(Persistent):
    '''
    Plan:
    
        atributes 
                _detalles: Lista de Turnos
    El plan tiene una lista de Turnos.
    En cada turno se llevan a cabo cierto tipo de reparaciones
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self._detalles = PersistentList()
        self._turnos = PersistentList()
        #Codigo que se le setea cuando esta aprobado:
        self._codigo = None

    def getDetalles(self):
        return self._detalles
            
    def addDetalle(self,unNuevoDetalle):
        self.getDetalles().append(unNuevoDetalle)
    
    def addTurno(self, nuevoTurno):    
        self._turnos.append(nuevoTurno)
    
    def getTurnos(self):
        return self._turnos
    
    def __str__(self):
        return 'Plan: \kn%s' %''.join('%s\n' %str(turno) for turno in self._turnos)
    
    def setCodigo(self, codigo):
        self._codigo = codigo
    
    def getCodigo(self):
        return self._codigo
    
    def horasOcupadasParaElDia(self, dia):
        '''
        @param dia: str del tipo 12/12/2012
        @return: Una lista de enteros que representan horas de turnos para el dia recibido
        '''
        turnos_del_dia = filter(lambda turno: turno.getFecha() == dia, self.getTurnos())
        return [turno.getHora() for  turno in turnos_del_dia]
    
    def getFechasDeTurnos(self):
        '''
        @return: una lista de fechas de tipo str
        '''
        return [turno.getFecha() for turno in self.getTurnos()]
