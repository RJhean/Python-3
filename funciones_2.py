def suma(valor1, valor2,valor3):
    return valor1+valor2+valor3

def devision(valor1,valor2):
    return valor1/valor2

def multiplicacion(valor1,valor2=0): #se puede colocar valor inicial 
    return valor1*valor2

def multiples_valores():
    return "Hola", 1,True ,2.4

# suma
resultado = suma(10,20,30)
print(resultado)

# formas de pasar parámetros
resultado = devision(100,10)
print("forma 1 ", resultado)
resultado=devision(valor2=10, valor1=100)
print("forma 2 ", resultado)
# multiplicacion
resultado = multiplicacion(5,9)
print(resultado)

# multiples valores
print(multiples_valores())
string, entero, bol , flo =multiples_valores()

print(string)
print(entero)
print(bol)
print(flo)

