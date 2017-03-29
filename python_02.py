"""
Cadenas
"""
cadena = "Hola 'Rudy'"
cadena = """Saltos de linea :
linea 1 
linea 2
            """
nombre = "Rudy "
apellido = "Rojas"

print(cadena)
"""
formas de concatenar texto
"""

print("Tu nombre es : "+ nombre + apellido)
print("Tu nombre es : %s %s" %(nombre, apellido))
print("Tu nombre es : {} {}".format(nombre, apellido))
print("Tu nombre es :",nombre, apellido)

"""
Listas 
"""

cadena2 = "Aprendiendo Python"
print(cadena2)
print(cadena2[9]) # empieza a contar de izquiera a derecha
print(cadena2[-2]) # empieza a contar de derecha a izquierda
print(cadena2[0:11]) # indicamos desde donde hasta donde queremos seleccionar
print(cadena2[-2:-1])
print(cadena2[0:11:2]) # indicamos que lea 1 y luego salte el siguiente 
print(cadena2[::-1]) # voltea todo el texto 

"""
Métodos de string
- formato
"""

nombre2 = "Rudy Jhean"
carrera = "Ingenieria de Sistemas"

resultado = '{a} estudiante de {b}'.format(a= nombre2, b = carrera)
resultado =resultado.lower() # nos da un nuevo string de salida pero en minusculas
resultado =resultado.upper() # nos da un nuevo string de salida pero en mayúsculas
resultado =resultado.title() 
print(resultado)

"""
búsqueda
"""

buscar = resultado.find('Estudiante') # nos muestra apartir de que num empieza la palabra
print(buscar)
contar = resultado.count('e')
print(contar)

"""
Sustitución
"""
nueva_cadena = resultado.replace('e','x')
print(nueva_cadena)

'''
convertir cadena en lista
'''
lista = resultado.split(' ')
print(lista)


