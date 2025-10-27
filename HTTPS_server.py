import http.server
import ssl

class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
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

def run(server_class=http.server.HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 9090)
    httpd = server_class(server_address, handler_class)
    
    # Load SSL/TLS certificates and keys
    certfile = '/home/iammint/Downloads/Assignment2_Logistics/openSSL_demo2/Alice/A.crt'
    keyfile = '/home/iammint/Downloads/Assignment2_Logistics/openSSL_demo2/Alice/privkey-A.pem'
    
    # Configure SSL context
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile=certfile, keyfile=keyfile)
    
    # Wrap the HTTP server with SSL/TLS support
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    
    print('Starting HTTPS server on port 9090...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()


