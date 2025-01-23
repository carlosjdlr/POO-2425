class Usuario:
    def __init__(self, nombre, edad, correo):
        """Constructor: Inicializa los atributos del usuario."""
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        print(f"Usuario {self.nombre} creado.")

    def mostrar_informacion(self):
        """Muestra la información del usuario."""
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Correo: {self.correo}"


class GestorUsuarios:
    def __init__(self, archivo_datos):
        """Constructor: Abre o crea el archivo para almacenar usuarios."""
        self.archivo_datos = archivo_datos
        self.archivo = open(archivo_datos, 'a+')
        print(f"Gestor de usuarios iniciado con el archivo '{archivo_datos}'.")

    def agregar_usuario(self, usuario):
        """Agrega un usuario al archivo de datos."""
        datos_usuario = f"{usuario.nombre},{usuario.edad},{usuario.correo}\n"
        self.archivo.write(datos_usuario)
        print(f"Usuario {usuario.nombre} agregado al archivo.")

    def listar_usuarios(self):
        """Lista todos los usuarios almacenados en el archivo."""
        self.archivo.seek(0)  # Volver al inicio del archivo
        print("Usuarios registrados:")
        for linea in self.archivo:
            nombre, edad, correo = linea.strip().split(',')
            print(f"- Nombre: {nombre}, Edad: {edad}, Correo: {correo}")

    def __del__(self):
        """Destructor: Cierra el archivo al finalizar."""
        if self.archivo:
            self.archivo.close()
            print(f"Archivo '{self.archivo_datos}' cerrado correctamente.")


# Programa principal
if __name__ == "__main__":
    gestor = GestorUsuarios("usuarios.txt")

    # Crear usuarios
    usuario1 = Usuario("Ana Pérez", 28, "ana.perez@example.com")
    usuario2 = Usuario("Carlos Gómez", 35, "carlos.gomez@example.com")

    # Agregar usuarios al archivo
    gestor.agregar_usuario(usuario1)
    gestor.agregar_usuario(usuario2)

    # Listar usuarios
    gestor.listar_usuarios()

    # Eliminar el gestor para forzar la llamada al destructor
    del gestor