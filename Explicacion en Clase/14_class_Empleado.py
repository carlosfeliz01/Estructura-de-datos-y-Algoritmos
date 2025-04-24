class Empleado:
    def __init__(self):
        self.nombre = input("Ingrese el nombre del empleado: ")
        self.sueldo = float(input("Ingrese el sueldo del empleado: "))  

    def Imprimir(self):
        print("Nombre del empleado:", self.nombre)
        print("Sueldo del empleado:", self.sueldo)
        print("***********************************************")
    
    def paga_impuestos(self):
        if self.sueldo > 20000:
            print("El empleado paga impuestos")
        else:
            print("El empleado no paga impuestos")

#programa principal
empleado1 = Empleado() #creando un objeto de la clase Empleado
empleado1.Imprimir() #imprimiendo el valor del atributo Nombre
empleado1.paga_impuestos() #imprimiendo el valor del atributo Nombre