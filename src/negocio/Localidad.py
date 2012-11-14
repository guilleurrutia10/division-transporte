# -*- coding: utf-8 -*-
'''
Created on 28/10/2012

@author: urrutia
'''

from persistent import Persistent

class Localidad(Persistent):
    '''
    classdocs
    @version: 
    @author: 
    '''


    def __init__(self, nombre, codigoPostal):
        '''
        Constructor
        @return: 
        @author: 
        '''
        self._nombre = nombre
        self._codigoPostal = codigoPostal
        
        
    """ ATTRIBUTES
    
       
    
    codigoPostal  (private)
    
       
    
    nombre  (private)
    
    """        