import random
print("1- Imprimir numeros aleatorios")
#Generar un numero aleatorio entre 1 y 100
numero = random.randint(1, 100)
print("El numero aleatorio es: ", numero)


#Generar 5 numeros aleatorios entre 1 y 100
print("2- Imprimir 5 numeros aleatorios")
for i in range(5):
    numero = random.randint(1, 100)
    print("El numero aleatorio es: ", numero)

#Generar 5 numeros aleatorios entre 1 y 10 sin repetir
print("3- Imprimir 5 numeros aleatorios sin repetir con for")
#Se utiliza una lista para almacenar los numeros elegidos
Elegidos = []
for i in range(5):
    numero = random.randint(1, 10)
    if numero in Elegidos:
        print("El numero ",numero," ya fue elegido")
    else:
        Elegidos.append(numero)
        print("El numero aleatorio es: ", numero)

#Generar 5 numeros aleatorios entre 1 y 10 sin repetir
print("4- Imprimir 5 numeros aleatorios sin repetir con while")
#while
contador=1
Elegidos.clear() #Limpiamos la lista Elegidos   
while contador <=5:
    numero = random.randint(1, 10)
    if numero not in Elegidos:
        Elegidos.append(numero)
        print("Contador: ",contador, " Numero aleatorio: ", numero)
        contador+=1 
#    else:
#        print("El numero ",numero," ya fue elegido")