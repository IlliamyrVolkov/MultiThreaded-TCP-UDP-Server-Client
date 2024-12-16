import socket

def start_udp_server(host='127.0.0.1', port=12345):
    udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_server_socket.bind((host, port))
    print(f"UDP-сервер слухає на {host}:{port}...")

    while True:
        data, addr = udp_server_socket.recvfrom(1024)  # Отримання повідомлення
        print(f"[{addr}] {data.decode('utf-8')}")
        response = "Повідомлення отримано!"
        udp_server_socket.sendto(response.encode('utf-8'), addr)  # Відповідь

if __name__ == "__main__":
    start_udp_server()
