from ZODB import DB

import transaction

class Local(object):

    """
       
    
    :version:
    :author:
    """

    @classmethod
    def obtenerBD(cls):
        import ZODB.config
        
        #Se conecta al Servidor de la BD a traves del archivo de configuracion zeo.conf
        #en donde se indica la IP:PORT
        db = ZODB.config.databaseFromURL('zeo.conf')
#        db = ZODB.config.databaseFromURL('C:\Transporte\Proyecto_Division_Transporte\zeo.conf')
        
        return db
            
    @classmethod
    def obtenerUsuarios(cls):
        db = Local.obtenerBD()
        conn = db.open()
        root = conn.root()
        
        usuario = root['usuarios']
        
        l = []
        for i in usuario:
            l.append(usuario[i])
            
        connection = db.close()
        root = connection
        return l
    
    @classmethod
    def cargarUsuarios(cls):
        db = Local.obtenerBD()
        conn = db.open()
        root = conn.root()
        
        try:
            usuario = root['usuarios']
            usuario['guille'] = ['Guillermo']
            root['usuarios'] = usuario
            transaction.commit()
            transaction.abort()
        except KeyError:
            root['usuarios'] = {'jefe':'Jefe de Division','administrativo':'Empleado Administrativo'}
            transaction.commit()
            transaction.abort()
            
        connection = db.close()
        root = connection
        
    @classmethod
    def cargarEmpleado(cls, objeto, valor):
        db = Local.obtenerBD()
        conn = db.open()
        root = conn.root()
        try:
            colEmpleados = root['empleados']
            colEmpleados[valor] = objeto
            
            root['empleados'] = colEmpleados
            transaction.commit()
            transaction.abort()
        except KeyError:
            root['empleados'] = {valor:objeto}
            transaction.commit()
            transaction.abort()
            
        connection = db.close()
        root = connection
        
    
    @classmethod
    def mostrarEmpleado(cls, valor):
        # Connect to your ZEO server
        db = Local.obtenerBD()
        conn = db.open()
        root = conn.root()
        
#        from negocio.Empleado import Empleado
#        empleados = [n is Empleado for n in root]
        colEmpleados = root['empleados']
        empleados = None
        
        try:
            empleados = colEmpleados[valor]
        except KeyError:
            print 'El empleado con documento %s no existe' %valor
        
        connection = db.close()
        root = connection
        
        return empleados
    
    @classmethod
    def mostrarEmpleados(cls):
        db = Local.obtenerBD()
        conn = db.open()
        root = conn.root()
        
#        from negocio.Empleado import Empleado
#        empleados = [n is Empleado for n in root]
#        empleados = []
#        l = root.keys()
#        for l in root:
#            if isinstance(root[l], Empleado) :
#                empleados.append(root[l])
        empleados = []
        try:
            colEmpleados = root['empleados']
            for i in colEmpleados:
                empleados.append(colEmpleados[i])
        except KeyError:
            root['empleados'] = {}
            transaction.commit()
            transaction.abort()
            
        connection = db.close()
        root = connection
        
        return empleados