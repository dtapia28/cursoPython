def saludo():
	print("Bienvenido a mi calculadora en Python")
	print("Primera versión: 20-11-2019")
	print("Versión actual: 21-11-2019")
	print("Por favor indica que operación quieres realizar: ")
	print("1. Suma\n2. Resta\n3. Multiplicación\n4. División")

def seguirA():
	seg = input("Deseas continuar? (si/no): ")
	if seg == "si":
		seguir = 1
	else:
		seguir = 0
		print("Adiós. Espero te haya servido")
	return seguir

def ingreso():
	try:
		elementos = []
		op = int(input("Número de operación a realizar: "))
		n1 = int(input("Ingresa el primer número: "))
		n2 = int(input("Ingresa el segundo número: "))
		elementos.extend([op,n1,n2])
	except ValueError:
		print("Error, debe ingresar un número")
		elementos = ingreso()

	return elementos

def calculadora(operacion, num1, num2):
	if operacion>=1 and operacion<=4:
		if operacion == 1:
			resultado = []
			resultado.append("suma")
			resultado.append(num1+num2)
			print("La "+resultado[0]+" es igual a "+str(resultado[1]))
			del resultado
		elif operacion == 2:
			resultado = []
			resultado.append("resta")
			resultado.append(num1-num2)
			print("La "+resultado[0]+" es igual a "+str(resultado[1]))
			del resultado
		elif operacion == 3:
			resultado = []
			resultado.append("multiplicación")
			resultado.append(num1*num2)
			print("La "+resultado[0]+" es igual a "+str(resultado[1]))
			del resultado
		else:
			resultado = []
			resultado.append("división")
			resultado.append(num1/num2)
			print("La "+resultado[0]+" es igual a "+str(resultado[1]))
			del resultado
	else:
		print("Operación no encontrada")		
			
def mostrar(seguir):
	saludo()
	while seguir == 1:
		ele = ingreso()
		calculadora(ele[0], ele[1], ele[2])
		seguir = seguirA()

mostrar(1)