import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar
import datetime

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda de Eventos")

        # Variables para almacenar los eventos
        self.eventos = []

        # Contenedores (Frames)
        self.frame_eventos = ttk.Frame(root, padding="10")
        self.frame_eventos.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.frame_entradas = ttk.Frame(root, padding="10")
        self.frame_entradas.grid(row=1, column=0, sticky=(tk.W, tk.E))

        self.frame_botones = ttk.Frame(root, padding="10")
        self.frame_botones.grid(row=2, column=0, sticky=(tk.W, tk.E))

        # Treeview para mostrar los eventos
        self.tree = ttk.Treeview(self.frame_eventos, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Scrollbar para el Treeview
        scrollbar = ttk.Scrollbar(self.frame_eventos, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Entradas para fecha, hora y descripción
        ttk.Label(self.frame_entradas, text="Fecha:").grid(row=0, column=0)
        self.fecha_entry = ttk.Entry(self.frame_entradas)
        self.fecha_entry.grid(row=0, column=1)
        ttk.Button(self.frame_entradas, text="Seleccionar Fecha", command=self.seleccionar_fecha).grid(row=0, column=2)

        ttk.Label(self.frame_entradas, text="Hora:").grid(row=1, column=0)
        self.hora_entry = ttk.Entry(self.frame_entradas)
        self.hora_entry.grid(row=1, column=1)

        ttk.Label(self.frame_entradas, text="Descripción:").grid(row=2, column=0)
        self.descripcion_entry = ttk.Entry(self.frame_entradas)
        self.descripcion_entry.grid(row=2, column=1)

        # Botones
        ttk.Button(self.frame_botones, text="Agregar Evento", command=self.agregar_evento).grid(row=0, column=0)
        ttk.Button(self.frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento).grid(row=0, column=1)
        ttk.Button(self.frame_botones, text="Salir", command=root.destroy).grid(row=0, column=2)

        # Configurar la expansión de filas y columnas
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        self.frame_eventos.columnconfigure(0, weight=1)
        self.frame_eventos.rowconfigure(0, weight=1)

    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

        if fecha and hora and descripcion:
            self.eventos.append((fecha, hora, descripcion))
            self.actualizar_treeview()
            self.fecha_entry.delete(0, tk.END)
            self.hora_entry.delete(0, tk.END)
            self.descripcion_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")

    def eliminar_evento(self):
        seleccion = self.tree.selection()
        if seleccion:
            respuesta = messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar el evento seleccionado?")
            if respuesta:
                item = seleccion[0]
                index = int(item[1:], 16) - 1
                del self.eventos[index]
                self.actualizar_treeview()
        else:
            messagebox.showerror("Error", "Por favor, seleccione un evento para eliminar.")

    def actualizar_treeview(self):
        self.tree.delete(*self.tree.get_children())
        for evento in self.eventos:
            self.tree.insert("", tk.END, values=evento)

    def seleccionar_fecha(self):
        top = tk.Toplevel(self.root)
        cal = Calendar(top, font="Arial 14", selectmode='day', cursor="hand1")
        cal.pack(fill="both", expand=True)
        ttk.Button(top, text="Seleccionar", command=lambda: self.obtener_fecha(cal, top)).pack()

    def obtener_fecha(self, cal, top):
        self.fecha_entry.delete(0, tk.END)
        self.fecha_entry.insert(0, cal.get_date())
        top.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()