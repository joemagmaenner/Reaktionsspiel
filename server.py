from http.server import BaseHTTPRequestHandler, HTTPServer
import json
# Importiere deine neuen Funktionen
from data import add_score, load_scores

# Initialisiere die Liste beim Start mit den bereits gespeicherten Daten
data_list = load_scores()

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def _set_headers(self, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        # Aktuelle Liste zurückgeben
        response = json.dumps(data_list)
        self.wfile.write(response.encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        try:
            data = json.loads(post_data)
            
            # Überprüfung der Felder basierend auf deinem Code
            if all(k in data for k in ('name_game', 'name_user', 'time')):
                # 1. In die Datei schreiben (via data.py)
                add_score(data['name_game'], data['name_user'], data['time'])
                
                # 2. Den lokalen Arbeitsspeicher (data_list) aktualisieren
                data_list.append(data)
                
                self._set_headers(201)
                response = {'message': 'Data added and saved successfully'}
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
