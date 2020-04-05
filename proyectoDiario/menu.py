from datetime import date
from datetime import datetime
from bdd import escribir_diario
from bdd import traer_todo
from bdd import traer_por_fecha
class Menu():

    def __init__(self):
        print("Un nuevo menú")

    def saludo(self):
        print("Bienvenido a tu Diario de Vida")

    def ver_opciones(self):    
        print("Por favor indícame que operación deseas realizar:")
        print("1. Escribir en mi diario\n2. Ver todo mi diario\n3. Ver diario por fecha\n4. Salir")

    def ingreso_opcion(self):
        try:
            self.opcion = int(input("Numero de operación que realizarás: "))
        except ValueError:
            print("Error, debe ingresar un número")
            #opcion = ingreso_opcion()
        return self.opcion  

    def escribir_en_diario(self):
        titulo = input("Ingresa el título de la entrada: ")
        fecha = date.today()
        texto = input("Ingresa texto de entrada: ")
        escribir_diario(titulo=titulo, texto=texto, fecha=fecha)

    def ver_todo(self):
        print("\nEsas son todas las entradas en tu diario:\n")
        escritos = traer_todo()
        if escritos is None:
            print("No hay entradas aún en tu Diario")
        else:    
            for escrito in escritos:
                print("Título: "+escrito.titulo)
                print("Fecha: "+str(escrito.fecha))
                print("Entrada: "+escrito.texto)
                print("============================================================================================\n")
            


    def ver_por_fecha(self):
        fecha_a = input("Indica fecha de las entradas: ")
        fecha = datetime.strptime(fecha_a, '%d-%m-%Y').date()
        escritos = traer_por_fecha(fecha)
        print("Estas son las entradas con fecha "+fecha_a+":\n")
        for escrito in escritos:
            print("Título: "+escrito.titulo)
            print("Entrada: "+escrito.texto)   
            print("============================================================================================\n")
    
    def opciones_disponibles(self, op):
        if op == 1:
            self.escribir_en_diario()
        elif op == 2:
            self.ver_todo()
        elif op == 3:
            self.ver_por_fecha()
        else:
            print("Adiós")        
