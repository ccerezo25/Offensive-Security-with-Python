import argparse
import subprocess
import signal
import sys
from concurrent.futures import ThreadPoolExecutor
from termcolor import colored

def def_handler(sig, frame):
    print(colored(f"\n[1] Saliendo del programa...\n", 'red'))
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

def get_arguments():
    parser = argparse.ArgumentParser(description="Herramienta para descubrir hosts activos en una red (ICMP)")
    parser.add_argument("-t", "--target", required=True, dest="target", help="Host o rango de red a escanear")
    args = parser.parse_args()
    return args.target

def parse_target(target_str):
    target_str_splitted = target_str.split('.')  # ["192", "168", "1", "1-100"]
    first_three_octets = '.'.join(target_str_splitted[:3])  # 192.168.1

    if len(target_str_splitted) == 4:
        if "-" in target_str_splitted[3]:
            start, end = target_str_splitted[3].split('-')
            return [f"{first_three_octets}.{i}" for i in range(int(start), int(end) + 1)]
        else:
            return [target_str]
    else:
        print(colored(f"\n[1] El formato de IP o rango de IP no es válido\n", 'red'))
        sys.exit(1)

def host_discovery(target):
    try:
        ping = subprocess.run(["ping", "-c", "1", target], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if ping.returncode == 0:
            print(colored(f"\n[+] Host {target} activo", 'green'))
        else:
            print(colored(f"\n[-] Host {target} inactivo", 'red'))
    except Exception as e:
        print(colored(f"\n[!] Error al escanear {target}: {e}", 'yellow'))

def main():
    target = get_arguments()
    targets = parse_target(target)

    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(host_discovery, targets)

if __name__ == '__main__':
    main()