class Lapiz:

    #constructor
    def __init__(self, color='Amarillo', contiene_borrador=False, usa_grafito=False):
        self.color = color # Atributos
        self.contiene_borrador = contiene_borrador
        self.usa_grafito = usa_grafito

    #Métodos (es una función dentro de nuestra clas)

    def dibujar(self):

        print("El lapiz esta dibujando")

    def borrar(self):
        if self.es_valido_para_borrar():
            print("El lapiz esta borrando")
        else:
            print("No es posible borrar")

    def es_valido_para_borrar(self):
        return self.contiene_borrador

# Esto es un objeto
lapiz_generico = Lapiz()

print(lapiz_generico.color)
lapiz_generico.dibujar()

lapiz_generico.borrar()