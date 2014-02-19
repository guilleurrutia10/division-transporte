'''
Created on 15/09/2013

@author: Usuario
'''
import unittest
from negocio.usuario import Usuario
from excepciones.Excepcion_usrInvalido import Excepcion_usrInvalido
from usuarios import Usuario
from negocio.excepciones.Excepcion_usrInvalido import Excepcion_usrInvalido
import hashlib

class TestUsuario(unittest.TestCase):
    '''
    Testea la clase Usuario.
    '''


    def setUp(self):
        name = "pepe1"
        password = hashlib.sha1(name + "1234").hexdigest()
        self.usr = Usuario(name, password)   #(sabiendo que pepe existe y que es jefe de division)

    def test_rol_de_usuario(self):
        '''
        Al "crear" un Usuario, lo que verdaderamente se hace es validarlo! ya que el usuario ya fue realmente creado.
        '''
        self.assertTrue(self.usr.es_jefeDivision())
        
    def test_creacion_de_objeto_usuario_no_valido(self):
        '''
        Al intentar validar un Usuariono valido, verificar la excepcion!.
        '''
        self.assertRaises(Excepcion_usrInvalido, Usuario, "cuchungoglui", "1234")
        
    def test_verificacion_de_permisos(self):
        '''
        Verifica si pepe1 puede hacer un alta de vehiculo.
        '''
        self.assertTrue(self.usr.puede("actionAlta_de_Vehiculo"))
