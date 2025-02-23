
# inventario.py

import os
import json


class Inventario:
    ARCHIVO_INVENTARIO = "inventario.txt"

    def __init__(self):
        self.productos = []
        self.cargar_desde_archivo()

    def agregar_producto(self, producto):
        if any(p["id"] == producto.get_id() for p in self.productos):
            print("Error: El ID del producto ya existe.")
            return

        self.productos.append({
            "id": producto.get_id(),
            "nombre": producto.get_nombre(),
            "cantidad": producto.get_cantidad(),
            "precio": producto.get_precio()
        })
        self.guardar_en_archivo()
        print("Producto agregado exitosamente.")

    def eliminar_producto(self, id_producto):
        self.productos = [p for p in self.productos if p["id"] != id_producto]
        self.guardar_en_archivo()
        print("Producto eliminado si existía.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p["id"] == id_producto:
                if cantidad is not None:
                    p["cantidad"] = cantidad
                if precio is not None:
                    p["precio"] = precio
                self.guardar_en_archivo()
                print("Producto actualizado.")
                return
        print("Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        return [p for p in self.productos if nombre.lower() in p["nombre"].lower()]

    def mostrar_productos(self):
        for p in self.productos:
            print(f"ID: {p['id']}, Nombre: {p['nombre']}, Cantidad: {p['cantidad']}, Precio: {p['precio']}")

    def guardar_en_archivo(self):
        try:
            with open(self.ARCHIVO_INVENTARIO, "w") as f:
                json.dump(self.productos, f, indent=4)
        except PermissionError:
            print("Error: No tienes permiso para escribir en el archivo.")
        except Exception as e:
            print(f"Error desconocido al guardar el archivo: {e}")

    def cargar_desde_archivo(self):
        if not os.path.exists(self.ARCHIVO_INVENTARIO):
            return

        try:
            with open(self.ARCHIVO_INVENTARIO, "r") as f:
                self.productos = json.load(f)
        except FileNotFoundError:
            print("Archivo de inventario no encontrado, iniciando con un inventario vacío.")
        except json.JSONDecodeError:
            print("Error al leer el archivo de inventario, formato incorrecto. Se usará un inventario vacío.")
            self.productos = []
        except Exception as e:
            print(f"Error desconocido al cargar el archivo: {e}")
            self.productos = []


# Clase Producto para manejar los datos de productos
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio


