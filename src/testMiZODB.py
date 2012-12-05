# -*- coding: utf-8 -*-
'''
Created on 11/11/2012

@author: urrutia
'''
import unittest
from numpy.ma.testutils import assert_equal, assert_not_equal

from MiZODB import ZopeDB, MiZODB
from negocio import TipoDocumento, Division_Transporte, Legajo
from MyExceptions import ObjeNoExiste

class Test(unittest.TestCase):
    
    def setUp(self):
        '''
            Prepara el entorno en el cual se ejecutan los TestCase.
        '''
        print 'Preparando el contexto'
        self.diccionarios = ['tiposDocumentos', 'divisionTrasnporte']
        self.CodigosDocumentos = ['D.N.I', 'L.C', 'N.N', 'N..', 'L.E']
        self.DescripcionesDocumentos = ['Documento Nacional de Identidad', 'Libreta Civica', 'Natalia Natalia', 'No, No', 'Libreta de Enrolamiento']
        self.bd = ZopeDB(MiZODB())
#        self.bd = ZopeDB(MiZODB('zeo.conf'))
        
    def testSave(self):
        '''
            Se prueba el método save() del módulo MiZODB, de la Clase MiZODB que guarda un objeto en un diccionario
            con un determinado nombre.
        '''
        documento1 = TipoDocumento.TipoDocumento(self.CodigosDocumentos[0], self.DescripcionesDocumentos[0])
        self.bd.save(self.diccionarios[0], documento1.get_codigo_tipo_documento(), documento1)
        documento2 = self.bd.get(self.diccionarios[0], documento1.get_codigo_tipo_documento())
        assert_equal(documento1, documento2, ''''Los elementos no son iguales, documento1: %s
        documento2: %s''' % (documento1, documento2))
    
    def testSaveAgregandoVariosTiposDocumentos(self):
        '''
            Se prueba el método save del módulo MiZODB, de la Clase MiZODB
            agregando varios tipos de documento utilizandolo como un add....
        '''
        documento1 = TipoDocumento.TipoDocumento(self.CodigosDocumentos[2], self.DescripcionesDocumentos[2])
        self.bd.save(self.CodigosDocumentos[0], documento1.get_codigo_tipo_documento(), documento1)
        documento2 = self.bd.get(self.CodigosDocumentos[0], documento1.get_codigo_tipo_documento())
        self.bd.zodb.close()
        
        self.bd.zodb.open()
        documento1 = TipoDocumento.TipoDocumento(self.CodigosDocumentos[0], self.DescripcionesDocumentos[0])
        self.bd.save(self.CodigosDocumentos[0], documento1.get_codigo_tipo_documento(), documento1)
        documento2 = self.bd.get(self.CodigosDocumentos[0], documento1.get_codigo_tipo_documento())
        assert_equal(documento1, documento2, ''''Los elementos no son iguales, documento1: %s
        documento2: %s''' % (documento1, documento2))
        self.bd.zodb.close()
        
        self.bd.zodb.open()
        documento1 = TipoDocumento.TipoDocumento(self.CodigosDocumentos[1], self.DescripcionesDocumentos[1])
        self.bd.save(self.CodigosDocumentos[0], documento1.get_codigo_tipo_documento(), documento1)
        documento2 = self.bd.get(self.CodigosDocumentos[0], documento1.get_codigo_tipo_documento())
        assert_equal(documento1, documento2, ''''Los elementos no son iguales, documento1: %s
        documento2: %s''' % (documento1, documento2))
        
#    def testSaving(self):
#        '''
#            Se prueba el método save del módulo MiZODB, de la Clase MiZODB
#            agregando varios tipos de documento utilizandolo como un add....
#        '''
#        for tipoDocumento in self.CodigosDocumentos:
#            documento1 = TipoDocumento.TipoDocumento(self.CodigosDocumentos[2],self.DescripcionesDocumentos[2])
#            self.bd.save(self.CodigosDocumentos[0], documento1.get_codigo_tipo_documento(), documento1)
#            documento2 = self.bd.get(self.CodigosDocumentos[0],documento1.get_codigo_tipo_documento())
#            assert_equal(documento1, documento2, ''''Los elementos no son iguales, documento1: %s documento2: %s'''%(documento1,documento2))
#            self.bd.zodb.close()
#            self.bd.zodb.open()
        
    def testGetOk(self):
        '''
            Se prueba obtener un objeto.
        '''
        documento1 = TipoDocumento.TipoDocumento(self.CodigosDocumentos[0], self.DescripcionesDocumentos[0])
        #En este caso se supone que el Tipo de Documento existe en la BD.
        documento2 = self.bd.get(self.diccionarios[0], documento1.get_codigo_tipo_documento())
        assert_equal(documento1, documento2, ''''Los elementos no son iguales, documento1: %s
        documento2: %s''' % (documento1, documento2))
        for var, value in vars(documento2).iteritems():
            print var, ':', value

    def testGetFail(self):
        '''
            Se prueba obtener un objeto que no existe.
        '''
        try:
            documento = self.bd.get(self.diccionarios[0], self.DescripcionesDocumentos[3])
        except ObjeNoExiste, e:
            documento = None
            print e.message
        assert documento is None
        
    def testModifyOK(self):
        '''
            Se prueba recuperar un objeto y tratar de modificar su información.
        '''
        try:
            documento1 = self.bd.get(self.diccionarios[0], self.CodigosDocumentos[2])
        except ObjeNoExiste:
            return
        documento2 = TipoDocumento.TipoDocumento(self.CodigosDocumentos[2], self.DescripcionesDocumentos[3])
        self.bd.modify(self.diccionarios[0], self.CodigosDocumentos[2], documento2)
        assert_equal(documento1, documento2, ''''Los elementos no son iguales, documento1: %s
        documento2: %s''' % (documento1, documento2))

    def testModifyFail(self):
        '''
            Se prueba recuperar un objeto y tratar de modificar su información.
        '''
        documento2 = TipoDocumento.TipoDocumento(self.DescripcionesDocumentos[2], self.DescripcionesDocumentos[3])
        try:
            self.bd.modify(self.diccionarios[0], self.CodigosDocumentos[3], documento2)
            doc = self.bd.get(self.diccionarios[0], self.CodigosDocumentos[4])
        except ObjeNoExiste, e:
            doc = None
            print e.message
        assert doc is None
        
    def testGetAlls(self):
        '''
            Se prueba recuperar un diccionario con los objetos pertenecietes a una 
            clase determinada.
        '''
        dictionaryTipoDocumentos = self.bd.getAlls(self.diccionarios[0])
        assert not (dictionaryTipoDocumentos is None)
        for tipoDocumento in dictionaryTipoDocumentos:
            print dictionaryTipoDocumentos[tipoDocumento]
            
    def testSaveDivisionTransporte(self):
        '''
            Probando para guardar en la bd el caso especial de la Division Transporte.
        '''
        division1 = Division_Transporte.Division_Transporte()
        self.bd.save(self.diccionarios[1], division1.id, division1)
        try:
            division2 = self.bd.get(self.diccionarios[1], division1.id)
        except ObjeNoExiste, e:
            division2 = None
            print e.message
        assert not(division2 is None)
        assert_equal(division1.id, division2.id, 'Los elementos no son iguales.')
        division1.tiposDeDocumentos = self.bd.getAlls(self.diccionarios[0])
        self.bd.save(self.diccionarios[1], division1.id, division1)
        try:
            division2 = self.bd.get(self.diccionarios[1], division1.id)
        except ObjeNoExiste, e:
            division2 = None
            print e.message
        print 'Imprimiendo tipos de Documentos de la Division'
        for tipoDocumento in division2.tiposDeDocumentos:
            print tipoDocumento
        assert not(division2 is None)
        assert_equal(division1.id, division2.id, 'Los elementos no son iguales.')
        
    def testSave1(self):
        documento1 = TipoDocumento.TipoDocumento(self.CodigosDocumentos[3], self.DescripcionesDocumentos[3])
        self.bd.save(self.diccionarios[0], documento1.get_codigo_tipo_documento(), documento1)
        documento2 = self.bd.get(self.diccionarios[0], documento1.get_codigo_tipo_documento())
        assert_not_equal(documento1, documento2, ''''Los elementos no son iguales, documento1: %s
        documento2: %s''' % (documento1, documento2))
        print documento2
        print '*' * 50
        documento2.set_descripcion('Nill')
        self.bd.save(self.diccionarios[0], documento2.get_codigo_tipo_documento(), documento2)
        print documento2
        print '*' * 50
        documento3 = self.bd.get(self.diccionarios[0], documento1.get_codigo_tipo_documento())
        assert_equal(documento2, documento3, '''Los elementos no son iguales, documento1: %s
        documento2: %s''' % (documento1, documento2))
        print documento2
        print '*' * 50
        
    def testSaveBien(self):
        vehiculo = Legajo.Legajo('123', 'Renault', '1', '2')
        vehiculo.save()
        vehiculo2 = self.bd.get('vehiculos', '123')
        assert_equal(vehiculo, vehiculo2, 'ERROR!!!!')
        
    def tearDown(self):
        '''
            Destruye el entorno en el cual se ejecutan los TestCase.
        '''
        print 'Destruyendo el Contexto'
        del self.CodigosDocumentos
        del self.DescripcionesDocumentos
        del self.diccionarios
        self.bd.zodb.close()
        del self.bd
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSave']
    unittest.main()
