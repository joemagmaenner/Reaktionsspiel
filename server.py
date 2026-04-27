from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Speicher für die Daten
data_list = []

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def _set_headers(self, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        # Alle gespeicherten Daten zurückgeben
        response = json.dumps(data_list)
        self.wfile.write(response.encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        try:
            # JSON-Daten parsen
            data = json.loads(post_data)
            # Erwartete Felder überprüfen
            if all(k in data for k in ('name_game', 'name_user', 'time')):
                data_list.append(data)
                self._set_headers(201)  # Created
                response = {'message': 'Data added successfully'}
            else:
                self._set_headers(400)
                response = {'error': 'Missing fields'}
        except json.JSONDecodeError:
            self._set_headers(400)
            response = {'error': 'Invalid JSON'}

        self.wfile.write(json.dumps(response).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Server running on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()