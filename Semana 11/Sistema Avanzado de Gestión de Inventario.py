import csv

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = int(id_producto)
        self.nombre = nombre
        self.cantidad = int(cantidad)
        self.precio = float(precio)

    def __str__(self):
        return f"{self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

class Inventario:
    def __init__(self, archivo_inventario="inventario.csv"):
        self.productos = {}
        self.archivo_inventario = archivo_inventario
        self.cargar_inventario()

    def cargar_inventario(self):
        try:
            with open(self.archivo_inventario, 'r', newline='', encoding='utf-8') as archivo:
                lector_csv = csv.reader(archivo, delimiter=';')
                next(lector_csv)  # Omitir encabezado si existe
                for fila in lector_csv:
                    id_producto, nombre, cantidad, precio = fila
                    self.productos[int(id_producto)] = Producto(id_producto, nombre, cantidad, precio)
            print("Inventario cargado exitosamente.")
        except FileNotFoundError:
            print(f"Archivo '{self.archivo_inventario}' no encontrado. Se creará uno nuevo al guardar.")
        except ValueError:
            print(f"Error: El archivo '{self.archivo_inventario}' contiene datos inválidos.")
        except Exception as e:
            print(f"Error inesperado al cargar el inventario: {e}")

    def guardar_inventario(self):
        try:
            with open(self.archivo_inventario, 'w', newline='', encoding='utf-8') as archivo:
                escritor_csv = csv.writer(archivo, delimiter=';')
                escritor_csv.writerow(["ID", "Nombre", "Cantidad", "Precio"])  # Encabezado
                for producto in self.productos.values():
                    escritor_csv.writerow([producto.id_producto, producto.nombre, producto.cantidad, producto.precio])
            print("Inventario guardado exitosamente.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("Error: Producto ya existe.")
        else:
            self.productos[producto.id_producto] = producto
            self.guardar_inventario()
            print(f"Producto '{producto.nombre}' agregado exitosamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            nombre_producto_eliminado = self.productos[id_producto].nombre
            del self.productos[id_producto]
            self.guardar_inventario()
            print(f"Producto '{nombre_producto_eliminado}' eliminado exitosamente.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if cantidad is not None:
                producto.cantidad = cantidad
            if precio is not None:
                producto.precio = precio
            self.guardar_inventario()
            print(f"Producto '{producto.nombre}' actualizado exitosamente.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        encontrado = False
        for producto in self.productos.values():
            if nombre.lower() in producto.nombre.lower():
                print(producto)
                encontrado = True
        if not encontrado:
            print("No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(producto)

def menu():
    inventario = Inventario()
    while True:
        print("\n--- Sistema de Gestión de Inventario ---")
        print("1. Agregar Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto")
        print("5. Mostrar Inventario")
        print("6. Guardar y Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            try:
                id_producto = int(input("ID del producto: "))
                nombre = input("Nombre del producto: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.agregar_producto(producto)
            except ValueError:
                print("Error: Datos inválidos. Asegúrese de ingresar números para ID, cantidad y precio.")
        elif opcion == '2':
            try:
                id_producto = int(input("ID del producto a eliminar: "))
                inventario.eliminar_producto(id_producto)
            except ValueError:
                print("Error: ID inválido. Debe ser un número entero.")
        elif opcion == '3':
            try:
                id_producto = int(input("ID del producto a actualizar: "))
                cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
                precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None
                inventario.actualizar_producto(id_producto, cantidad, precio)
            except ValueError:
                print("Error: Datos inválidos. Asegúrese de ingresar números para ID, cantidad y precio.")
        elif opcion == '4':
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == '5':
            inventario.mostrar_inventario()
        elif opcion == '6':
            inventario.guardar_inventario()
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()