class Carro:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo= modelo 
    
    #se remplaza el cls por la variable del constructor y se le añade deortivo 
    @classmethod
    def Modelo(cls,marca):
        
        return cls(marca,"deportivo")

    @classmethod
    def Modelo2(cls,marca):
        return cls(marca,"sean")
    
    #s pued enviar return sin el print y solo la f"""
    def __str__(self):
        
        return f"su modelo es {self.modelo} y su marca es {self.marca}"


modelo_1 = Carro.Modelo("Toyota")
print(modelo_1)

        