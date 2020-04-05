import os
from data import Personaje
from data import crear_y_conectar


if os.path.isfile('c:/Users/DanielT/Desktop/Estudios/Curso Python Udemy/StarWars/star_wars.bd'):
    personaje = Personaje.select()
else:
    crear_y_conectar()
    print("bdd creada")

