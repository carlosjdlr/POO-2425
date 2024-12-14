# Programación Tradicional

def ingresar_temperaturas():
    """Solicita al usuario que ingrese las temperaturas diarias de la semana."""
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio(temperaturas):
    """Calcula el promedio de una lista de temperaturas."""
    return sum(temperaturas) / len(temperaturas)

def main_tradicional():
    """Función principal para la solución en programación tradicional."""
    print("\n=== Programación Tradicional ===")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de temperaturas es: {promedio:.2f} °C")

# Programación Orientada a Objetos (POO)

class Clima:
    """Clase que representa las temperaturas diarias y calcula su promedio semanal."""
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperaturas(self):
        """Solicita al usuario que ingrese las temperaturas diarias de la semana."""
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        """Calcula el promedio semanal de las temperaturas."""
        if not self.temperaturas:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)

def main_poo():
    """Función principal para la solución en programación orientada a objetos."""
    print("\n=== Programación Orientada a Objetos ===")
    clima = Clima()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()
    print(f"El promedio semanal de temperaturas es: {promedio:.2f} °C")

# Ejecución de ambas implementaciones
if __name__ == "__main__":
    main_tradicional()
    main_poo()
