#Abstracción
#La clase Vehiculo representa el concepto general de un vehículo.

class Vehiculo:
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo
#Encapsulación
#Los atributos marca y modelo son privados.

    def salir(self):
        print("El vehículo está por salir")

#Herencia
#Las clases Coche y Motocicleta heredan de Vehiculo y agregan atributos específicos.
class Coche(Vehiculo):
    def __init__(self, marca, modelo, numero_puertas):
        super().__init__(marca, modelo)
        self.__numero_puertas = numero_puertas

#Polimorfismo
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.__cilindrada = cilindrada

# Uso del código:
coche1 = Coche("mazda", "infinit", 4)
moto1 = Motocicleta("pulsar", "400", 600)

coche1.salir()
moto1.salir()
