
"""
las variables globales si pueden ser accedidas desde cualquier lugar
las variables locales solo son accedidad destro de la función o donde esten teclaradas
"""
def palindromo():
    nuevo_valor = frase.replace(' ', '')#variables locales
    print(frase)
    return nuevo_valor == nuevo_valor[::-1]


frase = 'anita lava la tina' #variables globales
print(frase)
resultado = palindromo()
print(frase)
print(resultado)

"""
modificando el valor de la variable local
"""
def valor_global():
    global variable_global
    variable_global = 'cambiar valor'

variable_global= 'esto es una variable Global'

print(variable_global)
valor_global()
print(variable_global)