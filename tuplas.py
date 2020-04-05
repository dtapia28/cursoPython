#Una tupla es un arreglo de valores pero no mutables

#Asi se crea una tupla
tupla1 = (1,2,3,4,5)
print(tupla1)
print(tupla1[0:3])


#Creando lista desde tupla:
nueva_lista = list(tupla1)
print(nueva_lista)
del tupla1
#print(tupla1)

tupla2 = (2,7,9,7,4,2,1,0,5,4,9,3,2,8,4,9,0,1,4,7)
#contar cantidad de veces que hay x elemento en la tupla
a_buscar = 2
print("El número "+str(a_buscar)+" aparece "+str(tupla2.count(a_buscar))+" vez/veces en la tupla.")


#Largo de la tupla
print("El largo de la tupla es "+str(len(tupla2)))


#Tupla unitaria debe llevar ,
tupla_unitaria = ("Daniel",)
print(tupla_unitaria)


#Dar valor a variables con elementos en tupla
mis_datos = ("Daniel", "Tapia", 1989, 10, 25)
nombre,apellido,year,mes,dia=mis_datos
print("Este es el nombre: "+nombre)
print("Este es el apellido "+apellido)
print("Este es el año "+str(year))
print("Este es el mes "+str(mes))
print("Este es el día "+str(dia))