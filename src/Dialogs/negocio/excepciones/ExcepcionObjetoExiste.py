# -*- coding: utf-8 -*-
'''
Created on 12/11/2012

@author: urrutia
'''


class ExcepcionObjetoExiste(Exception):
    
    def __init__(self, message):
        self.message = message