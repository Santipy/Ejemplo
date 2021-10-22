class TinyIntError(Exception):    
    
    def __init__(self):
        self.mensaje = "El número no cuenta con las características de un número tinyInt"

    def __str__(self):
        return self.mensaje
 