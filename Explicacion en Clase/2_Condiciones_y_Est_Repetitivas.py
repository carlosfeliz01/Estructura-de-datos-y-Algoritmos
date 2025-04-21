#CONDICIONES

edad=int(input("Ingrese su edad:"))

if edad<edad:
    print("Eres menor de edad. ")
elif edad  == 18:
    print("acabo de cumplir 18")
else:
    print("eres mayor de edad")

#ESTRUCTURA REPETITIVAS:

#for
fruta=["Manzana","Pera","Naranja"]
for fruta in fruta:
    print(fruta)

#while
contador=0
while contador <=5:
    print("Contador: ",contador)
    #contador=contador+1
    contador+=1 #Esta opcion es mas optima

#while con tipo estructura Switch

while True:
    opcion = input ("Elige una opción (1-3, o elija 0 para salir): ")

    if opcion =="1":
        print("Opción 1 Seleccionada.")
    elif opcion =="2":
        print("Opción 2 Seleccionada.")
    elif opcion =="3":
        print("Opción 3 Seleccionada.")
    elif opcion =="0":
        print("👋 Saliendo del programa...")
        break
    else:
        print("❓ Opción no válida. Intenta de nuevo.")

