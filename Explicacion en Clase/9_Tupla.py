tupla =(1,2,3)
fecha = (2023, "Diciembre", 23)
coordenadas = (10.0, 20.0)
persona = ("Juan", "Perez", 25, "Ingeniero")
cedula=("001-000000-0","001-000000-1","001-000000-2")
print("tupla:", tupla)
print("fecha:", fecha)
print("coordenadas:", coordenadas)
print("persona:", persona)
print("cedula:", cedula)
print("la longitud de la tupla es:", len(tupla))#Longitud de la tupla
print("tupla[0]:", tupla[0]+1) #Acceso a un elemento de la tupla
print("tupla[0]:", tupla[0]) #Acceso a un elemento de la tupla


#METODOS MAS USADOS:
#count, index, len, min, max, sum, sorted, reversed, tuple
#count: Devuelve el numero de veces que un elemento aparece en la tupla
print("Metodo count: tupla.count(1) ")
print("El numero 1 aparece:", tupla.count(1), "veces en la tupla")

#index: Devuelve la posicion de un elemento en la tupla
print("Metodo index: tupla.index(1) ")
print("La posicion de 1 es:", tupla.index(1))

#len: Devuelve la longitud de la tupla
print("Metodo len: len(tupla) ")
print("La longitud de la tupla es:", len(tupla))

#min: Devuelve el elemento menor de la tupla
print("Metodo min: min(tupla) ")
print("El elemento menor de la tupla es:", min(tupla))

#max: Devuelve el elemento mayor de la tupla
print("Metodo max: max(tupla) ")
print("El elemento mayor de la tupla es:", max(tupla))

#sum: Devuelve la suma de los elementos de la tupla
print("Metodo sum: sum(tupla) ")
print("La suma de los elementos de la tupla es:", sum(tupla))

#sorted: Devuelve una lista con los elementos de la tupla ordenados
print("Metodo sorted: sorted(tupla) ")
print("Los elementos de la tupla ordenados son:", sorted(tupla))

#reversed: Devuelve una lista con los elementos de la tupla en orden inverso
print("Metodo reversed: list(reversed(tupla)) ")
tupla_reversed = list(reversed(tupla))
print("Los elementos de la tupla en orden inverso son:", tupla_reversed)

#tuple: Convierte una lista en una tupla
print("Metodo tuple: tuple([1,2,3]) ")
mi_lista = [1, 2, 3]
mi_tupla = tuple(mi_lista)
print("La lista convertida en tupla es:", mi_tupla)

