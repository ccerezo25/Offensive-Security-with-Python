#proyecto de videojugos 

mi_juego = ["Super mario bros","zelda","Cyberpunk","Final fantasis "]

#generos
genero = {

    "Super mario bros": "Aventura",
    "zelda": "Aventura",
    "Cyberpunk":"Rol",
    "Final fantasis ": "Rol"
}

#ventas y stock 

ventas_y_stock = {

    "Super mario bros":(400,200),
    "zelda": (600,200),
    "Cyberpunk":(60,120),
    "Final fantasis ": (924,3)

}

#clientes 

    
clientes = {

    "Super mario bros":{"Marcelo","Hackermate","Hackavis","Securiters","Lobotec"},
    "zelda":{"Hackermate","Hackavis","lucia","manolo","Pepe"},
    "Cyberpunk":{"Hackermate","Lobotec","Pepe","Raquel","Albert"},
    "Final fantasis ":{"Lucia","Manolo","Pepe","Securiters","Patricia","Moises"}

}




#sumario
def variable(mi_juego2):
    print(f"\n[i] Resumen del juego {mi_juego2}\n")
    print(f"\t[+] Genero del juego  {genero[mi_juego2]}")  # Cambié 'mi_juego' sin comillas
    print(f"\t[+] Total de ventas {ventas_y_stock[mi_juego2][0]} unidades") 
    print(f"\t[+] Total stock {ventas_y_stock[mi_juego2][1]} unidades") 
    print(f"\t[+] Clientes que han adquirido el juego {' ,'.join(clientes[mi_juego2])} unidades")  # Cambié 'mi_juego' sin comillas


for i in mi_juego:
    if ventas_y_stock[i][0] > 500: 
        variable(i)

ventas_tot = lambda: sum(i for i, _ in ventas_y_stock.values())

#recordar las funciones lamba se pones al final () para represnetar 

print(f"el total de ventas es {ventas_tot()}")