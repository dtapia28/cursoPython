def variable():
	global lista
	lista = {}

def saludo():
	print("Bienvenido a tu aplicación SuperLista!!")
	print("Por favor indica que operación quieres realizar: ")
	print("1. Agregar elemento\n2. Mirar elemento\n3. Eliminar elemento\n4. Eliminar elemento\n5. Salir")

def seguirA():
	seg = input("Deseas continuar? (si/no): ")
	if seg == "si":
		seguir = 1
	else:
		seguir = 0
		print("Desconectando...")
		print("Adión, esperamos vuelvas pronto")
	return seguir	

def ingresoOpcion():
	try:
		op = int(input("Número de operación a realizar: "))
	except ValueError:
		print("Error, debe ingresar un número")
		op = ingresoOpcion()

	return op

def ingresar():
	nombre = input("Ingresar nombre de contacto: ")
	cantidad = int(input("Ingresar número telefónico: "))
	lista[nombre] = cantidad
	print(lista)
	
	

def mirar():
	nombre = input("Ingresar nombre de elemento: ")
	print("Debes comprar "+str(lista[nombre])+ " de "+nombre)

def eliminar():
	nombre = input("Ingresar nombre de elemento: ")
	print("Se ha eliminado "+str(lista[nombre])+" de la lista.")
	del lista[nombre]

def salir():
	seguir = 0
	print("Desconectando...")
	print("Adión, esperamos vuelvas pronto")
	return seguir	


def opciones(op):
	disponibles = {1:ingresar, 2:mirar, 3:eliminar, 4:salir}
	x = disponibles[op]()

def mostrar():
	seguir = 1
	variable()
	while seguir == 1:
		a = saludo()
		x = ingresoOpcion()
		opciones(x)
		seguir = seguirA()


mostrar()	