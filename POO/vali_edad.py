class Persona : 
    def __init__(self,nombre,edad):
        self.nombre = nombre 
        self.__edad= edad 
    
    @property
    def Edad(self):
        return self.nombre

    @Edad.setter
    def Edad(self,edad):
        if edad < 0 : 
            print(f"escriba un numero positivo")
        else : 
            self.__edad = edad
            print(f"su nombre es:{self.nombre} y su edad {self.__edad}")


Boris = Persona("boris","27")
print(Boris.Edad)