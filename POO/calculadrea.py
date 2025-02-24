class Calculadora:
    def __init__(self):
        pass

    @staticmethod
    def Suma(i,j):
        return print(f"su resultado es {i+j}")
    
    @staticmethod
    def Resta(i,j):
        return print(f"su resultado es {i-j}")
    
    @staticmethod
    def Multiplicacion(i,j):
        return print(f"su resultado es {i*j}")
    
    @staticmethod
    def Dividir(i,j):
        return i/j if j !=0 else "error"
     

Calculadora.Suma(10,5)
Calculadora.Resta(10,5)
Calculadora.Multiplicacion(2,10)
