import socket

def main(*args):
    HOST, PORT = "10.10.11.2", 5000
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        message = " ".join(args[1:])
        sock.sendall(message)
        
        response = sock.recv(1024)
        print(f"Received: {response.decode('utf-8')}")

if __name__ == "__main__":
    main()