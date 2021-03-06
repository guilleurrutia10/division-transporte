# -*- coding: utf-8 -*-
'''
Created on 22/11/2012

@author: urrutia
'''

from ZODB import config
import transaction
from persistent.mapping import PersistentMapping

from Dialogs.negocio.Empleado import Empleado
from Dialogs.negocio.TipoDocumento import TipoDocumento

from MiZODB import ZopeDB, MiZODB
from pprint import pprint

if __name__ == '__main__':
    
    bd = ZopeDB(MiZODB())
    bd.cargarGestorDeCodigos()
    bd.cargarTiposDeDocumentos()
    bd.cargarTiposDeReparaciones()
    bd.cargarUsuarios()
    bd.cargarTiposDeRepuestos()
    bd.zodb.close()
    
    bd.zodb.open()
    tiposReparaciones = bd.getAlls('tiposReparaciones')
    pprint(tiposReparaciones)
    

    #bd.cargarDivision()
    usrs = bd.getAlls('USUARIOS')
    pprint(usrs)
    #pprint(bd.getAlls('DIVISION'))
    bd.zodb.close()

    
#    bd = config.databaseFromURL('zeo.conf')
#    conexion = bd.open()
#    raiz = conexion.root()
#    
#    tDoc = TipoDocumento('D.N.I','Documento Nacional de Identidad')
#    raiz['D.N.I'] = tDoc
#    bd._p_changed = True
#    transaction.commit()
#    print id(raiz['D.N.I'])
#    
#    empleado = Empleado('Guillermo','Urrutia','34665001',tDoc)
#    raiz[empleado.documento] = empleado
#    del tDoc
#    bd._p_changed = True
#    transaction.commit()
#    
#    print 'TipoDocumento: ', raiz['D.N.I']
#    print 'Empleado: ', raiz[empleado.documento]
#    print id(raiz[empleado.documento].tipoDocumento)
#    
#    del  raiz['D.N.I']
#    bd._p_changed = True
#    transaction.commit()
#    
#    print 'Empleado: ', raiz[empleado.documento]
#    print id(raiz[empleado.documento].tipoDocumento)
#    
#    conexion = bd.close()
#    raiz = conexion

class Clase1(object):

    def __init__(self, valor):
        self.valor = valor
        
def imprime(self):
    print self
            
objeto = Clase1('Hola soy el objeto instanciado de %s' % Clase1)

#En tiempo de Ejecución la instancia del objeto Clase1 adquiere una nueva funcionalidad.
objeto.imprime = imprime
objeto.imprime(objeto.valor)

#objeto2 = Clase1('2')
#objeto2.imprime(objeto2)

nuevaVariableDeInstancia = 2
#En tiempo de Ejecución la instancia del objeto Clase1 adquiere una nueva variable de instancia.
#print objeto.nuevaVariableDeInstancia
objeto.nuevaVariableDeInstancia = nuevaVariableDeInstancia
objeto.imprime(objeto.nuevaVariableDeInstancia)
#    raiz = conexion
