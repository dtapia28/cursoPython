# Agenda telefonica

# Saludo inicial y menu usuario

def variable():
	global lista
	lista = {}

def saludo():
	print("Bienvenido a mi agenda Telefónica")
	print("Por favor indica que operación quieres realizar: ")
	print("1. Agregar un contacto\n2. Eliminar contacto\n3. Actualizar contacto\n4. Ver contacto\n5. Ver todos los contactos")

#Repite o no el menu usuario
def seguirA():
	seg = input("Deseas continuar? (si/no): ")
	if seg == "si":
		seguir = 1
	else:
		seguir = 0
		print("Desconectando...")
		print("Adión, esperamos vuelvas pronto")
	return seguir

#Ingreso de opción
def ingresoOpcion():
	try:
		op = int(input("Número de operación a realizar: "))
	except ValueError:
		print("Error, debe ingresar un número")
		op = ingresoOpcion()

	return op

def agregar():
	nombre = input("Ingresar nombre de contacto: ")
	cantidad = int(input("Ingresar número telefónico: "))
	lista[nombre] = cantidad
	print("Contacto agregado a agenda")	

def eliminar():
	nombre = input("Ingresar nombre de contacto a eliminar: ")
	confirmar = input("Estás seguro de eliminar a "+nombre+" de tu agenda? (si/no)")
	if confirmar == "si":
		del lista[nombre]
		print("Se ha eliminado "+nombre+" de tu lista de contactos.")

def actualizar():
	print("Funcion actualizar")

def ver():
	print("Funcion ver")

def todos():
	print("Estos son los contactos en tu agenda: ")
	for x in lista:
		print(x+" - "+str(lista[x]))	


def opciones(op):
	disponibles = {1:agregar, 2:eliminar, 3:actualizar, 4:ver, 5:todos}
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