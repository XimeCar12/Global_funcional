#Datosestaticos
listaServicios = [
                "1. Aplicacion de pestañas",
                "2. Aplicacion de uñas",
                "3. Retiros (pestañas,uñas)",
                "4. Macroblading",
                "5. Manicure",
                "6. Pedicure",
                "7. Aplicacion de gelish",
                "8. Masajes",
                "9. Depilacion con cera",
                "10. Alisado permanente"]
listaPrecios = [
"$450.00",
"$320.00",
"$200.00",
"$1000.00",
"$230.00",
"$350.00",
"$200.00",
"$700.00",
"200.00",
"$400.00"
]
def Servicios():
    print('{:<30} {:10}'.format("|Servicios|","|Precios|"))
    for i in range (len(listaServicios)):
        print('{:<30} {:<10}'.format(listaServicios[i],listaPrecios[i]))


listaProductos=[
            "1. Perfumes",
            "2. Sombras para ojos",
            "3. Bolsas",
            "4. Shampoo",
            "5. Cremas",   
            "6. Joyeria",
            "7. Relojes",
            "8. Plancha para cabello",
            "9. Secadora de cabello",
            "10. Tenasas para risos",
            "11. Protectores de cabello",
            "12. Esponjas para maquillaje ",
            "13. Esmaltes",
            "14. Acrilicos",
            "15. Gelish",
            "16. Lampara para uñas",
            "17. Pinceles",
            "18. Labiales",
            "19. Mascara de pestañas",
            "20. Protector solar",
            ]

montoProductos=[
"500.00",
"350.00",
"600.00",
"55.00",
"45.00",
"300.00",
"350.00",
"400.00",
"350.00",
"400.00",
"150.00",
"100.00",
"150.00",
"250.00",
"250.00",
"500.00",
"150.00",
"200.00",
"100.00",
"150.00",
]

def Productos():
    print('{:<30} {:<10}'.format("|Productos|","|Precios|"))
    for i in range(len(listaProductos)):
        print('{:<30} {:<10}'.format(listaProductos[i],montoProductos[i]))


listaDiseños=[
                "Recubrimiento Acrílico",
                "Vitamina con calcio para tus uñas",
                "Esmalte en gel semi permanente",
                "Uñas acrílicas con Tip",
                "Uñas acrílicas Esculturales",
                "Retoque y mantenimiento de uñas acrílicas",
                "Relojes",
                "Decoración de uñas",
                "Retiro de acrílico",
                "Retiro de Esmalte en Gel semi permanente",
                "Vitamina con calcio para tus uñas",
                "-----Pestañas-----",
                "Esmalte Tradicional ",
                "Efecto Natural",
                "Efecto Cásico",
                "Efecto Glam",
                "Técnica Híbrida",
                "Volumen ruso",
                "-----Depilacion-----",
                "Facial",
                "Piernas",
                "Ceja",
                "Axila",
                "Brazos",
]
def Diseños():
    for i in range(len(listaDiseños)):
        print(f"{i+1}.{listaDiseños[i]}")
    elegirDiseño=int(input("Que diseño deseas: "))
    print(f"Tu diseño es: {listaDiseños[elegirDiseño-1]}")    


listaTrabajadores=[
                    "-----Trabajadores-----",
                    "Rosario Barrios García",
                    "Emilio Jiménez Rodríguez",
                    "Elena Flores López",
                    "Diego Reyes Martínez",
                    "Socorro Ortiz González",
                    "Santiago Aguilar Pérez",
                    "Valeria León Ramírez",
                    "Rodolfo Paredes Hernández",
                    "Silvia Cordero Silva",
                    "Fernando Valencia Torres"
]
def Trabajadores():
    for i in range(len(listaTrabajadores)):
        print(f"{i-1}.{listaTrabajadores[i]}")
    elegirTrabajador=int(input("Que trabajador quieres que te atienda:"))
    print(f"Tu trabajador a atender es: {listaTrabajadores[elegirTrabajador]}") 

listaClientes=[
                "Emma García",
                "Miguel Rodríguez",
                "Noah López",
                "Jorge Martínez",
                "Liam González",
                "Rafael Pérez",
                "Olivia Ramírez",
                "Feliciano Hernández",
                "Ava Silva",
                "Ariel Torres",
                "Isabella Díaz",
                "Nicolás Cruz",
                "Sophia Morales",
                "Benito Castro",
                "Mia Gómez",
                "Antonio Vargas"
                "Charlotte Mendoza",
                "Simón Ruiz",
                "Amelia Romero",
                "Eduardo Medina",
                "Harper Ríos",
                "Roberto Navarro",
                "Evelyn Sánchez",
                "Isidoro Castillo",
                "Abigail Ezpinoza",
                "Mauricio García",
                "Emily Rodríguez",
                "Kevin García",
                "Elizabeth Rodríguez",
                "Leister López",]
def Clientes():
    for i in range(len(listaClientes)):
        print(f"{i+1}.{listaClientes[i]}")
    elegirCliente=int(input("Ingres el numero de cliente: "))    
    print(f"Tu nombre es: {listaClientes[elegirCliente-1]}")

listaCombos=[
            "Pestañas y Sombra de ojos",
            "Macroblading y Plancha para cabello",
            "Aplicacion de gelish y depilacion de ceja",
            "Masaje y bolsa"
            "Alisado permanente y shapoo",
            "Manicure y Perfume",
            "Aplicacion de uñas y collar",
            "Tensas para risos y crema",
            "Esponjas para maquillaje y Retiro de uñas",
            "Secadora de cabello y protector solar",
            "Aplicacion de uñas y esmaltes",
            "Macroblading y Acrilicos",
            "Lampara de uñas y acrilicos",
            "Depilacion de Axilas y Mascara de pestañas",
            "Pedicure y Masaje",
            "Aplicacion de gelish y Lampara para uñas",
            "Protector solar y Bolsa",
            "Masaje y Aplicacion de gelish",
            "Manicure y Aplicacion de uñas",
            "Pedicure y Aretes"]

costoCombos=[
"600.00",
"950.00",
"250.00",
"950.00",
"350.00",
"600.00",
"650.00",
"300.00",
"250.00",
"450.00",
"500.00",
"1,125.00",
"675.00",
"270.00",
"945.00",
"630.00",
"675.00",
"810.00",
"495.00",
"585.00"]

def Combos():
    print('{:<10} {:<50} {:<10}'.format("|No.|","|Combos|","|Precios|"))
    for i in range (len(listaCombos)):
        print('{:<10} {:<50} {:<10}'.format(i+1,listaCombos[i],costoCombos[i]))
    elegirCombo=int(input("Que combo deseas: "))
    print(f"Tu combo es: {listaCombos[elegirCombo-1]}")
