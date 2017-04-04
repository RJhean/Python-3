import random

valor = random.randint(0,10)
print(valor)
lista = [True, "String",23,False]

valor = random.choice(lista)
print(valor)
print(lista)
random.shuffle(lista)
print(lista)

#________________________
import datetime

print(datetime.datetime.now())

#________________________
import sys
import time 

#for i in range(100):
    #time.sleep(0.5)
    #sys.stdout.write("\r%d %% "%i)
    #∫sys.stdout.flush()

#_______________________
"""
Argv
"""

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Es necesario colocar por lo menos un argumento")
    else:
        if sys.argv[1]=='help':
            print("Puedes contactar a Coders IT")
        print(sys.argv[1])