#10. Escribe un programa que sume dos números ingresados por el usuario hasta que el usuario ingrese "0" para salir.

def suma_dos_numeros():
    while True:
        try:
            num1 = int(input("Ingrese el primer número: "))
            if num1 == 0:
                salir()
                break
            num2 = int(input("Ingrese el segundo número: "))
            if num2 == 0:
                salir()
                break
            suma = num1 + num2
            print(f"La suma de {num1} y {num2} es: {suma}")
        except ValueError:
            print("❗ Error: Por favor, ingrese un número válido.")
        except Exception as e:
            print(f"❗ Error inesperado: {e}")  

def salir():
    print("👋 Saliendo del programa...")

print("Programa para sumar dos números")
print("Ingrese '0' para salir en cualquier momento.") 
suma_dos_numeros()
# Fin del programa