import http.server
import socketserver
import smtp
from urllib.parse import urlparse, parse_qs

PORT = 8000
DIR = 'pages'


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)

    def do_GET(self):
        query_string = urlparse(self.path).query
        fields = parse_qs(query_string) if query_string else {}
        min_fields = {"sender", "recipient"}
        if set(fields.keys()).issuperset(min_fields):
            domain = "google.com"
            sender = fields.get("sender", [""])[0]
            send_name = fields.get("name", [""])[0]
            recipient = fields.get("recipient", [""])[0]
            subject = fields.get("subject", [""])[0]
            message = fields.get("message", [""])[0]
            smtp.send(domain, sender, send_name, recipient, subject, message)

        return http.server.SimpleHTTPRequestHandler.do_GET(self)


with socketserver.TCPServer(("", PORT), Handler) as server:
    server.serve_forever()
