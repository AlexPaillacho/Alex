
quito=("Semana1","Semana2", "Semana3")
Guayaquil=("seman1", "seman2", "seman3")
cuenca=("sema1", "sema2","sema3")
result=("seman3")




temperaturas = [

  [
        [      #quito

            {"Semana1":"Lunes" ,"tempe": 28},
            {"Semana1": "Martes", "tempe": 26},
            {"Semana1": "Miércoles", "tempe": 24},
            {"Semana1": "Jueves", "tempe": 22},
            {"Semana1": "Viernes", "tempe": 24},
            {"Semana1": "Sábado", "tempe": 26}
        ],
        [   # Semana 2
            {"Semana2": "Lunes", "tempe": 20},
            {"Semana2": "Martes", "tempe": 19},
            {"Semana2": "Miércoles", "tempe": 20},
            {"Semana2": "Jueves", "tempe": 22},
            {"Semana2": "Viernes", "tempe": 20},
            {"Semana2": "Sábado", "tempe": 22}
        ],
        [   # Semana 3
            {"Semana3": "Lunes", "tempe": 25},
            {"Semana3": "Martes", "tempe": 26},
            {"Semana3": "Miércoles", "tempe": 26},
            {"Semana3": "Jueves", "tempe": 24},
            {"Semana3": "Viernes", "tempe": 24},
            {"Semana3": "Sábado", "tempe": 23}
        ],

    ],
     [       #cuenca
        [   # Semana 1
            {"Sema1": "Lunes", "tempe": 22},
            {"Sema1": "Martes", "tempe": 22},
            {"Sema1": "Miércoles", "tempe": 23},
            {"Sema1": "Jueves", "tempe": 24},
            {"Sema1": "Viernes", "tempe": 24},
            {"Sema1": "Sábado", "tempe": 23}
        ],
        [   # Semana 2
            {"Sema2": "Lunes", "tempe": 22},
            {"Sema2": "Martes", "tempe": 22},
            {"Sema2": "Miércoles", "tempe": 24},
            {"Sema2": "Jueves", "tempe": 26},
            {"Sema2": "Viernes", "tempe": 23},
            {"Sema2": "Sábado", "tempe": 23}
        ],
        [   # Semana 3
            {"Sema3": "Lunes", "tempe": 23},
            {"Sema3": "Martes", "tempe": 24},
            {"Sema3": "Miércoles", "tempe": 24},
            {"Sema3": "Jueves", "tempe": 21},
            {"Sema3": "Viernes", "tempe": 24},
            {"Sema3": "Sábado", "tempe": 23}
        ]
    ],
    [   # Guayaquil
        [   # Semana 1
            {"Seman1": "Lunes", "tempe": 35},
            {"Seman1": "Martes", "tempe": 30},
            {"Seman1": "Miércoles", "tempe": 31},
            {"Seman1": "Jueves", "tempe": 31},
            {"Seman1": "Viernes", "tempe": 33},
            {"Seman1": "Sábado", "tempe": 34}
        ],
        [   # Semana 2
            {"Seman2": "Lunes", "tempe": 36},
            {"Seman2": "Martes", "tempe": 34},
            {"Seman2": "Miércoles", "tempe": 36},
            {"Seman2": "Jueves", "tempe": 32},
            {"Seman2": "Viernes", "tempe": 29},
            {"Seman2": "Sábado", "tempe": 28}
        ],
        [   # Semana 3
            {"Seman3": "Lunes", "tempe": 29},
            {"Seman3": "Martes", "tempe": 28},
            {"Seman3": "Miércoles", "tempe": 27},
            {"Seman3": "Jueves", "tempe": 28},
            {"Seman3": "Viernes", "tempe": 26},
            {"Seman3": "Sábado", "tempe": 26}
        ]
    ]
]


for result in temperaturas:
    for semana in result:
        suma = 0
        for dia in semana:
            suma += dia["tempe"]
        print("ciudades", (suma))



def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t
    avg = sum_num / len(num)
    return avg
print("promedios ciudades  =" , cal_average([35,30,31,31,33,34]))
print("promedios ciudades=" , cal_average([36,34,36,32,29,28]))
print("promedios ciudades =" , cal_average([29,28,27,28,2626]))