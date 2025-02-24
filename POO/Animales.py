class Animal:
    def __init__(self,nombre,tipo):
        self.nombre = nombre
        self.tipo = tipo
    def descripcion(self):
        return f"Hola soy {self.nombre} y mi raza es{self.tipo}"

class Perro(Animal): 
    def __init__(self, nombre, tipo,sonido):
        super().__init__(nombre, tipo)
        self.sonido = sonido

    def descripcion(self):
        n1= super().descripcion()
        return f"{n1} y su sonido es {self.sonido} "

class Gato(Perro):
    def __init__(self, nombre, tipo, sonido):
        super().__init__(nombre, tipo, sonido)

    def descripcion(self):
        return super().descripcion()

n1 = [    
Perro("negro","chihuhua","gugugua"),
Gato("Negra","gatox","miau miau")
]

for i in n1:
    print(Animal.descripcion(i))