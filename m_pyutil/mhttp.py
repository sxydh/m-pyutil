import http.server
import socketserver
import threading


class CORSHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()


class Server(socketserver.TCPServer):

    def __init__(self, host='0.0.0.0', port=8080, is_cors=True):
        # noinspection PyTypeChecker
        super().__init__((host, port), CORSHTTPRequestHandler if is_cors else http.server.SimpleHTTPRequestHandler)

    def start(self) -> 'Server':
        threading.Thread(target=self.serve_forever).start()
        return self

    def close(self):
        self.shutdown()
        self.server_close()
