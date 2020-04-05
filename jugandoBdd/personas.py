from peewee import *
from datetime import date
from pip._vendor.certifi.core import where

# Indica motor de base de datos y nombre de bdd
db = SqliteDatabase('personas.db')

class Persona(Model):
    nombre = CharField()
    cumpleanos = DateField()

    class Meta:
        database = db # This model uses the "people.db" database.


class Mascota(Model):
    propietario = ForeignKeyField(Persona, related_name='mascotas')
    nombre = CharField()
    edad = DateField()
    especie = CharField()
    raza = CharField()

    class Meta:
        database = db

#crear bdd        
def create_and_connect():
    db.connect()
    db.create_tables([Persona, Mascota])

#Insertar
def insertar_persona():
       persona = Persona(nombre="Daniel", cumpleanos=date(1989,10,25),is_relative=True)
       persona.save()
       persona2 = Persona.create(nombre = "Natalia", cumpleanos=date(1986,1,18),is_relative=True) 

#Insertar con llave foranea
def insertar_mascota():
    persona = Persona.get(Persona.nombre == 'Daniel')
    mascota = Mascota.create(propietario=persona, nombre="Black", edad=3, especie="Perro", raza="callejero")
    print(mascota.nombre)


#Modificar
def modificar_persona():
    (Persona.update(nombre= "Daniel Isaac")
    .where(Persona.id == 1)
    .execute())
    
    #Otra forma
    persona = Persona.get(Persona.nombre == "Daniel Isaac")
    persona.nombre = "Daniel Isaac Tapia Pinto"
    persona.save()


def borrar_persona():
    persona = Persona.get(Persona.id == 1)
    print(persona.nombre)
    borrados = Persona.delete().where(Persona.id == 1).execute()
    print(borrados)

create_and_connect()
insertar_persona()
insertar_mascota()
modificar_persona()
borrar_persona()

