# Programa para calcular el área y el perímetro de un rectángulo.
# Utiliza tipos de datos como integer, float, string y boolean.

def calcular_area(base, altura):
    """Calcula el área de un rectángulo dado su base y altura."""
    return base * altura

def calcular_perimetro(base, altura):
    """Calcula el perímetro de un rectángulo dado su base y altura."""
    return 2 * (base + altura)

# Solicitar datos al usuario
print("¡Bienvenido al programa de cálculo de rectángulos!")

# Variables de entrada
base = float(input("Ingrese la base del rectángulo (en metros): "))
altura = float(input("Ingrese la altura del rectángulo (en metros): "))

# Cálculos
area = calcular_area(base, altura)
perimetro = calcular_perimetro(base, altura)

# Mostrar resultados
print("\nResultados:")
print(f"Área del rectángulo: {area} metros cuadrados")
print(f"Perímetro del rectángulo: {perimetro} metros")

# Verificación: comprobar si el rectángulo es un cuadrado
es_cuadrado = base == altura
if es_cuadrado:
    print("Nota: Este rectángulo es un cuadrado.")
else:
    print("Nota: Este rectángulo no es un cuadrado.")
