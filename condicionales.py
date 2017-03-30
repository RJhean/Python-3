"""
Condicionales

Operadores de comparación:
- >
- <
- >=
- <=
- !=
- ==

True = 1
False = 0

Lar variables que no tienen valor (Varias o Nulas) siempre seran Falsas.
    - []
    - {}
    - 0
    - ()
    - None
y las que tienen algun tipo de valor seran Verdaderos

None = Nos permite decir que una variable no tiene Valor.
"""

fruta= "Fresa"

if fruta == 'Fresa':
    print("La fruta es Fresa")
elif fruta == 'Pera':
    print("La fruta es Pera")
else:
    print("No son iguales")

# escribir la condicional en una sola linea
mensaje = "La Fruta es Fresa" if fruta == 'Fresa' else 'No son iguales'
print(mensaje)

if  0:
    print("Valor Verdadero")
else:
    print("Valor Falso")

"""
Operadores Lógicos

- and (tiene que cumplirse las 2 condiciones para que devuelva V de lo contratio devuelve F)
- or (Tiene que cumplirse una de las 2 condicionales para que sea V)
"""


valor = 2
valor2=32

if valor and valor2 > 20:
    print("Valor Verdadero")
else:
    print("Valor Falso")





