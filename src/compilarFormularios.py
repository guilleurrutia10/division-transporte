# -*- coding: utf-8 -*-
'''
Created on 28/09/2012

@author: Usuario
'''
import os
import glob 
import re,shutil

def buscarFormularios(pathBusqueda,extension):
        os.chdir(pathBusqueda)
        listaDeFormulariosEncontrados = glob.glob('*.'+str(extension))
        return listaDeFormulariosEncontrados

def moverCompilados(pathFuente,pathDestino):
                    
        listaCompilados = buscarFormularios(pathFuente, 'py')
        print listaCompilados    
        
        
        for unFrmCompilado in listaCompilados:
            shutil.copyfile(pathFuente+'\\'+str(unFrmCompilado), pathDestino+str(unFrmCompilado))
            print 'borrando',pathFuente+'\\'+str(unFrmCompilado),'...'
            os.remove(pathFuente+'\\'+str(unFrmCompilado))
    

if __name__ == "__main__":
        
        miPath = "C:\Users\Usuario\workspaceNEW\Proyecto_Division_Transporte\src\ui"
        listaDeFormularios = buscarFormularios(miPath,'ui')
        print listaDeFormularios
        
        for unFormulario in listaDeFormularios:
            print 'compilando',unFormulario,'...'
            #removemos la extension .ui...
            nombreDelFormulario = re.split("\.", unFormulario)
            #compilamos el formulario con el comando pyui4...
            os.system("pyuic4 -x " + unFormulario + " -o " + nombreDelFormulario[0] + ".py")
                
        
        #ruta destino de los formulario .py
        #ruta = "C:\\Users\\Usuario\\Desktop\\Nueva carpeta\\"
        ruta = 'C:\\Users\\Usuario\\workspaceNEW\\Proyecto_Division_Transporte\\src\\formularios\\'
        moverCompilados(miPath, ruta)
        
        os.system("PAUSE")
    