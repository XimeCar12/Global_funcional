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


    c.setFont('Helvetica-Bold', 26)
    c.drawString(200,780,"MUSA nail's")

    c.setFont('Helvetica-Bold', 16)
    c.drawString(40,750, "Cliente:")
    c.drawString(180,750, listaClientes[pos])
    c.drawString(40,730, "Fecha:")
    c.drawString(180,730,fecha_actual.strftime('%d/%m/%Y %H:%M:%S'))

    c.drawString(250,660, "Productos")

    x = 0
    y = A4[1]- 190
    c.line(x, y, x + 880, y)

    c.drawString(30,630, "Producto: ")
    c.drawString(30,600,listaProductos[pos])
    c.drawString(180,630, "Servicio: ")
    c.drawString(120,600, listaServicios[pos])
    c.drawString(400,630, "Combo: ")
    c.drawString(350,600, listaCombos[pos])



    x = 0
    y = A4[1] -220
    c.line(x,y,x+800,y)

    # QR
    informacion = f"Gracias por tu compra, Si sigues con nosotros puedes llevarte un premio e incluso obtener un premio"
    img = qrcode.make(informacion)
    nombreImagen = ruta + "miQR.png"
    img.save(nombreImagen)



    c.drawImage(nombreQR,220,100,100,100)
    c.drawString(100,50, "Escanea el QR para asi poder obtener algun premio")

    c.save()
    print("-------Reporte generado--------")