'''
Created on 11/02/2014

@author: LeoMorales
'''
from MiZODB import ZopeDB, MiZODB
from pprint import pprint

if __name__ == '__main__':

    
    bd = ZopeDB(MiZODB())
    bd.cargarUsuarios()
    #bd.cargarDivision()
    bd.zodb.close()
    
    bd.zodb.open()
    usrs = bd.getAlls('USUARIOS')
    pprint(usrs)
    #pprint(bd.getAlls('DIVISION'))
    bd.zodb.close()

        