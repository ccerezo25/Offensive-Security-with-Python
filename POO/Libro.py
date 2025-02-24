class Libro_Fisico:
    def __init__(self,titulo,autor,precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
    
    @staticmethod
    def total_ventas(i):
        return print(f"error{i}")
    

ec = Libro_Fisico("cesar","camilo",500)

print(Libro_Fisico.total_ventas(404))