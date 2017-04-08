class Circulo:

    _pi = 3.1416

    def __init__(self, radio):
        self.radio=radio

    def area(self):
        return self.radio * self.radio * self._pi 

print(Circulo._pi) # no se necesita crear un objeto para las vaiables de clase

circulo_uno = Circulo(4)
circulo_dos = Circulo(3)

#print(circulo_uno.radio)
#print(circulo_dos.radio)
print(circulo_uno.__dict__)
print(circulo_uno.area())