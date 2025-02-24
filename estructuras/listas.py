lista = [1,2,3,4,5]

print(lista[0:2])
print(lista[:-2])
print(len(lista))

#paea usar un while usanmos len ara recorrer 

i=0
while i < len(lista):
    print(lista[i])
    i+=1

#para usar l for usamos enumerate para rcorrrer 

for j,k in enumerate(lista):
    print(f"estas en la posicion {j+1} y tu ataque es {k}")

#podemos poner todo el for en una variabe 

attacks = ["pishing","cangre","test","tec"]
mayuscula = [attacks.lower() for i in attacks]
print(attacks)

#combinar 2 for 

name =["cesar", "boris", "marclo"]
name2= ["pepito","manuel"]
edad= [23,24,25]

for name, edad in zip(name,edad):
    print(f"{name} tine : {edad}")

#eliminar un elemento de una lista 

name.remove("cesar")

#lista son mutable se pude agregar cosas y eliminar 

name.insert(2,"chma alonso ")

#cobinar listas 

name.extend(name2)
