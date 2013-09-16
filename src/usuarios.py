# -*- coding: utf-8 -*-
'''
Created on 02/11/2012

@author: alum
'''
from excepciones.Excepcion_usrInvalido import Excepcion_usrInvalido

PERMISOS = {"jefeDivision": ['actionAlta_de_Vehiculo','actionRegistrar_Ingreso_de_Vehiculo',
                             'actionRegistrar_Egreso','actionModificacion_de_Vehiculo',
                             'actionVerificar_Reparaciones_Necesarias_del_Vehiculo',
                             'actionPlanificar_Reparaciones_de_Vehiculo','actionListado_Vehiculos_de_la_Division_2',
                             'actionListado_de_Reparaciones_Realizadas_a_un_Vehiculos_2',
                             'actionListado_Vehiculos_con_Reparaciones_Planificadas_2',
                             'actionListado_Vehiculos_con_Reparaciones_no_Planificadas_2',
                             'actionListado_Vehiculos_en_Reparacion_por_Seccion',
                             'actionListado_Vehiculos_Reparados_por_Seccion_2',
                             'actionListado_de_Tipos_de_Reparaciones_de_la_Division_2',
                             'actionAlta_de_Personal',
                             'actionBaja_de_Personal',
                             'actionModificacion_de_Personal',
                             'actionCambiar_de_Seccion_a_un_Empleado',
                             'actionCambiar_el_Encargado_de_una_Seccion',
                             'actionRemover_Empleado_de_Seccion',
                             'actionListado_de_Personal_de_la_Division',
                             'actionAlta_de_Repuesto',
                             'actionModificacion_de_Repuesto',
                             'actionRegistrar_Recepcion_de_Pedido_de_Actuacion',
                             'actionListado_de_Repuestos_de_la_Division',
                             'actionAlta_de_Seccion',
                             'actionAsignar_Reparacion',
                             'actionRegistrar_Finalizacion_de_Reparacion',
                             'actionListados_de_Seccion'],
            "jefeSeccion": ["finalizar_reparacion", "asiganr_reparacion"],
            "inspector": ['actionAlta_de_Seccion'],
            "administrativo": ["alta_repuesto"],
            "otro": []
            }

USUARIOS = [
    ("guille", "1234", "jefeDivision"),
    ("leo", "1234", "inspector"),
    ("samuel", "1234", "administrativo"),
    ("diego", "1234", "otro"),
    ("pepe1", "7800524dada57a4caf0f1cc37a13a881c3af5e88", "jefeDivision")
]

ROL = 2

class Usuario():
    def __init__(self, name, password):
        self.name = name
        self.rol = None
        self.permisos = []
        self.validar(password)
        
    def validar(self, password):
        """
        Valida si la contrasena ingresada pertenece al usuario.
        Ademas carga al usuario el rol y los permisos que posee. 
        """
        usrs = filter(lambda (n, p, r): self.name == n and p == password, USUARIOS)
        if not usrs:
            raise Excepcion_usrInvalido(self.name)
        usr = usrs[0]
        self.rol = usr[ROL] #Cargando rol...
        self.permisos = PERMISOS[usr[ROL]]  #Cargando permisos...
        return True
    
    def es_anonimo(self):
        return not self.permisos
    
    def es_jefeDivision(self):
        return self.rol == 'jefeDivision'
    
    def puede(self, permiso):
        return permiso in self.permisos
    
    def getPermisos(self):
        return self.permisos
        