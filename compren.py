

lista = []

for valor in range(0,100):
    if valor % 2 ==0: # condicional para que solo agregue los numero pares
        lista.append(valor)
print(lista)

"""
List Comprehensions

- valor a agregar ala lista
- un ciclo, for

"""

lista =[valor for valor in range(0,100) if valor % 2 ==0]
print(lista)

"""
Tuplas
"""
tupla =tuple((valor for valor in range(0,100) if valor % 2 !=0))
print(tupla)

"""
Diccinario
"""

diccionario = {indice:valor for indice, valor in enumerate(lista)}
print(diccionario)