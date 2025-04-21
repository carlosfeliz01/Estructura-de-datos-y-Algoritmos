#8. Escribe un programa que determine si un número entero es par o impar.
#   a. Si es par, imprima el mensaje "El número es par".   
#   b. Si es impar, imprima el mensaje "El número es impar".

def determinar_par_impar(numero):
    if numero % 2 == 0:
        return "El número es par"
    else:
        return "El número es impar" 

print("Programa para determinar si un número es par o impar")
numero = int(input("Ingrese un número entero: "))
resultado = determinar_par_impar(numero)
print(resultado)