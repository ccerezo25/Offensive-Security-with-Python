class Dispositivos_red:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
    
    def implementar(self):
       raise NotImplementedError("este metodo tiene que instalarse mas adelante")

class Router(Dispositivos_red):
    def implementar(self):
        return f"Router marca: {self.marca} y su modelo es: {self.modelo}"

class Pc(Dispositivos_red):
    def implementar(self):
        return f"Pc marca: {self.marca} y su modelo es: {self.modelo}" 

class Switch(Dispositivos_red):

    def implementar(self):
        return f"Switch{self.marca} y su modelo es: {self.modelo}"
    
def polimorfis(i):
     print(i.implementar())
        


Sw100=Switch("netgear","as200")
#Prueba1 = Dispositivos_red("Tlink","EB200")
polimorfis(Sw100)
#Router.implementar(Prueba1)


