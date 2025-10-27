from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('521.html', 'rb') as file:
                html_content = file.read()
            self.wfile.write(html_content)
        elif self.path == '/kfupm.png':
            self.send_response(200)
            self.send_header('Content-type', 'image/png')
            self.end_headers()
            with open('kfupm.png', 'rb') as file:
                png_content = file.read()
            self.wfile.write(png_content)
        elif self.path == '/instructor_photo.jpg':
            self.send_response(200)
            self.send_header('Content-type', 'image/jpeg')
            self.end_headers()
            with open('instructor_photo.jpg', 'rb') as file:
                jpg_content = file.read()
            self.wfile.write(jpg_content)
        elif self.path == '/favicon.ico':
            self.send_response(200)
            self.send_header('Content-type', 'image/x-icon')
            self.end_headers()
            with open('favicon.ico', 'rb') as file:
                icon_content = file.read()
            self.wfile.write(icon_content)
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 Not Found')

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 9595)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpsd server on port 9595')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
