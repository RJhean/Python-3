try:
    print(2/0)
except ZeroDivisionError as ex:
    print(ex)
    print("No es posible dividir con 0 ")


try:
    lista=[1,2]
    print(lista[9])
except IndexError as ex:
    print(ex)
    print("No es posible obtener el indice")

"""
Exception 
"""

try:# intentamos a ejecutar
    lista=[1,2]
    print(lista[9])
except Exception as ex:# ejecuta cuando ocurre un error
    print(ex)
    print("No se que paso, pero salio algo mal!")
finally: # se imprime siempre
    print("Se termino el script")
