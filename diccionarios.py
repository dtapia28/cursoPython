# Un  diccionario es un array llave:valor

calificaciones = {"Andres":7,"Maria":6,"Jorge":5,"Esteban":3}
print(calificaciones)
print(calificaciones["Jorge"])

#metodo para crear diccionarios
diccionario = dict([["primero",5],["segundo",20],["tercero",45]])
print(diccionario)

# Para agregar elementos a un diccionario

diccionario["cuarto"] = 82
print(diccionario)

# Para borrar elementos de un diccionario

del diccionario["cuarto"]
print(diccionario)

#Para acualizar (o ingresar más de un valor)

diccionario.update({"lunes":1,"primero":23})
print(diccionario)

# Iterar un diccionario
#El siguiente for imprime solamente las llaves
for x in diccionario:
	print(x)

#El siguiente for impprime los valores
for x in diccionario:
	print(diccionario[x])

#El siguiente for también imprime las llaves
for x in diccionario.keys():
	print(x)

#El siguiente for también imprime los valores
for x in diccionario.values():
	print(x)


#El siguiente for imprime llave y valor
for x in diccionario.items():
	print(x)