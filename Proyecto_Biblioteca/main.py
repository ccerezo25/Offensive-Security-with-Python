class Libro:

    def __init__(self,id_libro,autor, nombre_libro):
        self.id_libro = id_libro
        self.autor= autor 
        self.nombre_libro = nombre_libro
        self.esta_prestado = False

    def __str__(self):
        return f"Libro {self.id_libro} , {self.autor} , {self.nombre_libro}"
    
    def __repr__(self):
        return self.__str__()

class Biblioteca:

    def __init__(self):
        self.libros = {}
    
    def agregar_libro(self,libro):
        if libro.id_libro not in self.libros:
            self.libros[libro.id_libro] = libro # asi se añade ibros a un diccionario 
        else: 
            print(f"\n[!] No s posible agregar el libro con ID {libro.id_libro}")
    
    def prestar_libro(self,id_libro):
        if id_libro in self.libros and not self.libros[id_libro].esta_prestado:
            self.libros[id_libro].esta_prestado = True

        else: 
            print(f"\n[!] No es posible prestar el libro con id {id_libro}")

    @property
    def mostrar_libro(self):
        return [libro for libro in self.libros.values() if not libro.esta_prestado]
    
    @property
    def mostrar_libro_prestados(self):
        return [libro for libro in self.libros.values() if libro.esta_prestado]

class BibliotecaInfantil(Biblioteca):
    def __init__(self):
        super().__init__()
        self.libros_para_ninos= {}
    
    def agregar_libro(self, libro,es_para_ninos):
         super().agregar_libro(libro)
         self.libros_para_ninos[libro.id_libro] = es_para_ninos

    def prestar_libro(self, id_libro,es_nino):
         if id_libro in self.libros and self.libros_para_ninos[id_libro] == es_nino and not self.libros[id_libro].esta_prestado:
            self.libros[id_libro].esta_prestado = True

         else: 
            print(f"\n[!] No es posible prestar el libro con id {id_libro}")
        

if __name__ == '__main__':
    biblioteca = BibliotecaInfantil()

    libro1 = Libro(1,"marclo vasque","como ser un lammer de potencia maxima ")
    libro2 = Libro(2,"Pepito manolete","Arende a colorear desde 0 ")

    biblioteca.agregar_libro(libro1, es_para_ninos=False)
    biblioteca.agregar_libro(libro2, es_para_ninos=True)

    print(f"\n[+] Libros en biblioteca: {biblioteca.mostrar_libro}")
    
    biblioteca.prestar_libro(1, es_nino=False)

    print(f"\n[+] Libros en biblioteca: {biblioteca.mostrar_libro}")
