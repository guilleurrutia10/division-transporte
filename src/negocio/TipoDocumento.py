# -*- coding: utf-8 -*-
'''
Created on 28/10/2012

@author: urrutia
'''

from persistent import Persistent

class TipoDocumento(Persistent):
    '''
    classdocs
    @version: 
    @author: 
    '''

    """ ATTRIBUTES
    
    
    
    codigoTipoDocumento  (private)
    
    
    
    descripcion  (private)
    
    """
        
    def __init__(self, codigoTipoDocumento=None, descripcion=None):
        '''
        Constructor
        @return: 
        @author: 
        '''
        self.set_codigo_tipo_documento(codigoTipoDocumento)
        self.set_descripcion(descripcion)
        
    #===========================================================================
    # Tener en cuenta en el Save() de un objeto que, si no existe en la Base de
    # Datos debemos ejecutar el método de ZopeDB Save() sino directamente pedirle
    # a ZopeDB que realize un commit().
    # def save(self):
    #    try:
    #        ZopeDB.save()
    #    except ObjetoExiste:
    #        ZopeDB.commit()
    # De esta manera es posible modificar dinámicamente los objetos, aumentando 
    # sus variables de instancias, así como sus métodos y guardarlos sin 
    # problemas.....
    #===========================================================================
        
    def get_codigo_tipo_documento(self):
        '''
        @return: 
        @author: 
        '''
        return self.__codigoTipoDocumento


    def get_descripcion(self):
        '''
        @return: 
        @author: 
        '''
        return self.__descripcion


    def set_codigo_tipo_documento(self, value):
        '''
        @return: 
        @author: 
        '''
        self.__codigoTipoDocumento = value


    def set_descripcion(self, value):
        '''
        @return: 
        @author: 
        '''
        self.__descripcion = value


    def del_codigo_tipo_documento(self):
        '''
        @return: 
        @author: 
        '''
        del self.__codigoTipoDocumento


    def del_descripcion(self):
        '''
        @return: 
        @author: 
        '''
        del self.__descripcion

    codigoTipoDocumento = property(get_codigo_tipo_documento, set_codigo_tipo_documento, del_codigo_tipo_documento, "codigoTipoDocumento's docstring")
    descripcion = property(get_descripcion, set_descripcion, del_descripcion, "descripcion's docstring")
    
    def __str__(self):
        '''
        @return: 
        @author: 
        '''
        return 'Tipo de Documento: %s, descripción: %s' %(self.get_codigo_tipo_documento(),self.get_descripcion())
    
    def __eq__(self, tipoDocumento):
        '''
        @return: 
        @author: 
        '''
        esCodigo = ( self.get_codigo_tipo_documento() == tipoDocumento.get_codigo_tipo_documento() )
        esDescripcion = ( self.get_descripcion() == tipoDocumento.get_descripcion() )
        return (esCodigo and esDescripcion)