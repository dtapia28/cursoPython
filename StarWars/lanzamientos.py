import random
import dados


class Lanzamientos:
    
    def __init__(self, lista):
        self.tirada = ""
        self.exitos = 0
        self.ventajas = 0
        for dado in lista:
            if dado == "1b":
                dadito = dados.Beneficios()
                tirada = dadito.lanzar()
                self.verSimbolo(dado, tirada)
            elif dado == "1c":
                dadito = dados.Complicacion()
                tirada = dadito.lanzar()
                self.verSimbolo(dado, tirada)
            elif dado == "1ca":
                dadito = dados.Capacidad()
                tirada = dadito.lanzar()
                self.verSimbolo(dado, tirada)
            elif dado == "1d":
                dadito = dados.Dificultad()
                tirada = dadito.lanzar()                
                self.verSimbolo(dado, tirada)
            elif dado == "1p":
                dadito = dados.Pericia()
                tirada = dadito.lanzar()                
                self.verSimbolo(dado, tirada)                                        
        print("Los exitos son: " + str(self.exitos))
        print("Las ventajas son: " + str(self.ventajas))
        if self.exitos < 1:
            print("Has fallado")
        else:
            print("Lo has logrado")        
    
    def verCaras(self):
        return self.caras
    
    def verCantidad(self):
        return self.cantidad
    
    def verExitos(self):
        return self.exitos
    
    def verVentajas(self):
        return self.ventajas
    
    def verSimbolo(self, dado, cara):
        if dado == "1b":
            if cara == 1:
                print("nada")
                return "nada"
            elif cara == 2:
                print("nada")
                return "nada"
            elif cara == 3:
                print("1 éxito")
                self.exitos = self.exitos + 1
                return "1 éxito"
            elif cara == 4:
                print("1 éxito, 1 ventaja")
                self.exitos = self.exitos + 1
                self.ventajas = self.ventajas + 1
                return "1 éxito, 1 ventaja"
            elif cara == 5:
                print("2 ventajas")
                self.ventajas = self.ventajas + 2
                return "2 ventajas"
            elif cara == 6:
                print("1 ventaja")
                self.ventajas = self.ventajas + 1
                return "1 ventaja"
        elif dado == "1c":
            if cara == 1:
                print("nada")
                return "nada"
            elif cara == 2:
                print("nada")
                return "nada"
            elif cara == 3:
                print("1 fallo")
                self.exitos = self.exitos - 1
                return "1 fallo"
            elif cara == 4:
                print("1 fallo")
                self.exitos = self.exitos - 1
                return "1 fallo"
            elif cara == 5:
                print("1 amenaza")
                self.ventajas = self.ventajas - 1
                return "2 ventajas"
            elif cara == 6:
                print("1 amenaza")
                self.ventajas = self.ventajas - 1
                return "1 ventaja"
        elif dado == "1ca":
            if cara == 1:
                print("nada")
                return "nada"
            elif cara == 2:
                print("1 éxito")
                self.exitos = self.exitos + 1
                return "1 éxito"
            elif cara == 3:
                print("1 éxito")
                self.exitos = self.exitos + 1
                return "1 éxito"
            elif cara == 4:
                print("2 éxitos")
                self.exitos = self.exitos + 2
                return "2 éxitos"
            elif cara == 5:
                print("1 ventaja")
                self.ventajas = self.ventajas + 1
                return "1 ventaja"
            elif cara == 6:
                print("1 ventaja")
                self.ventajas = self.ventajas + 1
                return "1 ventaja"
            elif cara == 7:
                print("1 éxito, 1 ventaja")
                self.exitos = self.exitos + 1
                self.ventajas = self.ventajas + 1
                return "1 éxito, 1 ventaja"
            elif cara == 8:
                print("2 ventajas")
                self.ventajas = self.ventajas + 2
                return "2 ventajas"
        elif dado == "1d":
            if cara == 1:
                print("nada")
                return "nada"
            elif cara == 2:
                print("1 fallo")
                self.exitos = self.exitos - 1
                return "1 fallo"
            elif cara == 3:
                print("2 fallos")
                self.exitos = self.exitos - 2
                return "2 fallos"
            elif cara == 4:
                print("1 amenaza")
                self.ventajas = self.ventajas - 1
                return "1 amenaza"
            elif cara == 5:
                print("1 amenaza")
                self.ventajas = self.ventajas - 1
                return "1 amenaza"
            elif cara == 6:
                print("1 amenaza")
                self.ventajas = self.ventajas - 1
                return "1 amenaza"
            elif cara == 7:
                print("2 amenazas")
                self.ventajas = self.ventajas - 2
                return "2 amenazas"
            elif cara == 8:
                print("1 fallo, 1 amenaza")
                self.exitos = self.exitos - 1
                self.ventajas = self.ventajas - 1
                return "1 fallo, 1 amenaza"
        elif dado == "1p":
            if cara == 1:
                print("nada")
                return "nada"
            elif cara == 2:
                print("1 éxito")
                self.exitos = self.exitos + 1
                return "1 éxito"
            elif cara == 3:
                print("1 éxito")
                self.exitos = self.exitos + 1
                return "1 éxito"
            elif cara == 4:
                print("2 éxitos")
                self.exitos = self.exitos + 2
                return "2 éxitos"
            elif cara == 5:
                print("2 éxitos")
                self.exitos = self.exitos + 2
                return "2 éxitos"
            elif cara == 6:
                print("1 ventaja")
                self.ventajas = self.ventajas + 1
                return "1 ventaja"
            elif cara == 7:
                print("1 éxito, 1 ventaja")
                self.exitos = self.exitos + 1
                self.ventajas = self.ventajas + 1
                return "1 éxito, 1 ventaja"
            elif cara == 8:
                print("1 éxito, 1 ventaja")
                self.exitos = self.exitos + 1
                self.ventajas = self.ventajas + 1
                return "1 éxito, 1 ventaja"
            elif cara == 9:
                print("1 éxito, 1 ventaja")
                self.exitos = self.exitos + 1
                self.ventajas = self.ventajas + 1
                return "1 éxito, 1 ventaja"
            elif cara == 10:
                print("2 ventajas")
                self.ventajas = self.ventajas + 2
                return "2 ventajas"
            elif cara == 11:
                print("2 ventajas")
                self.ventajas = self.ventajas + 2
                return "2 ventajas"                                                                                               
        
    def verPuntaje(self):
        msj = ("Resultado tirada:\nÉxitos: {}\nVentajas: {}"
               .format(self.verExitos(),
                       self.verVentajas()))
        
        print(msj)
        if self.exitos > 0:
            print("Lo has logrado")
        else:
            print("No lo has logrado")    
    
    def mostrar(self):
            msj = ("Has lanzado un dado de tipo {}. El resultado es {}.".
                   format(self.verSimbolo(self.cara)))
            
            print(msj)  
