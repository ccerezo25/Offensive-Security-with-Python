
import scapy.all as scapy
import sys

def process_dns_packet(packet):
    if packet.haslayer(scapy.DNSQR):
        try:
            domain = packet[scapy.DNSQR].qname.decode()
        except UnicodeDecodeError:
            return  # Ignorar dominios con codificación inválida

        exclude_keywords = {"google", "cloud", "bing", "static", "sensic"}

        if domain not in domains_seen and not any(keyword in domain for keyword in exclude_keywords):
            domains_seen.add(domain)
            print(f"[+] Dominio: {domain}")

def sniff(interface):
    try:
        scapy.sniff(iface=interface, filter="udp and port 53", prn=process_dns_packet, store=0)
    except PermissionError:
        print("[-] Permiso denegado. Ejecuta el script con privilegios elevados.")
    except Exception as e:
        print(f"[-] Error al iniciar sniffing: {e}")

def main():
    interface = sys.argv[1] if len(sys.argv) > 1 else "ens33"
    print(f"[+] Iniciando sniffing en la interfaz: {interface}")
    sniff(interface)

if __name__ == "_main_":
    domains_seen = set()
    main()