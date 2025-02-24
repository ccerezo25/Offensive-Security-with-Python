class Online: 
    
    Tienda_inventario = []

    def __init__(self,producto,precio,descuento):
        self.producto = producto
        self.precio = precio
        self.descuento = descuento

    @classmethod
    def Descuento(slc,producto,precio,descuento):
        print(f"su prdcuto es  {producto}  su precio actual es {precio} ")
        monto_descuento = precio * (descuento /100.0)
        print(f"su descuento es: {monto_descuento}% ")
        precio -= monto_descuento
        print(f"su prcio actual de su producto {producto} es {precio}")
        
        slc.Tienda_inventario.append(slc(producto,precio,descuento))


Online.Descuento("Zapatos",100,25)