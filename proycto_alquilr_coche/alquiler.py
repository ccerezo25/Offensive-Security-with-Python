
class Vehiculo: 
    def __init__(self,matricula,modelo):
        self.matricula= matricula
        self.modelo = modelo
        self.disponible = True

    def alquiler(self):
        if self.disponible:
            self.disponible= False
        else:
            print(f"Vehiculo {self.modelo} no disonible")

    def devolver(self):
        if self.disponible == False:
            self.disponible= True
        else:
            print(f"Vehiculo {self.modelo} disonible")

    def __str__(self):
        return f"vhiculo {self.matricula}, {self.modelo},{self.disponible}"

class Flota:
    def __init__(self):
        self.vehiculos = [] #lista de objtos vehiculs

    def agregar_vhiculo(self,vehiculo):
        self.vehiculos.append(vehiculo)

    def alquilar_vehiculo(self,matricula):
        for i in self.vehiculos:
            if i.matricula == matricula: 
                i.alquiler()

    def devolver_vehiculo(self,matricula):
        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                vehiculo.devolver()


    def __str__(self):
        return "\n".join(str(vehiculo) for vehiculo in self.vehiculos) #tycast cambiar de str a int o viceversa

if __name__ == '__main__':
    flota = Flota()

    flota.agregar_vhiculo(Vehiculo("asadasd","toyota corolla")) #se puede instanciar las 2 de una 
    flota.agregar_vhiculo(Vehiculo("asadssd","honda civic"))

    print(f"\nFlota inicial")
    print(flota)

    flota.alquilar_vehiculo("asadasd")
    print(f"mostrando la flot despues de alquilar el toyota")

    print(flota)

    flota.devolver_vehiculo("asadasd")
    print(f"mostrando la flot despues de devolver  el toyota")

    print(flota)


