class Animal:
    def __init__(self,raza,edad,nombre,credito):
            self.raza = raza
            self.edad = edad
            self.nombre= nombre
            self.credito = credito
    
    def Edad (self):
          print(f"La edad de tu mascota llamada {self.nombre} es : {self.edad}")
    
    def Raza (self): 
          print(f"la raza de tu perrito es  {self.Raza}")
    
    def Saldo (self,saldo):
          print(f"Su saldo es: {saldo}")
          print(f"Su nombre es: {self.nombre}")



negro = Animal("chigugua","2 años","negrito",500)

print(negro.Saldo(500))