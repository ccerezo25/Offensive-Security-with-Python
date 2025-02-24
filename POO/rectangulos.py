class Suma:
    def __init__(self,Alto,Ancho):
        self.Alto = Alto
        self.Ancho = Ancho
    
    #el str es para poder llamar el objeto de una sin llamar  por medio de print(ejemplo())
    # sino print(ejemplo) 
    def __str__(self):
        
        return "Probando hola mundo "
    
    def Resultado(self):
        resultado = self.Alto * self.Ancho
        return (f"Su resultado es {resultado}")
    

resultado = Suma(8,5)

print(resultado.Resultado())

print(resultado)
    
