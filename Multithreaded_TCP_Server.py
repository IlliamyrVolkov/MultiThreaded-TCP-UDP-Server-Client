import socket
import threading

def handle_client(client_socket, addr):
    print(f"[НОВЕ ПІДКЛЮЧЕННЯ] {addr} підключено.")
    try:
        while True:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            print(f"[{addr}] Отримано: {data}")
            client_socket.send(f"Сервер отримав: {data}".encode('utf-8'))
    finally:
        print(f"[ВІДКЛЮЧЕНО] {addr} відключено.")
        client_socket.close()

def start_tcp_server(host='127.0.0.1', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Багатопотоковий TCP-сервер слухає на {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        thread.start()
        print(f"[АКТИВНІ ПІДКЛЮЧЕННЯ] {threading.active_count() - 1}")

if __name__ == "__main__":
    start_tcp_server()
