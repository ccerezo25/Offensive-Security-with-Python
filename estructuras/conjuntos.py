#eleentos tinen que ser unicos 
#se usan {}

mi_conjunto={1,2,3}
mi_2_conjunto={4,5,6,2}

#añadir conjunto 

mi_conjunto.add{7}

#eliminar 
mi_conjunto.remove(3)

#añadir 
mi_conjunto.update({8,9,77})

#cuando existe te lo borra cuando no pasa nada

mi_conjunto.discard(7)

#interseciones en conjuntos 

conjunto_final = mi_conjunto.intersection(mi_2_conjunto)

#uniones se juntan todos los cnjuntos como en sql intersecion , union , etc 

#se pude hacer busquedas
# con set se puede hacer conjunto 
mi_conjunto3 = set(range(1000))
print(1,2,3,4 in mi_conjunto3)

#en la intersecion son los qu no se repite n esa es la diferncia