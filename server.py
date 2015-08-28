import math

__author__ = 'nasyrovb'


import http.server
import socketserver
import urllib.parse


PORT = 8000


class HttpProcessor(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        s = urllib.parse.urlparse(self.path)
        if s.path == '/handler':
            t = urllib.parse.parse_qs(s.query)
            print(s)
            print(t)

            print('heavy job')
            a = 0;
            for i in range(500000):
                a = math.sin(i)
                print(a)

            self.send_response(200)
            self.send_header('content-type','application/json')
            self.end_headers()
            s = '{"testObject":{"id":0, "name": "NameT", "arr": [4,0,2]}}'
            self.wfile.write(s.encode('utf-8'))

            print('end heavy job')

Handler = HttpProcessor

httpd = socketserver.TCPServer(("", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()