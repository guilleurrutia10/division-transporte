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

from datetime import datetime

styles = getSampleStyleSheet()
Elements = []
width, height = A4

from negocio.Division_Transporte import Division_Transporte


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
    canvas.drawString(7.5*inch, height-20, dateString)
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


def imprimirListadoVehiculos1():
    '''
    Armar la cabecera del Listado de Vehiculos...
    Arma tabla de Flowables datos vehículos.
    '''
    doc = BaseDocTemplate('mi_basedoc.pdf', showBoundary=1)
    # normal frame as for SimpleFlowDocument
    frameT = Frame(doc.leftMargin, doc.bottomMargin,
                   doc.width, doc.height, id='normal')
    # Two Columns
#    frame1 = Frame(doc.leftMargin, doc.bottomMargin,
#     doc.width/2-6, doc.height, id='col1')

    heading = [[' ', Paragraph('Dominio', style=styles['Heading4']),
                Paragraph('Marca', style=styles["Heading4"]),
                Paragraph('Registro Interno', style=styles["Heading4"]),
                Paragraph('Número de Chasis', style=styles["Heading4"]),
                Paragraph('Comisaría', style=styles["Heading4"])]]
    data = [['1', 'aaa111', 'Renault', '123', '2314', 'Alguna'],
            ['2', 'aaa222', 'Renault', '123', '2314', 'Alguna']] * 30
    heading.extend(data)
    table = Table(heading, colWidths=inch,
                  style=[('GRID', (0, 0), (-1, -1), 0.5, colors.grey)])
    Elements.append(Paragraph('Listado de Vehículos', style=styles['Title']))
    Elements.append(table)
    Elements.append(PageBreak())
#     Elements.append(NextPageTemplate('OneCol'))
    doc.addPageTemplates([PageTemplate(frames=frameT, onPage=header,
                                       pagesize=A4, onPageEnd=footer)])
    # start the construction of the pdf
    doc.build(Elements)


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
#     Elements.append(PageBreak())
    imprimir(Elements, filename)

if __name__ == '__main__':
    division = Division_Transporte()
    vehiculos = division.getVehiculos().values()
    cabeceraVehiculos = ['',
                         'Dominio',
                         'Marca',
                         'Registro Interno',
                         u'Número de Chasis',
                         u'Comisaría'
                         ]
    imprimirListadoVehiculos(cabeceraVehiculos, vehiculos)
