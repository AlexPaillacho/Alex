# Creamos la clase que contiene en este caso una moto
# que contenga atributos marca_modelo y año
# utilizamos constructor __init__

class moto:
    def __init__(self,marca_modelo, año):
        self.marca_modelo = marca_modelo
        self.año = año
        print(f"creando un objeto moto: {marca_modelo} {año}")

# utilizamos un destrcutor __del__

    def __del__(self):
        print(f"destruye el objeto moto: {self.marca_modelo} {self.año}")

 #Creamos los objetos que contiene marca_modelo y año

moto_1 = moto("suzuki gixxer CC150", 2024)
moto_2 = moto("pulsar dominar CC400", 2025)

# Al finalizar el programa, se llamarán los destructores
# la imprimir nos da elresultado del constructor y tambien del destructor
