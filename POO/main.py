from player import Player
from enemigos import Enemigos
import edificios

dante = Player(60, 5, "guerrero", "hoja afilada")

paladin = Player(70, 5, "paladin", "Mazazo")

elfo = Player(50, 10, "elfo", "Flecha segura")

goblin = Enemigos(nombre="Goblin", fuerza=20, defensa=10, destreza=5)

print(goblin)

print("ataca con "+str(goblin.atacar()))

print(paladin.atacar())

print(elfo.atacar())

mi_casa = edificios.Casa(largo=100,ancho=80)

depto = Edificios()

print("La "+mi_casa.ver_tipo()+" está construida con "+mi_casa.ver_material())

print(dante)