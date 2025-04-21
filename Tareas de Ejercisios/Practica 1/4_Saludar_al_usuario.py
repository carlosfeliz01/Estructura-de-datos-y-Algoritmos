#4. Pedirle al suario su nombre y luego imprimir un saludo personalizado

def saludar_usuario(nombre):
    saludo = "Hola, " + nombre + "! Bienvenido/a."
    return saludo

nombre = input("Por favor, ingrese su nombre: ")
# Llamar a la función y mostrar el saludo 
print(saludar_usuario(nombre))
