import socket

def start_tcp_client(server_ip='127.0.0.1', port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, port))  # Підключення до сервера
    print(f"Підключено до сервера: {server_ip}:{port}")

    message = input("Введіть повідомлення серверу: ")
    client_socket.send(message.encode('utf-8'))  # Відправлення даних

    response = client_socket.recv(1024).decode('utf-8')  # Отримання відповіді
    print(f"Відповідь від сервера: {response}")
    client_socket.close()

if __name__ == "__main__":
    start_tcp_client()
