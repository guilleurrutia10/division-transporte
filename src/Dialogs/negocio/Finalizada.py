# -*- coding: utf-8 -*-
'''
Created on 28/11/2012

@author: alum
'''

class Finalizada(object):
    '''
    classdocs
    @version: 
    @author: 
    '''


    def __init__(self, ordenReparacion):
        '''
        Constructor
        @return: 
        @author: 
        '''
        super(Finalizada, self).__init__(ordenReparacion)
        
    def __str__(self):
        return 'Finalizada'
    
    def noEstoyFinalizada(self):
        return False