class Automovil:
   
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
    
    def describir (self):
        return f"vehiculo: {self.marca} {self.modelo}"

class Moto(Automovil):

    def describir(self):
        return f"moto: {self.marca}{self.modelo}" 
    

def polimor(i):
    print(i.describir())

coche = Automovil("Toyota","corola")
moto = Moto("honda","cbr")

polimor(coche)
polimor(moto)

#print(coche.describir())
#print(moto.describir())
