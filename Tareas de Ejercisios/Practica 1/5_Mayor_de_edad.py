#5. Pedile al usuario su edad y luego imprime si es mayor de edad o no

def es_mayor_de_edad(edad):
    if edad >= 18:
        print("Eres mayor de edad.")
    else:
        print("Eres menor de edad.")  
    
Mi_edad = int(input("Por favor, ingrese su edad: "))
# Llamar a la función y mostrar el resultado
es_mayor_de_edad(Mi_edad)