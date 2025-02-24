import os

if not os.path.exists("librerias comunes"): 
    os.mkdir("librerias comunes") #crea  directoio , dirctorios aninados 

print(f"[+] Listando todos los dirctorios: ")
archivos = os.listdir()

for archivo in archivos:
    print(archivo)

import shutil #sirve ara eliminar directoriso vacios 