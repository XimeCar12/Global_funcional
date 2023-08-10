#funciones....
from reportlab.pdfgen import canvas
from FuncionQR import *
from reportlab.lib.pagesizes import A4
from Datosestaticos import *
import datetime
import locale
locale.setlocale(locale.LC_ALL, '')
ruta="C:/Users/Aula 25/Desktop/funcional/"

nombreQR = ruta + "miQR.png"

def generarPDF(pos):
    fecha_actual = datetime.datetime.now()
    nombreArchivo=ruta+"reporteGlobal"+fecha_actual.strftime('%d_%m_%Y_%H_%M_%S')+".pdf"
    generarQR(nombreQR,"hola desde la funcion")
    c= canvas.Canvas(nombreArchivo)

    #now = datetime.now()
    #fecha = now.strftime("%Y_%m_%d %H_%M_%S")

    c.drawString(200,780,"MUSA nail's")

    c.setFont('Helvetica-Bold', 16)
    c.drawString(40,750, "Cliente:")
    c.drawString(180,750, listaClientes[pos])
    c.drawString(40,730, "Fecha:")
    #c.drawString(180,730, fecha )

    c.drawString(250,660, "Productos")

    x = 0
    y = A4[1]- 190
    c.line(x, y, x + 880, y)

    c.drawString(50,630, "Producto: ")
    c.drawString(50,600,listaProductos[pos])
    c.drawString(180,630, "Servicio: ")
    c.drawString(180,600, listaServicios[pos])
    c.drawString(180,630, "Combo: ")
    c.drawString(180,600, listaCombos[pos])
    c.drawString(310,630, "Precio: ")
    c.drawString(490,630, "Total")

    x = 0
    y = A4[1] -220
    c.line(x,y,x+800,y)

   #xInicial =200
    #yInicial = 700
    #c.drawImage(nombreQR,200,400,100,100)
    #for i in range(len(listaNombre)):
        #yInicial = yInicial -20
        #c.drawString(xInicial,yInicial,listaEdades[i])
        #c.drawString(xInicial+120,yInicial,listaNombre[i])
    c.save()
    print("-------Reporte generado--------")