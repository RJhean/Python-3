"""
Listas
"""
lista = ["cadena", 2,2.3,True]
lista.append(6)# agrega el num "6" ala lista tomando la ultima posición
lista.insert(1,"hola")# nos permite agregar ala posición que nosotros deseemos
lista.remove(2) # nos permite eliminar de la lista
print(lista)
nueva_lista = lista.pop() # nos permite eliminar el ultimo elemento de la lista
print(lista)
print(nueva_lista)

"""
ordenar las listas de los numeros
"""


lista2 = [1,22,34,5,43,32,3,4,5]
lista3 =  [56,2]
print(lista2)
#lista2.extend(lista3) # permite extender la lista
lista2.append(lista3) # permite agregar la lista dentro de la lista actual
print(lista2)
#lista2.sort(reverse=True) # perite ordenar de forma ascendete o descendente 
#print(lista2)
