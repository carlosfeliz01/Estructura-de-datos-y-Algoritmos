#7. Escribe un programa que determine el valor de una variable entera, si es mayor que 0, menor que 0 o igual a 0.
#   a. Si es mayor que 0, imprima el mensaje "El número es positivo".
#   b. Si es menor que 0, imprima el mensaje "El número es negativo".
#   c. Si es igual a 0, imprima el mensaje "El número es cero".

def determinar_valor(numero):
    if numero > 0:
        return "El número es positivo"
    elif numero < 0:
        return "El número es negativo"
    else:
        return "El número es cero"

print("Programa para determinar el valor de un número es positivo, negativo o cero")
numero = int(input("Ingrese un número entero: "))
resultado = determinar_valor(numero)
print(resultado)