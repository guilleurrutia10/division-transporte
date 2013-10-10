#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
'''
Created on 21/04/2013

@author: urrutia
'''

import os, sys
import glob 
import re, shutil
import argparse
#import filecmp

def buscarFormularios(pathBusqueda, extension):
        os.chdir(pathBusqueda)
        listaDeFormulariosEncontrados = glob.glob('*.' + str(extension))
        return listaDeFormulariosEncontrados

def moverCompilados(pathFuente, pathDestino):
    
    listaCompilados = buscarFormularios(pathFuente, 'py')
    print listaCompilados

    for i in listaCompilados:
#            if cmp(pathFuente + "\\" + str(i), pathDestino + "\\" + str(i), shallow=False) is False:
#            if os.path.getsize(pathFuente + "\\" + str(i)) == os.path.getsize(pathDestino + "\\" + str(i)):
#                if open(pathFuente + "\\" + str(i), 'r').read() == open(pathDestino + "\\" + str(i), 'r').read():
        print 'Copiando'
        shutil.copyfile(pathFuente + '\\' + str(i), pathDestino + '\\' + str(i))
        print 'borrando', pathFuente + '\\' + str(i), '...'
        os.remove(pathFuente + '\\' + str(i))
        
def compilarFormularios(pathFuente, pathDestino):
            
        miPath = pathFuente
        listaDeFormularios = buscarFormularios(miPath, 'ui')
        print listaDeFormularios
        
        ruta = pathDestino
        
        for unFormulario in listaDeFormularios:
            
            print 'compilando', unFormulario, '...'
            
            #removemos la extension .ui...
            nombreDelFormulario = re.split("\.", unFormulario)
            #compilamos el formulario con el comando pyui4...
            
#            ruta = pathDestino
            #===================================================================
            # 
            #===================================================================
            print "Archivo: " , unFormulario
            # os.stat() return the attributes correspond to the file.
            metaDatosFuente = os.stat(unFormulario)
            import time
            # fechaModificacionFuente = st_mtime - time of most recent content modification
            fechaModificacionFuente = time.localtime(metaDatosFuente.st_mtime)
            print "Fecha modificacion: ", fechaModificacionFuente
            
            try:
                archDestino = ruta + "\\" + nombreDelFormulario[0] + ".py"
                print "Archivo: " , archDestino
                metaDatosDestino = os.stat(archDestino)
                fechaModificacionDestino = time.localtime(metaDatosDestino.st_mtime)
                print "Fecha modificacion: ", fechaModificacionDestino
            #===================================================================
            # 
            #===================================================================
                if (fechaModificacionFuente > fechaModificacionDestino):
                    print "Debo compilar de nuevo....."
                    os.system("pyuic4 -x " + unFormulario + " -o " + nombreDelFormulario[0] + ".py")
                #Tener en cuenta que si la fecha del Fuente(.ui) es anterior a la fecha
                #del destino(.py) tampoco debo recompilar....
                else:
                    print "No debo recompilar."
            #WindowsError, No se encuentra el archivo destino... No se compiló nada anteriormente.
            except WindowsError:
                os.system("pyuic4 -x " + unFormulario + " -o " + nombreDelFormulario[0] + ".py")

        try:
            moverCompilados(miPath, ruta)
        except IOError, e:
            print e
            return
            
        os.system("PAUSE")
        
def process_command_line():
    # Instance the parser
    p = argparse.ArgumentParser(description='Compilación de Formularios', conflict_handler='resolve', usage='%(prog)s [options]')
    
    # Options that accepts a string argument
    p.add_argument("-s", '--source', dest="source", help='Directorio fuente', required=True, metavar='fuente')
    p.add_argument("-d", '--dest', dest="dest", help='Directorio destino', required=True, metavar='destino')
    
    # Parser options to return
    args = vars(p.parse_args())
    print args
    return args

if __name__ == "__main__":
    args = process_command_line()
    compilarFormularios(args['source'], args['dest'])
    sys.exit()
