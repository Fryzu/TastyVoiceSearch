from http.server import HTTPServer, BaseHTTPRequestHandler

import socketserver
import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        jsonData = importDataFromJson()

        self.send_response(200)
        self.end_headers()
        self.wfile.write(
            bytes(json.dumps(jsonData, ensure_ascii=False), 'utf-8'))


def importDataFromJson():
    with open('response.json') as json_file:
        data = json.load(json_file)
        return data['recipes']


def startServer(port):
    httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
    httpd.serve_forever()


if __name__ == '__main__':
    startServer(port=8080)
