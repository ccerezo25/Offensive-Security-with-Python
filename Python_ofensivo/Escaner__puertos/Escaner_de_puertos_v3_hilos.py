import socket
from termcolor import colored
import argparse
from concurrent.futures import ThreadPoolExecutor
import signal
import sys

# Lista para almacenar sockets abiertos
open_sockets = []

# Función para manejar la señal SIGINT (Ctrl + C)
def def_handler(sig, frame):
    print(colored("\n[!] Saliendo del programa...", 'red'))
    for socket in open_sockets:
        socket.close()  # Cerrar todos los sockets abiertos
    sys.exit(1)

# Registrar la señal SIGINT
signal.signal(signal.SIGINT, def_handler)

# Función para obtener los argumentos de la línea de comandos
def get_arguments():
    parser = argparse.ArgumentParser(description='Fast TCP Port Scanner')
    parser.add_argument("-t", "--target", dest="target", help="Victim target to scan (Ex: -t 192.168.1.1)", required=True)
    parser.add_argument("-p", "--port", dest="port", help="Port range scan (Ex: -p 1-100 or -p 80,443)", required=True)
    options = parser.parse_args()

    return options.target, options.port

# Función para crear un socket
def create_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)  # Establecer un timeout de 1 segundo
    open_sockets.append(s)  # Agregar el socket a la lista de sockets abiertos
    return s

# Función para escanear un puerto
def port_scanner(port, host):
    s = create_socket()
    try:
        s.connect((host, port))  # Intentar conectarse al puerto
        print(colored(f"El puerto {port} está abierto", 'green'))
    except (socket.timeout, ConnectionRefusedError):
        pass  # No hacer nada si el puerto está cerrado o no responde
    except Exception as e:
        print(colored(f"Error al escanear el puerto {port}: {e}", 'red'))
    finally:
        if s in open_sockets:
            s.close()  # Cerrar el socket en cualquier caso
            open_sockets.remove(s)  # Eliminar el socket de la lista de sockets abiertos

# Función para parsear el rango de puertos
def parse_ports(ports_str):
    if '-' in ports_str:  # Si es un rango de puertos (ejemplo: 1-100)
        start, end = map(int, ports_str.split('-'))
        return range(start, end + 1)  # Incluir el último puerto
    elif ',' in ports_str:  # Si son puertos separados por comas (ejemplo: 80,443)
        return list(map(int, ports_str.split(',')))
    else:  # Si es un solo puerto (ejemplo: 80)
        return [int(ports_str)]

# Función para escanear múltiples puertos usando ThreadPoolExecutor
def scan_ports(ports, target):
    with ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(lambda port: port_scanner(port, target), ports)

# Función principal
def main():
    target, ports_str = get_arguments()  # Obtener los argumentos
    ports = parse_ports(ports_str)  # Parsear los puertos
    scan_ports(ports, target)  # Escanear los puertos

if __name__ == '__main__':
    main()