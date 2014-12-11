# -*- coding: utf-8 -*-
'''
Created on 2/8/2014

@author: urrutia
'''

from reportlab.platypus import BaseDocTemplate, Frame, Paragraph,\
    PageTemplate, Table, PageBreak, Spacer
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

from datetime import datetime, date, timedelta as td
from Utiles_Dialogo import compara_fechas_en_cadenas

styles = getSampleStyleSheet()
Elements = []
width, height = A4

from negocio.Division_Transporte import Division_Transporte

import time
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image
from reportlab.lib.styles import ParagraphStyle
import os


def footer(canvas, doc):
    '''
        La función es llamada luego  de cargar los elementos en la página.
    '''
    canvas.saveState()
    canvas.setFont('Courier', 10)
    print width
    # Número de Página a la derecha
    canvas.drawString(inch, 0.75 * inch, "Page %d" % doc.page)
    # Número de Página a la izquierda
    canvas.drawString(width - (width/5), 0.75 * inch, "Page %d" % doc.page)
    canvas.restoreState()


def header(canvas, doc):
    '''
        La función es llamada antes de cargar los elementos en la página.
    '''
    canvas.saveState()
    canvas.setFont('Courier', 20)
#     canvas.drawCentredString(4*inch, height-50, 'header')
    canvas.setFont('Courier', 10)
    date = datetime.now()
    dateString = '%s/%s/%s' % (date.day, date.month, date.year)
    canvas.drawString(7.*inch, height-20, dateString)
    canvas.drawString(inch/2, height - 20, 'División Transporte')
    canvas.restoreState()


def headerOrdenReparacion(canvas, doc):
    '''
        La función es llamada antes de cargar los elementos en la página.
    '''
    header(canvas, doc)
    canvas.saveState()
    canvas.setFont('Courier', 10)
    canvas.drawInlineImage('logoDivisionTransporte.png', inch, height-70,
                           width=40, height=40)
    canvas.restoreState()


def imprimirOrdenDeReparacion():
    doc = BaseDocTemplate('mi_basedoc1.pdf', showBoundary=1)
    # normal frame as for SimpleFlowDocument
    frameT = Frame(doc.leftMargin, doc.bottomMargin,
                   doc.width, doc.height, id='normal')
    # Two Columns
#    frame1 = Frame(doc.leftMargin, doc.bottomMargin,
#     doc.width/2-6, doc.height, id='col1')
    now = datetime.now()
    fechaEntrada = '%s/%s/%s' % (now.day, now.month, now.year)
    modelo = 'Renault'
    kilometros = 100000
    equipamiento = 'Está equipado con coasa....'
    heading = [[Paragraph('Fecha de Entrada %s' % fechaEntrada,
                style=styles['Heading4']),
                '',
                Paragraph('R.I N°: %s' % 123, style=styles["Heading4"]),
                Paragraph('Modelo %s' % modelo, style=styles["Heading4"]),
                Paragraph('Kilometros %s' % kilometros,
                style=styles["Heading4"])]]
#     data = [['1', 'aaa111', 'Renault', '123', '2314', 'Alguna'],
#             ['2', 'aaa222', 'Renault', '123', '2314', 'Alguna']] * 30
    asignadoCon = 'ASIGNADO A: %s' % 'Pepe Pepito'
    equipadoCon = 'EQUIPADO CON: %s' % equipamiento * 4
    reparacionSolicitada = 'REPARACIÓN SOLICITADA: %s' % 'Gomassss'
    data = [
            [Paragraph(asignadoCon, style=styles['Normal'])],
            [Paragraph(equipadoCon, style=styles['Normal'])] * 2, [''], [''],
            [Paragraph(reparacionSolicitada, style=styles['Normal'])],
            [Paragraph('CANT', style=styles['Normal']),
             Paragraph('REPUESTOS COLOCADOS', style=styles['Normal']),
             [''],
             Paragraph('DETALLE DEL TRABAJO REALIZADO', style=styles['Normal'])
             ],
            ['', '', '', ''],
            ['', '', '', ''],
            ['', '', '', '']
            ]
    heading.extend(data)
    # (col, row)
#     table = Table(heading, colWidths=1.2*inch,
#                   style=[('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
#                          ('SPAN', (0, 0), (1, 0)),
#                          ('SPAN', (0, 1), (-1, 1)),
#                          ('SPAN', (0, 2), (-1, 2)),
#                          ('SPAN', (0, 3), (-1, 3)),
#                          ('SPAN', (0, 4), (-1, 4)),
#                          ('SPAN', (0, 5), (-1, 5)),
#                          ('SPAN', (0, 6), (-1, 6))])
    table = Table(heading, colWidths=1.2*inch,
              style=[('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
                     ('SPAN', (0, 0), (1, 0)),
                     ('SPAN', (0, 1), (-1, 1)),
                     ('SPAN', (0, 2), (-1, 2)),
                     ('SPAN', (0, 3), (-1, 3)),
                     ('SPAN', (0, 4), (-1, 4)),
                     ('SPAN', (0, 5), (-1, 5)),
                     ('SPAN', (1, 6), (2, 6)),
                     ('SPAN', (3, 6), (-1, 6)),
                     ('SPAN', (1, 7), (2, 7)),
                     ('SPAN', (3, 7), (-1, 7)),
                     ('SPAN', (1, 8), (2, 8)),
                     ('SPAN', (3, 8), (-1, 8)),
                     ('SPAN', (1, 9), (2, 9)),
                     ('SPAN', (3, 9), (-1, 9)),
                     ])
#     Elements.append(Paragraph('Listado de Vehículos', style=styles['Title']))
    tabla = Paragraph('Orden de Reparación N°: %s' % (00001), style=styles['Heading4'])
    space = Spacer(inch, 0.1*inch)
    Elements.append(tabla)
    Elements.append(space)
    Elements.append(table)
    Elements.append(PageBreak())
#     Elements.append(NextPageTemplate('OneCol'))
    doc.addPageTemplates([PageTemplate(frames=frameT,
                                       onPage=headerOrdenReparacion,
                                       pagesize=A4, onPageEnd=footer)])
    # start the construction of the pdf
    doc.build(Elements)


# def imprimir(tabla, header, footer):
# - header: que se debe imprimir en la cabecera
# - footer: que se debe imprimir en el pie
def imprimir(Elements, filename):
    filename = filename + '.pdf'
    doc = BaseDocTemplate(filename, showBoundary=1)
    # normal frame as for SimpleFlowDocument
    frameT = Frame(doc.leftMargin, doc.bottomMargin,
                   doc.width, doc.height, id='normal')
    doc.addPageTemplates([PageTemplate(frames=frameT, onPage=header,
                                       pagesize=A4, onPageEnd=footer)])
    # Construye el pdf
    doc.build(Elements)


def imprimirListadoVehiculos(cabecera, vehiculos, titulo='Listado de Vehículos',
                             filename='example.pdf'):
    '''
    TODO: Se pueden armar Templates para diferentes vistas...

    Arma tabla de Flowables datos vehículos.
    @params:
        - cabecera:
        - vehiculos: lista de vehiculos a listar.
        - titulo: nombre del título para el listado.
        - filename: nombre del archivo a generar.
    '''
    heading = []
    # Se Arma la cabecera del Listado de Vehiculos.
    for c in cabecera:
        heading.append([Paragraph(c, style=styles['Heading4'])])

    data = []
    # Se Arma los datos de los vehiculos del Listado de Vehiculos.
    for v in vehiculos:
        data.append([vehiculos.index(v),
                     v.getDominio(),
                     v.getMarca(),
                     v.getRegistroInterno(),
                     v.getNumeroChasis(),
                     v.getComisaria()
                     ])

    # Se arma el título del listado.
    title = Paragraph(titulo, style=styles['Title'])
    datos_tabla = []
    datos_tabla.append(heading)
    datos_tabla.extend(data)
    table = Table(datos_tabla, colWidths=inch,
                  style=[('GRID', (0, 0), (-1, -1), 0.5, colors.grey)])
    Elements = []
    Elements.append(title)
    Elements.append(table)
#     Elements.append(PageBreak())
    imprimir(Elements, filename)


def imprimirOrden(ordenReparacion, titulo='Listado de Vehículos',
                  filename='example.pdf'):
    '''
    TODO: Se pueden armar Templates para diferentes vistas...

    Arma tabla de Flowables datos vehículos.
    @params:
        - ordenReparacion: lista con los datos para conformar reporte de
        una Orden de Reparación.
        - titulo: nombre del título para el listado.
        - filename: nombre del archivo a generar.
    '''
    # Se arma el título del listado.
    title = Paragraph(titulo, style=styles['Heading4'])
    fechaDeEntrada = 'Fecha de Entrada %s' % ordenReparacion[0]
    registroInterno = u'R.I N°: %s' % ordenReparacion[1]
    modelo = 'Modelo %s' % ordenReparacion[2]
    kilometros = 'Kilometros %s' % ordenReparacion[3]
    heading = [[Paragraph(fechaDeEntrada, style=styles['Heading4'])],
               [Paragraph(registroInterno, style=styles["Heading4"])],
               [Paragraph(modelo, style=styles["Heading4"])],
               [Paragraph(kilometros, style=styles["Heading4"])]
               ]
    asignadoCon = 'ASIGNADO A: %s' % ordenReparacion[4]
    equipadoCon = 'EQUIPADO CON: %s' % ordenReparacion[5]
    reparacionSolicitada = u'REPARACIÓN SOLICITADA: %s' % ordenReparacion[6]
    data = [[Paragraph(asignadoCon, style=styles['Normal'])],
            [Paragraph(equipadoCon, style=styles['Normal'])],
            [Paragraph(reparacionSolicitada, style=styles['Normal'])]
            ]
    datos_tabla = []
    datos_tabla.append(heading)
    datos_tabla.extend(data)
    table = Table(datos_tabla, colWidths=1.5*inch,
                  style=[('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
                         ('SPAN', (0, 1), (-1, 1)),
                         ('SPAN', (0, 2), (-1, 2)),
                         ('SPAN', (0, 3), (-1, 3))
                         ])
    Elements = []
    Elements.append(title)
    Elements.append(table)
    imprimir(Elements, filename)


def imprimirPedidoDeActuacion(numeroPedido='', repuestosSolicitados='', filename='example.pdf'):
    '''
    TODO: Se pueden armar Templates para diferentes vistas...

    Arma tabla de Flowables datos vehículos.
    @params:

        - filename: nombre del archivo a generar.
    '''
    heading = []
    # Se Arma la cabecera del Listado de Vehiculos.
    heading.append([Paragraph(u'Renglon', style=styles['Heading4'])])
    heading.append([Paragraph(u'Cantidad', style=styles['Heading4'])])
    heading.append([Paragraph(u'DESCRIPCION', style=styles['Heading4'])])
    heading.append('')
    heading.append('')
    heading.append('')

    data = []
    table_style = [('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
                   ('SPAN', (2, 0), (-1, 0))]
    # Se Arma los datos de los vehiculos del Listado de Vehiculos.
    for rep in repuestosSolicitados:
        repuesto = []
        for item in rep:
            repuesto.append([Paragraph(item, style=styles['Normal'])])
        repuesto.append('')
        repuesto.append('')
        repuesto.append('')
        data.append(repuesto)
        i = repuestosSolicitados.index(rep) + 1
        table_style.append(('SPAN', (2, i), (-1, i)))

    # Se arma el título del listado.
    t = 'PEDIDO DE ACTUACION N°: %s' % numeroPedido
    title = Paragraph(t, style=styles['Title'])
    par = 'Atento a las necesidades de esta Sección, División, Área, Solicito\
    a Ud., tenga bien dar curso al siguiente pedido para adquirir los\
    elementos que a continuación se detallan con destino a la División\
    Transporte Dependiente del Área Logística.-'
    relato = Paragraph(par, style=styles['Heading4'])
    datos_tabla = []
    datos_tabla.append(heading)
    datos_tabla.extend(data)
    table = Table(datos_tabla, colWidths=inch,
                  style=table_style)
    Elements = []
    Elements.append(title)
    Elements.append(Spacer(inch, 0.2*inch))
    Elements.append(relato)
    Elements.append(Spacer(inch, 0.2*inch))
    Elements.append(table)
    imprimir(Elements, filename)


def generarHojaDeRuta(un_vehiculo, nombre_hoja_de_ruta):
    '''
    Recibe un vehiculo y genera su hoja de ruta con el nombre nombre_hoja_de_ruta
    '''
    turnos_ordenados = un_vehiculo.getTurnosOrdenados()
#    nombre_hoja_de_ruta = "%s.pdf" % nombre_hoja_de_ruta
    nombre_hoja_de_ruta = "%s.pdf" % nombre_hoja_de_ruta
    elements = []
    titulo = Paragraph("Hoja de Ruta", styles["Title"])
    elements.append(titulo)
    logo = "imagenes/logo_hoja_de_ruta.jpg"
    im = Image(logo, 2*inch, 2*inch)
    elements.append(im)

    styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))

    subtitulo = u"<b>Turnos del vehículo: %s</b>" % un_vehiculo.getDominio()
    elements.append(Paragraph(subtitulo, styles["Center"]))
    elements.append(Spacer(inch, 0.2*inch))
    cabecera_turno = []
    cabecera_turno.append([Paragraph(u'Número', styles['Heading4'])])
    cabecera_turno.append([Paragraph(u'Código', styles['Heading4'])])
    cabecera_turno.append([Paragraph(u'Día', styles['Heading4'])])
    cabecera_turno.append([Paragraph(u'Sección', styles['Heading4'])])
    table_style = [('GRID', (0, 0), (-1, -1), 0.5, colors.grey)]

    titulo_rep = []
    titulo_rep.append([Paragraph(u'Reparaciones:', styles['Heading4'])])
    titulo_rep.append('')
    titulo_rep.append('')
    titulo_rep.append('')
    # cabecera tabla reparaciones, tabla interior en turnos
    cabecera_rep = []
    cabecera_rep.append([Paragraph(u'Código', style=styles['Heading4'])])
    cabecera_rep.append([Paragraph(u'Tipo de reparación', style=styles['Heading4'])])
    cabecera_rep.append([Paragraph(u'Descripción', style=styles['Heading4'])])
    cabecera_rep.append('')
    ingresados = 2
    for nro, cada_turno in turnos_ordenados.iteritems():
        datos_turnos = []
        turnos = []
        datos_tabla = []
        datos_reparaciones = []
        datos_turnos.append([Paragraph(unicode(nro), style=styles['Normal'])])
        codigo = cada_turno.getCodigo()
        datos_turnos.append([Paragraph(unicode(codigo), style=styles['Normal'])])
        dia = '%s a las %dhs.' % (cada_turno.getFecha(), cada_turno.getHora())
        datos_turnos.append([Paragraph(dia, style=styles['Normal'])])
        nombre_seccion = cada_turno.getSeccion().getNombre()
        datos_turnos.append([Paragraph(nombre_seccion, style=styles['Normal'])])
        for reparacion in cada_turno.getDetalles():
            datos_reparaciones.append([Paragraph(reparacion.getCodigo(), style=styles['Normal'])])
            nombre = reparacion.getTipoDeReparacion().getNombre()
            datos_reparaciones.append([Paragraph(nombre, style=styles['Normal'])])
            descripcion = reparacion.getTipoDeReparacion().getDescipcion()
            datos_reparaciones.append([Paragraph(descripcion, style=styles['Normal'])])
            datos_reparaciones.append('')
        turnos.append(datos_turnos)
        turnos.append(titulo_rep)
        turnos.append(cabecera_rep)
        # SPAN Reparaciones:
        table_style.append(('SPAN', (0, ingresados), (-1, ingresados)))
        # SPAN Descripcion
        table_style.append(('SPAN', (2, ingresados+1), (3, ingresados+1)))
        table_style.append(('SPAN', (2, ingresados+2), (3, ingresados+2)))
        turnos.append(datos_reparaciones)
        datos_tabla.append(cabecera_turno)
        datos_tabla.extend(turnos)
        table = Table(datos_tabla, colWidths=1.2*inch, style=table_style)
        elements.append(table)
        elements.append(Spacer(inch, 0.2*inch))
    imprimir(elements, nombre_hoja_de_ruta)


def generarHojaDeRuta2(un_vehiculo, nombre_hoja_de_ruta):
    '''
    Recibe un vehiculo y genera su hoja de ruta con el nombre nombre_hoja_de_ruta
    '''
    turnos_ordenados = un_vehiculo.getTurnosOrdenados()

    nombre_hoja_de_ruta = "%s.pdf" % nombre_hoja_de_ruta
    doc = SimpleDocTemplate(nombre_hoja_de_ruta, pagesize=letter,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=18)
    Story = []
    logo = "imagenes/logo_hoja_de_ruta.jpg"

    formatted_time = time.ctime()

    styles = getSampleStyleSheet()
    title = Paragraph("\t\tHoja de Ruta", styles["Heading1"])
    Story.append(title)
    im = Image(logo, 2*inch, 2*inch)
    Story.append(im)

    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

    # Crear subtitulo Turnos:
    subtitulo = "Turnos del vehiculo: %s" % 'CGI12'
    ptext = '<font size=12>%s</font>' % subtitulo
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))

    # Informacion de los turnos
    for nro, cada_turno in turnos_ordenados.iteritems():

        ptext = '<font size=12>%s</font>' % '- - '*30
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size=12>#%d</font>' % nro
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size=12>%s</font>' % cada_turno.getCodigo()
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size=12>%s</font>' % '- - '*30
        Story.append(Paragraph(ptext, styles["Justify"]))

        ptext = '<font size=12>Dia: %s a las %dhs.</font>' % (cada_turno.getFecha(), cada_turno.getHora())
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size=12>Seccion: %s.</font>' % cada_turno.getSeccion()
        Story.append(Paragraph(ptext, styles["Justify"]))
        ptext = '<font size=12>Reparaciones:</font>'
        Story.append(Paragraph(ptext, styles["Justify"]))
        # Armamos un parrafito por cada reparacion del turno:
        parrafosreparaciones = [Paragraph("    "+textreparacion, styles["Justify"]) for textreparacion in [str(reparacion) for reparacion in cada_turno.getReparaciones()]]
        for parrafo in parrafosreparaciones:
            Story.append(parrafo)
        Story.append(Spacer(1, 12))

    ptext = '<font size=12>Generada: %s</font>' % formatted_time
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))
    doc.build(Story)


def generarAgendaParaUnDia(seccion, dia, folder):
    '''
    dia --> 12/12/2014
    type(dia) --> string

    Recordar que seccion.getAgendaDelDia()
    devuelve un diccionario (OBTree) con la forma:

    {   8:Turno_de_las_8,
        9:Turno_de_las_9,
        ...
        20:Turno_de_las_20

    }

    '''

#     print 'Generando reporte de %s, para el dia %s' % (seccion.getNombre(), dia)
#     print 'El dia %s la seccion posee los suguientes turnos:' % dia
#     for hora, turno in seccion.getAgendaDelDia(dia, si_no_existe_crear_registro=False).iteritems():
#         print hora, '->', turno

    # A partir de aca, generar el reporte...
    if not seccion.tieneRegistroParaElDia(dia):
        print u'La sección %s no posee registro para el día' % (seccion.getNombre())
        return
    elements = []
    titulo = u'Reporte de %s para el día %s' % (seccion.getNombre(), dia)
    elements.append(Paragraph(titulo, style=styles['Title']))
    elements.append(Spacer(inch, 0.2*inch))
    # Nos ubicamos en la carpeta seleccionada para generar el reporte
    os.chdir(folder)
    d, m, a = dia.split('/')
    filename = u'reporte-%s-%s-%s-%s' % (seccion.getNombre(), d, m, a)
    # cabecera tabla turnos
    cabecera = []
    cabecera.append([Paragraph(u'Hora', style=styles['Heading4'])])
    cabecera.append([Paragraph(u'Código', style=styles['Heading4'])])
    cabecera.append([Paragraph(u'Vehículo', style=styles['Heading4'])])
    cabecera.append([Paragraph(u'Sección', style=styles['Heading4'])])
    cabecera.append([Paragraph(u'Fecha', style=styles['Heading4'])])
    table_style = [('GRID', (0, 0), (-1, -1), 0.5, colors.grey)]

    titulo_rep = []
    titulo_rep.append([Paragraph(u'Reparaciones:', style=styles['Heading4'])])
    titulo_rep.append('')
    titulo_rep.append('')
    titulo_rep.append('')
    titulo_rep.append('')
    # cabecera tabla reparaciones, tabla interior en turnos
    cabecera_rep = []
    cabecera_rep.append([Paragraph(u'Código', style=styles['Heading4'])])
    cabecera_rep.append([Paragraph(u'Tipo de reparación', style=styles['Heading4'])])
    cabecera_rep.append('')
    cabecera_rep.append([Paragraph(u'Descripción', style=styles['Heading4'])])
    cabecera_rep.append('')
    # conteo de filas en la tabla
    ingresados = 2
    for hora, turno in seccion.getAgendaDelDia(dia, si_no_existe_crear_registro=False).iteritems():
        datos_tabla = []
        turnos = []
        datos_truno = []
        datos_reparaciones = []
        if not turno:
            continue
        hora_text = unicode(hora)
        datos_truno.append([Paragraph(hora_text, style=styles['Normal'])])
        datos_truno.append([Paragraph(turno.getCodigo(), style=styles['Normal'])])
        vehiculo = unicode(turno.getVehiculo().getDominio())
        datos_truno.append([Paragraph(vehiculo, style=styles['Normal'])])
        seccion = unicode(turno.getSeccion().getNombre())
        datos_truno.append([Paragraph(seccion, style=styles['Normal'])])
        fecha = unicode(turno.getFecha())
        datos_truno.append([Paragraph(fecha, style=styles['Normal'])])
        for reparacion in turno.getDetalles():
            datos_reparaciones.append([Paragraph(reparacion.getCodigo(), style=styles['Normal'])])
            nombre = reparacion.getTipoDeReparacion().getNombre()
            datos_reparaciones.append([Paragraph(nombre, style=styles['Normal'])])
            datos_reparaciones.append('')
            descripcion = reparacion.getTipoDeReparacion().getDescipcion()
            datos_reparaciones.append([Paragraph(descripcion, style=styles['Normal'])])
            datos_reparaciones.append('')
        turnos.append(datos_truno)
        turnos.append(titulo_rep)
        turnos.append(cabecera_rep)
        table_style.append(('SPAN', (0, ingresados), (-1, ingresados)))
        table_style.append(('SPAN', (1, ingresados+1), (2, ingresados+1)))
        table_style.append(('SPAN', (3, ingresados+1), (4, ingresados+1)))
        table_style.append(('SPAN', (1, ingresados+2), (2, ingresados+2)))
        table_style.append(('SPAN', (3, ingresados+2), (4, ingresados+2)))
        turnos.append(datos_reparaciones)
        datos_tabla.append(cabecera)
        datos_tabla.extend(turnos)
        table = Table(datos_tabla, colWidths=inch, style=table_style)
        elements.append(table)
        elements.append(Spacer(inch, 0.2*inch))

    imprimir(elements, filename)
    return filename


def generarAgendaParaRangoDias(seccion, desde, hasta, folder):
    '''
    Las fechas desde y hasta son strings con el siguiente formato:
        - 12/12/2014

    @precondition: hasta > desde
    '''
    print 'Generando reporte de %s, %s hasta %s' % (seccion.getNombre(), desde, hasta)

    # 1) Recuperar todas las agendas de los dias entre desde y hasta:
    diaD, mesD, anioD = [int(termino) for termino in desde.split('/')]
    diaH, mesH, anioH = [int(termino) for termino in hasta.split('/')]
    dateDesde = date(anioD, mesD, diaD)
    dateHasta = date(anioH, mesH, diaH)

    delta = dateHasta - dateDesde

    agenda = {}
    for dia_entre in range(delta.days + 1):
        diaAux = dateDesde + td(days=dia_entre)
        diaAux = "%s/%s/%s" % (diaAux.day,
                               diaAux.month,
                               diaAux.year
                               )
        # Solicitar el turno para el dia aux y guardarlo
        # agenda[diaAux] = 'RecuperarTablaDeTurnosParaElDiaAux%s'%diaAux
        agenda[diaAux] = seccion.getAgendaDelDia(diaAux, si_no_existe_crear_registro=False)

    print agenda
    agenda_ordenada = sorted(agenda.keys(), cmp=compara_fechas_en_cadenas)
    print "DEBUG: AGENDA ORDENADA:"
    print agenda_ordenada
    lista_reportes = []
    for dia in agenda_ordenada:
        print 'El dia %s la seccion posee los suguientes turnos:' % dia
        for hora, turno in agenda[dia].iteritems():
            print hora, '->', turno
        #
        if seccion.tieneRegistroParaElDia(dia):
            reporte = generarAgendaParaUnDia(seccion, dia, folder)
            print reporte
            lista_reportes.append(reporte)
    return lista_reportes

    # A partir de aca, generar el reporte...

if __name__ == '__main__':
#     division = Division_Transporte()
#     vehiculos = division.getVehiculos().values()
#     repuestosSolicitados = [['02', '01', 'Juego de juntas descarbonizacion'],
#                             ['03', '01', 'Juego de botadores'],
#                             ['04', '01', 'Juego de balancines'],
#                             ['05', '01', 'kit de distribucion']]
#     imprimirPedidoDeActuacion('002', repuestosSolicitados=repuestosSolicitados)
    elements = []
    nombre_hoja_de_ruta = "%s.pdf" % 'nombre_hoja_de_ruta'
    titulo = Paragraph("Hoja de Ruta", styles["Title"])
    elements.append(titulo)
    logo = "../imagenes/logo_hoja_de_ruta.jpg"
    im = Image(logo, 2*inch, 2*inch)
    elements.append(im)

    styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
    subtitulo = u"<b>Turnos del vehículo: %s</b>" % 'un_vehiculo'
    elements.append(Paragraph(subtitulo, styles["Center"]))
    imprimir(elements, nombre_hoja_de_ruta)
