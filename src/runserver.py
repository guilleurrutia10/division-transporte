'''
Created on 04/11/2013

@author: Usuario
'''
from os import system

def main():
    command = "python C:\Python27\Lib\site-packages\ZODB3-3.10.5-py2.7-win32.egg\ZEO\\runzeo.py -f C:\BaseZope\Data.fs -a localhost:9999"
    system(command)


if __name__ == '__main__':
    main()