from FuncionesPDF import*
from Datosestaticos import*
import os
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
        print("6.Lista de Trabajadores")
        print("7.Combos")
        print("8. Generar PDF")
        print("9. Generar QR")
        print("0. Salir")
        opcion = int(input("Elige una opcion "))
        os.system('cls')
        if(opcion ==1):
            pedirDatos()
        elif(opcion==2):
            Clientes()
        elif(opcion==3):
            Servicios()   
            input("Presione enter para continuar")
            os.system('cls')
        elif(opcion==4):
            print("----Productos----")
            Productos()    
            input("Presione enter para continuar")
            os.system('cls')
        elif(opcion==5):
            Diseños()    
            input("Presione enter para continuar")
            os.system('cls')
        elif(opcion==6):
            Trabajadores() 
            input("Presione enter para continuar")
            os.system('cls') 
        elif(opcion==7):
            print("----Combos----")
            Combos()    
            input("Presione enter para continuar")
            os.system('cls')
        elif(opcion==8):
            generarPDF(listaNombre,listaEdades)

def pedirDatos():
    listaClientes.append(input("Ingresa el nombre tu usuario: "))
    print("Guardado")

def imprimirdatos(listaClientes):
    print(f"----Clientes----: {listaClientes}")       