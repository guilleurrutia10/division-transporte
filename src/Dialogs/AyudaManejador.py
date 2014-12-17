# -*- coding: utf-8 -*-
'''
Created on 4/12/2014

@author: urrutia
'''
from PyQt4 import QtCore, QtGui


class AyudaManejador:
    '''
    Objeto que maneja el evento de presionar F1 para los diálogos y Widgets.
    **Interfaz similar para todos aquellos diálogos que deben tener ayuda
    en línea.
    Las demás teclas se manipulan según lo establecido por defecto.
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass

    def keyPressEvent(self, keyEvent):
        """
        Se sobreescribe el método para atrapar el evento de presionar
        alguna tecla.
        Al presionar la tecla F1 se visualizará la ayuda en línea a través
        de un browser.
        """
        # Super para manipular las demás teclas por defecto.
        super(type(self), self).keyPressEvent(keyEvent)
#        print 'Se presiono una tecla'
#         print self.windowTitle()
        # Atrapar el evento de teclear F1
        if keyEvent.key() == QtCore.Qt.Key_F1:
#            print 'Se presiono la tecla F1 en %s' % (self.windowTitle())
            qlanguage = QtCore.QLocale().language()
            #language = QtCore.QLocale.languageToString(qlanguage)
            language = 'Spanish'
            # Para mostrar internacionalización
#            print 'Mostrar ayuda para idioma: %s' % (language)
            path = QtCore.QDir.currentPath()
            urlTranslate = 'file://%s/Tranlate/%s/' % (path, language)
#            print 'URL - Translate:'
#            print urlTranslate
            # Se arma la URL para caragr en el Browser
            urlHelp = 'file:///%s/Help/%s/topics/%s.htm' % (path, language, self.objectName())
            url = QtCore.QUrl(urlHelp)
#            print 'URL - Help:'
#            print url.path()
            # Solicitamos que se abra el Browser con la url indicada
            QtGui.QDesktopServices.openUrl(url)
