"""
pasar n cantidad de argumentos a una función

* -> n valores para función se traducen en tuplas
** -> n valores para la función, se traduce en diccionarios
"""

def suma(*args):
    resultado = 0
    for valor in args:
        resultado= resultado+valor
    return resultado

resultado = suma(10,20,30)
print(resultado)
#____________________________

def suma(**kwargs):
    valor = kwargs.get('valor', 'No tiene el Valor')
    print(valor)

resultado = suma(valor = "jhean", x =2 , y = 5, z = True)
print(resultado)