# -*- coding: utf-8 -*-
'''
Created on 03/11/2012

@author: urrutia
'''

from ZODB import config
import transaction
from persistent.mapping import PersistentMapping

#from MyExceptions import ObjeNoExiste
from Dialogs.negocio.excepciones import ExcepcionObjetoNoExiste
from Dialogs.negocio.Division_Transporte import Division_Transporte
from copy import deepcopy

class MiZODB(object):
    '''
    Clase que representa la ZODB.
    classdocs
    @version: 
    @author: 
    '''

#    def __init__(self, url):
    def __init__(self):
        '''
        Constructor, se conecta al Servidor de la BD a través del archivo de configuracion zeo.conf
        en donde se indica la IP:PORT.
        @return: 
        @author: 
        '''
#        self.url = url
        self.url = 'zeo.conf'
        self.db = config.databaseFromURL(self.url)
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
            self.zodb.open()
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
            self.zodb.close()
            
    def get(self, lista, clave):
        try:
            self.zodb.open()
            raiz = self.zodb.raiz[lista]
            return deepcopy(raiz[clave])
#            objeto = raiz[clave]
        except KeyError:
#            raise ObjeNoExiste('El elemento no se encuentra.')
            raise ExcepcionObjetoNoExiste('El elemento no se encuentra.')
        finally:
            self.zodb.close()
#        return objeto
    
    def modify(self, lista, clave, objeto):
        '''
        @param lista: clave identificadora de los elementos que pertenecen a ese Diccionario.
        @param clave: clave identificadora del elemento que se trata de modificar.
        @param objeto: objeto que se trata de modificar en el diccionario.
        '''
        try:
            self.zodb.open()
            dictionary = PersistentMapping(self.zodb.raiz[lista])
        except KeyError:
            self.zodb.raiz[lista] = {}
            dictionary = PersistentMapping(self.zodb.raiz[lista])
        try:
#            objeto = dictionary[clave]
            dictionary[clave] = objeto
            self.zodb.commiting()
        except KeyError:
#            raise ObjeNoExiste('El elemento no Existe')
            raise ExcepcionObjetoNoExiste('El elemento no Existe')        
        finally:
            self.zodb.commiting()
#            transaction.abort()
            self.zodb.close()
            
    def getAlls2(self, lista):
        try:
            self.zodb.open()
            dictionary = deepcopy(self.zodb.raiz[lista])
        except KeyError:
            self.zodb.raiz[lista] = {}
            self.zodb.commiting()
            dictionary = deepcopy(self.zodb.raiz[lista])
            #Lanzar excepcion que dicho diccionario con esa clave no existe.
        finally:
            self.zodb.close()
        return dictionary

    def getAlls(self, lista):
        self.zodb.open()
        v = self.zodb.raiz[lista]
        self.zodb.close()
        return v
        
    
    def remove(self, lista, clave):
        try:
            self.zodb.open()
            raiz = self.zodb.raiz[lista]
            del raiz[clave]
            self.zodb.raiz[lista] = raiz
            transaction.commit()
            self.zodb.close()
#            self.zodb.commiting()
        except KeyError:
#            raise ObjeNoExiste('El elemento no se encuentra.')
            raise ExcepcionObjetoNoExiste('El elemento no se encuentra.')        
            
    def cargarTiposDeDocumentos(self):
        from Dialogs.negocio import TipoDocumento
        raiz = self.zodb.raiz
        documentos = {}
        siglas = ['D.N.I', 'C.I', 'L.E', 'L.C']
        descripciones = ['Documento Nacional de Identidad', 'Cedula de Identidad',
                         'Libreta de Enrolamiento', 'Libreta civica']
        for i in xrange(len(siglas)):
            tDoc = TipoDocumento.TipoDocumento(siglas[i], descripciones[i])
            documentos[str(tDoc.get_codigo_tipo_documento())] = tDoc
        raiz['tiposDocumentos'] = documentos
        self.zodb._p_changed = True
        transaction.commit()
    
    def cargarUsuarios(self):
         
        raiz = self.zodb.raiz
        import hashlib
        USUARIOS = [("guille", "e96ff3826368162ce83d6aa3aec79ed3b2f99291", "jefeDivision"),
                    ("loco", hashlib.sha1("loco"+"1234").hexdigest(), "jefeDivision"),
                    ("leo", "1234", "inspector"),
                    ("samuel", "e96ff3826368162ce83d6aa3aec79ed3b2f99291", "administrativo"),
                    ("diego", "1234", "otro"),
                    ("pepe1", "7800524dada57a4caf0f1cc37a13a881c3af5e88", "inspector")
                    ]

        raiz['USUARIOS'] = USUARIOS
        self.zodb._p_changed = True
        transaction.commit()

    def cargarDivision(self):
         
        raiz = self.zodb.raiz
        raiz['DIVISION'] = Division_Transporte()
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
        
    def cargarTiposDeReparaciones(self):
        from Dialogs.negocio.TipoDeReparacion import TipoDeReparacion
        raiz = self.zodb.raiz
        diccionario = {'Reacondicionamiento de motor':1,
                       'Afinado de motor':2,
                       'Ensayo de sistema de escape':3,
                       'Reparacion de ejes':4,
                       'Reparacion de frenos':5,
                       'Reparacion del tanque de combustible':6,
                       'Reparacion de radiador': 7}
        tiposReparaciones = {}
        from Dialogs.negocio.TipoRepuesto import TipoRepuesto
        unTipoRepuesto = TipoRepuesto('Bujia', 'Bujia universal')
        from Dialogs.negocio.RepuestoRequeridos import RepuestoRequeridos
        unRepRequerido = RepuestoRequeridos(unTipoRepuesto, 4)
        
        for nombre in diccionario:
            if nombre == 'Reparacion de frenos':
                otroTipoRepuesto = TipoRepuesto('Pastilla de Freno', 'Siempre frena p77')
                otroRepRequerido = RepuestoRequeridos(otroTipoRepuesto, 4)
                tRep = TipoDeReparacion(nombre, diccionario[nombre], [unRepRequerido, otroRepRequerido])
                print 'cargue rep frenos'
            elif nombre == 'Reparacion de radiador':
                otroTipoRepuesto = TipoRepuesto('Radiador', 'RAD ULTRA 7500')
                otroRepRequerido = RepuestoRequeridos(otroTipoRepuesto, 4)
                tRep = TipoDeReparacion(nombre, diccionario[nombre], [unRepRequerido, otroRepRequerido])
                print 'cargue Reparacion de radiador'
            else:
                tRep = TipoDeReparacion(nombre, diccionario[nombre], [unRepRequerido])
                print 'cargue Reparacion Normal'
                
            tiposReparaciones[nombre] = tRep
        
        raiz['tiposReparaciones'] = tiposReparaciones
        self.zodb._p_changed = True
        transaction.commit()

    def cargarTiposDeRepuestos(self):
        from Dialogs.negocio.TipoRepuesto import TipoRepuesto
        
        raiz = self.zodb.raiz
        infoRepuestos = [('1001', 'Bujia Universal 2', 'Bujia Universal Mejorada'),
                         ('1002', 'Neumatico Universales', 'Neumaticos Universales con el mejor agarre'),
                         ('1003', 'Llanta Universal 2', 'Llanta mas linda'),
                         ('1004', 'Espejo Universal', 'Espejos retovision maxima'),
                         ('1005', 'Tubo de Escape Universal', 'Tubo super'),
                         ('1006', 'Amortiguador Universal 2', 'Amortiguador'),
                         ('1007', 'Embrague 7000', 'Embragues Universal 2'),
                         ('1008', 'Correas 4900', 'Correa Universal 2'),
                         ('1009', 'Volante Super2', 'Volante Universal 2'),
                         ('1010', 'Freno de mano F2', 'Freno de mano Universal 2'),
                         ('1011', 'Filtros Fil7657', 'Filtros Universal 2'),
                         ('1012', 'Silenciador 409', 'Silenciadores Universal 2'),
                         ('1013', 'Pastillas de freno r700', 'Pastillas de freno Universal 2'),
                         ('1014', 'Bomba de agua 298', 'Bomba de agua Universal'),
                         ('1015', 'Aceite LubriMax', 'Aceite LubriMax Universal 2'),
                         ('1016', 'Anticongelante AntiMax2', 'Anticongelante Universal Mejorada'),
                         ('1017', 'Faro WQ200', 'Faro Universal Mejorada')
                         ]

        tiposRepuestos = {}
        for codigo, nombre, descripcion in infoRepuestos:
            tRepuesto = TipoRepuesto(codigo, nombre, descripcion)
            tiposRepuestos[codigo] = tRepuesto
        
        raiz['tiposRepuestos'] = tiposRepuestos
        self.zodb._p_changed = True
        transaction.commit()
        print "Tipos de Repuestos cargados con exito!"
