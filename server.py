from http.server import HTTPServer, SimpleHTTPRequestHandler

def read_port():
    with open("http.conf") as f:
        for line in f:
            if line.startswith("Port"):
                return int(line.split()[1])
    return 8080

PORT = read_port()
server = HTTPServer(("localhost", PORT), SimpleHTTPRequestHandler)
print(f"Server running on http://localhost:{PORT}")
server.serve_forever()
