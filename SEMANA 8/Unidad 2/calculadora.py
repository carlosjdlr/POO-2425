# Programa que suma los números ingresados por el usuario

def sumar_numeros():
    total = 0
    while True:
        try:
            numero = input("Ingresa un número (o escribe 'salir' para terminar): ")
            if numero.lower() == 'salir':
                break
            total += float(numero)
        except ValueError:
            print("Eso no es un número válido, por favor intenta de nuevo.")
    
    print(f"La suma total es: {total}")

sumar_numeros()
