#funciones....
from reportlab.pdfgen import canvas
from FuncionQR import *
import datetime
import locale
locale.setlocale(locale.LC_ALL, '')
ruta="C:/Users/Aula 25/Desktop/funcional/"

nombreQR = ruta + "miQR.png"

def generarPDF(listaNombre,listaEdades):
    fecha_actual = datetime.datetime.now()
    nombreArchivo=ruta+"reporteGlobal"+fecha_actual.strftime('%d_%m_%Y_%H_%M_%S')+".pdf"
    generarQR(nombreQR,"hola desde la funcion")
    c= canvas.Canvas(nombreArchivo)
    """xInicial =200
    yInicial = 700"""
    c.drawString(200,780,"MUSA nail's")

    c.setFont('Helvetica-Bold', 16)
    c.drawString(40,750, "Cliente:")
    c.drawString(180,750,)
    c.drawString(40,730, "Fecha:")
    c.drawString(180,730,)

    c.drawString(250,660, "Productos")

    x = 0
    y = A4[1]- 190
    c.line(x, y, x + 880, y)

    c.drawImage(nombreQR,200,400,100,100)
    for i in range(len(listaNombre)):
        yInicial = yInicial -20
        c.drawString(xInicial,yInicial,listaEdades[i])
        c.drawString(xInicial+120,yInicial,listaNombre[i])
    c.save()
    print("-------Reporte generado--------")