import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("700x500")

        # Frame de entrada de datos
        self.frame_input = ttk.Frame(self.root, padding=10)
        self.frame_input.pack(fill=tk.X)

        ttk.Label(self.frame_input, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = DateEntry(self.frame_input, date_pattern='yyyy-mm-dd')
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.frame_input, text="Hora:").grid(row=1, column=0, padx=5, pady=5)
        self.time_entry = ttk.Entry(self.frame_input)
        self.time_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.frame_input, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
        self.desc_entry = ttk.Entry(self.frame_input)
        self.desc_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(self.frame_input, text="Agregar Evento", command=self.add_event).grid(row=3, column=0, columnspan=2,
                                                                                         pady=10)

        # Frame de visualización de eventos
        self.frame_list = ttk.Frame(self.root, padding=10)
        self.frame_list.pack(fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(self.frame_list, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Botón de eliminar evento
        self.frame_buttons = ttk.Frame(self.root, padding=10)
        self.frame_buttons.pack(fill=tk.X)

        ttk.Button(self.frame_buttons, text="Eliminar Evento", command=self.delete_event).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.frame_buttons, text="Eliminar Todos", command=self.delete_all_events).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.frame_buttons, text="Salir", command=self.root.quit).pack(side=tk.RIGHT, padx=5)

    def add_event(self):
        fecha = self.date_entry.get()
        hora = self.time_entry.get()
        descripcion = self.desc_entry.get()

        if fecha and hora and descripcion:
            self.tree.insert("", "end", values=(fecha, hora, descripcion))
            self.time_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Todos los campos deben estar completos")

    def delete_event(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar")
            return

        confirm = messagebox.askyesno("Confirmar", "¿Está seguro de eliminar el evento?")
        if confirm:
            for item in selected_item:
                self.tree.delete(item)

    def delete_all_events(self):
        confirm = messagebox.askyesno("Confirmar", "¿Está seguro de eliminar todos los eventos?")
        if confirm:
            for item in self.tree.get_children():
                self.tree.delete(item)


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
