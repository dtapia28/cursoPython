class Edificios:
    material = "ladrillos"
    tipo = "edificio"
    
    def __init__(self,**kwargs):
        self.largo = kwargs.get("largo", 40)
        self.ancho = kwargs.get("ancho", 60)
        self.color = kwargs.get("color", "rojo")
     
    
    def ver_material(self):
        return self.material
    
    def ver_largo(self):
        return self.largo
    
    def ver_ancho(self):
        return self.ancho
    
    def ver_color(self):
        return self.color
    
    def ver_tipo(self):
        return self.tipo


class Casa(Edificios):
    tipo = "casa"
    material = "palitos"
    
# Sobreescritura de metodos
    def ver_material(self):
        return "{} y ladrillos ".format(self.material)
               