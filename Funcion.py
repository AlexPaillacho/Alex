

# Ciudades _ Semanas _ Días de la semana
temperaturas = [
    [  # Ciudad_1
        [("Lunes", 40), ("Martes", 23), ("Miércoles", 35), ("Jueves", 33), ("Viernes", 20), ("Sábado", 32), ("Domingo", 21)], # Semana_1
        [("Lunes", 23), ("Martes", 28), ("Miércoles", 26), ("Jueves", 24), ("Viernes", 22), ("Sábado", 33), ("Domingo", 20)], # Semana_2
        [("Lunes", 27), ("Martes", 29), ("Miércoles", 29), ("Jueves", 22), ("Viernes", 23), ("Sábado", 30), ("Domingo", 28)], # Semana_3
        [("Lunes", 26), ("Martes", 28), ("Miércoles", 26), ("Jueves", 23), ("Viernes", 22), ("Sábado", 31), ("Domingo", 20)]  # Semana_4
    ],
    [  # Ciudad_2
        [("Lunes", 30), ("Martes", 27), ("Miércoles", 33), ("Jueves", 25), ("Viernes", 34), ("Sábado", 31), ("Domingo", 30)], # Semana_1
        [("Lunes", 40), ("Martes", 26), ("Miércoles", 24), ("Jueves", 26), ("Viernes", 38), ("Sábado", 37), ("Domingo", 35)], # Semana_2
        [("Lunes", 24), ("Martes", 28), ("Miércoles", 34), ("Jueves", 23), ("Viernes", 35), ("Sábado", 36), ("Domingo", 34)], # Semana_3
        [("Lunes", 23), ("Martes", 20), ("Miércoles", 26), ("Jueves", 35), ("Viernes", 33), ("Sábado", 32), ("Domingo", 31)]  # Semana_4
    ],
    [  # Ciudad_3
        [("Lunes", 24), ("Martes", 28), ("Miércoles", 18), ("Jueves", 37), ("Viernes", 35), ("Sábado", 24), ("Domingo", 33)], # Semana_1
        [("Lunes", 25), ("Martes", 38), ("Miércoles", 29), ("Jueves", 37), ("Viernes", 36), ("Sábado", 25), ("Domingo", 34)], # Semana_2
        [("Lunes", 35), ("Martes", 27), ("Miércoles", 18), ("Jueves", 16), ("Viernes", 25), ("Sábado", 23), ("Domingo", 32)], # Semana_3
        [("Lunes", 19), ("Martes", 35), ("Miércoles", 36), ("Jueves", 37), ("Viernes", 25), ("Sábado", 24), ("Domingo", 33)]  # Semana_4
    ]
]



def temperaturas_promedios(arreglo_temperaturas, ciudad, semana):
    dato = 0


    for dia, temperatura in arreglo_temperaturas[ciudad][semana]:
        dato += temperatura

    # Calcular el promedio
    dato = dato / len(arreglo_temperaturas[ciudad][semana])

    return dato
temperaturas_promedios(temperaturas,2,3)
resultado=(temperaturas_promedios(temperaturas,2,3))
print(resultado)







