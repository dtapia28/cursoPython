import random
class Dados:
    
    def __init__(self,**kwargs):
        self.caras = kwargs.get("caras")
        self.tipo = kwargs.get("tipo")
    
    def verCaras(self):
        return self.caras  

    def lanzar(self):
        self.cara = random.randint(1,self.caras)
        return self.cara
    
    def verTipo(self):
        return self.tipo
    
    
    def __str__(self):
        msj = ("Se lanza dado de tipo {}, que tienen {} caras".
               format(
                      self.verTipo(),
                      self.verCaras()))
        
        return msj

class Beneficios(Dados):
    
    def __init__(self):
        self.tipo = "Beneficios"
        self.caras = 6
    
class Complicacion(Dados):
    
    def __init__(self):
        self.tipo="Complicación"
        self.caras = 6

class Capacidad(Dados):
    
    def __init__(self):
        self.tipo="Capacidad"
        self.caras=8

class Dificultad(Dados):
    
    def __init__(self):
        self.tipo="Dificultad"
        self.caras=8

class Pericia(Dados):
    
    def __init__(self):
        self.tipo="Pericia"
        self.caras=12
                                
               