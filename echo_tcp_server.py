import socketserver


class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self, secret):
        self.data = self.request.recv(1024).strip()
        print(self.data.decode('utf-8'))
        # secretLen = len(secret)


if __name__ == "__main__":
    HOST, PORT, SECRET = "localhost", 5000, 'SECRET'
    
    with socketserver.TCPServer((HOST, PORT), TCPHandler(SECRET)) as server:
        print(f"Server started at {HOST}:{PORT}")
        server.serve_forever()