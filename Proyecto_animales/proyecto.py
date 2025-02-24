class Animal: 
    def __init__(self,nombre,especie):
        self.nombre = nombre
        self.especie = especie
        self.alimntado = False

    def alimentar(self):
        self.alimntado = True

    def __str__(self):
        return f"{self.nombre} {self.especie} - {'Alimentado' if self.alimntado else 'hambiento'}"
    
class TiendaAnimales: 
    def __init__(self,nombre):
        self.nombre = nombre
        self.animales = []
    
    def agregar_animal(self,animal):
        self.animales.append(animal)

    def mostrar_animales(self):
        for animal in self.animales:
            print(animal)

    def alimentar_animales(self):
        for animmal in self.animales:
            animmal.alimentar()

    def vender_animal(self,nombre):
        for animmal in self.animales:
            if animmal.nombre == nombre:
                self.animales.remove(animmal)
                return #se utiliza para trinar la funcin 
            
        print(f"n\[!] No se ha encontrado nngun animal n la tnda ")

if __name__ == '__main__':
    tienda = TiendaAnimales("Mi tienda de animales")
    
    gato = Animal("tijuana","gato")
    perro = Animal("Juan","Perro")

    tienda.agregar_animal(gato)
    tienda.agregar_animal(perro)

    tienda.mostrar_animales()
    tienda.alimentar_animales()

    print(f"Mostrando los animales una vz ests han sido alimentados ")

    tienda.mostrar_animales()
    tienda.vender_animal("tijuana")

    print(f"Mostrando los animales una vz tijuana sea vendida ")

    tienda.mostrar_animales()
