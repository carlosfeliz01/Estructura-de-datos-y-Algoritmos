def mostrar_mensaje(mensaje):
    print("**************************************************")
    print(mensaje)
    print("**************************************************")

def cargar_suma():
    valor1 = int(input("Ingrese el primer valor: "))
    valor2 = int(input("Ingrese el segundo valor: "))
    suma = valor1 + valor2
    print("La suma de los valores es:", suma)

#programa principal
mostrar_mensaje("El programa ha comenzado")
cargar_suma()
mostrar_mensaje("El programa ha terminado")