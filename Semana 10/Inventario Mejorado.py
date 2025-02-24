class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio}"

class Inventario:
    def __init__(self):
        self.productos = {}

    def cargar_inventario(self):
        try:
            with open('inventario.txt', 'r') as file:
                for line in file:
                    id_producto, nombre, cantidad, precio = line.strip().split(';')
                    self.productos[int(id_producto)] = Producto(int(id_producto), nombre, int(cantidad), float(precio))
            print("Inventario cargado exitosamente.")
        except FileNotFoundError:
            print("Archivo 'inventario.txt' no encontrado. Se creará uno nuevo al guardar.")
        except ValueError:
            print("Error: El archivo 'inventario.txt' contiene datos inválidos.")

# Se crea la funcion guardar en nuestro archivo "inventario.txt"

    def guardar_inventario(self):
        try:
            with open('inventario.txt', 'w') as file:
                for producto in self.productos.values():
                    file.write(f"{producto.id_producto} {producto.nombre} {producto.cantidad} {producto.precio} \n")
            print("Inventario guardado exitosamente.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

# Se imprime un mensaje "Inventario guardado exitosamente." y "Error al guardar el inventario

# en caso de tener errores


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

# Interfaz de usuario en la consola
def menu():
    inventario = Inventario()
    inventario.cargar_inventario()  # Cargar inventario al iniciar
    while True:
        print("\n1. Agregar Producto\n2. Eliminar Producto\n3. Actualizar Producto\n4. Buscar Producto\n5. Mostrar Inventario\n6. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '6':
            break
        elif opcion == '1':
            # Agregar producto
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
            # Eliminar producto
            try:
                id_producto = int(input("ID del producto a eliminar: "))
                inventario.eliminar_producto(id_producto)
            except ValueError:
                print("Error: ID inválido. Debe ser un número entero.")
        elif opcion == '3':
            # Actualizar producto
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
            # Buscar producto
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == '5':
            # Mostrar inventario
            inventario.mostrar_inventario()

if __name__ == "__main__":
    menu()