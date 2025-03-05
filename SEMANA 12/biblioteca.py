class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn
        self.disponible = True

    def __str__(self):
        return f"{self.info[0]} de {self.info[1]} (Categoría: {self.categoria}, ISBN: {self.isbn}, Disponible: {'Sí' if self.disponible else 'No'})"


class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.user_id})"

    def mostrar_libros_prestados(self):
        if self.libros_prestados:
            print(f"Libros prestados por {self.nombre}:")
            for libro in self.libros_prestados:
                print(libro)
        else:
            print(f"{self.nombre} no tiene libros prestados.")


class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}

    def agregar_libro(self, libro):
        self.libros[libro.isbn] = libro
        print(f"Libro agregado: {libro}")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print("Libro no encontrado.")

    def registrar_usuario(self, usuario):
        self.usuarios[usuario.user_id] = usuario
        print(f"Usuario registrado: {usuario}")

    def dar_de_baja_usuario(self, user_id):
        if user_id in self.usuarios:
            usuario = self.usuarios[user_id]
            if usuario.libros_prestados:
                print("El usuario tiene libros prestados y no puede ser dado de baja.")
            else:
                del self.usuarios[user_id]
                print(f"Usuario con ID {user_id} eliminado.")
        else:
            print("Usuario no encontrado.")

    def prestar_libro(self, user_id, isbn):
        if user_id in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[user_id]
            libro = self.libros[isbn]
            if libro.disponible:
                usuario.libros_prestados.append(libro)
                libro.disponible = False
                print(f"Libro prestado a usuario {user_id}: {libro}")
            else:
                print("El libro no está disponible.")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, user_id, isbn):
        if user_id in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[user_id]
            libro = self.libros[isbn]
            if libro in usuario.libros_prestados:
                usuario.libros_prestados.remove(libro)
                libro.disponible = True
                print(f"Libro devuelto por usuario {user_id}: {libro}")
            else:
                print("El usuario no tiene prestado ese libro.")
        else:
            print("Usuario o libro no encontrado.")

    def buscar_libro(self, filtro):
        resultados = [libro for libro in self.libros.values() if filtro.lower() in libro.info[0].lower() or filtro.lower() in libro.info[1].lower() or filtro.lower() in libro.categoria.lower()]
        if resultados:
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros.")

    def listar_libros_prestados(self, user_id):
        if user_id in self.usuarios:
            usuario = self.usuarios[user_id]
            usuario.mostrar_libros_prestados()
        else:
            print("Usuario no encontrado.")

    def mostrar_catalogo(self):
        if self.libros:
            print("Catálogo de la biblioteca:")
            for libro in self.libros.values():
                print(libro)
        else:
            print("La biblioteca no tiene libros registrados.")

    def menu(self):
        while True:
            print("\nMenú Biblioteca Digital")
            print("1. Agregar libro")
            print("2. Quitar libro")
            print("3. Registrar usuario")
            print("4. Dar de baja usuario")
            print("5. Prestar libro")
            print("6. Devolver libro")
            print("7. Buscar libro")
            print("8. Mostrar catálogo")
            print("9. Listar libros prestados")
            print("10. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                titulo = input("Título: ")
                autor = input("Autor: ")
                categoria = input("Categoría: ")
                isbn = input("ISBN: ")
                self.agregar_libro(Libro(titulo, autor, categoria, isbn))
            elif opcion == "2":
                isbn = input("ISBN del libro a eliminar: ")
                self.quitar_libro(isbn)
            elif opcion == "3":
                nombre = input("Nombre del usuario: ")
                user_id = input("ID del usuario: ")
                self.registrar_usuario(Usuario(nombre, user_id))
            elif opcion == "4":
                user_id = input("ID del usuario a eliminar: ")
                self.dar_de_baja_usuario(user_id)
            elif opcion == "5":
                user_id = input("ID del usuario: ")
                isbn = input("ISBN del libro: ")
                self.prestar_libro(user_id, isbn)
            elif opcion == "6":
                user_id = input("ID del usuario: ")
                isbn = input("ISBN del libro a devolver: ")
                self.devolver_libro(user_id, isbn)
            elif opcion == "7":
                filtro = input("Ingrese título, autor o categoría: ")
                self.buscar_libro(filtro)
            elif opcion == "8":
                self.mostrar_catalogo()
            elif opcion == "9":
                user_id = input("ID del usuario: ")
                self.listar_libros_prestados(user_id)
            elif opcion == "10":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida.")

# Iniciar la biblioteca con menú interactivo
biblioteca = Biblioteca()
biblioteca.menu()