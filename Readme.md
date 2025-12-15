# Sistema de Gestión de Productos en Python

## Descripción
Este es un sistema simple de gestión de productos realizado en Python que utiliza una base de datos SQLite para almacenar y manipular información sobre productos. El sistema permite realizar las siguientes operaciones:

- **Agregar productos**: Ingresar nuevos productos con detalles como nombre, descripción, categoría, cantidad y precio.
- **Listar productos**: Mostrar todos los productos registrados en la base de datos.
- **Actualizar productos**: Modificar los detalles de un producto ya existente.
- **Eliminar productos**: Eliminar productos por su ID.
- **Buscar productos**: Buscar productos por nombre.
- **Reporte de bajo stock**: Mostrar productos cuyo stock esté por debajo de un valor mínimo establecido.
  
El sistema también maneja errores en la entrada de datos y valida que los valores sean correctos antes de almacenarlos en la base de datos.

---

## Requisitos
- Python 3.x
- Bibliotecas:
  - **sqlite3** (Para gestionar la base de datos SQLite)
  - **colorama** (Para agregar color y formato a la interfaz de texto)

Puedes instalar `colorama` utilizando pip:

```bash
pip install colorama
Estructura de la Base de Datos
La base de datos es un archivo SQLite llamado base-de-datos.db y contiene una tabla llamada productos con los siguientes campos:

id: Identificador único del producto (clave primaria, autoincremental).
nombre: Nombre del producto (único).
descripcion: Descripción del producto.
categoria: Categoría del producto.
cantidad: Cantidad disponible en stock.
precio: Precio del producto.
El código incluye una comprobación al inicio para asegurarse de que la tabla exista, creando la tabla si es necesario.

Funcionalidades
1. Alta de productos
Permite ingresar nuevos productos a la base de datos. El sistema valida que el nombre del producto no exista previamente en la base de datos.

Flujo:

Ingresar el nombre del producto.
Ingresar la descripción del producto.
Ingresar la categoría.
Ingresar la cantidad en stock.
Ingresar el precio.
2. Listado de productos
Muestra una lista completa de los productos almacenados en la base de datos, mostrando su id, nombre, descripcion, categoria, cantidad y precio.

3. Actualizar productos
Permite actualizar los detalles de un producto. El usuario debe seleccionar el id del producto a modificar y luego podrá cambiar los campos: nombre, descripcion, categoria, cantidad y precio.

4. Eliminar productos
Permite eliminar un producto de la base de datos usando su id.

5. Buscar productos
Permite buscar un producto por su nombre. Si el producto existe, se muestra su información. Si no se encuentra, el sistema notifica al usuario.

6. Reporte de bajo stock
Permite generar un reporte de productos cuyo stock esté por debajo de un valor mínimo determinado por el usuario.

Menú Principal
Al ejecutar el programa, se muestra un menú interactivo con las siguientes opciones:

Alta de productos nuevos
Listado completo de productos
Actualizar productos
Eliminar productos
Buscar productos por nombre
Reporte de bajo stock
Salir
El sistema acepta solo números del 1 al 7 como opción. Si se ingresa una opción no válida, el sistema informará el error y pedirá una nueva opción.

Manejo de Errores
El programa está diseñado para manejar errores comunes, como:

Entrada de datos no válida: Si el usuario ingresa un valor no numérico cuando se requiere un número (por ejemplo, para la cantidad o el precio), el sistema pedirá que ingrese un valor correcto.
Productos duplicados: Si el usuario intenta agregar un producto con un nombre que ya existe en la base de datos, el sistema notificará que el nombre está duplicado y pedirá un nuevo nombre.
Campos vacíos: Para los campos de descripción y categoría, el sistema validará que se ingresen valores no vacíos.
Instrucciones de uso
Clona o descarga este proyecto en tu máquina local.

Instala las dependencias necesarias con pip:

bash
Copy code
pip install colorama
Ejecuta el archivo Python que contiene el código. Esto abrirá el menú principal y te permitirá interactuar con el sistema.

bash
Copy code
python gestion_productos.py
Sigue las instrucciones en pantalla para realizar las operaciones que desees.

Ejemplo de Salida
Al ejecutar el programa, el menú inicial podría verse así:

markdown
Copy code
 _____________________________________________________
 Welcome al Menu de gestion de productos Compro Clever 
 \---------------------------------------------------/ 

 1. Alta de productos nuevos
 2. Listado completo de productos 
 3. Actualizar productos
 4. Eliminar productos 
 5. Buscar productos
 6. Reporte de bajo stock 
 7. Salir 
Si seleccionas la opción para agregar un producto nuevo, podrías ver algo así:

yaml
Copy code
Ingrese el nombre del producto: Camisa
Ingrese la descripcion del producto: Camisa de algodón
Ingrese la categoria del producto: Ropa
Ingrese la cantidad en stock: 100
Ingrese el precio del producto: 25.50
Producto Camisa agregado exitosamente.
