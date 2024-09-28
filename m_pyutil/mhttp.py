from http.server import SimpleHTTPRequestHandler
from http.server import ThreadingHTTPServer


class CORSHTTPRequestHandler(SimpleHTTPRequestHandler):

    def __init__(self, *args, get_handler=None, directory=None, **kwargs):
        super().__init__(*args, directory=directory, **kwargs)
        self.get_handler = get_handler

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()

    def do_GET(self):
        self.get_handler(self) if self.get_handler else super().do_GET()


class Server(ThreadingHTTPServer):

    # noinspection PyTypeChecker
    def __init__(self,
                 host='0.0.0.0',
                 port=8080,
                 is_cors=True,
                 get_handler=None,
                 static_dir=None):
        handler_class = CORSHTTPRequestHandler if is_cors else SimpleHTTPRequestHandler
        super().__init__((host, port), lambda *args, **kwargs: handler_class(*args, get_handler=get_handler, directory=static_dir, **kwargs))

    def start(self) -> 'Server':
        self.serve_forever()
        return self

    def close(self):
        self.shutdown()
        self.server_close()
