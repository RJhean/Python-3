class Animal:
    valador = True

class Cocodrilo(Animal):

    def __init__(self, nombre):
        self.nombre = nombre

    @classmethod
    def new(cls, nombre):
        cls.volador=False
        return Cocodrilo(nombre)

cocodrilo = Cocodrilo.new('coco')
print(cocodrilo.nombre)
print(cocodrilo.volador)

"""

Las variables privadas solo se puden utilizar con un objeto
"""
"""
Métodos mágicos (modifican el comportamiento de las clases)
"""
class Usuario:
    def __new__(cls):
        print("Este método es el primero en ejecutarse")
        return super().__new__(cls)

    def __init__(self):
        print("Este método es el segundo en ejecutarse")
        
    def __str__(self):
        return "Esto se imprime cuando trata de mostrar el objeto"

    def __getattr__(self, nombres):
        print("Aquí mostramos lo que no se encontro en el atributo")
        self.otros_metodos()

    def otros_metodos(self):
        print("otro método")

usuario = Usuario()
print(usuario)
print(usuario.apellido)




