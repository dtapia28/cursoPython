#Manejo de excepciones python

class Calculadora:


    def __init__(self, **kwargs):
        self.numero_1 = kwargs.get("num_1", 1)
        self.numero_2 = kwargs.get("num_2", 1)


    def sumar(self):
        try:
            return self.numero_1+self.numero_2
        except TypeError:
            print("Los valores ingresados deben ser números")
        finally:
            print("Holanda que Talca")    


    def restar(self):
        try:
            return self.numero_1-self.numero_2
        except TypeError:
            print("Los valores ingresados deben ser números")


    def multiplicar(self):
        try:
            return self.numero_1*self.numero_2
        except TypeError:
            print("Los valores ingresados deben ser números")


    def dividir(self):
        try:
            return self.numero_1/self.numero_2
        except ZeroDivisionError:
            return self.numero_1/1
        except TypeError:
            print("Los valores ingresados deben ser números")        


calculadora = Calculadora(num_1 = "hola", num_2=2)
print(calculadora.sumar())
print(calculadora.restar())
print(calculadora.multiplicar())
print(calculadora.dividir())