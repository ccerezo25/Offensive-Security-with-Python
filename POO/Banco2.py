class Producto: 

    stock_minimo = 10
    inventario= []

    def __init__(self,nombre,stock,precio):
            self.nombre=nombre
            self.stock=stock
            self.precio=precio
    
    @classmethod
    def Comparacion(slc,nombre,stock,precio):
        
        if stock > slc.stock_minimo:
              slc.inventario.append(slc(nombre,stock,precio))
              return f" su stock {nombre} con precio de {precio}  ya lo anexamos al inventario "
        else:
             return f"producto menor al stock permitido "

print(Producto.Comparacion("Doritos",5,100))
Producto.Comparacion("Papitas",5,200)
print(Producto.Comparacion("Chetos",11,300))
Producto.Comparacion("Ches tres",14,500)



#for i in Producto.inventario:
     #print(f"{i.nombre}")
          
     
    
