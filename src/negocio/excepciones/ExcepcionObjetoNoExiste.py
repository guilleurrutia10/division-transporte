'''
Created on 07/02/2014

@author: urrutia
'''
class ExcepcionObjeNoExiste(Exception):
    
    def __init__(self, message):
        self.message = message