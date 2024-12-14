## Ejemplos de Técnicas de Programación: Abstracción, Encapsulación, Herencia y Polimorfismo

# Abstracción
# Ejemplo: Clase abstracta y métodos abstractos
from abc import ABC, abstractmethod

class Vehiculo(ABC):
    @abstractmethod
    def moverse(self):
        pass

    @abstractmethod
    def detenerse(self):
        pass

class Automovil(Vehiculo):
    def moverse(self):
        return "El automóvil está en movimiento."

    def detenerse(self):
        return "El automóvil se ha detenido."

# Encapsulación
# Ejemplo: Uso de atributos privados y métodos getter y setter
class Cuenta:
    def __init__(self, saldo):
        self.__saldo = saldo

    def obtener_saldo(self):
        return self.__saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            return f"Depósito exitoso. Nuevo saldo: {self.__saldo}"
        return "Cantidad inválida."

# Herencia
# Ejemplo: Clase base y clase derivada con métodos extendidos
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def sonido(self):
        return "Sonido genérico"

class Perro(Animal):
    def sonido(self):
        return f"{self.nombre} dice: Guau"

# Polimorfismo
# Ejemplo: Uso de métodos con el mismo nombre en diferentes clases
class Gato(Animal):
    def sonido(self):
        return f"{self.nombre} dice: Miau"

animales = [Perro("Rex"), Gato("Luna")]
for animal in animales:
    print(animal.sonido())
