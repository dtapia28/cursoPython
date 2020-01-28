numeros = [0,1,2,3,4,5,6,7,8,9,10]
# Tomo desde la posición 0 a la posición 5
numeros_2 = numeros[0:6]
print(numeros_2)
# Resultado: [0, 1, 2, 3, 4, 5]

# Para sacar todos los elementos
todos = numeros[0:]
print(todos)
# Resultado: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
algo = numeros[-6:-3]
print(algo)

# Steps o saltar

lista = [0,1,2,3,4,5,6,7,8,9,10]
lista_2 = lista[::2]
print(lista_2)
# Resultado: [0, 2, 4, 6, 8, 10]
lista_3 = lista[::3]
print(lista_3)
# Resultado: [0, 3, 6, 9]
lista_4=lista[2:8:2]
print(lista_4)
#Resultado: [2, 4, 6]
lista_5=lista[-2:-5:-1]
print(lista_5)
#Resultado: [9, 8, 7]

# Borrar ocupando slices
del numeros[0:4]
print(numeros)

#insertar ocupando slices
numeros[0:1] = [1,2,3,4]
print(numeros)	