from http.server import SimpleHTTPRequestHandler
from http.server import ThreadingHTTPServer


class CORSHTTPRequestHandler(SimpleHTTPRequestHandler):

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()


class Server(ThreadingHTTPServer):

    def __init__(self, host='0.0.0.0', port=8080, is_cors=True):
        # noinspection PyTypeChecker
        super().__init__((host, port), CORSHTTPRequestHandler if is_cors else SimpleHTTPRequestHandler)

    def start(self) -> 'Server':
        self.serve_forever()
        return self

    def close(self):
        self.shutdown()
        self.server_close()
