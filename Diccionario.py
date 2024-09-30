#diccionario de informacion personal de una persona nombre edad y ciudad


informacion_personal={"nombre":"Andres", "edad":20,
                      "Ciudad":"quito"}

# Agregamos una clave-valor nuevo al diccionario esta es la profesion
informacion_personal["profesion"]= "Ingeniero"

# ingresamos al valor ciudad del diccionario
print(informacion_personal["Ciudad"])

# Modificamos un valor este caso ciudad cambiamos de quito a galapagos en el diccionario
informacion_personal["Ciudad"]="Galapagos"


# verificar si una clave si existe esta clave es telefono
key=informacion_personal.get("telefono", "telefono no se encuentra")


# agregar un valor y clave agregamos telefono al diccionario
informacion_personal["telefono"]= "0978654545"


# eliminar una clave eliminamos la edad
del informacion_personal["edad"]

# imprimimos todos los cambios realizados en el diccionario
print(key)
print(informacion_personal)
