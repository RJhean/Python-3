"""
Tuplas:
    - las tuplas son inmutables, no se pueden agregar ni quitar elementos
"""

tupla = (1, "hola", True)

print(tupla[1])

"""
Diccionarios
- las llaves deven de ser inmutables
- si tenemos 2 o mas lleves iguales, python tomará el ultimo valor
- Si la llave existe actualiza, si no crea uno nuevo
"""

diccionario={'nombre':"Rudy", 'edad':22}

diccionario['cumpleaños']="14 de septiembre" # agregamos un nuevo elemento
diccionario['edad']=21
#valor = diccionario['nombre']
valor = diccionario.get('a','No Existe') # permite seleccionar un atributo del diccionario le 
                                         # pasamos 2 valores una llave y sien el caso que no se
                                         # encuentra un mensaje
#del diccionario['cumpleaños']
#print(diccionario)
#print(valor)

llaves = list(diccionario.keys() )
valores = list(diccionario.values())
diccionario2={ 'b' :23,'c':33}
#diccionario['b']=diccionario2['b']
#diccionario['c']=diccionario2['c']
diccionario.update(diccionario2)
print(llaves)
print(valores)
print(diccionario)