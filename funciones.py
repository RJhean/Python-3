"""
Funciones

si una funcion no tiene "return " nos deolvera un "None"
"""
def factorial(numero):

    #numero = int(input("Ingrese un número: "))
    factorial = 1 
    while numero > 0:
        factorial = factorial*numero
        numero-=1
    return factorial
numero = int(input("Ingrese un número: "))
print(factorial(numero))

resultado = factorial(7)
print(resultado)
print(factorial(9))