#5. Pidele al usuario que ingrese dos numeros y luego imprime la suma, resta, multiplicacion y division de esos dos numeros

def operaciones_aritmeticas(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2 if num2 != 0 else "Error: Division por cero"
    
    return suma, resta, multiplicacion, division

print("Operaciones Aritmeticas")
# Pedir los numeros al usuario
num1 = float(input("Por favor ingrese el primer numero: "))
num2 = float(input("Por favor ingrese el segundo numero: "))    

# Llamar a la funcion y mostrar los resultados
suma, resta, multiplicacion, division = operaciones_aritmeticas(num1, num2) 
print("La suma es:", suma)
print("La resta es:", resta)
print("La multiplicacion es:", multiplicacion)
print("La division es:", division)