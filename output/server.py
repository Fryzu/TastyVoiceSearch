from http.server import HTTPServer, BaseHTTPRequestHandler

import socketserver
import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        jsonData = importDataFromJson()

        self.wfile.write(
            bytes(json.dumps(jsonData, ensure_ascii=False), 'utf-8'))


def importDataFromJson():
    with open('response.json') as json_file:
        data = json.load(json_file)
        return data['recipes']


def startServer(port):
    httpd = HTTPServer(('localhost', 8080), SimpleHTTPRequestHandler)
    httpd.serve_forever()


if __name__ == '__main__':
    startServer(port=8080)
