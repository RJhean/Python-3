
"""
generadores
"""
def generador(*args):
    for valor in args:
        yield valor * 10


for valor in generador(1,2,3,4,5,6,7,8,9):
    print(valor)

