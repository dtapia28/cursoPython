class Usuario:

    
    def __init__(self, usuario, password, email):
        self.usuario = usuario
        self.__password = self.__encriptar(password)
        self.email = email


    def __encriptar(self,y):
        x1=y.replace('s', '0')
        x2=x1.replace('a', '1')
        x3=x2.replace('l', '2')
        x4=x3.replace('o', '3')
        x5=x4.replace('n', '4')
        x6=x5.replace('b', '5')
        x7=x6.replace('e', '6')
        x8=x7.replace('t', '7')
        x9=x8.replace('i', '8')
        x0=x9.replace('u', '9')
        return x0


    def get_password(self):
        return self.__password           


eduardo = Usuario('eduardo', 'secreto', 'example@example.cl')

print(eduardo.usuario)
print(eduardo.get_password())
print(eduardo.email)