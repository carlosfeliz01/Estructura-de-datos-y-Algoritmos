#clase padre
class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
    
    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}")

    def encender(self):
        print("El vehículo está encendido.")

    def acelerar(self):
        print("El vehículo está acelerando...")

    def frenar(self):
        print("El vehículo está frenando...")
    
    def apagar(self):
        print("El vehículo está apagado.")

    

#clase hija : Auto
#ejemplo de herencia simple, donde la clase hija hereda de la clase padre Vehiculo y sus metodos modificados

class Auto(Vehiculo):
    def encender(self):
        print(f"Encendiendo el auto {self.marca} {self.modelo}...")
    def acelerar(self):
        print(f"El auto {self.marca} {self.modelo} está acelerando...") 
    def frenar(self):
        print(f"El auto {self.marca} {self.modelo} está frenando...")
    def apagar(self):
        print(f"Apagando el auto {self.marca} {self.modelo}...")

class Motocicleta(Vehiculo):
    def encender(self):
        print(f"Encendiendo la motocicleta {self.marca} {self.modelo}...")
    def acelerar(self):
        print(f"El auto {self.marca} {self.modelo} está acelerando...") 
    def frenar(self):
        print(f"El auto {self.marca} {self.modelo} está frenando...")
    def apagar(self):
        print(f"Apagando el auto {self.marca} {self.modelo}...")

class Camioneta(Vehiculo):
    def encender(self):
        print(f"Encendiendo la camioneta {self.marca} {self.modelo}...")
    def acelerar(self):
        print(f"El auto {self.marca} {self.modelo} está acelerando...") 
    def frenar(self):
        print(f"El auto {self.marca} {self.modelo} está frenando...")
    def apagar(self):
        print(f"Apagando el auto {self.marca} {self.modelo}...")

#creando objetos de las clases hijas
auto1 = Auto("Toyota", "Corolla", 2020)
moto1 = Motocicleta("Honda", "CBR", 2019)
camioneta1 = Camioneta("Ford", "F-150", 2021)

#mostrando la información de los vehículos
auto1.mostrar_info()
auto1.encender()
auto1.acelerar()
auto1.frenar()
auto1.apagar()

moto1.mostrar_info()
moto1.encender()
moto1.acelerar()
moto1.frenar()
moto1.apagar()

camioneta1.mostrar_info()
camioneta1.encender()
camioneta1.acelerar()
camioneta1.frenar()
camioneta1.apagar()
        