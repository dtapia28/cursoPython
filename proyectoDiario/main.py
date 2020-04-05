from bdd import revisar_creacion
from menu import Menu

# Este es el main del proyecto.

if __name__ == '__main__':
    revisar_creacion()
    menu = Menu()
    menu.saludo()
    seguir = 1
    while seguir == 1:
        menu.ver_opciones()
        op=menu.ingreso_opcion()
        if op != 4:
            menu.opciones_disponibles(op)
        else:
            seguir = 0
            print("Hasta pronto") 

   
