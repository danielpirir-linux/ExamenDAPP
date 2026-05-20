import mysql.connector

conexion = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456789",
        database = "Restaurante_db"
    )

cursor = conexion.cursor()

print("Empezando sistema de Restaurante...")

while True:
        print("--------------------------------")
        print("Sistema de Menu de Restaurante")
        print("--------------------------------")
        print("1. Crear nuevo platillo")
        print("2. Eliminar un platillo")
        print("3. Mostrar todos los platillos")
        print("4. Salir del sistema")
        print("--------------------------------")

        opcion = input("Ingrese una opcion a realizar: ")

        if opcion == "1":
            print("------------------------------------------------")
            platillo = input("Ingrese un platillo al menu: ").strip()
            if platillo:
                sql = "INSERT INTO Platillo (nombrePlatillo) VALUES (%s)"
                valores = (platillo,)
                cursor.execute(sql, valores)
                conexion.commit()
                print(f" platillo '{platillo}' agregado con exito.\n")
            else:
                print(" No se puede agregar un platillo vacio.\n")

        elif opcion == "2":
            print("------------------------------------------------")
            platillo = input("ingrese un platillo a eliminar del menu: ").strip()
            if platillo:
                sql = "DELETE FROM Platillo WHERE nombrePlatillo = %s"
                valores = (platillo,)
                cursor.execute(sql, valores)
                conexion.commit()
                print(f"platillo '{platillo}' eliminado con exito")
            else:
                print("Este platillo no se encuentra en el menu del sistema")
        elif opcion == "3":
            print("------------------------------------------------")
            print("                 Menu Actual")
            cursor.execute("SELECT idPlatillo, nombrePlatillo FROM Platillo")
            platillos = cursor.fetchall()
            if len(platillos) == 0:
                print("El catálogo está vacío.\n")
            else:
                print("\n Catálogo de Platillos: ")
                for plat in platillos:
                    print(f"{plat[0]}. {plat[1]}")
                print()
        elif opcion == "4":
            print("-----------------------------------------------------")
            print("Gracias por usar el sistema. Tenga un muy buen dia")
            print("-----------------------------------------------------")
            break
        else:
            print("-----------------------------------------------------")
            print("Opcion no válida, ingrese una opcion del 1 al 4")
            print("-----------------------------------------------------")

cursor.close()
conexion.close()