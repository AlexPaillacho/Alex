import tkinter as tk
from tkinter import messagebox

def crear_lista_tareas():
    """Crea la ventana principal y los widgets de la aplicación."""

    ventana = tk.Tk()
    ventana.title("Lista de Tareas")
    ventana.configure(bg="lightblue")  # Cambia el fondo a azul claro

    # Campo de entrada para nuevas tareas
    entrada_tarea = tk.Entry(ventana, width=40)
    entrada_tarea.grid(row=0, column=0, padx=10, pady=10)

    # Lista de tareas
    lista_tareas = tk.Listbox(ventana, width=50)
    lista_tareas.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    def agregar_tarea():
        """Añade una nueva tarea a la lista."""
        tarea = entrada_tarea.get()
        if tarea:
            lista_tareas.insert(tk.END, tarea)
            entrada_tarea.delete(0, tk.END)  # Limpiar el campo de entrada
        else:
            messagebox.showwarning("Advertencia", "Por favor, introduce una tarea.")

    def marcar_completada():
        """Marca la tarea seleccionada como completada."""
        try:
            indice = lista_tareas.curselection()[0]
            tarea = lista_tareas.get(indice)
            lista_tareas.delete(indice)
            lista_tareas.insert(indice, "[COMPLETADA] " + tarea)
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

    def eliminar_tarea():
        """Elimina la tarea seleccionada de la lista."""
        try:
            indice = lista_tareas.curselection()[0]
            lista_tareas.delete(indice)
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

    # Botones
    boton_agregar = tk.Button(ventana, text="Añadir Tarea", command=agregar_tarea)
    boton_agregar.grid(row=0, column=1, padx=5, pady=10)

    boton_completar = tk.Button(ventana, text="Marcar como Completada", command=marcar_completada)
    boton_completar.grid(row=0, column=2, padx=5, pady=10)

    boton_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea)
    boton_eliminar.grid(row=2, column=0, columnspan=3, pady=10)

    # Manejo de evento para la tecla Enter
    entrada_tarea.bind("<Return>", lambda event: agregar_tarea())

    ventana.mainloop()

if __name__ == "__main__":
    crear_lista_tareas()