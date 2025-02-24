import os
from gestor_notas import GestorNotas
#from notas import Nota

def main():

    gestor = GestorNotas()
    
    while True:
        print(f"\n-------------------\nMENU\n--------------------")
        print(f"1.Agregar una nota ")
        print(f"2.Leer nota")
        print(f"3.Buscar por una nota")
        print(f"4.Eliminar una nota")
        print(f"5.salir")

        opcion = input("\n[+] Escoge una opcion: ")

        if opcion == "1": 
            contenido = input("\n[+] Contenido de la nota: ")
            gestor.agregar_nota(contenido)
        elif opcion == "2":
            notas = gestor.leer_notas()
            print("\n[+] Mostrando todas las notas almacenadas: ")
            for i, nota in enumerate(notas):
                print(f"{i}:{nota}")
        elif opcion == "5": 
            break

        else:
            input("\n[+] presiona enter para continuar... ")

            



if __name__ == '__main__':
    main()