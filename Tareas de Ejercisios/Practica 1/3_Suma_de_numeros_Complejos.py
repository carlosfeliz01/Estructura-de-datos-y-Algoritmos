#3. Suma de dos numeros complejos, pidele al usuario dos numeros complejos y luego imprime el resultado de la suma

def suma_numeros_complejos(complejo1, complejo2):
    suma = complejo1 + complejo2
    return suma 

print("Suma de dos numeros complejos")
# Pedir los numeros complejos al usuario
complejo1 = complex(input("Por favor ingrese el primer numero complejo (ejemplo: 1+2j): "))
complejo2 = complex(input("Por favor ingrese el segundo numero complejo (ejemplo: 3+4j): "))
suma = suma_numeros_complejos(complejo1, complejo2)
print("La suma de los numeros complejos es:", suma)