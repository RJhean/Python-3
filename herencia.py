class Animal:

    @property
    def terrestre(self):
        return True

class Felino(Animal): # clase padre

    @property
    def garras_retractiles(self):
        return True

    def cazar(self):
        print("El felino esta cazando")

class Mascota:
    #nombre = '' # todas necesitan un nombre

    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_nombre(self):
        print(self.nombre)

class Gato(Felino, Mascota): # herencia multiple

    def __init__(self, nombre):
        Mascota.__init__(self, nombre)
        self.nombre = nombre

    def gato_cazador(self):
        self.cazar()

    def mostrar_nombre(self): # Sobre escritura de método
        print("El nombre del gato es : {}".format(self.nombre))

class Jaguar(Felino):
    pass

gato = Gato('Gaturno')
jaguar = Jaguar()


print(gato.garras_retractiles)
print(jaguar.terrestre)
gato.mostrar_nombre()