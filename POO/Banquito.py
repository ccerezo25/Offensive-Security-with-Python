class CuentaBancaria: 
    def __init__(self,depositar,retirar,mostrar_saldo):
        self.depositar = depositar
        self.retirar = retirar
        self._mostrar_saldo = mostrar_saldo
        self.__saldo =  0

    def Mostrar_saldo(self):
        return f"su saldo es:{self._mostrar_saldo}"

    def Deposita(self,noney):
        if noney < 0:
            return f" no puede introducir cantidades negativas"
        else:
            self.__saldo += noney
    
    def Retirar(self,noney):
         if noney > self.__saldo:
            return f"no tines dinero suficiente"
         else:
            self.__saldo -= noney 
