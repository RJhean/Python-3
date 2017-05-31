class TinyIntError(Exception):
    
    def __init__(self):
        self.message= 'El número no cuenta con las características de un numero tiny_init'

    def __str__(self):
        return self.message