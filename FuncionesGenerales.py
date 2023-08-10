from FuncionesPDF import*
from Datosestaticos import*
import os
listaNombre = []
listaEdades = []
def menu():
    opcion ="1"
    while(opcion!="0"):
        print("1.Registrarme")
        print("2.Cliente existente")
        print("3.Lista de Servicios")
        print("4.Lista de Productos")
        print("5.Lista de Diseños")
        print("6.Lista de Trabajadores")
        print("7.Combos")
        print("8. Generar PDF")
        print("9. Generar QR")
        print("0. Salir")
        opcion =input("Elige una opcion ")
        os.system('cls')
        if(opcion =="1"):
            pedirDatos()
        elif(opcion=="2"):
            Clientes()
        elif(opcion=="3"):
            Servicios()   
            input("Presione enter para continuar")
            os.system('cls')
        elif(opcion=="4"):
            print("----Productos----")
            Productos()    
            input("Presione enter para continuar")
            os.system('cls')
        elif(opcion=="5"):
            Diseños()    
            input("Presione enter para continuar")
            os.system('cls')
        elif(opcion=="6"):
            Trabajadores() 
            input("Presione enter para continuar")
            os.system('cls') 
        elif(opcion=="7"):
            print("----Combos----")
            Combos()    
            input("Presione enter para continuar")
            os.system('cls')
        elif(opcion=="8"):
            generarPDF(pos=0)

        elif(opcion=="0"):
            print("---Saliedo----")
        else:
            print("Funcion invalida") 
            input("Presione enter para continuar")
            os.system('cls')

def pedirDatos():
    listaClientes.append(input("Ingresa el nombre tu usuario: "))
    print("Guardado")

def imprimirdatos(listaClientes):
    print(f"----Clientes----: {listaClientes}") 

def Servicios():
    print('{:<10} {:<30} {:10}'.format("|No.|","|Servicios|","|Precios|"))
    for i in range (len(listaServicios)):
        print('{:<10} {:<30} {:<10}'.format(i+1,listaServicios[i],listaPrecios[i]))
    elegirServicio=int(input("Que servicio deseas adquirir: "))
    print(f"Tu Servicio elegido es: {listaServicios[elegirServicio-1]}") 

def Productos():
    print('{:<10} {:<30} {:<10}'.format("|No.|","|Productos|","|Precios|"))
    for i in range(len(listaProductos)):
        print('{:<10} {:<30} {:<10}'.format(i+1,listaProductos[i],montoProductos[i]))
    elegirProducto=int(input("Que producto deseas adquirir: "))
    print(f"Tu producto es: {listaProductos[elegirProducto-1]}") 

def Diseños():
    for i in range(len(listaDiseños)):
        print(f"{i+1}.{listaDiseños[i]}")
    elegirDiseño=int(input("Que diseño deseas: "))
    print(f"Tu diseño es: {listaDiseños[elegirDiseño-1]}")    

def Trabajadores():
    for i in range(len(listaTrabajadores)):
        print(f"{i-1}.{listaTrabajadores[i]}")
    elegirTrabajador=int(input("Que trabajador quieres que te atienda:"))
    print(f"Tu trabajador a atender es: {listaTrabajadores[elegirTrabajador]}")

def Clientes():
    for i in range(len(listaClientes)):
        print(f"{i+1}.{listaClientes[i]}")
    elegirCliente=int(input("Ingres el numero de cliente: "))    
    print(f"Tu nombre es: {listaClientes[elegirCliente-1]}")

def Combos():
    print('{:<10} {:<50} {:<10}'.format("|No.|","|Combos|","|Precios|"))
    for i in range (len(listaCombos)):
        print('{:<10} {:<50} {:<10}'.format(i+1,listaCombos[i],costoCombos[i]))
    elegirCombo=int(input("Que combo deseas: "))
    print(f"Tu combo es: {listaCombos[elegirCombo-1]}")