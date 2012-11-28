# -*- coding: utf-8 -*-
'''
Created on 28/11/2012

@author: urrutia
'''
import unittest


class Test(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def testNombreLocalidad(self):
        pass
    
    def tearDown(self):
        unittest.TestCase.tearDown(self)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testNombreLocalidad']
    unittest.main()