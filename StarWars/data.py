from peewee import *

db = SqliteDatabase('star_wars.bd')

class Obligacion(Model):
    nombre = CharField(30)
    detalle = CharField(500)

    class Meta:
        database = db


class Especie(Model):
    nombre = CharField(30)
    fortaleza = IntegerField(2)
    agilidad = IntegerField(2)
    intelecto = IntegerField(2)
    astucia = IntegerField(2)
    voluntad = IntegerField(2)
    presencia = IntegerField(2)
    umbral_herida = IntegerField(2)
    umbral_tension = IntegerField(2)
    experiencia_inicial = IntegerField(3)
    
    class Meta:
        database = db


class Profesion(Model):
    nombre = CharField(30)
    
    class Meta:
        database = db


class Personaje(Model):
    nombre = CharField(30)
    especie = ForeignKeyField(Especie, related_name='especie')
    profesion = ForeignKeyField(Profesion, related_name="profesion")
    obligacion = ForeignKeyField(Obligacion, related_name="obligacion")
    
    class Meta:
        database = db


def crear_y_conectar():
    db.connect()
    db.create_tables([Obligacion, Especie, Profesion, Personaje])                
            