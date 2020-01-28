class Enemigos:

#Crea clase mediante diccionario

    
    def __init__(self,**kwargs):
        self.nombre = kwargs.get("nombre", "enemigo")
        self.fuerza = kwargs.get("fuerza", 30)
        self.defensa = kwargs.get("defensa", 30)
        self.destreza = kwargs.get("destreza", 30)
     
    
    def atacar(self):
        return self.fuerza