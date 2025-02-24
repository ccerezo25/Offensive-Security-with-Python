class empleado():
    hora_extra = 10
    bono = 100
    def __init__(self,nombre,salario_base):
        self.nombre = nombre
        self.salario_base = salario_base
    def imprimir_salario(self):
        return f"Hola su nombre es {self.nombre} su salario es {self.salario_base}"

class empleado_hora(empleado):
    def __init__(self, nombre, salario_base,hra_etra):
        super().__init__(nombre, salario_base)
        self.hra_etra=hra_etra
        
    def imprimir_salario(self):
        #n1 = super().imprimir_salario()
       salario_total = self.salario_base + (self.hora_extra * self.hra_etra)  
       return f"{super().imprimir_salario()} , con {self.hra_etra}  horas extra, su salario total es {salario_total}"
    
class empleado_fijo(empleado):
    def __init__(self, nombre, salario_base):
        super().__init__(nombre, salario_base)

    def imprimir_salario(self):
        salario_total = self.salario_base + self.bono
        return f"{super().imprimir_salario()} Con un bono de {self.bono}, su salario total es {salario_total}"
    
    

empleados_lista = [
    empleado_hora("cesar",100,10),
    empleado_fijo("marceo",200)
]

for i in empleados_lista:
    print(i.imprimir_salario())