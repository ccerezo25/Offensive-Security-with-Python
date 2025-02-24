class CuentaB:

    Minimo= 50
    clientes = []

    def __init__(self,nombre,saldo):
        self.nombre = nombre
        self.saldo= saldo
    
    @classmethod
    def Apertura_cuenta (cls,nombre,fondos):
        if fondos < cls.Minimo:
            return f"su saldo es insuficinte cliente {nombre} , el fondo minimo es {cls.Minimo}"
        
        f = cls(nombre,fondos)
        cls.clientes.append(f)
        return f
        
    
        
CuentaB.Apertura_cuenta("marcelo",25)
CuentaB.Apertura_cuenta("cesar",100)
CuentaB.Apertura_cuenta("michael",300)

for i,j in enumerate(CuentaB.clientes,1):
    print(f"cliente numero {i}: su nombre es {j.nombre} y su saldo es {j.saldo} ")