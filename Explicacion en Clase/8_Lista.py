#definir una lista que almacene 5 numeros enteros, sumar todos los elementos y mostrar dicha suma

numeros = [1, 2, 3, 4, 5]
suma = 0    
for i in range(len(numeros)):
    suma += numeros[i]
print("La suma de los elementos de la lista es:", suma)


#version de la clase
mi_lista=[10,20,30,40,50]
suma=0
x=0
while x < len(mi_lista):
    suma+=mi_lista[x]
    x+=1    
print("los elementos de la lista son:", mi_lista)
print("La suma de los elementos de la lista es:", suma)

#METODOS MAS USADOS:
#append, insert, pop, remove, clear, sort, reverse, index, count, reversed, extend, copy

#append: Agrega un elemento al final de la lista
print("Metodo append: mi_lista.append(60) ")
mi_lista.append(60)
print("los elementos de la lista son:", mi_lista)

#insert: Agrega un elemento en una posicion especifica de la lista
print("Metodo insert: mi_lista.insert(2,70) ")
mi_lista.insert(2,70)
print("los elementos de la lista son:", mi_lista)

#pop: Elimina el ultimo elemento de la lista y lo devuelve
print("Metodo pop: mi_lista.pop() ")
mi_lista.pop()
print("los elementos de la lista son:", mi_lista)

#remove: Elimina un elemento especifico de la lista
print("Metodo remove: mi_lista.remove(30) ")
mi_lista.remove(30)
print("los elementos de la lista son:", mi_lista)

#sort: Ordena la lista de menor a mayor
print("Metodo sort: mi_lista.sort() ")
mi_lista.sort()
print("los elementos de la lista son:", mi_lista)

#reverse: Invierte el orden de los elementos de la lista
print("Metodo reverse: mi_lista.reverse() ")
mi_lista.reverse()
print("los elementos de la lista son:", mi_lista)

#index: Devuelve la posicion de un elemento en la lista
print("Metodo index: mi_lista.index(20) ")
print("La posicion de 20 es:", mi_lista.index(20))

#reversed: Devuelve una lista con los elementos en orden inverso
print("Metodo reversed: list(reversed(mi_lista)) ")
mi_lista_reversed = list(reversed(mi_lista))
print("los elementos de la lista son:", mi_lista_reversed)

#count: Devuelve la cantidad de veces que un elemento aparece en la lista
print("Metodo count: mi_lista.count(10) ")
print("El numero 10 aparece:", mi_lista.count(10), "veces en la lista")

#extend: Agrega los elementos de otra lista al final de la lista
print("Metodo extend: mi_lista.extend([80,90]) ")
mi_lista.extend([80,90])
print("los elementos de la lista son:", mi_lista)

#copy: Crea una copia de la lista
print("Metodo copy: mi_lista.copy() ")
mi_lista_copia = mi_lista.copy()
print("los elementos de la lista copia son:", mi_lista_copia)

#clear: Elimina todos los elementos de la lista
print("Metodo clear: mi_lista.clear() ")    
mi_lista.clear()
print("los elementos de la lista son:", mi_lista)
