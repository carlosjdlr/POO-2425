import json


class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def to_dict(self):
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }


class Inventario:
    def __init__(self):
        self.productos = {}
        self.cargar_desde_archivo()

    def agregar_producto(self, producto):
        self.productos[producto.id_producto] = producto
        self.guardar_en_archivo()

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].actualizar_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].actualizar_precio(precio)
            self.guardar_en_archivo()

    def buscar_producto(self, nombre):
        return [p.to_dict() for p in self.productos.values() if nombre.lower() in p.nombre.lower()]

    def mostrar_productos(self):
        return [p.to_dict() for p in self.productos.values()]

    def guardar_en_archivo(self, archivo="inventario.json"):
        with open(archivo, "w") as f:
            json.dump([p.to_dict() for p in self.productos.values()], f, indent=4)

    def cargar_desde_archivo(self, archivo="inventario.json"):
        try:
            with open(archivo, "r") as f:
                datos = json.load(f)
                for d in datos:
                    self.productos[d["id_producto"]] = Producto(
                        d["id_producto"], d["nombre"], d["cantidad"], d["precio"])
        except FileNotFoundError:
            pass


# Interfaz de usuario

def menu():
    inventario = Inventario()
    while True:
        print("\n--- Sistema de Gestión de Inventario ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))
            print("Producto agregado con éxito.")
        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
            print("Producto eliminado.")
        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (deje en blanco para no cambiar): ")
            precio = input("Nuevo precio (deje en blanco para no cambiar): ")
            inventario.actualizar_producto(id_producto, int(cantidad) if cantidad else None,
                                           float(precio) if precio else None)
            print("Producto actualizado.")
        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            print("Resultados:", resultados)
        elif opcion == "5":
            productos = inventario.mostrar_productos()
            print("Inventario:", productos)
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intente nuevamente.")


if __name__ == "__main__":
    menu()
