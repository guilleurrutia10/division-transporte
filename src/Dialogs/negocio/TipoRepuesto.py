# -*- coding: utf-8 -*-
'''
Created on 28/10/2012

@author: urrutia
'''

from persistent import Persistent

from DetalleRepuesto import *

class TipoRepuesto(Persistent):
    '''
    classdocs
    @version: 
    @author: 
    '''

    '''     ATTRIBUTES
        
    codigoRepuesto  (private)
        
    nombre  (private)
        
    descripcion  (private)
    
    '''

    def __init__(self, nombre, descripcion):
        '''
        Constructor
        @return: 
        @author: 
        '''
        self._nombre = nombre
        self._descripcion = descripcion
        self._codigo = None
        
    def setCodigo(self, codigo):
        '''
        @return: 
        @author: 
        '''
        self._codigo = codigo
        
    def getCodigo(self):
        '''
        @return: 
        @author: 
        '''
        return self._codigo
    
    def setNombre(self, nombre):
        '''
        @return: 
        @author: 
        '''
        self._nombre = nombre
        
    def getNombre(self):
        '''
        @return: 
        @author: 
        '''
        return self._nombre
    
    def setDescripcion(self, descripcion):
        '''
        @return: 
        @author: 
        '''
        self._descripcion = descripcion
        
    def getDescripcion(self):
        '''
        @return: 
        @author: 
        '''
        return self._descripcion
    
    def datosRepuesto(self):
        '''
        @return: 
        @author: 
        '''
        pass
    
    def addRepuesto(self):
        '''
        @return: 
        @author: 
        '''
        pass
    
    def __str__(self):
        return '%s: %s' % (self._nombre, self._descripcion)
    
    def save(self):
        from MiZODB import ZopeDB, MiZODB
        zodb = ZopeDB(MiZODB())
#        zodb = ZopeDB(MiZODB('zeo.conf'))
        zodb.save('tiposRepuestos', self.getNombre(), self)
