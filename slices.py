numeros = [0,1,2,3,4,5,6,7,8,9,10]
# Tomo desde la posición 0 a la posición 5
numeros_2 = numeros[0:6]
print("Tomando desde la posición 0 a la 5: "+str(numeros_2))
# Resultado: [0, 1, 2, 3, 4, 5]

# Para sacar todos los elementos
todos = numeros[0:]
print("Toda la lista: "+str(todos))
# Resultado: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
algo = numeros[-6:-3]
print("Tomando desde posición -6 a -3: "+str(algo))

# Steps o saltar

lista = [0,1,2,3,4,5,6,7,8,9,10]
lista_2 = lista[::2]
print("Saltando de 2 posiciones: "+str(lista_2))
# Resultado: [0, 2, 4, 6, 8, 10]
lista_3 = lista[::3]
print("Saltando de 3 posiciones: "+str(lista_3))
# Resultado: [0, 3, 6, 9]
#detalle de lista[2:8:2] El primer 2 indica que se parte desde la 2° posicion, el 8 es que llega hasta la
# 8° posicion y el último 2 es que se hará de 2 en 2. 
lista_4=lista[2:8:2]
print("Desde la 2° posicion a la 8° posicion, saltando de 2 en 2: "+str(lista_4))
#Resultado: [2, 4, 6]
lista_5=lista[-2:-5:-1]
print("Desde la posición -2° a la -5°, saltando -1: "+str(lista_5))
#Resultado: [9, 8, 7]


# Borrar ocupando slices
del numeros[0:4]
print(numeros)


#insertar ocupando slices
numeros[0:1] = [1,2,3,4]
print(numeros)


#Transformar lista en tupla:
para_tupla = lista[2:9:2]
nueva_tupla = tuple(para_tupla)
print(nueva_tupla)
