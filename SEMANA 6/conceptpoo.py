# Clase base que representa un Vehículo
class Vehiculo:
    def __init__(self, marca, modelo, año):
        self._marca = marca  # Atributo encapsulado
        self._modelo = modelo
        self._año = año

    def mostrar_informacion(self):
        """Método para mostrar la información del vehículo."""
        return f"{self._marca} {self._modelo} ({self._año})"

    def arrancar(self):
        """Método genérico para arrancar un vehículo."""
        return "El vehículo está arrancando."


# Clase derivada que representa un Auto
class Auto(Vehiculo):
    def __init__(self, marca, modelo, año, tipo_auto):
        super().__init__(marca, modelo, año)
        self.tipo_auto = tipo_auto

    def arrancar(self):
        """Método sobrescrito para especificar el arranque de un auto."""
        return f"El auto {self.mostrar_informacion()} está arrancando con suavidad."


# Clase derivada que representa una Moto
class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, tipo_moto):
        super().__init__(marca, modelo, año)
        self.tipo_moto = tipo_moto

    def arrancar(self):
        """Método sobrescrito para especificar el arranque de una moto."""
        return f"La moto {self.mostrar_informacion()} está arrancando rápidamente."


# Función principal para demostrar el programa
def main():
    # Crear instancias de Auto y Moto
    auto1 = Auto("Toyota", "Corolla", 2021, "Sedán")
    moto1 = Moto("Yamaha", "MT-03", 2022, "Deportiva")

    # Demostrar funcionalidad de las clases
    print(auto1.mostrar_informacion())  # Uso de un método heredado
    print(auto1.arrancar())  # Polimorfismo en acción
    print(moto1.mostrar_informacion())  # Uso de un método heredado
    print(moto1.arrancar())  # Polimorfismo en acción

    # Ejemplo de acceso a atributos encapsulados
    print(f"Marca del auto: {auto1._marca}")  # No recomendado, pero permitido
    print(f"Marca de la motocicleta: {moto1._marca}")

if __name__ == "__main__":
    main()
