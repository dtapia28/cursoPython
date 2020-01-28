#Importa la clase random
import random
import time

#Genera un número aleatorio
aleatorio = random.randint(0,100)

#Saludo inicial
def saludo():
	print("Bienvenid@!!")
	time.sleep(1)
	print("Este es el clásico juego: Adivina el número!! Espero que lo disfrutes")
	time.sleep(2)
	print("Ahora dime que quieres hacer: ")
	print("1. Jugar al juego\n2. De qué se trata?\n3. Saber como funciona\n4. Salir\n")

#Ingreso de opción
def ingresoOpcion():
	try:
		op = int(input("Número de operación a realizar: "))
	except ValueError:
		print("Error, debe ingresar un número")
		op = ingresoOpcion()

	return op	

def preparar():
	global nPista
	nPista = 0
	global intentos
	intentos = 0
	global puntaje
	puntaje = 100
	global aleatorio
	aleatorio = random.randint(0,100)


def primero():
	print("Espera un momento...")
	print("Nuestros adivinenses estás generando todo lo necesario para tu juego...")
	time.sleep(2)		
	print("Estás preparad@??")
	time.sleep(2)
	print("A jugar!!!")

def jugar():
	global puntaje
	if puntaje > 0:
		print("Tu puntaje actual es "+str(puntaje))
		try:
			time.sleep(1)
			opcion = input("Quieres una pista o intentar con un número??\n(Escribe pista o ingresa un número): ")
		except ValueError:
			print("Solamente puedes ingresar 'pista' o probar con un número")
			opcion = jugar()
		if opcion == "pista":
			global nPista
			nPista = nPista+1
			puntaje = puntaje-10
			time.sleep(1)
			pista = random.randint(0,100)
			if pista > aleatorio:
				print("El número buscado es menor que "+str(pista))
				jugar()
			elif pista < aleatorio:
				print("El número buscado es mayor que "+str(pista))
				jugar()	
			else:
				print(str(pista)+" Estás muy cerca o incluso ahí")
				jugar()	
		else:
			opcion = int(opcion)
			global intentos
			intentos = intentos+1
			if opcion == aleatorio:
				print("veamos si has acertado")
				time.sleep(1)
				print("Felicitaciones, lo has encontrado")
				print("Lo lograste ocupando "+str(nPista)+ " pistas y con "+str(intentos)+" intentos.")
				print("Tu puntaje final es: "+str(puntaje))
			elif opcion > aleatorio:
				puntaje = puntaje-5
				print("veamos si has acertado")
				time.sleep(1)			
				print(str(opcion)+" es mayor que el número buscado")
				jugar()
			else:
				puntaje = puntaje-5
				print("veamos si has acertado")
				time.sleep(1)			
				print(str(opcion)+" es menor que el número buscado")
				jugar()
	else:
		print("Tu puntaje es 0. Has perdido")				

def comoJugar():
	print("Adivina el número!!\nObjetivo:\nEn este juego lo que el jugador busca lograr es adivinar un número creado por nuestros adivinenses\nCómo se juega?\n Tienes 2 opciones: ingresar 'pista' para que nuestros adivinenses te den una pista (esto te quita 10 puntos) o intentar adivinar el número ingresandolo (cada intento fallido son -5 puntos). Pierdes cuando no te quede más puntaje (comienzas con 100 puntos)")

def comoFunciona():
	print("Una breve explicación de como supuestamente se genera la partida")

def salir():
	print("Hace lo que dice que hace")		

#Decide a que función enviar al usuario
def opciones(op):
	disponibles = {1:jugar, 2:comoJugar, 3:comoFunciona, 4:salir}
	x = disponibles[op]()

def auxiliar(a):
	if a == 1:
		preparar()
		primero()	
		opciones(a)
	else:
		opciones(a)
		saludo()			
		a = ingresoOpcion()
		auxiliar(a)


def mostrar():
	saludo()
	a = ingresoOpcion()
	auxiliar(a)

mostrar()		