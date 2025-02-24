class Personas: 
    #mtodo s igual a las funcones
    def __init__(self,nombre,edad):
        self.nombre= nombre
        self.edad= edad
    
    @property
    def saludos(self):
        return f"hola soy {self.nombre} y tengo {self.edad}"

cesar = Personas("Cesar",25)

print(cesar.saludos)