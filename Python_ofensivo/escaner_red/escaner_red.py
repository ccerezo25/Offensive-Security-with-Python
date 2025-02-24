import scapy.all as scapy  # Importamos la librería Scapy para manejar paquetes de red
import argparse  # Importamos argparse para manejar argumentos desde la terminal

def get_arguments():
    # Creamos un analizador de argumentos
    parser = argparse.ArgumentParser(description="ARP Scanner")
    
    # Agregamos el argumento obligatorio '-t' o '--target' para ingresar la IP o el rango de IPs
    parser.add_argument("-t", "--target", required=True, dest="target", help="Host / IP Range to Scan")
    
    args = parser.parse_args()  # Analizamos los argumentos ingresados por el usuario
    return args.target  # Retornamos la IP o rango de IPs que se ingresó

def scan(ip):
    # Creamos un paquete ARP que pregunta por la dirección MAC de la IP destino
    arp_packet = scapy.ARP(pdst=ip)
    
    # Creamos un paquete Ethernet de broadcast (se envía a todos los dispositivos de la red)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    
    # Unimos ambos paquetes: Ethernet (broadcast) + ARP (petición de MAC)
    arp_packet = broadcast_packet/arp_packet
    
    # Enviamos los paquetes y esperamos respuestas (timeout de 1 segundo)
    answered, unanswered = scapy.srp(arp_packet, timeout=1, verbose=False)
    
    # Obtenemos un resumen de las respuestas recibidas
    response = answered.summary()
    
    # Si hay dispositivos que respondieron, mostramos la información
    if response:
        print(response)

def main():
    target = get_arguments()  # Obtenemos la IP o rango de IPs ingresado por el usuario
    scan(target)  # Ejecutamos el escaneo con la IP o rango ingresado

# Verificamos si el script se está ejecutando directamente y no como módulo
if __name__ == '__main__':
    main()