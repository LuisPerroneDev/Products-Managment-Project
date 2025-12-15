import sqlite3
from colorama import init, Fore, Back, Style

init(autoreset=True)

errores_color = Fore.RED

conexion = sqlite3.connect("./base-de-datos.db")  # Conecta a la base de datos y crea un archivo .db
cursor = conexion.cursor()  # Variable para conectar a la db.

cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nombre TEXT UNIQUE NOT NULL,
               descripcion TEXT NOT NULL,
               categoria TEXT NOT NULL,
               cantidad INTEGER NOT NULL,
               precio REAL NOT NULL
               )''')  # Crea la base de datos.

conexion.close()


def pedir_cantidad():  # Funcion que pide la cantidad al agregar o modificar un producto.
    conexion = sqlite3.connect("./base-de-datos.db")
    cursor = conexion.cursor()
    cantidad = 0
    while cantidad <= 0:
        try:
            cantidad = int(input(Fore.LIGHTGREEN_EX + "\nIngrese la cantidad en stock: "))
            if cantidad < 0:
                print(errores_color + "\nIngrese un número mayor que 0\n")
        except ValueError:
            print(errores_color + "\nIngrese un número válido\n")
            cantidad = 0
    return cantidad


def pedir_precio():  # Funcion que pide el precio al agregar o modificar un producto.
    conexion = sqlite3.connect("./base-de-datos.db")
    cursor = conexion.cursor()
    precio = 0.0
    while precio <= 0:
        try:
            precio = float(input(Fore.LIGHTGREEN_EX + "\nIngrese el precio del producto: ")) 
            if precio <= 0:
                print(errores_color + "\nIngrese un número mayor que 0\n")
        except ValueError:
            print(errores_color + "\nIngrese un número válido\n")
            precio = 0.0
    return precio


def agregar_productos(nombre, descripcion, categoria, cantidad, precio):  # Agrega los productos ingresados a la base de datos
    datos = [nombre, descripcion, categoria, cantidad, precio]
    conexion = sqlite3.connect("./base-de-datos.db")
    cursor = conexion.cursor()

    # Primero valida si el producto ya existe.
    cursor.execute("SELECT COUNT(*) FROM productos WHERE nombre = ?", (nombre,))
    if cursor.fetchone()[0] > 0:
        print(errores_color + "Error: El nombre del producto ya existe en la base de datos.")
        conexion.close()
        return  # Sale de la funcion si el producto ya existe.

    try:
        cursor.execute("INSERT INTO productos (nombre, descripcion, categoria, cantidad, precio) VALUES (?,?,?,?,?)", datos)
        conexion.commit()
        print(Fore.LIGHTYELLOW_EX + f"Producto {nombre} agregado exitosamente.\n")
    except sqlite3.IntegrityError:
        print(errores_color + "Error: El nombre del producto ya existe en la base de datos.")
    except sqlite3.Error as e:
        print(errores_color + f"Error al agregar el producto: {e}")
    finally:
        conexion.close()


def mostrar_productos(productos=0, unico_producto=False):  # Muestra los productos o el unico producto
    col_widths = {
        'id': 10,
        'nombre': 20,
        'descripcion': 20,
        'categoria': 15,
        'cantidad': 10,
        'precio': 10
    }  # Arma las columnas con espacios
    print(Back.BLACK + Fore.LIGHTCYAN_EX + "----------------------------Listado completo de productos------------------------")
    print(Back.BLACK + Fore.LIGHTMAGENTA_EX + "_________________________________________________________________________________")
    print(Fore.LIGHTMAGENTA_EX + f"{'Id':<{col_widths['id']}}{'Nombre':<{col_widths['nombre']}}{'Descripcion':<{col_widths['descripcion']}}{'Categoria':<{col_widths['categoria']}}{'Cantidad':<{col_widths['cantidad']}}{'Precio':<{col_widths['precio']}}")
    print(Back.BLACK + Fore.LIGHTMAGENTA_EX + "---------------------------------------------------------------------------------")
    if productos == 0:  # Condicion para saber si muestra todo o un producto.
        conexion = sqlite3.connect("./base-de-datos.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos")
        resultados = cursor.fetchall()
        for registro in resultados:
            print(Fore.LIGHTGREEN_EX + Style.DIM + f"{registro[0]:<{col_widths['id']}}{registro[1]:<{col_widths['nombre']}}{registro[2]:<{col_widths['descripcion']}}{registro[3]:<{col_widths['categoria']}}{registro[4]:<{col_widths['cantidad']}}{registro[5]:<{col_widths['precio']}}")
        conexion.close()
    else:
        if unico_producto:
            print(Fore.LIGHTGREEN_EX + Style.DIM +f"ID: {productos[0]:<{col_widths['id']}} Nombre: {productos[1]:<{col_widths['nombre']}} Descripcion: {productos[2]:<{col_widths['descripcion']}} Categoria: {productos[3]:<{col_widths['categoria']}} Cantidad: {productos[4]:<{col_widths['cantidad']}} Precio: {productos[5]:<{col_widths['precio']}}")
        else:
            for registro in productos:
                print(Fore.LIGHTGREEN_EX + Style.DIM +f"{registro[0]:<{col_widths['id']}}{registro[1]:<{col_widths['nombre']}}{registro[2]:<{col_widths['descripcion']}}{registro[3]:<{col_widths['categoria']}}{registro[4]:<{col_widths['cantidad']}}{registro[5]:<{col_widths['precio']}}")


def actualizar_productos():
    print(Fore.GREEN + Style.BRIGHT + "\nLos productos en el inventario son:\n")
    mostrar_productos()
    id_producto = 0
    while id_producto <= 0:
        try:
            id_producto = int(input(Fore.LIGHTYELLOW_EX + "\nIngrese el id del producto a modificar: \n"))
            if id_producto <= 0:
                print(errores_color + "\nIngrese un número mayor que 0\n")
        except ValueError:
            print(errores_color + "\nIngrese un número válido\n")
            id_producto = 0
    nombre = input(Fore.LIGHTGREEN_EX + "Ingrese el nuevo nombre del producto: ").capitalize()
    while True: #Valida que la descripcion sean letras y no este vacia.
        descripcion = input(Fore.LIGHTGREEN_EX + "Ingrese la nueva descripcion del producto: ").capitalize()
        if descripcion.replace(" ", "").isalpha():
            break  # Si el input is valido, sale del loop.
        else:
                    print(Fore.RED + "La descripcion del producto debe contener solo letras y no puede estar vacío.")
    categoria = input(Fore.LIGHTGREEN_EX + "Ingrese la nueva categoria del producto: ").capitalize()
    cantidad = pedir_cantidad()  # Usa la funcion para pedir cantidad
    precio = pedir_precio()      # Usa la funcion para pedir precio.
    conexion = sqlite3.connect("./base-de-datos.db")
    cursor = conexion.cursor()
    cursor.execute('''UPDATE productos SET nombre = ?, descripcion = ?, categoria = ?, cantidad = ?, precio = ? WHERE id = ?''',(nombre, descripcion, categoria, cantidad, precio, id_producto))
    conexion.commit()
    print(Fore.LIGHTYELLOW_EX + f"Producto {nombre} actualizado exitosamente.\n")
    conexion.close()


def eliminar_producto():  # Funcion que elimina productos.
    mostrar_productos()
    id = 0
    while id <= 0:  # Pide un Id.
        try:
            id = int(input(Fore.LIGHTYELLOW_EX + "\nIngrese el id a eliminar: \n"))
            if id <= 0:
                print(errores_color + "\nIngrese un número mayor que 0\n")
        except ValueError:
            print(errores_color + "\nIngrese un número válido\n")
            id = 0
    try:
        with sqlite3.connect("./base-de-datos.db") as cursor:
            cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
            print(errores_color + Style.BRIGHT + "\nProducto eliminado \n")
    except ValueError:
        print(errores_color + "\nId incorrecto\n")
    conexion.close()


def reporte_bajo_stock():
    cantidad = 0
    while cantidad <= 0:
        try:
            cantidad = int(input("Ingrese la cantidad minima que puede haber en stock: \n"))
            if cantidad <= 0:
                print(errores_color +  "\nIngrese un número mayor que 0\n")
        except ValueError:
            print(errores_color +  "\nIngrese un número válido\n")
            cantidad = 0
    conexion = sqlite3.connect("./base-de-datos.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE cantidad <= ?",(cantidad, ))
    resultados = cursor.fetchall()
    print(Back.BLACK + Fore.LIGHTCYAN_EX + "--------------------------Los productos con bajo stock son------------------------")
    mostrar_productos(resultados)
    conexion.close()


def buscar_productos_por_nombre():
    nombre = input("Ingrese el producto a buscar: ").strip().lower().capitalize()
    conexion = sqlite3.connect("./base-de-datos.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE nombre = ?",(nombre,))
    resultados = cursor.fetchone()
    if resultados:  # Valida si resultados es None.
        mostrar_productos(resultados, True)
    else:
        print(errores_color + f"\nProducto '{nombre}' no encontrado. \n")
    conexion.close()


def mostrar_menu():  # Muestra el menu de opciones.
    print(Fore.LIGHTMAGENTA_EX + " _____________________________________________________")
    print(Fore.LIGHTMAGENTA_EX + " Welcome al Menu de gestion de productos Compro Clever \n \---------------------------------------------------/ \n")
    print( Fore.LIGHTCYAN_EX + " 1. Alta de productos nuevos")
    print(Fore.LIGHTCYAN_EX + " 2. Listado completo de productos \n 3. Actualizar productos")
    print(Fore.LIGHTCYAN_EX + " 4. Eliminar productos \n 5. Buscar productos")
    print(Fore.LIGHTCYAN_EX + " 6. Reporte de bajo stock \n 7. Salir \n")


def main():  # Entra a la aplicacion.
    menu = True
    while menu:
        mostrar_menu()
        while True:
            try:
                opcion = int(input(Fore.LIGHTYELLOW_EX + "\nIngrese la opcion deseada (1-7) y presione enter: \n"))
                break
            except ValueError:
                print(Fore.RED + "Ingresaste una letra. Debes ingresar un número válido del 1 al 7.")  # Mensaje de error por input incorrecto

        if opcion == 1:  # Pide los datos del nuevo producto a ingresar.
            print(Fore.LIGHTCYAN_EX + "Alta de producto")
            while True:
                nombre = input(Fore.LIGHTGREEN_EX + "Ingrese el nombre del producto: ").capitalize()

                # Valida si el producto ya existe.
                conexion = sqlite3.connect("./base-de-datos.db")
                cursor = conexion.cursor()
                cursor.execute("SELECT COUNT(*) FROM productos WHERE nombre = ?", (nombre,))
                if cursor.fetchone()[0] > 0:
                    print(errores_color + "El producto con ese nombre ya existe. Ingrese un nuevo nombre.")
                else:
                    break
                conexion.close()
            while True: #Valida que la descripcion sean letras y no este vacia.
                descripcion = input(Fore.LIGHTGREEN_EX + "Ingrese la descripcion del producto: ").capitalize()
                if descripcion.replace(" ", "").isalpha():
                    break  # Si el input is valido, sale del loop.
                else:
                    print(Fore.RED + "La descripcion del producto debe contener solo letras y no puede estar vacío.")
            categoria = input(Fore.LIGHTGREEN_EX + "Ingrese la categoria del producto: ").capitalize()
            cantidad = pedir_cantidad()  # Llama a la funcion que pide la cantidad del producto.
            precio = pedir_precio()      # Llama a la fucion que pide el precio.
            agregar_productos(nombre, descripcion, categoria, cantidad, precio)  # Pasa lo ingresado a esta funcion.

        elif opcion == 2:
            mostrar_productos()  # Llama a la funcion para mostrar los productos.
        elif opcion == 3:
            actualizar_productos()  # Llama a la funcion para actualizar los productos.
        elif opcion == 4:
            eliminar_producto()  # Llama a la funcion para eliminar un producto por ID.
        elif opcion == 5:
            buscar_productos_por_nombre()  # Llama a la funcion para buscar productos por nombre.
        elif opcion == 6:
            reporte_bajo_stock()  # Llama a la funcion para mostrar los productos con bajo stock.
        elif opcion == 7:
            print("\nSaliste del programa.\n")
            menu = False  # Sale del programa
        else:
            print(errores_color + "\nOpcion incorrecta. Ingresaste una opcion fuera del rango 1-7.\n")

# Llamada inicial al menú
main()
