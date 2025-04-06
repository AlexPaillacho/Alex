import tkinter as tk
from tkinter import ttk, messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root  # Guarda la ventana principal de la aplicación.
        self.root.title("Lista de Tareas Pendientes")  # Establece el título de la ventana.

        self.tasks = []  # Inicializa una lista vacía para almacenar las tareas. Cada tarea será un diccionario.
        self.task_var = tk.StringVar(value=[])  # Crea una variable de cadena de Tkinter para actualizar la Listbox. Inicialmente está vacía.

        # Campo de entrada para añadir nuevas tareas
        self.new_task_entry = ttk.Entry(root)  # Crea un widget de entrada (campo de texto) para que el usuario escriba nuevas tareas.
        self.new_task_entry.pack(pady=5, padx=10, fill=tk.X)  # Coloca el campo de entrada en la ventana con relleno vertical y horizontal, y se expande horizontalmente.
        self.new_task_entry.bind("<Return>", self.add_task)  # Vincula la tecla "Enter" al evento de añadir una nueva tarea.

        # Botones de acción
        button_frame = ttk.Frame(root)  # Crea un marco para contener los botones.
        button_frame.pack(pady=5, padx=10, fill=tk.X)  # Coloca el marco en la ventana con relleno y expansión horizontal.

        self.add_button = ttk.Button(button_frame, text="Añadir Tarea", command=self.add_task)  # Crea un botón para añadir tareas y lo vincula a la función add_task.
        self.add_button.pack(side=tk.LEFT, padx=5)  # Coloca el botón a la izquierda del marco con un pequeño relleno horizontal.

        self.complete_button = ttk.Button(button_frame, text="Marcar como Completada", command=self.mark_complete)  # Crea un botón para marcar tareas como completadas y lo vincula a la función mark_complete.
        self.complete_button.pack(side=tk.LEFT, padx=5)  # Coloca el botón a la izquierda del botón anterior con relleno horizontal.

        self.delete_button = ttk.Button(button_frame, text="Eliminar Tarea", command=self.delete_task)  # Crea un botón para eliminar tareas y lo vincula a la función delete_task.
        self.delete_button.pack(side=tk.LEFT, padx=5)  # Coloca el botón a la izquierda de los botones anteriores con relleno horizontal.

        # Lista de tareas
        self.task_listbox = tk.Listbox(root, listvariable=self.task_var, selectmode=tk.SINGLE)  # Crea una lista para mostrar las tareas. El contenido se basa en task_var, y solo se puede seleccionar un elemento a la vez.
        self.task_listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)  # Coloca la lista con relleno en todas las direcciones y se expande para llenar el espacio disponible.
        self.task_listbox.bind("<Double-Button-1>", self.mark_complete)  # Vincula el doble clic izquierdo a la función de marcar como completada.

        # Atajos de teclado
        root.bind("<Escape>", self.close_app)  # Vincula la tecla "Escape" a la función para cerrar la aplicación.
        root.bind("<c>", self.mark_complete_shortcut)  # Vincula la tecla "c" a la función de marcar como completada (atajo).
        root.bind("<Delete>", self.delete_task_shortcut)  # Vincula la tecla "Delete" a la función de eliminar tarea (atajo).
        root.bind("<d>", self.delete_task_shortcut)  # Vincula la tecla "d" a la función de eliminar tarea (otro atajo).

        self.update_task_list()  # Llama a la función para mostrar inicialmente la lista de tareas (que puede estar vacía).

    def add_task(self, event=None):
        new_task = self.new_task_entry.get().strip()  # Obtiene el texto del campo de entrada y elimina los espacios en blanco al principio y al final.
        if new_task:  # Si el texto no está vacío:
            self.tasks.append({"text": new_task, "completed": False})  # Añade un nuevo diccionario a la lista de tareas con el texto y el estado "no completado".
            self.new_task_entry.delete(0, tk.END)  # Limpia el campo de entrada.
            self.update_task_list()  # Actualiza la visualización de la lista de tareas.

    def mark_complete(self):
        selected_index = self.task_listbox.curselection()  # Obtiene el índice del elemento seleccionado en la lista.
        if selected_index:  # Si se ha seleccionado algún elemento:
            index = selected_index[0]  # Obtiene el primer índice de la selección (solo se permite una selección).
            self.tasks[index]["completed"] = not self.tasks[index]["completed"]  # Invierte el estado de "completado" de la tarea seleccionada.
            self.update_task_list()  # Actualiza la visualización de la lista de tareas.

    def mark_complete_shortcut(self, event):
        self.mark_complete()  # Llama a la función mark_complete cuando se presiona el atajo de teclado.

    def delete_task(self):
        selected_index = self.task_listbox.curselection()  # Obtiene el índice del elemento seleccionado en la lista.
        if selected_index:  # Si se ha seleccionado algún elemento:
            index = selected_index[0]  # Obtiene el primer índice de la selección.
            del self.tasks[index]  # Elimina la tarea seleccionada de la lista.
            self.update_task_list()  # Actualiza la visualización de la lista de tareas.

    def delete_task_shortcut(self, event):
        self.delete_task()  # Llama a la función delete_task cuando se presiona el atajo de teclado.

    def update_task_list(self):
        display_tasks = []  # Inicializa una lista vacía para almacenar el texto a mostrar.
        for task in self.tasks:  # Itera a través de la lista de tareas.
            if task["completed"]:  # Si la tarea está completada:
                striked_text = "".join(f"\u0336{char}" for char in task['text'])  # Crea una versión tachada del texto de la tarea (si el terminal/fuente lo soporta).
                display_tasks.append(f"[Completada] {striked_text}")  # Añade "[Completada]" y el texto tachado a la lista para mostrar.
            else:
                display_tasks.append(task["text"])  # Si no está completada, añade el texto normal a la lista.
        self.task_var.set(display_tasks)  # Actualiza la variable de Tkinter, lo que hace que la Listbox se actualice.
        self._visual_feedback()  # Llama a la función para aplicar un feedback visual adicional (cambio de color).

    def _visual_feedback(self):
        for i, task in enumerate(self.tasks):  # Itera a través de la lista de tareas con su índice.
            if task["completed"]:  # Si la tarea está completada:
                self.task_listbox.itemconfig(i, foreground="grey", selectforeground="grey")  # Cambia el color del texto y el color de selección a gris.
            else:
                self.task_listbox.itemconfig(i, foreground="black", selectforeground="blue")  # Restablece el color del texto a negro y el color de selección a azul.

    def close_app(self, event=None):
        self.root.destroy()  # Destruye la ventana principal, cerrando la aplicación.

if __name__ == "__main__":
    root = tk.Tk()  # Crea la ventana principal de Tkinter.
    app = TodoApp(root)  # Crea una instancia de la clase TodoApp, pasando la ventana principal.
    root.mainloop()  # Inicia el bucle principal de Tkinter, que mantiene la ventana abierta y gestiona los eventos.