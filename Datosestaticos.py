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
    print('{:<20} {:10}'.format("|Servicios|","|Precios|"))
    for i in range (len(listaServicios)):
        print('{:<20} {:<10}'.format(i+listaServicios[i],listaPrecios[i]))


listarProductos=[
    "-----Productos-----",
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
    "20. Protector solar",]
listaPreciosProductos =[
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
    "150.00"]
def Productos():
    print('{:<20} {:10}'.format("|Producto|","|Precios|"))
    for i in range (len(listarProductos)):
        print('{:<20} {:<10}'.format(i+listarProductos[i],listaPreciosProductos[i]))


"""listaDiseños=[
                "-----Diseños-----",
                "1. Recubrimiento Acrílico",
                "2. Vitamina con calcio para tus uñas",
                "3. Esmalte en gel semi permanente",
                "4. Uñas acrílicas con Tip",
                "5. Uñas acrílicas Esculturales",
                "6. Retoque y mantenimiento de uñas acrílicas",
                "7. Relojes",
                "8. Decoración de uñas",
                "9. Retiro de acrílico",
                "10. Retiro de Esmalte en Gel semi permanente",
                "11. Vitamina con calcio para tus uñas",
                "-----Pestañas-----",
                "12. Esmalte Tradicional ",
                "13. Efecto Natural",
                "14. Efecto Cásico",
                "15. Efecto Glam",
                "16. Técnica Híbrida",
                "17. Volumen ruso",
                "-----Depilacion-----",
                "18. Facial",
                "19. Piernas",
                "20. Ceja",
                "21. Axila",
                "22. Brazos",
]
def Diseños():
    for i in range(len(listaDiseños)):
        print(f"{i+1}.{listaDiseños[i]}")
    elegirDiseño=int(input("Que diseño deseas: "))
    print(f"Tu diseño es: {listaDiseños[elegirDiseño-1]}")    


listaTrabajadores=[
                    "-----Trabajadores-----",
                    "1. Rosario Barrios García",
                    "2. Emilio Jiménez Rodríguez",
                    "3. Elena Flores López",
                    "4. Diego Reyes Martínez",
                    "5. Socorro Ortiz González",
                    "6. Santiago Aguilar Pérez",
                    "7. Valeria León Ramírez",
                    "8. Rodolfo Paredes Hernández",
                    "9. Silvia Cordero Silva",
                    "10.Fernando Valencia Torres"
]
def Trabajadores():
    for i in range(len(listaTrabajadores)):
        print(f"{i+1}.{listaTrabajadores[i]}")
    elegirTrabajador=int(input("Que trabajador quieres que te atienda:"))
    print(f"Tu trabajador a atender es: {listaTrabajadores[elegirTrabajador]}")"""    

listaClientes=[
                "-----Clientes-----",
                "1. Emma García",
                "2. Miguel Rodríguez",
                "3. Noah López",
                "4. Jorge Martínez",
                "5. Liam González",
                "6. Rafael Pérez",
                "7. Olivia Ramírez",
                "8. Feliciano Hernández",
                "9. Ava Silva",
                "10. Ariel Torres",
                "11. Isabella Díaz",
                "12. Nicolás Cruz",
                "13.Sophia Morales",
                "14. Benito Castro",
                "15.Mia Gómez",
                "16. Antonio Vargas"
                "17. Charlotte Mendoza",
                "18. Simón Ruiz",
                "19. Amelia Romero",
                "20. Eduardo Medina",
                "21. Harper Ríos",
                "22. Roberto Navarro",
                "23. Evelyn Sánchez",
                "24. Isidoro Castillo",
                "25.Abigail Ezpinoza",
                "26. Mauricio García",
                "27. Emily Rodríguez",
                "28. Kevin García",
                "29. Elizabeth Rodríguez",
                "30. Leister López"
]
def Clientes():
    for i in range(len(listaClientes)):
        print(f"{i+1}.{listaClientes[i]}")
    elegirCliente=int(input("Eres un cliente existente"))    
    print(f"Tu nombre es: {listaClientes[elegirCliente-1]}")

"""listaCombos=[
    "Combo 1: Pestañas y Sombra de ojos",
    "Combo 2: Macroblading y Plancha para cabello",
    "Combo 3: Aplicacion de gelish y depilacion de ceja",
    "Combo 4: Masaje y bolsa"
    "Combo 5: Alisado permanente y shapoo",
    "Combo 6: Manicure y Perfume",
    "Combo 7: Aplicacion de uñas y collar",
    "Combo 8: Tensas para risos y crema",
    "Combo 9: Esponjas para maquillaje y Retiro de uñas",
    "Combo 10: Secadora de cabello y protector solar",
    "Combo 11: Aplicacion de uñas y esmaltes",
    "Combo 12: Macroblading y Acrilicos",
    "Combo 13: Lampara de uñas y acrilicos",
    "Combo 14: Depilacion de Axilas y Mascara de pestañas",
    "Combo 15: Pedicure y Masaje",
    "Combo 16: Aplicacion de gelish y Lampara para uñas",
    "Combo 17: Protector solar y Bolsa",
    "Combo 18: Masaje y Aplicacion de gelish",
    "Combo 19: Manicure y Aplicacion de uñas",
    "Combo 20: Pedicure y Aretes"]

preciosCombos=[
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
    "1,125.00"
    "675.00",
    "270.00",
    "945.00",
    "630.00",
    "675.00"
    "810.00"
    "495.00",
    "585.00"]
def Combos():
    for i in range (len(listaCombos)):
        print(f"{listaCombos[i]}-{preciosCombos[i]}")

listaCombos()"""