class Circulo:

    @staticmethod # le pertenece a la clase
    def pi():
        return 3.1416

    def __init__(self, radio):
        self.radio=radio

    def area(self): # metodos de instancia
        return self.radio * self.radio * self.pi()

print(Circulo.pi())
circulo_uno = Circulo(4)
print(circulo_uno.area())