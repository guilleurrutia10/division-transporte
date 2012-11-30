# -*- coding: utf-8 -*-
'''
Created on 28/11/2012

@author: urrutia
'''
import unittest

from Localidad import Localidad

class Test(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.localidad =  Localidad('Rawson', 9000)
        
    def testNombreLocalidad(self):
        print self.localidad.getNombre()
        assert self.localidad.getNombre() is 'Rawson'
    
    def tearDown(self):
        unittest.TestCase.tearDown(self)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testNombreLocalidad']
    unittest.main()