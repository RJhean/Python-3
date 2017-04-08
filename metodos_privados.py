class Usuario:
    def __init__(self, username, password, email):
        self.username=username
        self.__password=self.__generar_password(password)#Atributo Privado
        self.email=email
    def __generar_password(sel, password): #metodo privado
        return password.upper()

    def get_password(self):
        return self.__password

jhean = Usuario('jhean','rudy','jhean.rp@asd.com')
print(jhean.username)
#print(jhean.password)
print(jhean.email)
print(jhean.get_password())