import socket


def start_tcp_server(host='127.0.0.1', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"TCP-сервер слухає на {host}:{port}...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Підключено клієнта: {addr}")
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Отримано від клієнта: {data}")

        response = f"Сервер отримав: {data}"
        client_socket.send(response.encode('utf-8'))
        client_socket.close()


if __name__ == "__main__":
    start_tcp_server()
