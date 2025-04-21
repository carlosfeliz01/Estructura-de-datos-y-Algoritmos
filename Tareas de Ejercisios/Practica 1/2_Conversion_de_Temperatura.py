#2. Convertir temperatura de Celsius a Fahrenheit, pidele al usuario la temperatura en Celsius y luego imprime el resultado en Fahrenheit

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

print("Convertir temperatura de Celsius a Fahrenheit")
# Pedir la temperatura en Celsius al usuario
celsius = float(input("Por favor ingrese la temperatura en Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print("La temperatura en Fahrenheit es:", fahrenheit)   
