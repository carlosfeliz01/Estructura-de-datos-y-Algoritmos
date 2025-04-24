#CRUD
#C=reate
#R=ead
#U=pdate
#D=elete

#CRUD= Create, Read, Update, Delete

diccionario = {
    "nombre": "Juan",
    "apellido": "Perez",
    "edad": 25,
    "profesion": "Ingeniero",
    "cedula": "001-000000-0",
    "telefono": "809-555-5555",
    "direccion": "Santo Domingo, RD",
    "correo": "correo@ejemplo.com",
    "fecha_nacimiento": "1998-01-01",
    "nacionalidad": "Dominicana",
    "estado_civil": "Soltero",
    "genero": "Masculino",
    "altura": 1.75,
    "peso": 70
}

print(diccionario)

#accediedo a un elemento del diccionario
print(diccionario["nombre"])

#modificando un elemento del diccionario
print(diccionario["nombre"])
diccionario["nombre"] = "Pedro" #modificando el valor de la clave "nombre"
print(diccionario["nombre"])

#agregando un elemento al diccionario
diccionario["telefono2"] = "809-444-4444" 
print(diccionario["telefono2"])

#eliminando un elemento del diccionario
del diccionario["telefono2"] #eliminando el elemento con la clave "telefono2"
print(diccionario)


#METODOS MAS USADOS:

#keys, values, items, get, pop, popitem, clear, update, setdefault, copy, fromkeys, dict, len, sorted, reversed

#keys: Devuelve una lista con las claves del diccionario
print("Metodo keys: diccionario.keys() ")
print("Las claves del diccionario son:", diccionario.keys())

#values: Devuelve una lista con los valores del diccionario
print("Metodo values: diccionario.values() ")
print("Los valores del diccionario son:", diccionario.values())

#items: Devuelve una lista de tuplas con las claves y valores del diccionario
print("Metodo items: diccionario.items() ")
print("Las claves y valores del diccionario son:", diccionario.items())

#get: Devuelve el valor de una clave especifica del diccionario
print("Metodo get: diccionario.get('nombre') ")
print("El valor de la clave 'nombre' es:", diccionario.get("nombre"))

#pop: Elimina un elemento del diccionario y devuelve su valor
print("Metodo pop: diccionario.pop('nombre') ")
print("El valor de la clave 'nombre' es:", diccionario.pop("nombre")) #eliminando el elemento con la clave "nombre"
print("El diccionario es:", diccionario)

#popitem: Elimina el ultimo elemento del diccionario y devuelve su clave y valor
print("Metodo popitem: diccionario.popitem() ") 
print("El ultimo elemento del diccionario es:", diccionario.popitem()) #eliminando el ultimo elemento del diccionario
print("El diccionario es:", diccionario)    

#Update: Actualiza el diccionario con los elementos de otro diccionario
print("Metodo update: diccionario.update({'telefono': '809-666-6666'}) ")
diccionario.update({"telefono": "809-666-6666"}) #actualizando el diccionario con un nuevo elemento
print("El diccionario es:", diccionario)

#setdefault: Devuelve el valor de una clave especifica del diccionario, si no existe la clave, la agrega con un valor por defecto
print("Metodo setdefault: diccionario.setdefault('telefono', '809-777-7777') ")
print("El valor de la clave 'telefono' es:", diccionario.setdefault("telefono", "809-777-7777")) #agregando un elemento con un valor por defecto
print("El diccionario es:", diccionario)

#copy: Crea una copia del diccionario
print("Metodo copy: diccionario.copy() ")
diccionario_copia = diccionario.copy() #creando una copia del diccionario
print("El diccionario copia es:", diccionario_copia)

#fromkeys: Crea un diccionario con las claves especificadas y un valor por defecto
print("Metodo fromkeys: dict.fromkeys(['nombre', 'apellido'], 'Juan') ")
diccionario_nuevo = dict.fromkeys(["nombre", "apellido"], "Juan") #creando un diccionario con las claves especificadas y un valor por defecto
print("El diccionario nuevo es:", diccionario_nuevo)

#dict: Crea un diccionario a partir de una lista de tuplas
print("Metodo dict: dict([('nombre', 'Juan'), ('apellido', 'Perez')]) ")
diccionario_nuevo2 = dict([("nombre", "Juan"), ("apellido", "Perez")]) #creando un diccionario a partir de una lista de tuplas
print("El diccionario nuevo2 es:", diccionario_nuevo2)

#len: Devuelve la longitud del diccionario
print("Metodo len: len(diccionario) ")
print("La longitud del diccionario es:", len(diccionario)) #longitud del diccionario

#sorted: Devuelve una lista con las claves del diccionario ordenadas
print("Metodo sorted: sorted(diccionario) ")
print("Las claves del diccionario ordenadas son:", sorted(diccionario)) #claves del diccionario ordenadas

#reversed: Devuelve una lista con las claves del diccionario en orden inverso
print("Metodo reversed: list(reversed(diccionario)) ")
print("Las claves del diccionario en orden inverso son:", list(reversed(diccionario))) #claves del diccionario en orden inverso


#clear: Elimina todos los elementos del diccionario
print("Metodo clear: diccionario.clear() ")
diccionario.clear() #eliminando todos los elementos del diccionario
print("El diccionario es:", diccionario)

