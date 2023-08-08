from FuncionesPDF import*
from Datosestaticos import*
listaNombre = []
listaEdades = []
def menu():
    opcion =1
    while(opcion!=0):
        print("1.Registrarme")
        print("2.Cliente existente")
        print("3.Lista de Servicios")
        print("4.Lista de Productos")
        print("5.Lista de Diseños")
        print("6.")
        print("7. Generar PDF")
        print("8. Generar QR")
        print("0. Salir")
        opcion = int(input("Elige una opcion "))
        if(opcion ==1):
            pedirDatos()
        elif(opcion==2):
            imprimirdatos()
        elif(opcion==3):
            Servicios()   
        elif(opcion==4):
            Productos()
        elif(opcion==5):
            ()
        elif(opcion==7):
            generarPDF(listaNombre,listaEdades)

def pedirDatos():
    listaClientes.append(input("Ingresa el nombre tu usuario: "))
    print("Guardado")

def imprimirdatos():
    for i in range(len(listaNombre)):
        print(f"Nombre:{listaNombre[i]} Edad: {listaEdades[i]}")        