
#Este codigo permite que el usuario calcule el promedio de la tempratura
#semanal. El usuario debe ingresar las temperaturas para obtener un promedio
#en base a los dias de la semana

def ingresar_temperaturas():
  """Solicita al usuario las temperaturas de cada día de la semana y las almacena en una lista."""
  temperaturas = []
  dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
  for dia in dias:
    temperatura = float(input(f"Ingrese la temperatura del {dia}: "))
    temperaturas.append(temperatura)
  return temperaturas

def calcular_promedio(temperaturas):
  """Calcula el promedio de una lista de temperaturas."""
  suma = sum(temperaturas)
  promedio = suma / len(temperaturas)
  return promedio

# Llamamos a las funciones
temperaturas_semanales = ingresar_temperaturas()
promedio_semanal = calcular_promedio(temperaturas_semanales)

# Mostramos el resultado
print(f"El promedio de temperatura semanal es: {promedio_semanal:.2f} °C")