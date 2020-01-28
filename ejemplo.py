# Este es un comentario en python
# Condiciones en python
edad = 10
if edad>=18:
	print ("Puedes entrar")
elif edad < 12:
	print ("Anda a tomar leche")
else:
	print("No puedes entrar. Eres menor de edad")


#Funciones en python
def pedir_pizza (base, queso, donde):
	print ("Tu pedido es de una pizza con las siguientes caracteristicas:")
	print("Quieres una pizza con "+base)
	if queso == 1:
		print("Con queso normal")
	else:
		print("Extra queso")

	if donde == "casa":
		print("Reparto a domicilio")
	else:
	 print("Para comer en el local")


pedir_pizza("carne", 2, "local")

# Listas en python 

lista = []
# Agregar elementos a la lista
lista.append(1)
lista.append("durazno")
lista.append(["luz", "gas", "agua"])
print(lista)
# Para agregar más de un elemento a la lista
lista.extend([2,3,4])
print(lista)
# Para eliminar de una lista
lista.remove(["luz", "gas", "agua"])
print(lista)
# otra forma de crear una lista
lista2 = list([1,2,3,4,5])
print(lista2)
#al crear una lista con un string, esta crea la lista con cada letra del string

nombre = list("Daniel")
print(nombre)
# Resultado: ['D', 'a', 'n', 'i', 'e', 'l']

# Para crear una lista con palabras separadas
listaPalabras = "Sueños con serpientes".split()
print(listaPalabras)
#resultado : ['Sueños', 'con', 'serpientes']

#Split indicando separador
comidas = "Arroz,puré,fideos,papas,lentejas".split(",")
print(comidas)
#Resultado: ['Arroz', 'puré', 'fideos', 'papas', 'lentejas']

#Pasar de una lista a un string
comidas2 =", ".join(comidas)
print(comidas2)
# Resultado: Arroz, puré, fideos, papas, lentejas


#Indices, posición de elemento en una lista
print("La letra buscada está en la posición "+str(nombre.index("e")))

#Para borrar una variable o un elemento de una lista se puede ocupar del

borrar = "Borrame"
print(borrar)
del borrar
del nombre[0]
print(nombre)

# palabra recerbada in para saber si algo esta o en un string o en una lista

if "a" in nombre:
	print("a está en la variable nombre")
else:
	print("No está")


# Ciclo while

cerdito = 10

while cerdito >= 0:
	if cerdito != 0:
		print("El lobo se comió al cerdito número "+str(cerdito))
	else:
		print("El lobo se comió a todos los cerditos")
	cerdito-=1

# Ciclo for
for x in range(1,10):
	print(x)

# For ara iterar una lista
nombre2 = list("Daniel")
for x in nombre2:
	if nombre2.index(x) == 0:
		print("Daniel tu nombre comienza con una "+x)
	else:
		print("luego le sigue una "+x)	
print(nombre2)

#Reto de ciclos

vocales = "aeiou"
vocales_lista = list(vocales)
for x in vocales_lista:
	print(x.upper())


#Input

nombre = input("Introduce tu nombre por favor ")
nombre2 = list(nombre)
for x in nombre2:
	if nombre2.index(x) == 0:
		print(nombre+" tu nombre comienza con una "+x)
	else:
		print("luego le sigue una "+x)	
print(nombre)

#para parsear a int
numero = int(input("Indica un número "))
print("Esta es la tabla del número "+str(numero))
for x in range(1,11):
	print(str(numero)+" x "+str(x)+" = "+str(numero*x))


# Prueba
def ingresar():
	num1 = int(input("Ingresar primer número "))
	num2 = int(input("Ingresar segundo número "))
	suma = num1+num2
	return suma

try:
	suma = ingresar()
except ValueError:
	suma = ingresar()
print("La suma es "+str(suma))	
