class Persona:#definicion de la clase Persona o plantilla
    def NombrePersona(self, nombre):#metodo para asignar un valor al atributo Nombre
        self.Nombre= nombre#atributo Nombre
    def EdadPersona(self, edad):#metodo para asignar un valor al atributo Edad
        self.Edad= edad#atributo Edad
    def cedulaPersona(self, cedula):#metodo para asignar un valor al atributo Cedula
        self.Cedula= cedula#atributo Cedula
        

    def imprimir(self):#metodo para imprimir el valor del atributo Nombre
        print("El nombre es: ", self.Nombre)
        print("La edad es: ", self.Edad)
        print("La cedula es: ", self.Cedula)
        print("***********************************************")
#Fin de la clase Persona

#programa principal

persona1 = Persona() #creando un objeto de la clase Persona
persona1.NombrePersona("Juan") #asignando un valor al atributo Nombre
persona1.EdadPersona(25) #asignando un valor al atributo Edad
persona1.cedulaPersona("001-000000-0") #asignando un valor al atributo Cedula
persona1.imprimir() #imprimiendo el valor del atributo Nombre


jaime = Persona() #creando un objeto de la clase Persona
jaime.NombrePersona("Jaime") #asignando un valor al atributo Nombre
jaime.EdadPersona(30) #asignando un valor al atributo Edad
jaime.cedulaPersona("001-000000-1") #asignando un valor al atributo Cedula
jaime.imprimir() #imprimiendo el valor del atributo Nombre
