class Player:
    
    def __init__(self, puntos_golpes=30, mana=5, vocacion="sin vocación", ataque="puff"):
        self.puntos_golpe = puntos_golpes
        self.mana = mana
        self.vocacion = vocacion
        self.ataque = ataque
        self.nombre = input("Escribe tu nombre: ")
    
    def __str__(self):
        s = ('El personaje tiene las siguientes características:\nSu nombre es {}.\nSus puntos de golpe son {}'
        .format(self.nombre, self.puntos_golpe))
        return s
        
    def atacar(self):
        return self.ataque
