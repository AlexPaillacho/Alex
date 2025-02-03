import os

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu(true=True):
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'SEMESTRE II/Semana 2/Programación Orientada a Objetos.py',
        '2': 'SEMESTRE II/Semana 3/Programación Tradicional.py',
        '3': 'SEMESTRE II/Semana 4/EjemplosMundoReal_POO.py',
        '4': 'SEMESTRE II/Semana 5/Tipos de datos Identificadores.py',
        '5': 'SEMESTRE II/Semana 6/Aplicación de Conceptos de POO en Python.py',
        '6': 'SEMESTRE II/Semana 7/Constructores y Destructores.py',



        # Agrega aquí el resto de las rutas de los scripts
    }

    while true:
        print("\n********Menu Principal - Dashboard*************")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()