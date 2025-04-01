import tkinter as tk
from tkinter import messagebox

def agregar_tarea(event=None):
    if event and event.widget == entrada_tarea:
        return  # Evitar que los atajos se activen en el campo de entrada
    tarea = entrada_tarea.get().strip()
    if tarea:
        lista_pendientes.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
        guardar_tareas()
    else:
        messagebox.showwarning("Advertencia", "No puedes agregar una tarea vacía.")

def marcar_completada(event=None):
    try:
        index = lista_pendientes.curselection()[0]
        tarea = lista_pendientes.get(index)
        lista_pendientes.delete(index)
        lista_completadas.insert(tk.END, f"✔ {tarea}")
        guardar_tareas()
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea pendiente para marcar como completada.")

def eliminar_tarea(event=None):
    try:
        widget_focused = root.focus_get()
        if widget_focused == lista_pendientes:
            index = lista_pendientes.curselection()[0]
            lista_pendientes.delete(index)
        elif widget_focused == lista_completadas:
            index = lista_completadas.curselection()[0]
            lista_completadas.delete(index)
        guardar_tareas()
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

def cerrar_app(event=None):
    respuesta = messagebox.askyesno("Confirmación", "¿Estás seguro de que quieres salir?")
    if respuesta:
        guardar_tareas()
        root.quit()

def guardar_tareas():
    with open("tareas.txt", "w") as file:
        file.write("[Pendientes]\n")
        for tarea in lista_pendientes.get(0, tk.END):
            file.write(tarea + "\n")
        file.write("[Completadas]\n")
        for tarea in lista_completadas.get(0, tk.END):
            file.write(tarea + "\n")

def cargar_tareas():
    try:
        with open("tareas.txt", "r") as file:
            seccion = None
            for linea in file:
                linea = linea.strip()
                if linea == "[Pendientes]":
                    seccion = lista_pendientes
                elif linea == "[Completadas]":
                    seccion = lista_completadas
                elif seccion is not None:
                    seccion.insert(tk.END, linea)
    except FileNotFoundError:
        pass

root = tk.Tk()
root.title("Gestión de Tareas")
root.geometry("400x500")

entrada_tarea = tk.Entry(root, width=40)
entrada_tarea.pack(pady=10)
entrada_tarea.bind("<Return>", agregar_tarea)

boton_agregar = tk.Button(root, text="Añadir Tarea", command=agregar_tarea)
boton_agregar.pack()

tk.Label(root, text="Tareas Pendientes:").pack()
lista_pendientes = tk.Listbox(root, width=50, height=8)
lista_pendientes.pack(pady=5)

boton_completar = tk.Button(root, text="Marcar como Completada", command=marcar_completada)
boton_completar.pack()

tk.Label(root, text="Tareas Completadas:").pack()
lista_completadas = tk.Listbox(root, width=50, height=8)
lista_completadas.pack(pady=5)

boton_eliminar = tk.Button(root, text="Eliminar Tarea", command=eliminar_tarea)
boton_eliminar.pack()

root.bind("<c>", marcar_completada)
root.bind("<d>", eliminar_tarea)
root.bind("<Delete>", eliminar_tarea)
root.bind("<Escape>", cerrar_app)

cargar_tareas()

root.mainloop()