import tkinter as tk
from tkinter import messagebox


class GUIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación GUI Avanzada")
        self.root.geometry("500x400")

        # Etiqueta de instrucción
        self.label = tk.Label(root, text="Ingrese un dato:", font=("Arial", 12))
        self.label.pack(pady=5)

        # Campo de texto
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=5)

        # Botón para agregar
        self.add_button = tk.Button(root, text="Agregar", command=self.add_data, bg="lightblue")
        self.add_button.pack(pady=5)

        # Lista para mostrar datos
        self.listbox = tk.Listbox(root, width=60, height=10)
        self.listbox.pack(pady=5)

        # Botón para eliminar seleccionado
        self.delete_button = tk.Button(root, text="Eliminar Seleccionado", command=self.delete_selected,
                                       bg="lightcoral")
        self.delete_button.pack(pady=5)

        # Botón para limpiar la lista
        self.clear_button = tk.Button(root, text="Limpiar Lista", command=self.clear_data, bg="lightgray")
        self.clear_button.pack(pady=5)

        # Contador de elementos
        self.counter_label = tk.Label(root, text="Elementos en la lista: 0", font=("Arial", 10))
        self.counter_label.pack(pady=5)

    def add_data(self):
        data = self.entry.get()
        if data:
            self.listbox.insert(tk.END, data)
            self.entry.delete(0, tk.END)
            self.update_counter()
        else:
            messagebox.showwarning("Advertencia", "El campo está vacío")

    def delete_selected(self):
        try:
            selected_index = self.listbox.curselection()[0]
            self.listbox.delete(selected_index)
            self.update_counter()
        except IndexError:
            messagebox.showwarning("Advertencia", "Seleccione un elemento para eliminar")

    def clear_data(self):
        self.listbox.delete(0, tk.END)
        self.update_counter()

    def update_counter(self):
        count = self.listbox.size()
        self.counter_label.config(text=f"Elementos en la lista: {count}")


if __name__ == "__main__":
    root = tk.Tk()
    app = GUIApp(root)
    root.mainloop()
