from http.server import SimpleHTTPRequestHandler
from http.server import ThreadingHTTPServer
from typing import Optional, Callable


class CORSHTTPRequestHandler(SimpleHTTPRequestHandler):

    def __init__(self, *args, get_handler=None, directory=None, **kwargs):
        self.get_handler = get_handler
        super().__init__(*args, directory=directory, **kwargs)

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()

    def do_GET(self):
        self.get_handler(self) if self.get_handler else super().do_GET()


class Server(ThreadingHTTPServer):

    # noinspection PyTypeChecker
    def __init__(self,
                 host: str = '0.0.0.0',
                 port: int = 8080,
                 is_cors: bool = True,
                 get_handler: Optional[Callable[[SimpleHTTPRequestHandler], None]] = None,
                 static_dir: str = None):
        if is_cors:
            super().__init__((host, port), lambda *args, **kwargs: CORSHTTPRequestHandler(*args, get_handler=get_handler, directory=static_dir, **kwargs))
        else:
            super().__init__((host, port), SimpleHTTPRequestHandler)

    def start(self) -> 'Server':
        self.serve_forever()
        return self

    def close(self):
        self.shutdown()
        self.server_close()
