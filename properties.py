class Usuario:
    def __init__(self, username, password, email):
        self.username=username
        self.__password=self.__generar_password(password)#Atributo Privado
        self.email=email

    def __generar_password(sel, password): #metodo privado
        return password.upper()

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, valor):
        self.__password=self.__generar_password(valor)

jhean = Usuario('jhean','rudy','jhean.rp@asd.com')

print(jhean.password)

jhean.password='Nuevo Pass'
print(jhean.password)