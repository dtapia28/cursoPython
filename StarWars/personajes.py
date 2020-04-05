class Personajes:
    
    def __init__(self,**kwargs):
        self.nombre = kwargs.get("nombre")
        self.especie = kwargs.get('especie')
        self.profesion = kwargs.get("profesion")
        self.fortaleza = 0
        self.agilidad = 0
        self.intelecto = 0
        self.astucia = 0
        self.voluntad = 0
        self.presencia = 0    
    
    def ver_nombre(self):
        return self.nombre
    
    def ver_especie(self):
        return self.especie
    
    def ver_profesion(self):
        return self.profesion


    def ver_fortaleza(self):
        return self.fortaleza
    
    def ver_agilidad(self):
        return self.agilidad
    
    def ver_intelecto(self):
        return self.intelecto
    
    def ver_astucia(self):
        return self.astucia
    
    def ver_voluntad(self):
        return self.voluntad
    
    def ver_presencia(self):
        return self.presencia     
    
    
    def __str__(self):
        msj = ("Mi nombre es {}, pertenezco al pueblo {} y me desempeño como {}".
               format(
                   self.ver_nombre(),
                   self.ver_especie(),
                   self.ver_profesion()))
        
        return msj     


class Twilek(Personajes):
    
    def __init__(self,**kwargs):
        self.nombre = kwargs.get("nombre")
        self.especie = "Twi'lek"
        self.profesion = kwargs.get("profesion")
        self.fortaleza = 1
        self.agilidad = 2
        self.intelecto = 2
        self.astucia = 2
        self.voluntad = 2
        self.presencia = 3
        self.umbral_heridas = 10+self.ver_fortaleza()
        self.umbral_tension = 10+self.ver_voluntad()
        self.experiencia = 100        

class Bothans(Personajes):
    
    def __init__(self,**kwargs):
        self.nombre = kwargs.get("nombre")
        self.especie = "Bothan"
        self.profesion = kwargs.get("profesion")
        self.fortaleza = 1
        self.agilidad = 2
        self.intelecto = 2
        self.astucia = 3
        self.voluntad = 2
        self.presencia = 2
        self.umbral_heridas = 10+self.ver_fortaleza()
        self.umbral_tension = 11+self.ver_voluntad()
        self.experiencia = 100


class Droides(Personajes):
    
    def __init__(self,**kwargs):
        self.nombre = kwargs.get("nombre")
        self.especie = "Droide"
        self.profesion = kwargs.get("profesion")
        self.fortaleza = 1
        self.agilidad = 1
        self.intelecto = 1
        self.astucia = 1
        self.voluntad = 1
        self.presencia = 1
        self.umbral_heridas = 10+self.ver_fortaleza()
        self.umbral_tension = 10+self.ver_voluntad()
        self.experiencia = 175
        

class Gandianos(Personajes):
    
    def __init__(self,**kwargs):
        self.nombre = kwargs.get("nombre")
        self.especie = "Droide"
        self.profesion = kwargs.get("profesion")
        self.fortaleza = 2
        self.agilidad = 2
        self.intelecto = 2
        self.astucia = 2
        self.voluntad = 3
        self.presencia = 1
        self.umbral_heridas = 10+self.ver_fortaleza()
        self.umbral_tension = 10+self.ver_voluntad()
        self.experiencia = 100


class Humanos(Personajes):
    
    def __init__(self,**kwargs):
        self.nombre = kwargs.get("nombre")
        self.especie = "Droide"
        self.profesion = kwargs.get("profesion")
        self.fortaleza = 2
        self.agilidad = 2
        self.intelecto = 2
        self.astucia = 2
        self.voluntad = 2
        self.presencia = 2
        self.umbral_heridas = 10+self.ver_fortaleza()
        self.umbral_tension = 10+self.ver_voluntad()
        self.experiencia = 110                                         