#3. Crea una calculadora usando funciones y muestra el resultado de una suma, resta, multiplicacion y division
def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division por cero"
def mostrar_menu():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def calculadora():
    print("Calculadora:")
    mostrar_menu()
    operacion = input("Ingresa un numero del 1 al 5 para elegir la opción deseada: ")
    
    while operacion not in ["1", "2", "3", "4", "5"]:
        print("❗ Error: Opción no valida, Por favor ingrese un numero del 1 al 5")
        mostrar_menu()  
        operacion = input("Ingresa un numero del 1 al 5 para elegir la opción deseada: ")          

    a = float(input("Ingresa el primer numero: "))
    b = float(input("Ingresa el segundo numero: "))
    if operacion == "1":
        print(f"Resultado de la suma: {suma(a, b)}")
    elif operacion == "2":
        print(f"Resultado de la resta: {resta(a, b)}")
    elif operacion == "3":
        print(f"Resultado de la multiplicacion: {multiplicacion(a, b)}")
    elif operacion == "4":
        print(f"Resultado de la divicion: {division(a, b)}")
    else:
        print("Saliendo de la calculadora...")
        
calculadora()