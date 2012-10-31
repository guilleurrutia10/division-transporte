# -*- coding: utf-8 -*-
'''
Created on 24/10/2012

@author: urrutia
'''

import negocio

class controlador(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
from PyQt4.QtCore import *

class Singleton (object):
    instance = None       
    def __new__(cls, *args, **kargs): 
        if cls.instance is None:
            cls.instance = object.__new__(cls, *args, **kargs)
        return cls.instance
 
#Usage
mySingleton1 = Singleton()
mySingleton2 = Singleton()
 
#mySingleton1 y mySingleton2 son la misma instancia
assert mySingleton1 is mySingleton2
print "Id mySingleton1: %s e Id mySingleton2: %s" %(mySingleton1,mySingleton2)

#class Singleton1(type):
# 
#    def __init__(cls, name, bases, dct):
#        cls.__instance = None
#        type.__init__(cls, name, bases, dct)
# 
#    def __call__(cls, *args, **kw):
#        if cls.__instance is None:
#            cls.__instance = type.__call__(cls, *args,**kw)
#        return cls.__instance
# 
#class A:
#    __metaclass__ = Singleton1
#    # Definir aqu� el resto de la interfaz
