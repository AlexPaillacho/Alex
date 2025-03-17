import tkinter as tk
from tkinter import ttk

class GestorDatosGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Datos")
        self.root.configure(bg="#E0F2F7")
# Color de fondo de la ventana

 # Estilo para los widgets
        style = ttk.Style()
        style.configure("TLabel", background="#E0F2F7")
        style.configure("TButton", background="#81D4FA")
        style.configure("TEntry", fieldbackground="white")

 # Etiqueta y Campo de Texto
        self.label_entrada = ttk.Label(root, text="Ingrese Datos:")
        self.label_entrada.pack(pady=5)
        self.entrada_datos = ttk.Entry(root)
        self.entrada_datos.pack(pady=5)

 # Botón Agregar
        self.boton_agregar = ttk.Button(root, text="Agregar", command=self.agregar_dato)
        self.boton_agregar.pack(pady=5)

 # Lista/Tabla (Usaremos una lista simple para este ejemplo)
        self.lista_datos = tk.Listbox(root, bg="#F0F8FF")
        # Color de fondo de la lista
        self.lista_datos.pack(pady=5)

 # Botón Limpiar
        self.boton_limpiar = ttk.Button(root, text="Limpiar", command=self.limpiar_lista)
        self.boton_limpiar.pack(pady=5)

    def agregar_dato(self):
        dato = self.entrada_datos.get()
        if dato:
            self.lista_datos.insert(tk.END, dato)
            self.entrada_datos.delete(0, tk.END)

# Limpiar el campo de texto

    def limpiar_lista(self):
        self.lista_datos.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = GestorDatosGUI(root)
    root.mainloop()