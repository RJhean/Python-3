"""
Ciclo While
La utilizaos cuando no sabemos cuantos iteraciones queremos realizar.
Continue = nos permite que el ciclo continue su ejecución
Break = nos permite cortar el ciclo de forma abrupta
"""

contador = 0

while contador<=10:
    print ("Hola", contador)
    contador+=1
    if contador==5:
        continue
    elif contador==6:
        break
else:
    print("El ciclo ha terminado")