import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")

def mark_completed():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        task_text = listbox_tasks.get(selected_task_index)
        listbox_tasks.delete(selected_task_index)
        listbox_tasks.insert(selected_task_index, f"✔ {task_text}")
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

def add_task_enter(event):
    add_task()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("400x400")

# Entrada de texto para nuevas tareas
entry_task = tk.Entry(root, width=40)
entry_task.pack(pady=10)
entry_task.bind("<Return>", add_task_enter)  # Permitir añadir tarea con Enter

# Botones
frame_buttons = tk.Frame(root)
frame_buttons.pack()
btn_add = tk.Button(frame_buttons, text="Añadir Tarea", command=add_task)
btn_add.pack(side=tk.LEFT, padx=5)
btn_complete = tk.Button(frame_buttons, text="Marcar como Completada", command=mark_completed)
btn_complete.pack(side=tk.LEFT, padx=5)
btn_delete = tk.Button(frame_buttons, text="Eliminar Tarea", command=delete_task)
btn_delete.pack(side=tk.LEFT, padx=5)

# Listbox para mostrar las tareas
listbox_tasks = tk.Listbox(root, width=50, height=15)
listbox_tasks.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()
