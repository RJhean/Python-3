"""
Ciclo for:

la utilizamos cuando sabemos la cantidad de iteraciones que queremos realizar.

range : nos permite generar numeros
range(donde queremos que inicie, hasta que numero queremos generar, la cantidad de saltos que queremos que tenga )

"""

lista = [1,2,3,4,5,6,7,8,9,10]

for valor in lista:
    print("Valor de la lista :  ", valor)

nuevo_rango =  range(0,10,2)
for valor in nuevo_rango:
    print("Valor generado por range : ", valor)


for indice, valor in enumerate(lista):
    print(valor , "tiene el indice ", indice)

for valor in range(0, len(lista)):
    print(valor)


for valor in 'Hola': # iterando un string
    print(valor)

diccionario = {'a':200, 'b':322}

for llave, valor in diccionario.items(): # iterando un diccionario
    print("La llave ", llave , "Tiene el valor de " , valor)