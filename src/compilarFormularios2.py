#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
'''
Created on 28/09/2012

@author: Usuario
'''
import os, sys
import glob 
import re,shutil

def buscarFormularios(pathBusqueda,extension):
        os.chdir(pathBusqueda)
        listaDeFormulariosEncontrados = glob.glob('*.'+str(extension))
        return listaDeFormulariosEncontrados

def moverCompilados(pathFuente,pathDestino):
                    
        listaCompilados = buscarFormularios(pathFuente, 'py')
        print listaCompilados    
        
        
        for i in listaCompilados:
            shutil.copyfile(pathFuente+'\\'+str(i), pathDestino+'\\'+str(i))
            print 'borrando',pathFuente+'\\'+str(i),'...'
            os.remove(pathFuente+'\\'+str(i))
    
if __name__ == "__main__":
        
        if sys.argv.__len__()<3:
            print "Error de invocacion"
            print "Modo de Uso: <nombreProg> <directorioFuente> <directorioDestino>"
            os.system("PAUSE")
            sys.exit()
            
        miPath = sys.argv[1]
        listaDeFormularios = buscarFormularios(miPath,'ui')
        print listaDeFormularios
        
        for unFormulario in listaDeFormularios:
            
            print 'compilando',unFormulario,'...'
            
            #removemos la extension .ui...
            nombreDelFormulario = re.split("\.", unFormulario)
            #compilamos el formulario con el comando pyui4...
            
            ruta = sys.argv[2]
            
            os.system("pyuic4 -x " + unFormulario + " -o " + nombreDelFormulario[0] + ".py")
                
        
        moverCompilados(miPath, ruta)
        
        os.system("PAUSE")
    