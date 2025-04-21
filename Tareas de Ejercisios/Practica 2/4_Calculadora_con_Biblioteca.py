#4. Crear una calculadora usando funciones y una biblioteca externa para realizar las operaciones matematicas.
#   - Importar la biblioteca math para realizar operaciones matematicas avanzadas.
#   - crear funciones con la libreria math para realizar operaciones como raiz cuadrada, potencia, seno, coseno y tangente.
#   - Crear un menu para que el usuario elija la operacion deseada y mostrar el resultado.
#   - Manejar errores de entrada del usuario y mostrar mensajes de error adecuados.

import math as m

operaciones = {
    "1": "Raiz Cuadrada",
    "2": "Potencia",
    "3": "Seno",
    "4": "Coseno",
    "5": "Tangente",
    "6": "Salir"
}

def mostrar_menu():
    print("Calculadora Avanzada")
    print("Seleccione una operación:")
    for key, value in operaciones.items():
        print(f"{key}. {value}")    

def raiz_cuadrada(numero):
    if numero < 0:
        raise ValueError("❗ Error: No se puede calcular la raíz cuadrada de un número negativo.")
    return m.sqrt(numero)
def potencia(base, exponente):
    return m.pow(base, exponente)
def seno(angulo):
    return m.sin(m.radians(angulo))
def coseno(angulo):
    return m.cos(m.radians(angulo))
def tangente(angulo):
    return m.tan(m.radians(angulo))
def calcular():
    while True:
        mostrar_menu()
        operacion = input("Ingrese el número de la operación deseada: ")
        
        if operacion == "1":
            numero = float(input("Ingrese un número: "))
            resultado = raiz_cuadrada(numero)
            print(f"La raíz cuadrada de {numero} es: {resultado}")
            break
        elif operacion == "2":
            base = float(input("Ingrese la base: "))
            exponente = float(input("Ingrese el exponente: "))
            resultado = potencia(base, exponente)
            print(f"{base} elevado a {exponente} es: {resultado}")
            break
        elif operacion == "3":
            angulo = float(input("Ingrese el ángulo en grados: "))
            resultado = seno(angulo)
            print(f"El seno de {angulo} grados es: {resultado}")
            break
        elif operacion == "4":
            angulo = float(input("Ingrese el ángulo en grados: "))
            resultado = coseno(angulo)
            print(f"El coseno de {angulo} grados es: {resultado}")
            break
        elif operacion == "5":
            angulo = float(input("Ingrese el ángulo en grados: "))
            resultado = tangente(angulo)
            print(f"La tangente de {angulo} grados es: {resultado}")
            break
        elif operacion == "6":
            print("👋 Saliendo de la calculadora...")   
            break
        else:
            print("❗ Error: Opción no válida, por favor ingrese un número del 1 al 6.")

calcular()  

# Fin del programa


