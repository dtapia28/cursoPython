import re

#Leyendo archivo txt

file = open("texto.txt",encoding="utf-8")


info = file.read()

print(info)

file.close()


#Buscar dentro de un archivo

buscador = re.search("[123]", info)

print(buscador)
##hay un metodo match también, pero no me funcionó

matchador = re.match("\w", info)

print(matchador)


#buscar letras mayusculas

mayusculas = re.findall("[A-Z]+", info)

print(mayusculas)

#Crear archivo
archivo_lista = open("lista.txt", "w")
archivo_lista.write("Mi primer archivo creado con Python\n")
archivo_lista.write("Segunda linea en mi primer archivo")
archivo_lista.close()