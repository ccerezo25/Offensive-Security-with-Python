import argparse
import subprocess
import re


def get_arguments():
    parser = argparse.ArgumentParser(description="Herramienta ara cambiar la mac e una interfaz de red")
    parser.add_argument("-i", "--interface", help="interfaz de red ", required=True, dest="interface")
    parser.add_argument("-m", "--mac", help="Nueva direcion mac para la interfaz de red", dest="mac_addres", required=True)

    return parser.parse_args()

def is_valid_input(interface,mc_addres):

    is_valid_interface = re.match(r'^[e][n][t][s][h]\d{1,2}$', interface)
    is_valid_mac_adrdress = re.match(r'^[0-9A-Fa-f]{2}([-:])[0-9A-Fa-f]{2}(\1[0-9A-Fa-f]{2}){4}$', mc_addres)

    return is_valid_interface and is_valid_mac_adrdress

def change_mac_addres(interface,mc_addres):
    if is_valid_input(interface,mc_addres):
        subprocess.run(["ifconfig", interface, "down"])#comandos en linux
        subprocess.run(["ifconfig", interface, "hw","ether", mc_addres])#comandos en linux
        subprocess.run(["ifconfig", interface, "up"])
        print("se cambio exitosamente")
    else:
        print("los datos no se cambiaron correctamnte ")


def main():
    args = get_arguments()
    change_mac_addres(args.interface, args.mac_addres)

if __name__ == '__main__':
    main()