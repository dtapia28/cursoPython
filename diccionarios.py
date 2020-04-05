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


#Generar diccionario, donde las llaves serán tuplas

tupla_elementos = ("nombre", "apellido", "dia", "mes", "año")
lista_datos = ["Daniel", "Tapia", 25, 10, 1989]
new_diccionario = dict(zip(tupla_elementos, lista_datos))
print(new_diccionario)


#Diccionario con tupla adentro

jugador = {"nombre": "Edson Arantes do Nascimento", "nacimiento":"23/10/1940", "posición": "delantero",
				"equipos":['Santos FC', 'Cosmos NY'], 'partidos':{"Santos FC":665, "Cosmos NY":64},
				"goles":{"Santos FC":647, "Cosmos NY":37}, "retiro": "01/10/1977"}

print("\nEl rey Pelé:\nDe nombre "+jugador['nombre']+ " nació el "+jugador['nacimiento']+
		". Se desempeñó en la posición de "+jugador['posición']+" y marcó un total de "+
		str(jugador['goles']['Santos FC']+jugador['goles']['Cosmos NY'])+" goles en un total de "+
		str(jugador['partidos']['Santos FC']+jugador['partidos']['Cosmos NY'])+
		" partidos. Lo que da una media de "+str((jugador['goles']['Santos FC']+
		jugador['goles']['Cosmos NY'])/(jugador['partidos']['Santos FC']+jugador['partidos']['Cosmos NY']))+
		" goles por partido. Jugó en los equipos "+jugador['equipos'][0]+" y "+jugador['equipos'][1]+
		".\nSe retiró del futbol porfesional el día "+jugador['retiro'])

