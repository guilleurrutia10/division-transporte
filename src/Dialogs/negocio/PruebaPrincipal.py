'''
Created on 13/07/2014

@author: LeoMorales
'''
from Seccion import Seccion
from Legajo import Legajo
from TipoDeReparacion import TipoDeReparacion
from Reparacion import Reparacion
from Turno import Turno
from DetallePlan import DetallePlan
from Empleado import Empleado

if __name__ == '__main__':
    empleado1 = Empleado(nombre = 'Juan', apellido = 'Perez', documento = 180111222, tipoDocumento = 'DNI', fechaNacimiento = None, domicilio = None, telefono = None, email = None, localidad = None)
    
    codigoSeccion, nombre, empleados, encargado = '1111', 'Seccion1', [empleado1],[]
    seccion1 = Seccion(codigoSeccion, nombre, empleados, encargado)
    
    print 'Seccion tiene registro?', seccion1.tieneRegistroParaElDia('10/10/2014')
    
    #Alta de vehiculo:
    dominio, marca, registroInterno, numeroChasis, comisaria = 'ERR333', 'Ford','1111','0001','Primera'
    vehiculo1  = Legajo(dominio, marca, registroInterno, numeroChasis, comisaria)
    
    #Registro de nuevo ingreso:
    kilometrajeActual, combustibleActual, equipamiento, reparacion, comisaria, localidad, fecha = 1000, 20, '-', '-', 'Primera', 'Rw', '9/07/2014'
    seRegistro = vehiculo1.registrarNuevoIngreso(kilometrajeActual, combustibleActual, equipamiento, reparacion, comisaria, localidad, fecha)
    print '\nSe pudo registrar el ingreso: ', seRegistro, '\n', vehiculo1.ordenesDeReparacion, '\n', vehiculo1.obtenerOrdenDeReparacionEnCurso()
    
    #Registramos reparaciones necesarias:
    tipoDeReparacion, descripcion, repuestosUtilizados = TipoDeReparacion('Afinado de motor', 'El afinado de motor consiste en...'), 'Estandar', []
    reparacion1 = Reparacion(tipoDeReparacion, descripcion, repuestosUtilizados)
    vehiculo1.registrarReparaciones([reparacion1])
    seGenero = vehiculo1.generarPedidoDeActuacion()
    print '\nSe pudo registrar reparaciones: ', seGenero, '\n',vehiculo1.obtenerOrdenDeReparacionEnCurso()
    
    #Le indicamos al vehiculo que ya llego su pedido de actuacion:
    seRecepciono = vehiculo1.registrarRecepcionPedidoActuacion('10/10/2014')
    print '\nSe pudo registrar recepcion Pedido: ', seRecepciono, '\n',vehiculo1.obtenerOrdenDeReparacionEnCurso()
    
    #Generamos los turnos, para planificar
    if seccion1.tieneTurnoLibreParaFechaHora('12/10/2014', 8):
        turnes = Turno(seccion1, vehiculo1, '12/10/2014', 8)
        #En este turno, se van a tratar las siguientes reparaciones
        turnes.addDetalle(DetallePlan(reparacion1, '12/10/2014'))
        seccion1.registrarTurno(turnes)
        vehiculo1.agregarTurnoAlPlan(turnes)
        vehiculo1.agregarTurnoAlPlan(turnes)
        finPlanificacion = vehiculo1.planificacionFinalizada()
    
    print '\nSe pudo finalizar la planificacion: ', finPlanificacion, '\n',vehiculo1.obtenerOrdenDeReparacionEnCurso(),'\n', vehiculo1.obtenerOrdenDeReparacionEnCurso().getPlan()

#    #Start Prueba
#    #Formas de recuperar un turno    
#    #turnes_1 = seccion1.getTurnoDeFechaHora('12/10/2014', 8)
#    #turnes_1 = vehiculo1.obtenerOrdenDeReparacionEnCurso().getPlan().getTurnos()[0]
#    turnes_1 = vehiculo1.getTurnosSinAtender()[0]
#    #MArcar el turno como finalizado no significa que la reparacion esta finalizada (puede llevarse a cabo en varios turnos...puede?)
#    turnes_1.finalizar()
#    #Finalizar la reparacion
#    print 'Estado reparacion 1:', turnes_1.getDetalles()[0].getReparacion().estado()
#    #reparacion1.finalizar()
#    turnes_1.finalizarTodasLasReparaciones()
#    print 'Estado reparacion 1:', turnes_1.getDetalles()[0].getReparacion().estado()
#    #End Prueba
    
    #Volviendo al circuito
    print "".join(empleado.quienSos() for empleado in seccion1.getEmpleados())
    turnes_1 = seccion1.getTurnoDeFechaHora('12/10/2014', 8)
    turnes_1.asignarEmpleados([seccion1.getEmpleados()[0]])
    print 'Estado reparacion 1:', turnes_1.getDetalles()[0].getReparacion().estado()
    turnes_1.finalizar()
    turnes_1.finalizarTodasLasReparaciones()
    print 'Estado reparacion 1:', turnes_1.getDetalles()[0].getReparacion().estado()