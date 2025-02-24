import socket

host = '192.168.3.1'
port = 80

def port_scanner(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #esto sirve para crear un socket el objecto 
    s.settimeout(0.2)
    if s.connect_ex((host,port)) == 0 : 
        print(f"el puerto {port} esta abierto")
    else:
        print(f"el puerto {port} esta cerrado")
    s.close
def main():
    port_scanner(port)

if __name__ == '__main__':
    main()