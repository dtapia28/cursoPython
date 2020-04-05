import os
from peewee import *

db = SqliteDatabase("diario.db")

class Escritos(Model):
        titulo = CharField(30)
        texto = CharField(500)
        fecha = DateField()

        class Meta:
            database = db


def crear_y_conectar():
    db.connect()
    db.create_tables([Escritos]) 


def revisar_creacion():
    if os.path.isfile('C:/Users/DanielT/Desktop/Estudios/Curso Python Udemy/proyectoDiario/diario.db'):
        print("bdd ya existe")
    else:
        crear_y_conectar()


def escribir_diario(**kwargs):
    titulo = kwargs.get("titulo")
    texto = kwargs.get("texto")
    fecha = kwargs.get("fecha")
    escrito = Escritos.create(titulo=titulo, texto=texto, fecha=fecha, is_relative=True)

def traer_todo():
    escritos = Escritos.select()
    return escritos

def traer_por_fecha(fecha):
    escritos = Escritos.select().where(Escritos.fecha == fecha)
    return escritos