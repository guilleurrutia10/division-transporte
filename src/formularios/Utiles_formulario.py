'''
Created on 28/01/2014

@author: Usuario
'''
from PyQt4 import QtGui

class TablaSuper(QtGui.QTableWidget):
    
    def cargarGrilla(self, lista_empleados):
        fila = 0
        self.clearContents()
        self.setRowCount(len(lista_empleados))
        for empleado in lista_empleados:
            columna = 0
            itemDocumento = QtGui.QTableWidgetItem()
            itemDocumento.setText(unicode(empleado.documento))
            self.setItem(fila, columna, itemDocumento)
            columna += 1
            itemNombre = QtGui.QTableWidgetItem()
            itemNombre.setText(unicode(empleado.nombre))
            self.setItem(fila, columna, itemNombre)
            fila += 1
            
    def cargarGrillaTwo(self, lista_empleados):
        fila = 0
        self.clearContents()
        self.setRowCount(len(lista_empleados))
        for empleado in lista_empleados:
            print empleado.nombreCompleto()
            columna = 0
            infoEmpleado = empleado.getInfo() 
            for clave in infoEmpleado.keys():
                unItem = QtGui.QTableWidgetItem()
                unItem.setText(unicode(infoEmpleado[clave]))
                print infoEmpleado[clave]
                self.setItem(fila, columna, unItem)
                columna += 1
            fila += 1
