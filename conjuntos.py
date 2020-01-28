#python 3.7.1

def saludo():
  print("Bienvenido a la app de conjuntos")

def ingreso():
  conjunto_a = set(input("Conjunto a: ").split())
  conjunto_b = set(input("Conjunto b: ").split())
  array =[conjunto_a, conjunto_b]
  return array

def operaciones():
  print("Operaciones disponibles:")
  print("1. Unión")
  print("2. Intersección")
  print("3. Diferencia")
  print("4. Diferencia simétrica")
  print("5. Ver operaciones")
  print("6. Ingresar nuevos conjuntos")
  print("7. Salir")

def ingreso_operacion():
  print("Ingrese operación a realizar:")
  try:
  	op = int(input(": "))
  except ValueError:
  	print("Introduce un número del 1 al 6")
  else:
  	return op


#Funciones de operaciones

def union(a, b):
  print("La unión es: "+str(a|b))

def interseccion(a, b):
  print("La intersección es "+str(a&b))

def diferencia(a, b):
  print("La diferencia para el conjunto A es "+str(a-b))
  print("La diferencia para el conjunto B es "+str(b-a))

def simetrica(a, b):
  print("La diferencia simétrica es "+str(a^b))
  

def mostrar_operacion(con_a, con_b, op):
  if op == 1:
    union(con_a, con_b)
  elif op == 2:
    interseccion(con_a, con_b)
  elif op == 3:
    diferencia(con_a, con_b)
  elif op == 4:
    simetrica(con_a, con_b)
  elif op == 5:
  	operaciones()
  elif op == 6:
  	mostrar()	 

def mostrar():
  saludo()
  conjuntos=ingreso()
  operaciones()
  while True:
    a=ingreso_operacion()
    if a == 7:
      print("Adiós")
      break
    else:
      mostrar_operacion(conjuntos[0], conjuntos[1], a)

mostrar()
