"""
funciones anónimas
"""


mi_funcion = lambda valor1,valor2: valor1+valor2
resultado = mi_funcion(50,60)
print(resultado)

formato = lambda sentencia : '¿{}?'.format(sentencia)
resultado = formato("Hola")
print(resultado)