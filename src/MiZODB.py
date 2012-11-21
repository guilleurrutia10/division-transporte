# -*- coding: utf-8 -*-
'''
Created on 03/11/2012

@author: urrutia
'''

from ZODB import config
import transaction
from persistent.mapping import PersistentMapping

from MyExceptions import ObjeNoExiste

class MiZODB(object):
    '''
    Clase que representa la ZODB.
    classdocs
    @version: 
    @author: 
    '''

    def __init__(self, url):
        '''
        Constructor, se conecta al Servidor de la BD a traves del archivo de configuracion zeo.conf
        en donde se indica la IP:PORT.
        @return: 
        @author: 
        '''
        self.url = url
        self.db = config.databaseFromURL(url)
        self.conexion = self.db.open()
        self.raiz = self.conexion.root()
        
    def open(self):
        '''
        Abre la conexion con la base de datos.
        @return: 
        @author: 
        '''
        self.db = config.databaseFromURL(self.url)
        self.conexion = self.db.open()
        self.raiz = self.conexion.root()
        
    def close(self):
        '''
        Cierra la conexion con la base de datos.
        @return: 
        @author: 
        '''
        self.conexion.close()
        self.db.close()
        self.raiz = None 
        
    def commiting(self):
        '''
        Realiza una confirmación en la base de datos.
        @return: 
        @author: 
        '''
        self.db._p_changed = True # The object has been changed.
        transaction.commit()
    
class ZopeDB(object):
    
    def __init__(self, zodb):
        self.zodb = zodb
        
    def save(self, lista, clave, objeto):
        '''
            Guarda un objeto en la base de datos.
            @param lista: diccionario de objetos similares.
            @param clave: clave identificadora del objeto en la Base de Datos.
            @param objeto: Objeto que se va a guardar en la Base de Datos.
            @return: 
            @author: 
        '''
        try:
            dictionary = PersistentMapping(self.zodb.raiz[lista])
        except KeyError, AttributeError:
            self.zodb.raiz[lista] = {}
            dictionary = PersistentMapping(self.zodb.raiz[lista])
        try:
            #Existe la clave, lanzar una excepción de objeto con esa clave Existe.
#            raise ObjetoExiste('''El elemento que se trata de ingresar ya existe, probar recuperarlo
#            y modificar su información''')
            objeto = dictionary[clave]
            self.zodb.commiting()
        except KeyError:
            dictionary[clave] = objeto
            self.zodb.raiz[lista] = dictionary
        finally:
            self.zodb.commiting()
            transaction.abort()
            
    def get(self, lista, clave):
        try:
            raiz = self.zodb.raiz[lista]
            objeto = raiz[clave]
        except KeyError:
            raise ObjeNoExiste('El elemento no se encuentra.')
        return objeto
    
    def modify(self, lista, clave, objeto):
        '''
        @param lista: clave identificadora de los elementos que pertenecen a ese Diccionario.
        @param clave: clave identificadora del elemento que se trata de modificar.
        @param objeto: objeto que se trata de modificar en el diccionario.
        '''
        try:
            dictionary = PersistentMapping(self.zodb.raiz[lista])
        except KeyError:
            self.zodb.raiz[lista] = {}
            dictionary = PersistentMapping(self.zodb.raiz[lista])
        try:
            objeto = dictionary[clave]
            self.zodb.commiting()
        except KeyError:
            raise ObjeNoExiste('El elemento no Existe')
        finally:
            self.zodb.commiting()
            transaction.abort()
            
    def getAlls(self, lista):
        try:
            dictionary = self.zodb.raiz[lista]
        except KeyError:
            self.zodb.raiz[lista] = {}
            self.zodb.commiting()
            dictionary = self.zodb.raiz[lista]
            #Lanzar excepcion que dicho diccionario con esa clave no existe.
        return dictionary
    
    def remove(self, lista, clave):
        try:
            raiz = self.zodb.raiz[lista]
            del raiz[clave]
            self.zodb.commiting()
        except KeyError:
            raise ObjeNoExiste('El elemento no se encuentra.')
            
    def cargarTiposDeDocumentos(self):
        from negocio import TipoDocumento
        raiz = self.zodb.raiz
        documentos = {}
        siglas = ['D.N.I', 'C.I','L.E','L.C']
        descripciones = ['Documento Nacional de Identidad', 'Cedula de Identidad',
                         'Libreta de Enrolamiento', 'Libreta civica']
        for i in xrange(len(siglas)):
            tDoc = TipoDocumento.TipoDocumento(siglas[i],descripciones[i])
            documentos[str(tDoc.get_codigo_tipo_documento())] = tDoc
        raiz['tiposDocumentos'] = documentos
        self.zodb._p_changed = True
        transaction.commit()
    
    def addTiposDeDocumentos(self, clave, documento):
        '''
        @param documento: argumento de TipoDeDocumento.
        @param clave: valor de identificación en el diccionario.
        '''
        raiz = self.zodb.raiz
        diccionarioTipoDeDocumentos = raiz['tiposDocumentos']
        diccionarioTipoDeDocumentos[clave] = documento
        self.zodb._p_changed = True
        transaction.commit()
    
    def getTiposDeDocumentos(self):
        try:
            raiz = self.zodb.raiz
            diccinarioTiposDeDocumentos = raiz['tiposDocumentos']
        except KeyError:
            pass
        return diccinarioTiposDeDocumentos

    def getDivisionTransporte(self):
        division = None
        try:
            raiz = self.zodb.raiz
            keys = raiz['divisionTransporte'].keys()
            division = raiz['divisionTransporte'][keys[0]]
        except KeyError:
            #lanzar Excepcion No existe Diccionario de DivisionTransporte
            raiz['divisionTransporte'] = {}
            pass
        return division
    
    def setDivisionTransporte(self, clave, division):
        raiz = self.zodb.raiz
        diccinarioDivisionTransporte = raiz['divisionTransporte']
        diccinarioDivisionTransporte[clave] = division
        self.zodb._p_changed = True
        transaction.commit()