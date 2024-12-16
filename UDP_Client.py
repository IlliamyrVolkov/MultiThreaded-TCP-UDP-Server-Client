import socket

def start_udp_client(server_ip='127.0.0.1', port=12345):
    udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        message = input("Введіть повідомлення серверу (або 'exit' для виходу): ")
        if message.lower() == 'exit':
            break
        udp_client_socket.sendto(message.encode('utf-8'), (server_ip, port))  # Відправлення даних
        data, _ = udp_client_socket.recvfrom(1024)  # Отримання відповіді
        print(f"Відповідь від сервера: {data.decode('utf-8')}")

    udp_client_socket.close()

if __name__ == "__main__":
    start_udp_client()
