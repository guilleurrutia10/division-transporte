'''
Created on 13/10/2012

@author: urrutia
'''


from ZODB.FileStorage import FileStorage
from ZODB.DB import DB

storage = FileStorage('Data.fs')    #donde almacenar
db = DB(storage)                    #BD
connection = db.open()              #conexion
root = connection.root()            #ruta, raiz de la BD

from negocio.Empleado import Empleado
#empleados = [n == Empleado for n in root]

import transaction

root['2'] = Empleado("Guille","Urrutia")
root['3'] = Empleado("Pepe", "kaka")
transaction.commit()
transaction.abort()

lista = []
l = root.keys()
for l in root:
    if isinstance(root[l], Empleado) :
        lista.append(root[l])

print "Tamanio de Lista empleados: ", lista.__len__()        
for i in lista:
    print i.apellido
    
print root['2'].nombre

connection = db.close()
root = connection
storage.close()