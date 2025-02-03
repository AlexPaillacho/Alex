#Se crean objetos de las clases Loro y Gato

   #Tambien se crean atributos

class Animal:
    def __init__(self, nombre, especie):
        self.__nombre = nombre
        self.__especie = especie

    #La variable animales es una lista

    # que puede contener objetos de diferentes tipos.

    def comer(self):
        print(f"{self.__nombre} Esta comiendo.")

    def su_sonido(self):
        pass
        # Método abstracto

# Las clases Loro y Gato heredan de la clase Animal

# compartiendo atributos y métodos comunes.

class loro(Animal):
    def __init__(self, nombre, especie, raza):
        super().__init__(nombre, especie)
        self.__raza = raza

    def su_sonido(self):
        print("Garrir!")

class Gato(Animal):
    def __init__(self, nombre, especie, color):
        super().__init__(nombre, especie)
        self.__color = color

    def su_sonido(self):
        print("Miau!")

#Se introduce nombre, especie,raza,color
#Al momento de imprimir nos da resultado nombres atributos etc.


def main():
    loro_1 = loro("paco", "ave", "loro gris africano")
    gato_1 = Gato("blanco", "Felino", "blanco")

    animales = [loro_1, gato_1]

    for animal in animales:
        animal.comer()
        animal.su_sonido()

if __name__ == "__main__":
    main()