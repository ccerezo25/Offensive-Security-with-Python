import socket
from termcolor import colored
import sys
import argparse

def get_arguments():
    parser = argparse.ArgumentParser(description='Fast TCP Port Scanner')
    parser.add_argument("-t", "--target", dest="target", help="Victim target to scan (Ex: -t 192.168.1.1)", required=True)
    parser.add_argument("-p", "--port", dest="port", help="Port range scan (Ex: -p 1-100 or -p 80,443)", required=True)
    options = parser.parse_args()

    if not options.target or not options.port:
        parser.print_help()
        sys.exit(1)
    
    return options.target, options.port

def create_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Crear un socket
    s.settimeout(1)  # Establecer un timeout de 1 segundo
    return s

def port_scanner(port, host, s):
    try:
        s.connect((host, port))  # Intentar conectarse al puerto
        print(colored(f"El puerto {port} está abierto", 'green'))
        s.close()
    except (socket.timeout, ConnectionRefusedError):
        s.close()

def parse_ports(ports_str):
    if '-' in ports_str:  # Si es un rango de puertos (ejemplo: 1-100)
        start, end = map(int, ports_str.split('-'))
        return range(start, end + 1)  # Incluir el último puerto
    elif ',' in ports_str:  # Si son puertos separados por comas (ejemplo: 80,443)
        return list(map(int, ports_str.split(',')))
    else:  # Si es un solo puerto (ejemplo: 80)
        return [int(ports_str)]

def scan_ports(ports, target):
    for port in ports:
        s = create_socket()
        port_scanner(port, target, s)

def main():
    target, ports_str = get_arguments()  # Obtener los argumentos
    ports = parse_ports(ports_str)  # Parsear los puertos
    scan_ports(ports, target)  # Escanear los puertos

if __name__ == '__main__':
    main()