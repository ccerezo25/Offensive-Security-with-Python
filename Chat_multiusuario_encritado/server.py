import socket
import threading

def client_thread(clients_socket, clients, usernames):
    try:
        username = clients_socket.recv(1024).decode()
        usernames[clients_socket] = username

        print(f"\n[+] El usuario {username} se ha conectado a la sesión.")

        # Notificar a otros clientes
        for client in clients:
            if client != clients_socket:
                client.sendall(f"\n[+] El usuario {username} ha entrado al chat\n\n".encode())

        while True:
            try:
                message = clients_socket.recv(1024).decode()

                if not message:
                    break

                # Reenviar mensaje a todos los clientes excepto al remitente
                for client in clients:
                    if client != clients_socket:
                        client.sendall(f"{username}: {message}\n".encode())
            except:
                break
    finally:
        print(f"\n[-] El usuario {usernames[clients_socket]} se ha desconectado.")
        clients.remove(clients_socket)
        del usernames[clients_socket]
        clients_socket.close()


def server_program():
    host = 'localhost'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"\n[+] El servidor está en escucha de conexiones entrantes...")

    clients = []
    usernames = {}

    while True:
        clients_socket, address = server_socket.accept()
        clients.append(clients_socket)
        print(f"\n[+] Se ha conectado un nuevo cliente: {address}")

        thread = threading.Thread(target=client_thread, args=(clients_socket, clients, usernames))
        thread.daemon = True
        thread.start()

if __name__ == '__main__':
    server_program()
