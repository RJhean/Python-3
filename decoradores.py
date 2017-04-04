def decorador(is_valid = True):
    def _decorador(func):
        def before_action():
            print("Vamos a ejecutar la función")
        def after_action():
            print("Se ejecuto la función")

        def nueva_funcion(*args, **kwargs):
            if is_valid:
                before_action()
            resultado = func(*args, **kwargs)
            after_action()

            return resultado
        return nueva_funcion
    return _decorador

@decorador()
def suma(num_uno, num_dos):
    return num_uno+num_dos

resultado = suma(10,20)
print(resultado)


