# En el siguiente codigo que creamos
# sirve para calcular el area de un cuadrado
#creamos la calse cuadrado area 1
class Cuadrado_area_1:

    def __init__(self,lado):
        self.lado=lado

# se calcula el area con la formula (area = lado * lado)

    def area(self):
        return (self.lado * self.lado)

# utilizamos tipos de datos integer, float, string
lado = 8.5

#Utilizamos el identificador descriptivo snake_case
# tenemos los resultados esperados ejecutando el codigo

Cuadrado_area = Cuadrado_area_1(lado)
resultado_final = Cuadrado_area.area()

print("El area del cuadrado es de",resultado_final,"Cm2")
