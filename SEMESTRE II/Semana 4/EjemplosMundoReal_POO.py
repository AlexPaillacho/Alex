# En este codigo se representa la venta de un producto
# el calculo total que tien que pagar nuestro cliente
#tenenemos nuestro producto precio y stock
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

# aqui añadimos al cliente
class Cliente:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.canasta = []
# agreagamos funcion  calcular total  y donde guardar la compra
    def agregar_al_canasta(self, producto):
        self.canasta.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self.canasta:
            total += producto.precio
        return total


#tenemos el primer producto
producto = Producto("pantalon", 15, 5)

cliente_1 = Cliente("ANDRES PASCAL", "QUITO")
cliente_1.agregar_al_canasta(producto)

#imprimimos el total a pagar de la compra del cliente

print(f"Total a pagar por su compra : ${cliente_1.calcular_total()}")