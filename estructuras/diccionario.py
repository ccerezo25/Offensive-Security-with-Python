#tambien se usa en {}

mi_diccionario = {"nombre":"cesar","edad":15, "profesion":"software"}

#se pude imprimir el diconari con la clave 

print(mi_diccionario["profesion"])

#para cambiar 

mi_diccionario["edad"]=26

print(mi_diccionario)

#para eliminar 

del mi_diccionario["edad"]

print(mi_diccionario)

#para encontrar una clave solo se busca a clave 

if "nombre" in mi_diccionario:
    print(f"encontrado")
else:
    print(f"no encontrado")

#longitud 

print(len(mi_diccionario))

#limiar el dicionario

#mi_diccionario.clear()

#print(mi_diccionario)

#cuadrados de cada numero: 

cuadrados= {x:x**2 for x in range(6)}

#x**2 es la variable ue se estan multiplicando 

print(cuadrados)

#buscar valores con get  

print(mi_diccionario.get("nombre","no ncontrado"))

#añadir todo se hace con un update 

dic1 = {"nombre":"pepepancho","edad":15}
dic2 = {"profsion":"contador", "estao civi":"soltero" }

dic1.update(dic2)

print(dic1)

#dicionario aninado 

dic4 = {

    "nombre" : "cesar",
    "hobbies": {"primero":"futbol","segundo":"futbol"},
    "edad" : 28
}

print(dic4)
print(dic4["hobbies"]["primero"]) #llamada dentro dl diconario 

#recorrel los diconarios 

for i in dic4:
    print(i)


print(f"---------------------------")
#rcorrer clave:valor 

for key,value in dic4.items():
    print(f"{key}:{value}")