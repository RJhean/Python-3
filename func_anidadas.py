"""
Funciones Anidadas
"""

def division(numero1, numero2):

    def validacion():
        return numero1 > 0 and numero2 > 0
    if validacion():
        return numero1/numero2

resultado= division(10,2)
print(resultado)


"""
Closures
es cuando una funcion retorna una funcion anidada
"""

def multiplicacion2(numero3, numero4):

    def validacion():
        print("Se ejecuta valicadion")
        return numero3 > 0 and numero4 > 0
    return validacion

def aplicar_funcion(func):
    resuntaldo = func()
    print(resuntaldo)
nueva_fucion = multiplicacion2(10, -5)
aplicar_funcion(nueva_fucion)

