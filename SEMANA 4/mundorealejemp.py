class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"'{self.titulo}' por {self.autor} (ISBN: {self.isbn}) - Estado: {estado}"

    def cambiar_estado(self):
        self.disponible = not self.disponible


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def prestar_libro(self, libro):
        if libro.disponible:
            self.libros_prestados.append(libro)
            libro.cambiar_estado()
            print(f"{self.nombre} ha prestado el libro '{libro.titulo}'.")
        else:
            print(f"El libro '{libro.titulo}' no está disponible.")

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)
            libro.cambiar_estado()
            print(f"{self.nombre} ha devuelto el libro '{libro.titulo}'.")
        else:
            print(f"{self.nombre} no tiene el libro '{libro.titulo}' prestado.")


class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.catalogo = []

    def agregar_libro(self, libro):
        self.catalogo.append(libro)

    def mostrar_catalogo(self):
        print(f"\nCatálogo de la Biblioteca '{self.nombre}':")
        for i, libro in enumerate(self.catalogo, start=1):
            print(f"{i}. {libro.mostrar_informacion()}")

    def buscar_libro(self, titulo):
        for libro in self.catalogo:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None


# Menú interactivo
def menu():
    biblioteca = Biblioteca("Biblioteca Digital")
    biblioteca.agregar_libro(Libro("Cien Años de Soledad", "Gabriel García Márquez", "1234567890"))
    biblioteca.agregar_libro(Libro("1984", "George Orwell", "9876543210"))
    biblioteca.agregar_libro(Libro("El Principito", "Antoine de Saint-Exupéry", "1122334455"))

    usuario = Usuario("Juan Pérez", "U001")

    while True:
        print("\n--- Menú Biblioteca ---")
        print("1. Ver catálogo")
        print("2. Buscar libro")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            biblioteca.mostrar_catalogo()

        elif opcion == "2":
            titulo = input("Ingresa el título del libro que deseas buscar: ")
            libro = biblioteca.buscar_libro(titulo)
            if libro:
                print(libro.mostrar_informacion())
            else:
                print(f"El libro '{titulo}' no está en el catálogo.")

        elif opcion == "3":
            titulo = input("Ingresa el título del libro que deseas prestar: ")
            libro = biblioteca.buscar_libro(titulo)
            if libro:
                usuario.prestar_libro(libro)
            else:
                print(f"El libro '{titulo}' no está en el catálogo.")

        elif opcion == "4":
            titulo = input("Ingresa el título del libro que deseas devolver: ")
            libro = biblioteca.buscar_libro(titulo)
            if libro:
                usuario.devolver_libro(libro)
            else:
                print(f"El libro '{titulo}' no está en el catálogo.")

        elif opcion == "5":
            print("¡Gracias por usar la Biblioteca Digital! Hasta pronto.")
            break

        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Inicia el programa
menu()
