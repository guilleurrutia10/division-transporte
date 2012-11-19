# -*- coding: utf-8 -*-
'''
Created on 02/11/2012

@author: alum
'''

PERMISOS = {
    "jefeDivision": ["alta_seccion", "alta_repuesto", "modificar_repuesto"],
    "jefeSeccion": ["finalizar_reparacion", "asiganr_reparacion"],
    "inspector": ["verificar_reparacion"],
    "administrativo": ["alta_repuesto"],
    "otro": []
      
}

USUARIOS = [
    ("guille", "1234", "jefeDivision"),
    ("leo", "1234", "inspector"),
    ("samuel", "1234", "administrativo"),
    ("diego", "1234", "otro")
]

class Usuario():
    def __init__(self, name):
        self.name = name
        self.rol = None
        self.permisos = []
        
    def validar(self, password):
        u = filter(lambda (n, p, r): self.name == n and p == password, USUARIOS)
        if not u:
            return False
        u = u[0]
        self.rol = u[2]
        self.permisos = PERMISOS[u[2]]
        return True
    
    def es_anonimo(self):
        return not self.permisos
    
    def puede(self, permiso):
        return permiso in self.permisos
        
def main():
    username = "diego"
    username = "guille"
    password = "1234"
    usuario = Usuario(username)
    if not usuario.validar(password):
        print "%s nombre o clave incorrecta" % username
    
    if usuario.puede("alta_repuesto"):
        print "puede hacer alta repuesto"    

    if usuario.puede("alta_seccion"):
        print "puede hacer alta seccion"
        
    if usuario.puede("verificar_reparacion"):
        print "puede hacer verificar reparacion"
        
    if usuario.es_anonimo():
        print "es un usuario anonimo"    
    
if __name__ == "__main__":
    main()