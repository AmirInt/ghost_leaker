import socket


HOST = "127.0.0.1"
PORT = 10000

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"New connection made from {addr}")
            print("Ghost says: '" + conn.recv(11).decode() + "'")

if __name__ == "__main__":
    main()