class Vehiculo : 
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.vendido = False

    def vender (self):
        self.vendido = True
    
    def __str__(self):
        return f"{self.marca},{self.modelo}"
    
class Agencia(Vehiculo): 
    def __init__(self,nombre):
        self.nombre = nombre
        self.vehiculos = []

    def agregar_vehiculo(self,vehiculo):
        self.vehiculos.append(vehiculo)

    def mostrar_vehiculos(self):
        for i in self.vehiculos: 
            print(i)
    
    def vender_vehiculo(self,modelo):
        for i in self.vehiculos:
            if i.modelo == modelo:
                Vehiculo.vender()

    def eliminar_vehiculo(self,modelo):
        for i in self.vehiculos:
            if i.modelo == modelo:
                self.vehiculos.remove(i)

primer_vehiculo = Vehiculo("mazda","sedan")
primer_vehiculo.


#primer_vehiculo = Vehiculo("toyota","raze")
#mi_Agencia =  Agencia("mi agencia ")
#Agencia(primer_vehiculo).agregar_vehiculo
#Agencia(primer_vehiculo).mostrar_vehiculos
#mi_Agencia.agregar_vehiculo(primer_vehiculo)
#mi_Agencia.mostrar_vehiculos()