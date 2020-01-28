class Player:
    
    def __init__(self, puntos_golpes=30, mana=5, vocacion="sin vocación", ataque="puff"):
        self.puntos_golpe = puntos_golpes
        self.mana = mana
        self.vocacion = vocacion
        self.ataque = ataque
        
    def atacar(self):
        return self.ataque
