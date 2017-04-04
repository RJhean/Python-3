#import calculadora 

from calculadora import suma
from calculadora import resta as r1

#resultado = calculadora.suma(2,3)
resultado = suma(2,3)
print(resultado)

resultado = r1(4,5)
print(resultado)


from calculadora import __name__ as __name__caculadora__
print(__name__)
print(__name__caculadora__)

if __name__ == '__main__': # es este el script principal