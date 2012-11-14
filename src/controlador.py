# -*- coding: utf-8 -*-
'''
Created on 24/10/2012

@author: urrutia
'''
from negocio import TipoDocumento

tDoc = TipoDocumento.TipoDocumento('DNI','documento nacional de identidad')
print tDoc

from negocio import Division_Transporte

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
class Singleton1(type):
 
    def __init__(cls, name, bases, dct):
        cls.__instance = None
        type.__init__(cls, name, bases, dct)
 
    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = type.__call__(self, *args,**kwargs)
        return self.__instance
 
class A:
    __metaclass__ = Singleton1
    # Definir aqu� el resto de la interfaz
    
a = A()
b = A()
assert a is b
print "Id de a: %s     Id de b: %s" %(a,b)