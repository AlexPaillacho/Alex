#En este codigo se implementa las tecnicas de programacion
# para el funcionamiento de el calculo promedio semanal

class Dia:
    def __init__(self, fecha, temperatura):
        self.__fecha = fecha
        self.__temperatura = temperatura

    def get_temperatura(self):
        return self.__temperatura

    def set_temperatura(self, nueva_temperatura):
        self.__temperatura = nueva_temperatura

def calcular_promedio_semanal(dias):
    """Calcula el promedio de temperatura de una lista de días."""
    total_temperatura = sum(dia.get_temperatura() for dia in dias)
    cantidad_dias = len(dias)
    return total_temperatura / cantidad_dias

#Crear una lista de objetos Dia
dias_semana = []
for dia in range(1, 8):
    fecha = f"Día {dia}"
    temperatura = float(input(f"Ingrese la temperatura del {fecha}: "))
    dias_semana.append(Dia(fecha, temperatura))

#Calcular y mostrar el promedio
promedio = calcular_promedio_semanal(dias_semana)
print(f"El promedio de temperatura semanal es: {promedio:.2f} °C")