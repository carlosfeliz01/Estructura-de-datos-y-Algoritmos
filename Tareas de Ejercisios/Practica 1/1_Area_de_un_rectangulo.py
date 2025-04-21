#1.calcular el area de un rectangulo, pedirle al usuario la base y la altura y luego imprimir el resultado

# Definicion de la funcion
def area_rectangulo(base, altura):
    area = base * altura
    return area

print("Calcular el area de un rectangulo")
# Pedir la base y la altura al usuario
base = float(input("Por favor ingrese la base del rectangulo: "))
altura = float(input("Por favor ingrese la altura del rectangulo:"))
area = area_rectangulo(base, altura)
print("El area del rectangulo es:", area)
