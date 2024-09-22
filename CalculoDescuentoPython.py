#Crea una función llamada calcular_descuento que tome dos parámetros
# el monto total de la compra y un valor 15 % de descuento

def calcular_descuento(montototal, descuento=15):
    descuento= 15
    valor_total = 100

    descuento_total = montototal * (descuento/ 100)

    valor_con_descuento_total = montototal - descuento_total


    print("El monto total de la compra es", montototal, "$")
    print(f"El valor total a pagar es {valor_con_descuento_total}$")
    print(f"Su descuento es de", descuento_total,"$")


calcular_descuento(310,)


