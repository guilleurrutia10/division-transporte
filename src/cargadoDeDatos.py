'''
Created on 22/11/2012

@author: urrutia
'''

from ZODB import config
import transaction
from persistent.mapping import PersistentMapping

from negocio.Empleado import Empleado
from negocio.TipoDocumento import TipoDocumento
from MiZODB import MiZODB, ZopeDB

from MiZODB import MiZODB, ZopeDB

from MiZODB import MiZODB, ZopeDB

if __name__ == '__main__':
    
    bd = ZopeDB(MiZODB('zeo.conf'))
    bd.cargarTiposDeDocumentos()
    bd.cargarTiposDeReparaciones()
    bd.zodb.close()
    
    bd.zodb.open()
    print bd.getAlls('tiposReparaciones')
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