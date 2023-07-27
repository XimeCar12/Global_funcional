#funciones....
from reportlab.pdfgen import canvas
from FuncionQR import *
import datetime
import locale
locale.setlocale(locale.LC_ALL, '')
ruta="C:/Users/Aula 25/Desktop/globalX/"
nombreQR = ruta + "miQR.png"

def generarPDF(listaNombre,listaEdades):
    fecha_actual = datetime.datetime.now()
    nombreArchivo=ruta+"reporteGlobal"+fecha_actual.strftime('%d_%m_%Y_%H_%M_%S')+".pdf"
    generarQR(nombreQR,"hola desde la funcion")
    c= canvas.Canvas(nombreArchivo)
    xInicial =200
    yInicial = 700
    c.drawString(xInicial,yInicial,"Edad")
    c.drawString(xInicial+120,yInicial,"Nombre")

    c.drawImage(nombreQR,200,400,100,100)
    for i in range(len(listaNombre)):
        yInicial = yInicial -20
        c.drawString(xInicial,yInicial,listaEdades[i])
        c.drawString(xInicial+120,yInicial,listaNombre[i])
    c.save()
    print("-------Reporte generado--------")